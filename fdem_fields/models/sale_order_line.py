# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

import logging

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit='sale.order.line'

    @api.onchange('product_packaging_id')
    def _onchange_product_packaging_id(self):
        #Désactivation de la fenêtre d'avertissement
        unactive = True