from odoo import fields, models

class HelpAttribute(models.Model):
    _name = "ma.help.attribute"
    _description = "This is a help attribute"

    name = fields.Char(string='Name', help="This is Help Attribute")


