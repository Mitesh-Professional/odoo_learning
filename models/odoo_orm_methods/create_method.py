from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CreateMethod(models.Model):
    _name = "ma.create.method"
    _description = "This is a Create Method"

    name = fields.Char(string='Name', required=True)
    person_age = fields.Integer(string='Age', default=1)

    @api.model
    def create(self, vals):
        records = super(CreateMethod, self).create(vals)

        for record in records:
            if record.person_age<18:
                raise ValidationError("You Are Not Eligible")
            else:
                return records


