# -*- encoding: utf-8 -*-
import abc
import collections
import copy
from supriya.tools.servertools.ServerObjectProxy import ServerObjectProxy


class Node(ServerObjectProxy):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_is_paused',
        '_name',
        '_node_id',
        '_node_id_is_permanent',
        '_parent',
        )

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(self, name=None):
        ServerObjectProxy.__init__(self)
        self._is_paused = False
        self._name = name
        self._node_id = None
        self._node_id_is_permanent = None
        self._parent = None

    ### SPECIAL METHODS ###

    def __float__(self):
        return float(self.node_id)

    def __int__(self):
        return int(self.node_id)

    def __repr__(self):
        class_name = type(self).__name__
        node_id = '???'
        if self.node_id is not None:
            node_id = self.node_id
        if self.name is None:
            string = '<{class_name}: {node_id}>'.format(
                class_name=class_name,
                node_id=node_id,
                )
        else:
            string = '<{class_name}: {node_id} ({name})>'.format(
                class_name=class_name,
                name=self.name,
                node_id=node_id,
                )
        return string

    ### PRIVATE METHODS ###

    def _cache_named_children(self):
        name_dictionary = {}
        if hasattr(self, '_named_children'):
            for name, children in self._named_children.items():
                name_dictionary[name] = copy.copy(children)
        if hasattr(self, 'name') and self.name is not None:
            if self.name not in name_dictionary:
                name_dictionary[self.name] = set()
            name_dictionary[self.name].add(self)
        return name_dictionary

    def _cache_control_interface(self):
        return self._control_interface.as_dict()

    def _handle_response(self, response):
        from supriya.tools import responsetools
        if isinstance(response, responsetools.NodeInfoResponse):
            if response.action == responsetools.NodeAction.NODE_REMOVED:
                self._set_parent(None)
                self._unregister_with_local_server()
            elif response.action == responsetools.NodeAction.NODE_ACTIVATED:
                self._is_paused = False
            elif response.action == responsetools.NodeAction.NODE_DEACTIVATED:
                self._is_paused = True
            elif response.action == responsetools.NodeAction.NODE_MOVED:
                new_parent = self.server._nodes[response.parent_group_id]
                if new_parent is self.parent:
                    new_index = 0
                    if response.previous_node_id is not None:
                        previous_node = \
                            self.server._nodes[response.previous_node_id]
                        new_index = new_parent.index(previous_node) + 1
                    elif response.next_node_id is not None:
                        next_node = self.server._nodes[response.next_node_id]
                        new_index = new_parent.index(next_node)
                    old_index = self.parent.index(self)
                    if new_index != self.parent.index(self):
                        if new_index < old_index:
                            self.parent._children.remove(self)
                            self.parent._children.insert(new_index, self)
                        else:
                            self.parent._children.insert(new_index, self)
                            self.parent._children.pop(old_index)
                else:
                    self._set_parent(new_parent)
                    index = 0
                    if response.previous_node_id is not None:
                        previous_node = \
                            self.server._nodes[response.previous_node_id]
                        index = new_parent.index(previous_node) + 1
                    elif response.next_node_id is not None:
                        next_node = self.server._nodes[response.next_node_id]
                        index = new_parent.index(next_node)
                    new_parent._children.insert(index, self)

    @staticmethod
    def _iterate_nodes(nodes):
        for x in nodes:
            yield x
            if hasattr(x, '_children'):
                for y in Node._iterate_nodes(x):
                    yield y

    def _register_with_local_server(
        self,
        node_id_is_permanent=False,
        server=None,
        ):
        if server is None or not server.is_running:
            raise ValueError
        if self.server is not None or self in server._nodes:
            return
        id_allocator = server.node_id_allocator
        if node_id_is_permanent:
            node_id = id_allocator.allocate_permanent_node_id()
        else:
            node_id = server.node_id_allocator.allocate_node_id()
        if node_id is None:
            raise ValueError
        elif node_id in server._nodes:
            raise ValueError
        ServerObjectProxy.allocate(self, server=server)
        self._node_id = node_id
        self._node_id_is_permanent = bool(node_id_is_permanent)
        self._server._nodes[self._node_id] = self
        return node_id

    def _remove_from_parent(self):
        if self._parent is not None:
            if self in self._parent:
                self._parent._children.remove(self)
        self._parent = None

    def _remove_control_interface_from_parentage(self, name_dictionary):
        if self._parent is not None and name_dictionary:
            for parent in self.parentage[1:]:
                parent._control_interface.remove_controls(name_dictionary)

    def _remove_named_children_from_parentage(self, name_dictionary):
        if self._parent is not None and name_dictionary:
            for parent in self.parentage[1:]:
                named_children = parent._named_children
                for name in name_dictionary:
                    for node in name_dictionary[name]:
                        named_children[name].remove(node)
                    if not named_children[name]:
                        del(named_children[name])

    def _set_parent(self, new_parent):
        named_children = self._cache_named_children()
        control_interface = self._cache_control_interface()
        self._remove_named_children_from_parentage(named_children)
        self._remove_control_interface_from_parentage(control_interface)
        self._remove_from_parent()
        self._parent = new_parent
        self._restore_named_children_to_parentage(named_children)
        self._restore_control_interface_to_parentage(control_interface)

    def _restore_control_interface_to_parentage(self, name_dictionary):
        if self._parent is not None and name_dictionary:
            for parent in self.parentage[1:]:
                parent._control_interface.add_controls(name_dictionary)

    def _restore_named_children_to_parentage(self, name_dictionary):
        if self._parent is not None and name_dictionary:
            for parent in self.parentage[1:]:
                named_children = parent._named_children
                for name in name_dictionary:
                    if name in named_children:
                        named_children[name].update(name_dictionary[name])
                    else:
                        named_children[name] = copy.copy(name_dictionary[name])

    def _unregister_with_local_server(self):
        node_id = self.node_id
        if self.server is not None:
            del(self._server._nodes[self._node_id])
            if self.node_id_is_permanent:
                self.server.node_id_allocator.free_permanent_node_id(
                    self.node_id,
                    )
        self._node_id = None
        self._node_id_is_permanent = None
        ServerObjectProxy.free(
            self,
            )
        return node_id

    ### PUBLIC METHODS ###

    @abc.abstractmethod
    def allocate(
        self,
        add_action=None,
        node_id_is_permanent=False,
        target_node=None,
        ):
        from supriya.tools import servertools
        target_node = Node.expr_as_target(target_node)
        server = target_node.server
        node_id = self._register_with_local_server(
            node_id_is_permanent=node_id_is_permanent,
            server=server,
            )
        target_node_id = target_node.node_id
        add_action = servertools.AddAction.from_expr(add_action)
        if add_action == servertools.AddAction.ADD_TO_HEAD:
            assert isinstance(target_node, servertools.Group)
            self._set_parent(target_node)
            target_node._children.insert(0, self)
        elif add_action == servertools.AddAction.ADD_TO_TAIL:
            assert isinstance(target_node, servertools.Group)
            self._set_parent(target_node)
            target_node._children.append(self)
        elif add_action == servertools.AddAction.ADD_BEFORE:
            self._set_parent(target_node.parent)
            index = self.parent._children.index(target_node)
            self._parent._children.insert(index, self)
        elif add_action == servertools.AddAction.ADD_AFTER:
            self._set_parent(target_node.parent)
            index = self.parent._children.index(target_node)
            self._parent._children.insert(index + 1, self)
        elif add_action == servertools.AddAction.REPLACE:
            assert target_node.parent is not self.server.root_node
            self._set_parent(target_node.parent)
            index = self.parent._children.index(target_node)
            self._parent._children[index] = self
            target_node._unregister_with_local_server()
            target_node._set_parent(None)
        else:
            raise ValueError
        return add_action, node_id, target_node_id

    @staticmethod
    def expr_as_node_id(expr):
        from supriya.tools import servertools
        if isinstance(expr, servertools.Server):
            return 0
        elif isinstance(expr, Node):
            return expr.node_id
        elif expr is None:
            return None
        elif isinstance(expr, int):
            return expr
        raise TypeError(expr)

    @staticmethod
    def expr_as_target(expr):
        from supriya.tools import servertools
        if expr is None:
            return Node.expr_as_target(servertools.Server())
        elif isinstance(expr, servertools.Server):
            return expr.default_group
        elif isinstance(expr, Node):
            return expr
        elif isinstance(expr, int):
            raise NotImplementedError
        raise TypeError(expr)

    def free(self):
        from supriya.tools import requesttools
        self._set_parent(None)
        server = self.server
        if self.node_id is not None and server.is_running:
            node_id = self._unregister_with_local_server()
            node_free_request = requesttools.NodeFreeRequest(
                node_ids=(node_id,),
                )
            node_free_request.communicate(
                server=server,
                sync=False,
                )
        return self

    def pause(self):
        from supriya.tools import requesttools
        if self.is_paused:
            return
        self._is_paused = True
        if self.is_allocated:
            request = requesttools.NodeRunRequest(
                node_id_run_flag_pairs=(
                    (self.node_id, False),
                    ),
                )
            request.communicate(
                server=self.server,
                sync=False,
                )

    def unpause(self):
        from supriya.tools import requesttools
        if not self.is_paused:
            return
        self._is_paused = False
        if self.is_allocated:
            request = requesttools.NodeRunRequest(
                node_id_run_flag_pairs=(
                    (self.node_id, True),
                    ),
                )
            request.communicate(
                server=self.server,
                sync=False,
                )

    def precede_by(self, expr):
        if not isinstance(expr, collections.Sequence):
            expr = [expr]
        index = self.parent.index(self)
        self.parent[index:index] = expr

    def replace_with(self, expr):
        if not isinstance(expr, collections.Sequence):
            expr = [expr]
        index = self.parent.index(self)
        self.parent[index:index + 1] = expr

    def succeed_by(self, expr):
        if not isinstance(expr, collections.Sequence):
            expr = [expr]
        index = self.parent.index(self)
        self.parent[index + 1:index + 1] = expr

    ### PUBLIC PROPERTIES ###

    @property
    def is_allocated(self):
        if self.server is not None:
            return self in self.server
        return False

    @property
    def is_paused(self):
        return self._is_paused

    @property
    def is_running(self):
        return self.server is not None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, expr):
        assert isinstance(expr, (str, type(None)))
        old_name = self._name
        for parent in self.parentage[1:]:
            named_children = parent._named_children
            if old_name is not None:
                named_children[old_name].remove(self)
                if not named_children[old_name]:
                    del named_children[old_name]
            if expr is not None:
                if expr not in named_children:
                    named_children[expr] = set([self])
                else:
                    named_children[expr].add(self)
        self._name = expr

    @property
    def node_id(self):
        return self._node_id

    @property
    def node_id_is_permanent(self):
        return self._node_id_is_permanent

    @property
    def parent(self):
        return self._parent

    @property
    def parentage(self):
        parentage = []
        node = self
        while node is not None:
            parentage.append(node)
            node = node.parent
        return tuple(parentage)