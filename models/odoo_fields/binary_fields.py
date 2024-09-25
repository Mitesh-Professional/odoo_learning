from odoo import fields,models

class BinaryField(models.Model):
    _name = "ma.binary.field"
    _description = "This is Binary Fields"

    first_name = fields.Binary(string='Enter First Name:-')
    file_name = fields.Char("File Name")