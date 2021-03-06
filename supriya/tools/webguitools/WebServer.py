# -*- encoding: utf-8 -*-
import threading
import tornado.web


class WebServer(threading.Thread):

    ### INITIALIZER ###

    def __init__(self, server):
        from supriya.tools import systemtools
        from supriya.tools import webguitools
        threading.Thread.__init__(self)
        self.server = server
        self.server.subscription_service.subscribe(self, 'server-booted')
        self.server.subscription_service.subscribe(self, 'server-meters')
        self.server.subscription_service.subscribe(self, 'server-quit')
        self.server.subscription_service.subscribe(self, 'server-status')
        handlers = [
            (r'/', webguitools.MainHandler),
            (r'/websocket', webguitools.SocketHandler),
            ]
        self.application = tornado.web.Application(
            handlers,
            cookie_secret='MAGIC',
            static_path=systemtools.Assets['webgui/static'],
            template_path=systemtools.Assets['webgui/templates'],
            #static_path=os.path.join(os.path.dirname(__file__), 'static'),
            #template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            websocket_allow_origin='*',
            xsrf_cookies=True,
            )
        self.application.watchers = set()
        self.ioloop = tornado.ioloop.IOLoop.instance()
        self.daemon = True

    ### PUBLIC METHODS ###

    def notify(self, topic, event):
        for watcher in self.application.watchers:
            self.ioloop.add_callback(watcher.update, topic, event)

    def run(self):
        self.application.listen(8888)
        self.ioloop.start()