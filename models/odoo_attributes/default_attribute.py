from odoo import fields, models

class DefaultAttribute(models.Model):
    _name = "ma.default.attribute"
    _description = "This is a default attribute"

    name = fields.Char(string='Name', default="Your Name")


