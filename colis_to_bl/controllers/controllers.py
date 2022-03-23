# -*- coding: utf-8 -*-
# from odoo import http


# class ColisToBl(http.Controller):
#     @http.route('/colis_to_bl/colis_to_bl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/colis_to_bl/colis_to_bl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('colis_to_bl.listing', {
#             'root': '/colis_to_bl/colis_to_bl',
#             'objects': http.request.env['colis_to_bl.colis_to_bl'].search([]),
#         })

#     @http.route('/colis_to_bl/colis_to_bl/objects/<model("colis_to_bl.colis_to_bl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('colis_to_bl.object', {
#             'object': obj
#         })
