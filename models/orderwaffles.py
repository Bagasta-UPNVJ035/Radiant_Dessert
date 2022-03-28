from odoo import api, fields, models


class OrderWaffles(models.Model):
    _name = 'dessert.orderwaffles'
    _description = 'New Description'

    name = fields.Char(string='Order Code')


class OrderWafflesDetail(models.Model):
    _name = 'dessert.orderwafflesdetail'
    _description = 'New Description'

    name = fields.Char(string='Name')

