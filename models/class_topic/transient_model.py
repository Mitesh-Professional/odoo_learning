from odoo import fields,models

class User(models.Model):
    _name="ma.user.info"
    _description = "This model make for learning a Transient Model."

    enter_name = fields.Char(string="Enter User Name")