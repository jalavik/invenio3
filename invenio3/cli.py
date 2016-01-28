# -*- coding: utf-8 -*-

"""invenio3 base Invenio configuration."""

from __future__ import absolute_import, print_function

from invenio_base.app import create_cli

from .factory import create_app

cli = create_cli(create_app=create_app)

# from invenio_workflows.tasks import celery_run
# celery_run.delay('MyWorkflow', [1])
