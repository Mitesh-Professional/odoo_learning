from odoo import fields, models,api
from odoo.exceptions import ValidationError


class ExceptionHandling(models.Model):
    _name = 'ma.exception.handling'

    name = fields.Char(string="Name")

    def check_name(self):
        for record in self:  # This allows the method to process each record in the recordset
            try:
                if record.name == "Mitesh":
                    raise ValidationError("Success!")
            except ValidationError as e:
                print(f"ValidationError caught: {e}")
                raise  # Reraise the validation error to be caught by Odoo's framework
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                raise ValidationError("An unexpected error occurred.")
            finally:
                print("You Are Model Author")