# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

import requests

class StockMove(models.Model):
    _inherit =  "stock.move.line"
    
    bp_old_value_qty_done = fields.Float()
    
    def action_call_balance(self):
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1",params={})
        json_response = response.json()
        self.bp_old_value_qty_done = self.qty_done
        self.qty_done = json_response['id']

    
    # def action_old_value(self):
    #     self.qty_done = self.bp_old_value_qty_done
        
    def action_reset_line(self):
        self.qty_done = 0.0