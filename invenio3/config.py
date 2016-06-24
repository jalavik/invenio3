# -*- coding: utf-8 -*-

"""invenio3 base Invenio configuration."""

from __future__ import absolute_import, print_function


# Identity function for string extraction
def _(x):
    return x

# Default language and timezone
BABEL_DEFAULT_LANGUAGE = 'en'
BABEL_DEFAULT_TIMEZONE = 'Europe/Zurich'
I18N_LANGUAGES = [
]

BASE_TEMPLATE = "invenio_theme/page.html"
COVER_TEMPLATE = "invenio_theme/page_cover.html"
SETTINGS_TEMPLATE = "invenio_theme/settings/content.html"

# WARNING: Do not share the secret key - especially do not commit it to
# version control.
SECRET_KEY = "xIgd8IAyQhrdQJz0YK4EaVCdjzi7DhotgEdAJaopoIV5gURnlbxm6o06PQIcyrUW76feCwVBqhuqQiN0hSzzexuhcN18fiMgALoQXMQKnB3paZMxfDP3MmL8uuCWjdmRyaVqarQZxxuroYdLLwm4OtCRbSiJFIkgEfMHsMNCy8JOo1NBDqMjnltdnGtKaPxUCTIiO7MqsjlSGRXpFWazrKhQSpUNsboN0c3dgwbJktttiGyWbh3JITotBUWri8U7"

# Theme
THEME_SITENAME = _("invenio3")


# Files
BASE_FILES_LOCATION = "/Users/jlavik/Envs/inspirehep/var/inspirehep-instance/files"

SEARCH_UI_SEARCH_API = 'invenio_search_ui.api'
SEARCH_UI_BASE_TEMPLATE = 'invenio_theme/page.html'

ASSETS_DEBUG = False

WORKFLOWS_UI_DATA_TYPES = dict(
    hep=dict(
        search_index='workflows-hep',
        search_type='hep',
    ),
    authors=dict(
        search_index='workflows-authors',
        search_type='authors',
    ),
)
WORKFLOWS_OBJECT_CLASS = "invenio_workflows_files.api.WorkflowObject"
