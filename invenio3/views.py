# -*- coding: utf-8 -*-

"""invenio3 Invenio sample blueprint."""

from flask import Blueprint

blueprint = Blueprint(
    'invenio3_main',
    __name__,
    template_folder='templates',
    static_folder='static'
)
