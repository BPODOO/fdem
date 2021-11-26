# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class colis_sur_bl(models.Model):
#     _name = 'colis_sur_bl.colis_sur_bl'
#     _description = 'colis_sur_bl.colis_sur_bl'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
