import logging
from odoo import fields, models, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class UnlinkMethod(models.Model):
    _name = "ma.unlink.method"
    _description = "This is a Unlink Method"

    name = fields.Char(string='Name', required=True)
    person_age = fields.Integer(string='Age', default=1)


    @api.model
    def create(self, vals):
        if 'person_age' in vals and vals['person_age'] < 18:
            raise ValidationError("You Are Not Eligible")
        record = super(UnlinkMethod, self).create(vals)
        return record

    @api.model
    def write(self, vals):
        if 'person_age' in vals and vals['person_age'] < 18:
            raise ValidationError("You Are Not Eligible")
        result = super(UnlinkMethod, self).write(vals)
        return result

    def unlink(self):
        invalid_records = self.filtered(lambda r: r.person_age <= 50)
        valid_records = self.filtered(lambda r: r.person_age >= 50)
        # print(f"*********************************************{valid_records}*********************************************")
        if valid_records:
            return super(UnlinkMethod, valid_records).unlink()
        elif invalid_records:
            error_message = "You are not eligible to delete records with age 50 or below. Invalid record IDs: " + ", ".join(map(str, invalid_records.ids))
            raise ValidationError(error_message)
        return True