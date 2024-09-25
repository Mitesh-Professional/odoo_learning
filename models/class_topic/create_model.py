from odoo import fields,models

class CreateModel(models.Model):
    _name="ma.create.model"
    _description = "This Model Create by Mitesh Amin. For Fresher"
    _rec_name = "name"

    name = fields.Char(string="Enter Name.")