from odoo import fields,models

class FormView(models.Model):
    _name="ma.form.view"
    _description = "This is Form View."

    name = fields.Char("Enter Your Name")
    age = fields.Integer("Enter your Age")

    def action_confirm(self):
        pass
