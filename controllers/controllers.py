# -*- coding: utf-8 -*-
# from odoo import http


# class RadiantDessert(http.Controller):
#     @http.route('/radiant__dessert/radiant__dessert/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/radiant__dessert/radiant__dessert/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('radiant__dessert.listing', {
#             'root': '/radiant__dessert/radiant__dessert',
#             'objects': http.request.env['radiant__dessert.radiant__dessert'].search([]),
#         })

#     @http.route('/radiant__dessert/radiant__dessert/objects/<model("radiant__dessert.radiant__dessert"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('radiant__dessert.object', {
#             'object': obj
#         })
