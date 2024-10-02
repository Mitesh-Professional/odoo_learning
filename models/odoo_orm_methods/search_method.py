from odoo import fields, models

class SearchMethod(models.Model):
    _name = "ma.search.method"
    _description = "This is a Search Method"

    name = fields.Char(string='Name', required=True)
    person_age = fields.Integer(string='Age', default=1)

    def search_method(self):
        search_value = self.env['ma.search.method'].search([])
        for value in search_value:
            print(f"************************{value.name}********************************")

