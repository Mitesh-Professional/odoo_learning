from odoo import fields, models, api


class SearchMethod(models.Model):
    _name = "ma.search.count.method"
    _description = "This is a Search Method"

    name = fields.Char(string='Name', required=True)
    total_entries = fields.Integer(string='Total Entries',readonly=1, default=0, compute="_id_create")

    def _id_create(self):
        search_value = self.env['ma.search.count.method'].search_count([])
        self.total_entries = search_value