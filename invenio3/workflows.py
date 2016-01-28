# -*- coding: utf-8 -*-

"""invenio3 Invenio sample workflow."""

from __future__ import absolute_import, print_function


def task_add(obj, eng):
    obj.data += 10

def task_print(obj, eng):
    print(obj.data)

def halt(obj, eng):
    eng.halt(action="Approval")


class MyWorkflow(object):
    workflow = [task_add, halt, task_add, task_print]


__all__ = ('MyWorkflow',)
