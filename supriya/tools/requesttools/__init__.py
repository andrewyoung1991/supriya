# -*- encoding: utf-8 -*-

r'''
Tools for object-modeling OSC requests made to **scsynth**.
'''

from abjad.tools import systemtools

systemtools.ImportManager.import_structured_package(
    __path__[0],
    globals(),
    )