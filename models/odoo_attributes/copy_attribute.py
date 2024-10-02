from odoo import fields, models

class CopyAttribute(models.Model):
    _name = "ma.copy.attribute"
    _description = "This is a copy attribute"

    name = fields.Char(string='Name', copy=False)

