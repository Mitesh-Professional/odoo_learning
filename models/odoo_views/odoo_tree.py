from odoo import fields,models

class TreeView(models.Model):
    _name="ma.tree.view"
    _description = "This is Tree View."

    name = fields.Char("Enter Your Name")
    age = fields.Integer("Enter your Age")

