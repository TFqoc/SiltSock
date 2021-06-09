from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.product'
    
    @api.multi
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, record.name))
        return res