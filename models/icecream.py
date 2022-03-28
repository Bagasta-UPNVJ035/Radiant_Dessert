from odoo import api, fields, models


class IceCream(models.Model):
    _name = 'dessert.icecream'
    _description = 'Ice Cream is one of the menus in Radiant Dessert with the price'

    name = fields.Char(string='Ice Cream Name')
    desc = fields.Char(string='Ice cream Description')
    price = fields.Integer(string='Price')
    stock = fields.Integer(string='Stock')
    