# -*- coding: utf-8 -*-
# from odoo import http


# class DebtorStatus(http.Controller):
#     @http.route('/debtor_status/debtor_status/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/debtor_status/debtor_status/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('debtor_status.listing', {
#             'root': '/debtor_status/debtor_status',
#             'objects': http.request.env['debtor_status.debtor_status'].search([]),
#         })

#     @http.route('/debtor_status/debtor_status/objects/<model("debtor_status.debtor_status"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('debtor_status.object', {
#             'object': obj
#         })
