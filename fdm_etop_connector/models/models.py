# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class fdm_etop_connector(models.Model):
#     _name = 'fdm_etop_connector.fdm_etop_connector'
#     _description = 'fdm_etop_connector.fdm_etop_connector'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
