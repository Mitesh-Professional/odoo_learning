from odoo import fields, models

class Order(models.Model):
    _name = "ma.order"
    _description = "allowing you to control how records are displayed in lists."
    _order = "name asc"

    name = fields.Char(string="Enter Your Name")