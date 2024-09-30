from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ApiReturns(models.Model):
    _name = 'ma.api.returns'
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        record = super(ApiReturns, self).create(vals)
        print(f"This is a Id of Record {record.id}")
        return record
