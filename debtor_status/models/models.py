from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.product'
    _rec_name = 'name'