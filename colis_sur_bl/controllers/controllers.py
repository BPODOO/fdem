# -*- coding: utf-8 -*-
# from odoo import http


# class ColisSurBl(http.Controller):
#     @http.route('/colis_sur_bl/colis_sur_bl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/colis_sur_bl/colis_sur_bl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('colis_sur_bl.listing', {
#             'root': '/colis_sur_bl/colis_sur_bl',
#             'objects': http.request.env['colis_sur_bl.colis_sur_bl'].search([]),
#         })

#     @http.route('/colis_sur_bl/colis_sur_bl/objects/<model("colis_sur_bl.colis_sur_bl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('colis_sur_bl.object', {
#             'object': obj
#         })
