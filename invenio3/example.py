# -*- coding: utf-8 -*-

from invenio_workflows.tasks import celery_run
celery_run.delay('MyWorkflow', [1])
