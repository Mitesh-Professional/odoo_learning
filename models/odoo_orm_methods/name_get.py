from odoo import fields, models, api


class NameGetMethod(models.Model):
    _name = "ma.name.get.method"
    _description = "This is a Name Get Method"

    name = fields.Char(string='Name', required=True)
    user = fields.Many2one("ma.read.group.method", string='Name', required=True)

    # def _compute_display_name(self):
    #     for vals in self:
    #         vals.display_name = f"[{vals.name} {vals.gender}]"
    # Check read_group Model it Make more Clear to understand

