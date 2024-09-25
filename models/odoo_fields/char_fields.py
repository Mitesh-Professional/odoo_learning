from odoo import fields,models

class CharField(models.Model):
    _name = "ma.char.field"
    _description = "This is Char Fields"

    first_name = fields.Char(string='Enter First Name:-')