from odoo import fields, models

class IndexAttribute(models.Model):
    _name = "ma.index.attribute"
    _description = "This is a index attribute"

    name = fields.Char(string='Name', index=True)


