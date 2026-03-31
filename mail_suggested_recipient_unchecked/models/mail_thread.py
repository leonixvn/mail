# Copyright 2025 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _message_add_suggested_recipients(self, force_primary_email=False):
        suggested = super()._message_add_suggested_recipients(
            force_primary_email=force_primary_email
        )
        for rec in self:
            suggested[rec.id]['partners'] = self.env['res.partner']
            suggested[rec.id]['email_to_lst'] = []
        return suggested
