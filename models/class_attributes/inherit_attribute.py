from odoo import fields, models

class Inherit(models.Model):
    _name="ma.inherit"
    _description = "This Is Inherit Field."

    name= fields.Text("Enter Your Name:-")


class Profile(models.Model):
    _name="ma.inherited"
    _description="This inherited Field"
    _inherit = ['ma.inherit']

    address= fields.Text(string="Enter Your Address")