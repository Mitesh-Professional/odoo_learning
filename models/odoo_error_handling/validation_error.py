from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError, RedirectWarning
import logging

_logger = logging.getLogger(__name__)

class Validation(models.Model):
    _name = 'ma.validation.handling'
    _description = 'Validation Handling Example'

    name = fields.Char(string="Name")

    @api.constrains('name')
    def check_name(self):
        for record in self:  # Process each record in the recordset
            match record.name:
                case "Validation Error":
                    raise ValidationError("This is a Validation Error")
                case "User Error":
                    raise UserError("This is a User Error")
                case "Redirect Error":
                    # Provide the required arguments for RedirectWarning
                    action = {
                        'type': 'ir.actions.act_url',
                        'url': 'https://www.odoo.com/documentation/17.0/',  # Replace with the actual URL to redirect to
                        'target': 'self',
                    }
                    raise RedirectWarning(action=action, button_text='Go to Action', message="This is a Redirect Error")
                case "Warning Error":
                    _logger.warning("This is a Warning Error for record: %s", record.name)
                    raise UserError("This is a Warning Error, but the process will continue.")
