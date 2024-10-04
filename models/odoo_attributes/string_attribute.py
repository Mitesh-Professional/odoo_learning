from odoo import fields, models

class StringAttribute(models.Model):
    _name = "ma.string.attribute"
    _description = "This is a String attribute"

    name = fields.Char(string='User Name',translate=True)


