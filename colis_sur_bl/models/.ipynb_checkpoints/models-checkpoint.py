# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)



class StockMoveLine(models.Model):
    _inherit="stock.move.line"
    product_packaging=fields.Many2one('product.packaging','Colis', copy=True)

    
class SaleOrder(models.Model):
    _inherit='sale.order'
    
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for so in self:
            if so.picking_ids.mapped('id'):
                sml=self.env['stock.move.line'].search([('picking_id','in',so.picking_ids.mapped('id'))])
                treated_ids=[]
                for i in so.order_line:
                    stock_lines=sml.filtered(lambda x: x.product_id==i.product_id and not x.product_packaging and x.id not in treated_ids)
                    if len(stock_lines)>1:
                        if sum(stock_lines.mapped('product_uom_qty')) == i.product_uom_qty:
                            stock_lines.product_packaging =i.product_packaging.id
                            treated_ids+=stock_lines.mapped('id')  
                        elif sum(stock_lines.mapped('product_uom_qty')) > i.product_uom_qty:
                            c=i.product_uom_qty
                            item=0
                            while c > 0:
                                stock_lines[item].product_packaging = i.product_packaging.id
                                treated_ids.append(stock_lines[item].id)
                                c+=-stock_lines[item].product_uom_qty
                                item+=1       
                    elif len(stock_lines)==1:
                        stock_lines.product_packaging =i.product_packaging.id
                        treated_ids.append(stock_lines.id)       
        return res

    
class BOG(models.TransientModel):
    _inherit="stock.backorder.confirmation"

    def process(self):
        res = super(BOG, self).process()
        for record in self:
            bl=record.pick_ids
            sol=self.env['sale.order.line'].search([('order_id.name',"=",bl.origin)])
            sol=sol.filtered(lambda x: x.product_uom_qty-x.qty_delivered > 0 and x.qty_delivered!=0)
            qtys=sol.mapped(lambda x: x.product_uom_qty-x.qty_delivered)
            prod_ids=sol.mapped('product_id')
            sml=self.env['stock.move.line'].search([('origin','=',bl.origin),('product_id.id','in',prod_ids.mapped('id')),("product_uom_qty",'in',qtys),('state','not in',['done','cancel'])])
            treated_ids=[]
            for i in sol:
                stock_lines=sml.filtered(lambda x: x.product_id==i.product_id and not x.product_packaging and x.id not in treated_ids)
                if len(stock_lines)>1:
                    if sum(stock_lines.mapped('product_uom_qty')) == i.product_uom_qty - i.qty_delivered:
                        stock_lines.product_packaging =i.product_packaging.id
                        treated_ids+=stock_lines.mapped('id')  
                    elif sum(stock_lines.mapped('product_uom_qty')) > i.product_uom_qty - i.qty_delivered:
                        c=i.product_uom_qty - i.qty_delivered
                        item=0
                        while c > 0:
                            stock_lines[item].product_packaging = i.product_packaging.id
                            treated_ids.append(stock_lines[item].id)
                            c+=-stock_lines[item].product_uom_qty
                            item+=1
                elif len(stock_lines)==1:
                    stock_lines.product_packaging =i.product_packaging.id
                    treated_ids.append(stock_lines.id)

        return res
    
class StockPickings(models.Model):
    _inherit='stock.picking'
    
    def action_assign(self):
        res = super(StockPickings, self).action_assign()
        for record in self:
            sol=self.env['sale.order.line'].search([('order_id.name',"=",record.origin)])
            sol=sol.filtered(lambda x: x.product_uom_qty-x.qty_delivered > 0 and x.qty_delivered!=0)
            sml=record.move_line_ids_without_package
            treated_ids=[]
            for i in sol:
                _logger.info(i.product_id.name)
                stock_lines=sml.filtered(lambda x: x.product_id==i.product_id and not x.product_packaging and x.id not in treated_ids).sorted(key=lambda x:x.id)
                _logger.info(stock_lines)
                if len(stock_lines)>1:
                    _logger.info(1)
                    if sum(stock_lines.mapped('product_uom_qty')) == i.product_uom_qty - i.qty_delivered:
                        _logger.info(1.1)
                        stock_lines.product_packaging =i.product_packaging.id
                        treated_ids+=stock_lines.mapped('id')  
                    elif sum(stock_lines.mapped('product_uom_qty')) > i.product_uom_qty - i.qty_delivered:
                        _logger.info(1.2)
                        c=i.product_uom_qty - i.qty_delivered
                        _logger.info(c)
                        item=0
                        while c > 0:
                            _logger.info(c)
                            _logger.info(stock_lines[item].product_uom_qty)
                            stock_lines[item].product_packaging = i.product_packaging.id
                            treated_ids.append(stock_lines[item].id)
                            c+=-stock_lines[item].product_uom_qty
                            item+=1
                elif len(stock_lines)==1:
                    _logger.info(2)
                    stock_lines.product_packaging =i.product_packaging.id
                    treated_ids.append(stock_lines.id)
                        
        return res
