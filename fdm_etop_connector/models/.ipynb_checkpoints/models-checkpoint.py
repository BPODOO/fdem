# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

import requests

class StockMove(models.Model):
    _inherit =  "stock.move"
    
    def action_call_balance(self):
        response = requests.get("https://random-data-api.com/api/v2/beers",params={})
        json_response = response.json()
        self.product_uom_qty = json_response['id']
        return
