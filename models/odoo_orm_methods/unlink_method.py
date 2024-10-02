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
        delete_record = self.filtered(lambda r: r.person_age >= 50)
        if delete_record:
            return super(UnlinkMethod,delete_record).unlink()
        else:
            raise ValidationError("This Data Can't Be Deleted.")
        return True