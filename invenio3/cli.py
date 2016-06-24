# -*- coding: utf-8 -*-

"""invenio3 base Invenio configuration."""

from __future__ import absolute_import, print_function

import click
import os

from flask_cli import with_appcontext

from invenio_base.app import create_cli

from .factory import create_app

cli = create_cli(create_app=create_app)


@click.group()
def fixtures():
    """Command related to migrating INSPIRE data."""


@fixtures.command()
@with_appcontext
def init():
    """Init the system with fixtures."""
    from invenio_files_rest.models import Location
    from flask import current_app
    from invenio_db import db
    try:
        uri = current_app.config['BASE_FILES_LOCATION']
        if uri.startswith('/') and not os.path.exists(uri):
            os.makedirs(uri)
        loc = Location(
            name="default",
            uri=uri,
            default=True
        )
        db.session.add(loc)
        db.session.commit()
        return loc
    except Exception:
        db.session.rollback()
        raise

    try:
        uri = current_app.config['WORKFLOWS_FILE_LOCATION']
        if uri.startswith('/') and not os.path.exists(uri):
            os.makedirs(uri)
        loc = Location(
            name=current_app.config["WORKFLOWS_DEFAULT_FILE_LOCATION_NAME"],
            uri=uri,
            default=False
        )
        db.session.add(loc)
        db.session.commit()
        return loc
    except Exception:
        db.session.rollback()
        raise

cli.add_command(fixtures)
