from odoo import fields, models, api


class SearchReadMethod(models.Model):
    _name = "ma.search.read.method"
    _description = "This is a Search Read Method"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    value = fields.Float(string='Value')

    @api.model
    def search_read_custom(self, name=None, domain=None, fields=['name', 'description'], offset=0, limit=100):
        if domain is None:
            domain = []

        if name is None:
            domain.append(('name', 'ilike', name))

        value_read = self.search_read(domain, fields, offset=offset, limit=limit)
        print(f"********************************{value_read}********************************")
        return value_read
