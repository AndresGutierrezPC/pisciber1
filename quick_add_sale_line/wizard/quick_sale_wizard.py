# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp


class QuickSaleWizard(models.TransientModel):
    _name = 'quick.sale.wizard'
    
    wizard_line_ids = fields.One2many(
        'quick.sale.wizard.line',
        'wizard_id',
        string='Wizard',
    )
    total_amount = fields.Float(
        string='Total Amount'
    )
    
    def add_lines(self):
        active_model = self._context.get('active_model', False)
        active_id = self._context.get('active_id', False)
        if active_model == 'sale.order':
            order_id = self.env[active_model].browse(active_id)
        for line in self.wizard_line_ids:
            line_vals = {
                'order_id': order_id.id,
                'product_id' : line.product_id.id,
                'product_uom_qty' : line.quantity,
                'discount':line.discount,
#                 'layout_category_id':line.layout_category_id.id
            }
            order_line = self.env['sale.order.line'].create(line_vals)
            order_line.product_id_change()


class QuickSaleWizardLine(models.TransientModel):
    _name = 'quick.sale.wizard.line'
    
    wizard_id = fields.Many2one(
        'quick.sale.wizard',
        string='Wizard',
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True
    )
    quantity = fields.Float(
        string='Quantity',
        required=True,
        default=1
    )
    price = fields.Float(
        string="Price",
        compute='_get_price'
    )
    sub_total = fields.Float(
        string="Sub Total",
        compute='_get_sub_total'
    )
    discount = fields.Float(
        string='Discount (%)',
        digits=dp.get_precision('Discount'),
        default=0.0
    )
    layout_category_id = fields.Many2one(
        'sale.layout_category',
        string='Section'
    )
    
    @api.depends('product_id')
    def _get_price(self):
        for line in self:
            line.price = line.product_id.lst_price * (1 - (line.discount or 0.0) / 100.0)
        
    @api.depends('product_id', 'discount', 'quantity')
    def _get_sub_total(self):
        for line in self:
            price = line.product_id.lst_price * (1 - (line.discount or 0.0) / 100.0)
            line.sub_total = price * line.quantity

