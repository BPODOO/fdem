# -*- coding: utf-8 -*-
# from odoo import http


# class FdemFields(http.Controller):
#     @http.route('/fdem_fields/fdem_fields', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fdem_fields/fdem_fields/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fdem_fields.listing', {
#             'root': '/fdem_fields/fdem_fields',
#             'objects': http.request.env['fdem_fields.fdem_fields'].search([]),
#         })

#     @http.route('/fdem_fields/fdem_fields/objects/<model("fdem_fields.fdem_fields"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fdem_fields.object', {
#             'object': obj
#         })
