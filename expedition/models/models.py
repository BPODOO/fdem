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
        for record in self.move_line_ids:
            tab.append(record.id)
        self.lesInfos = tab
    
#     def print_report(self):
#         _logger.info("IN PRINT stock picking")
#         data = {
#             'id': self.id,
#         }
#         return self.env.ref('expedition.report_etiquette_view').report_action(self, data=data)
    
    #Identifiant du matériel connecté
    device_id = fields.Many2one('iot.device',string='IoT Device',domain="[('type','=','scanner')]")
    ip = fields.Char(related='device_id.iot_id.ip')
    identifier = fields.Char(related='device_id.identifier')
    
    
class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    
    def printEtiquette(self, leBl):
        _logger.info("IN PRINT stock move")
    
#         _logger.info(leBl.id)
#         _logger.info(self.product_id.list_price)
        _logger.info(self.move_id.sale_line_id.price_unit)
        prix = self.move_id.sale_line_id.price_unit
        devise = self.product_id.currency_id.symbol
        _logger.info(devise)
        data = {
            'id': self.id,
            'id_bl': leBl.id,
            'article_name' : self.product_id.name,
            'poids' : leBl.valeur,
#             'prixKg' : self.product_id.list_price
        }
        return self.env.ref('expedition.report_etiquette_view').report_action(self, data=data)
       
    
    def getPoids(self):
        #Récupère le BL
        leBl = self.env['stock.picking'].search([('id','=',self.picking_id.id)])
        
        #Affiche l'id du picking //Le BL actuel à traiter
        _logger.info(self.picking_id.id)
        
        #Affiche la valeur de la balance dans le BL
        _logger.info(leBl.valeur)
        #Retourne normalement toujours TRUE mais on sait jamais
        if(leBl):
            #Stockage de la valeur précédente en cas d'erreur de saisie ?
            previousValue = self.qty_done
            #Ajoute la nouvelle quantité à celle déjà faite
            self.qty_done = float(self.qty_done) + float(leBl.valeur)
        else:
            raise ValidationError("Aucun Bon de Livraison détecté !")
            
        #Enregistre l'article actuel et le poids balance pour l'étiquette
        print = self.printEtiquette(leBl)
        if(print != None):   
            return print