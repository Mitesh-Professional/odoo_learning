from odoo import fields,models

class TextField(models.Model):
    _name = "ma.text.field"
    _description = "This is Text Fields"

    first_name = fields.Char(string='Enter First Name:-')
    last_name = fields.Char(string='Enter Last Name:-')
