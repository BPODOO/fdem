# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class Expedition(models.Model):
    _inherit = 'stock.picking'

    valeur = fields.Char(string="Valeur de la balance : ",store=True)# Mettre le champ en readonly="True" ?
    
    leContext = fields.Char(string="Le Context : ", compute="getContext")
    
    lesInfos = fields.Char(string="Infos : ", compute="getInfo")
        
    def valueTo(self):
        #Affiche la valeur du champ
#         _logger.info("Valeur :" + str(self.valeur))
#         _logger.info(self.env['stock.move'].getLine())
#         _logger.info(self.env['stock.move'].getIdLine())
#         for record in self.move_lines:
#             if(record.id == 1159):
#                 record.quantity_done = self.valeur
        return True

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
  
    def getPoids(self):
        #Affiche l'id du picking //Le BL actuel à traiter
        _logger.info(self.picking_id.id)
        #Récupère le BL
        leBl = self.env['stock.picking'].search([('id','=',self.picking_id.id)])
        #Affiche la valeur de la balance dans le BL
        _logger.info(leBl.valeur)
        if(leBl):
            self.quantity_done = leBl.valeur
        else:
            raise ValidationError("Aucun Bon de Livraison détecté !")