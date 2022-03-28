from odoo import api, fields, models


class Drinks(models.Model):
    _name = 'dessert.drinks'
    _description = 'Drinks is one of the menu in Radiant Dessert. this models contain is name, desc, price'

    name = fields.Char(string='Drink Name')
    desc = fields.Char(string='Description of Drink')
    price = fields.Integer(string='Price')
    stock = fields.Integer(string='Ice Cream Stock')
    