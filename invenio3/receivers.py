# -*- coding: utf-8 -*-

"""invenio3 Invenio sample receivers."""

from __future__ import absolute_import, print_function

from invenio_workflows.signals import workflow_started


@workflow_started.connect
def workflow_saved(sender, **kwargs):
    print("LOLOLOL")


__all__ = ('workflow_saved',)
