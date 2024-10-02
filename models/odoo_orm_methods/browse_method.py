from odoo import fields, models

class BrowseMethod(models.Model):
    _name = "ma.browse.method"
    _description = "This is a Browse Method"

    name = fields.Char(string='Name', required=True)
    person_age = fields.Integer(string='Age', default=1)

    def get_record(self):
        search_value = self.env['ma.browse.method'].browse(self.id)

        print(f"*******************{search_value.name}************************")
