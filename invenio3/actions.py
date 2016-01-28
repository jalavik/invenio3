# -*- coding: utf-8 -*-

"""invenio3 Invenio sample action."""

from __future__ import absolute_import, print_function

from flask import url_for, render_template

from flask_babelex import gettext as _


class Approval(object):
    """Class representing the approval action."""

    def __init__(self):
        self.name = _("Approve")
        self.url = url_for("invenio_workflows_ui.resolve_action")

    def render_mini(self, obj):
        """Method to render the minified action."""
        return render_template(
            'actions/approval_mini.html',
            message=obj.get_action_message(),
            object=obj,
            resolve_url=self.url,
        )

    def render(self, obj):
        """Method to render the action."""
        return {
            "side": render_template('actions/approval_side.html',
                                    message=obj.get_action_message(),
                                    object=obj,
                                    resolve_url=self.url,),
            "main": render_template('actions/approval_main.html',
                                    message=obj.get_action_message(),
                                    object=obj,
                                    resolve_url=self.url,)
        }

    def resolve(self, bwo):
        """Resolve the action taken in the approval action."""
        from flask import request
        value = request.form.get("value", None)

        bwo.remove_action()
        extra_data = bwo.get_extra_data()

        if value == 'accept':
            extra_data["approved"] = True
            bwo.set_extra_data(extra_data)
            bwo.save()
            bwo.continue_workflow(delayed=True)
            return {
                "message": "Record has been accepted!",
                "category": "success",
            }
        elif value == 'reject':
            extra_data["approved"] = False
            bwo.set_extra_data(extra_data)
            bwo.save()
            bwo.continue_workflow(delayed=True)
            return {
                "message": "Record has been rejected (deleted)",
                "category": "warning",
            }

__all__ = ('Approval',)
