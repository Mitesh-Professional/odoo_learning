from odoo import fields, models

class Name(models.Model):
    # it important attribute for us it's define a model
    _name = "ma.name"
    _description = "_name is model name."