# -*- coding: utf-8 -*-
# from odoo import http


# class Expedition(http.Controller):
#     @http.route('/expedition/expedition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/expedition/expedition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('expedition.listing', {
#             'root': '/expedition/expedition',
#             'objects': http.request.env['expedition.expedition'].search([]),
#         })

#     @http.route('/expedition/expedition/objects/<model("expedition.expedition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('expedition.object', {
#             'object': obj
#         })
