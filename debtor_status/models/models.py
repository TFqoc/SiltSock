from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.product'
    
    @api.multi
    def name_get(self):
        res = []
        for record in self:
            name = str(record.name)
            res.append((record.id, name))
        return res