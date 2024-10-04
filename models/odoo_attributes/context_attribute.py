from odoo import fields, models, api

class ContextAttribute(models.Model):
    _name = "ma.context.attribute"
    _description = "This is a context attribute"

    name_value = fields.Char(string='User Name', default ="", readonly=True)

    @api.model
    def create(self,vale):
        if 'name' in self.env.context:
            vale['name_value'] = self.env.context['name']
            return super(ContextAttribute,self).create(vale)