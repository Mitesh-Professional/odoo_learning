from odoo import fields, models, api
from odoo.exceptions import ValidationError


class WriteMethod(models.Model):
    _name = "ma.write.method"
    _description = "This is a Write Method"

    name = fields.Char(string='Name', required=True)
    person_age = fields.Integer(string='Age', default=1)

    @api.model
    def create(self, vals):

        if 'person_age' in vals and vals['person_age'] < 18:
            raise ValidationError("You Are Not Eligible")

        record = super(WriteMethod, self).create(vals)
        return record

    @api.model
    def write(self, vals):
        if 'person_age' in vals:
            if vals['person_age'] < 18:
                raise ValidationError("You Are Not Eligible")
        result = super(WriteMethod, self).write(vals)
        return result
