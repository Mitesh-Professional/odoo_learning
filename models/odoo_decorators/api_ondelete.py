from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ApiOndelete(models.Model):
    _name = 'ma.api.delete'

    name = fields.Char(string="Name")
    related_field = fields.Many2one('ma.api.delete.related.model', string="Related Field")

    @api.ondelete(at_uninstall=False)
    def _unlink_if_related_field(self):
        if self.related_field:
            raise ValidationError("Can't delete this record because it has a related field set.")

class RelatedModel(models.Model):
    _name = 'ma.api.delete.related.model'

    name = fields.Char(string="Name")
