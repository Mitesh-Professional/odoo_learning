from odoo import fields, models

class CopyMethod(models.Model):
    _name = "ma.copy.method"
    _description = "This is a Copy Method"

    name = fields.Char(string='Name', required=True)
    person_age = fields.Integer(string='Age', default=1)

    def copy_method(self):
        copy_value = self.env['ma.copy.method'].browse(self.id)
        copy_value.copy()