from odoo import fields, models

class RequiredAttribute(models.Model):
    _name = "ma.required.attribute"
    _description = "This is a required attribute"

    name = fields.Char(string='Name', required=True)


