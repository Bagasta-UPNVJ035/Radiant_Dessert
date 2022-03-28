from odoo import api, fields, models


class Package(models.Model):
    _name = 'dessert.package'
    _description = 'Package Dessert is one of the menus in Radiant Dessert with the price'
    
    name = fields.Char(string='Name', required=True)
    drinks_id = fields.Many2one(comodel_name='dessert.drinks', 
                                string='Drinks',
                                required=True)
    icecream_id = fields.Many2one(comodel_name='dessert.icecream', 
                                string='Ice Cream',
                                required=True)
    pack = fields.Selection(string='Type of Package', selection=[('choco pack', 'Chocolate Package'), ('fruit pack', 'Fruit Package')]) 
    desc = fields.Char(string='Package Description')
    
    price = fields.Integer(compute='_compute_price', string='Price')
    
    
    @api.depends('drinks_id', 'icecream_id')
    def _compute_price(self):
        for record in self:
            record.price = record.drinks_id.price + record.icecream_id.price
    
    stock = fields.Integer(string='Package Stock')   
    
    desc_drinks = fields.Char(compute='_compute_desc_drinks', string='Drinks Description')
    
    @api.depends('drinks_id')
    def _compute_desc_drinks(self):
        for record in self:
            record.desc_drinks = record.drinks_id.desc
            
    desc_icecream = fields.Char(compute='_compute_desc_icecream', string='Ice Cream Description')
    
    @api.depends('icecream_id')
    def _compute_desc_icecream(self):
        for record in self:
            record.desc_icecream = record.icecream_id.desc