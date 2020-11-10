# -*- coding: utf-8 -*-

from odoo import models, fields


class DebtorContact(models.Model):
    _inherit = 'res.partner'
    _name = 'debtor.status'
    _description = "Adds the trust field to the contact page"

    debtor_status = fields.Many2one(comodel_name='trust')
