# -*- coding: utf-8 -*-

"""invenio3 Invenio sample receivers."""

from __future__ import absolute_import, print_function

from flask import current_app

from os.path import exists
from os import makedirs

from invenio_files_rest.models import Location
from invenio_db import db


def loadlocation(force=False):
    """Load default file store location."""
    try:
        uri = current_app.config['BASE_FILES_LOCATION']
        if uri.startswith('/') and not exists(uri):
            makedirs(uri)
        loc = Location(name='default', uri=uri, default=True, )
        db.session.add(loc)
        db.session.commit()
        return loc
    except Exception:
        db.session.rollback()
        raise
