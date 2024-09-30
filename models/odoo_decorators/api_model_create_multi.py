from odoo import models, fields, api

class ApiModelCreateMulti(models.Model):
    _name = 'ma.api.model.create.multi'

    name = fields.Char(string='Name')
    value = fields.Integer(string='Value')

    @api.model_create_multi
    def create(self, vals_list):
        records = super(ApiModelCreateMulti, self).create(vals_list)
        return records

    @api.model
    def create_multiple_records(self,*args):
        data = [
            {'name': 'Record 1', 'value': 10},
            {'name': 'Record 2', 'value': 20},
            {'name': 'Record 3', 'value': 30},
        ]
        self.create(data)
