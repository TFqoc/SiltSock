# -*- coding: utf-8 -*-

from odoo import models, fields


class DebtorContact(models.Model):
    _inherit = 'res.partner'
    _name = 'debtor.status'

    debtor_status = fields.Many2one(comodel_name='trust')
