# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

import requests

class StockMove(models.Model):
    _inherit =  "stock.move.line"
    
    bp_old_value_qty_done = fields.Float()
    
    def action_call_balance(self):
        response = requests.get("http://86.201.126.45:7878/site/etq_hst_cab?reverse=1&limit=1",params={})
        json_response = response.json()
        self.bp_old_value_qty_done = self.qty_done
        self.qty_done = json_response[0]['liquido']

    
    # def action_old_value(self):
    #     self.qty_done = self.bp_old_value_qty_done
        
    def action_reset_line(self):
        self.qty_done = 0.0