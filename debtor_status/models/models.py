# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class debtor_status(models.Model):
#     _name = 'debtor_status.debtor_status'
#     _description = 'debtor_status.debtor_status'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
