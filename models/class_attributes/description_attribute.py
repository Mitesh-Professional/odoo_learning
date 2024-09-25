from odoo import fields, models

class Description(models.Model):
    # it important attribute for us it's define a model description
    _name = "ma.description"
    _description = "_description is model details."