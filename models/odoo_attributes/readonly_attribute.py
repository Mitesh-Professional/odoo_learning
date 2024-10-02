from odoo import fields, models

class ReadOnlyAttribute(models.Model):
    _name = "ma.readonly.attribute"
    _description = "This is a readonly attribute"

    name = fields.Char(string='User Name', default = "This is ReadOnly Field And Achieved by Readonly Attribute", readonly=True)


