from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ApiReturns(models.Model):
    _name = 'ma.api.returns'
    _description = "The @api.returns decorator in Odoo specifies the return type of a method, ensuring that the method outputs the expected data format or model instance."
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        record = super(ApiReturns, self).create(vals)
        print(f"This is a Id of Record {record.id}")
        return record
