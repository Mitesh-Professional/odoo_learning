from odoo import fields,models

class IntegerField(models.Model):
    _name = "ma.integer.field"
    _description = "This is Char Fields"

    user_age = fields.Integer(string='Enter Your Age:-')