# -*- coding: utf-8 -*-

"""invenio3 Invenio sample workflow."""

from __future__ import absolute_import, print_function


def task_add(obj, eng):
    obj.data += 10

def task_print(obj, eng):
    print(obj.data)

def add_file(obj, eng):
    obj.files["testfile.pdf"] = open('/Users/jlavik/Downloads/1007.5048.pdf', 'r')

def halt(obj, eng):
    eng.halt(action="Approval")


class MyWorkflow(object):
    data_type = "hp"
    workflow = [task_add, halt, task_add, halt, task_print, halt]


class MyRecordWorkflow(object):
    data_type = "hep"
    workflow = [add_file, halt, task_print]


class MyAuthWorkflow(object):
    data_type = "authors"
    workflow = [halt, task_print]


__all__ = ('MyWorkflow', 'MyRecordWorkflow', 'MyAuthWorkflow')
