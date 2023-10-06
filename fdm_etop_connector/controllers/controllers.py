# -*- coding: utf-8 -*-
# from odoo import http


# class FdmEtopConnector(http.Controller):
#     @http.route('/fdm_etop_connector/fdm_etop_connector/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fdm_etop_connector/fdm_etop_connector/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fdm_etop_connector.listing', {
#             'root': '/fdm_etop_connector/fdm_etop_connector',
#             'objects': http.request.env['fdm_etop_connector.fdm_etop_connector'].search([]),
#         })

#     @http.route('/fdm_etop_connector/fdm_etop_connector/objects/<model("fdm_etop_connector.fdm_etop_connector"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fdm_etop_connector.object', {
#             'object': obj
#         })
