# -*- coding: utf-8 -*-

from odoo import models, fields


class DebtorContact(models.Model):
    _inherit = 'res.partner'

    debtor_status = fields.Many2One(comodel_name='trust')
