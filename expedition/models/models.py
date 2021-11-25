# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class Expedition(models.Model):
    _inherit = 'stock.picking'

    valeur = fields.Char(string="Valeur : ",store=True)#compute="getValue"
    
#     @api.model
#     def getValue(self, data):
#         return 0
    leContext = fields.Char(string="Le Context : ", compute="getContext")
    
    lesInfos = fields.Char(string="Infos : ", compute="getInfo")
        
    def valueTo(self):
        #Affiche la valeur du champ
        _logger.info("Valeur :" + str(self.valeur))
#         _logger.info(self.env['stock.move'].getLine())
        _logger.info(self.env['stock.move'].getIdLine())
        for record in self.move_lines:
            if(record.id == 50):
                record.quantity_done = self.valeur
                
    
    def getContext(self):
        self.leContext = dict(self.env.context)
    
    def getInfo(self):
        tab = []
        for record in self.move_lines:
            tab.append(record.id)
        self.lesInfos = tab
    
    #Identifiant du matériel connecté
    device_id = fields.Many2one('iot.device',string='IoT Device',domain="[('type','=','scanner')]")
    ip = fields.Char(related='device_id.iot_id.ip')
    identifier = fields.Char(related='device_id.identifier')
    
class StockMove(models.Model):
    _inherit = 'stock.move'
  
    
    def _quantity_done_set(self):
        _logger.info("ID de la ligne : " + str(self.getIdLine()))
        res = super(StockMove, self)._quantity_done_set()
        return res
    
    def getIdLine(self):
        return self.id
    