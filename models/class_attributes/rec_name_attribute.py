from odoo import fields, models

class RecName(models.Model):
    _name = "ma.rec.name"
    _description = "the _rec_name attribute specifies the field that will be used as the display name for records of the model."
    _rec_name = "name"

    name = fields.Char(string="Enter Your Name")