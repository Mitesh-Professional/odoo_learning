from odoo import fields, models

class ReadMethod(models.Model):
    _name = "ma.read.method"
    _description = "This is a Read Method"

    name = fields.Char(string='Name', required=True)
    person_age = fields.Integer(string='Age', default=1)

    def read_method(self):
        read_value = self.env['ma.read.method'].search([])
        print(f"****************************{read_value.read(['name'])}****************************")
