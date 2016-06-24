# -*- coding: utf-8 -*-

"""invenio3 Invenio sample action."""

from __future__ import absolute_import, print_function

from flask import url_for, render_template

from flask_babelex import gettext as _

from invenio_db import db


class Approval(object):
    """Class representing the approval action."""

    def __init__(self):
        self.name = _("Approve")

    def render_mini(self, obj):
        """Method to render the minified action."""
        return render_template(
            'actions/approval_mini.html',
            message=obj.get_action_message(),
            object=obj,
        )

    def render(self, obj):
        """Method to render the action."""
        return {
            "side": render_template('actions/approval_side.html',
                                    message=obj.get_action_message(),
                                    object=obj),
            "main": render_template('actions/approval_main.html',
                                    message=obj.get_action_message(),
                                    object=obj)
        }

    def resolve(self, bwo):
        """Resolve the action taken in the approval action."""
        from flask import request
        value = request.form.get("value", None)

        bwo.remove_action()
        if value == 'accept':
            bwo.extra_data["approved"] = True
            message = "Record has been accepted!"
            category = "success"
        elif value == 'reject':
            bwo.extra_data["approved"] = True
            message = "Record has been rejected (deleted)"
            category = "danger"
        bwo.continue_workflow(delayed=True)

        return {
            "message": message,
            "category": category
        }

__all__ = ('Approval',)
