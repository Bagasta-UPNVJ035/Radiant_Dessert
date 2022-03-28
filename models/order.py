from odoo import api, fields, models


class Order(models.Model):
    _name = 'dessert.order'
    _description = 'New Description'

    orderpackagedetail_ids = fields.One2many(
        comodel_name='dessert.order_packagedetail',
        inverse_name='order_id',
        string='Order Package Detail')
    
    orderwafflesdetail_ids = fields.One2many(
        comodel_name='dessert.order_wafflesdetail',
        inverse_name='orderw_id',
        string='Order Waffles Detail')

    
    name = fields.Char(string='Order Code', required=True)
    order_date = fields.Datetime(string='Order Date', default=fields.Datetime.now())
    
    total = fields.Integer(compute='_compute_total', string='Total Price', store=True)
    
    @api.depends('orderpackagedetail_ids', 'orderwafflesdetail_ids')
    def _compute_total(self):
        for record in self:
            totals_package = sum(self.env['dessert.order_packagedetail'].search([('order_id', '=', record.id)]).mapped('total_price'))
            totals_waffles = sum(self.env['dessert.order_wafflesdetail'].search([('orderw_id', '=', record.id)]).mapped('total_price'))
            record.total = totals_package + totals_waffles

    

class OrderPackageDetail(models.Model):
    _name = 'dessert.order_packagedetail'
    _description = 'New Description'
    
    order_id = fields.Many2one(comodel_name='dessert.order', string='Package Order')
    package_id = fields.Many2one(comodel_name='dessert.package', string='Package')
    
    name = fields.Selection(string='Name', selection=[('package', 'Package'),('waffles', 'Waffles'),('icecream', 'Ice Cream')])
    total_price = fields.Integer(compute='_compute_total_price', string='Total Price')
    qty = fields.Integer(string='Quantity')
    price_pcs = fields.Integer(compute='_compute_price_pcs', string='Price / Pcs')
    
    @api.depends('package_id')
    def _compute_price_pcs(self):
        for record in (self):
            record.price_pcs = record.package_id.total_price 
    
    
    @api.depends('qty', 'price_pcs')
    def _compute_total_price(self):
        for record in self:
            record.total_price= record.price_pcs * record.qty 


    @api.model
    def create(self,vals):
        record = super(OrderPackageDetail, self).create(vals)
        if record.qty:
            self.env['dessert.package'].search([('id', '=', record.package_id.id)]).write({'stock':record.package_id.stock - record.qty})
            return record
        

class OrderWafflesDetail(models.Model):
    _name = 'dessert.order_wafflesdetail'
    _description = 'New Description'
    
    orderw_id = fields.Many2one(comodel_name='dessert.order', string='Order Waffles')
    waffles_id = fields.Many2one(comodel_name='dessert.waffles', string='waffles')
    
    name = fields.Selection(string='Name', selection=[('package', 'Package'),('waffles', 'Waffles'),('icecream', 'Ice Cream')]) 
    price_pcs = fields.Integer(compute='_compute_price_pcs', string='Price / Pcs')
    
    @api.depends('waffles_id')
    def _compute_price_pcs(self):
        for record in (self):
            record.price_pcs = record.waffles_id.price 
    
    qty = fields.Integer(string='Quantity')
    
    total_price = fields.Integer(compute='_compute_total_price', string='Total Price')
    
    @api.depends('qty', 'price_pcs')
    def _compute_total_price(self):
        for record in self:
            record.total_price= record.price_pcs * record.qty 


    @api.model
    def create(self,vals):
        record = super(OrderWafflesDetail, self).create(vals)
        if record.qty:
            self.env['dessert.waffles'].search([('id', '=', record.waffles_id.id)]).write({'stock':record.waffles_id.stock - record.qty})
            return record

