from odoo import fields,models

class BooleanField(models.Model):
    _name = "ma.boolean.field"
    _description = "This is Char Fields"

    you_are_above_18 = fields.Boolean(string='Your Are Above 18:-')