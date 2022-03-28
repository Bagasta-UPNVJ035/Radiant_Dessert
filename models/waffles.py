from odoo import api, fields, models


class Waffles(models.Model):
    _name = 'dessert.waffles'
    _description = 'Waffles is one of the menu in Radiant Dessert. this models contains data about waffles and the price'

    name = fields.Char(string='Waffles Name')
    type = fields.Selection(string='Type of Waffles', selection=[('choco', 'Choco'),('fruit', 'Fruit'),('other', 'Others')])
    stock = fields.Integer('Stock')
    price = fields.Integer('Price')
    
    
