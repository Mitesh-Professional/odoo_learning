from odoo import fields,models

class CharField(models.Model):
    _name = "ma.float.field"
    _description = "This is float Fields"

    user_avg_presents = fields.Char(string='Enter Your Presents:-', default="0.0")