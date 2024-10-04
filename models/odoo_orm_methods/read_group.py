from pyasn1_modules.rfc2985 import gender

from odoo import fields, models, api

class ReadGroupMethod(models.Model):
    _name = "ma.read.group.method"
    _description = "This is a read group Method"
    _rec_names_search = ['gender','name']
    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], string='Gender')

    @api.model
    def get_read_group_by(self, *args, **kwargs):
        get_value = self.read_group([('gender','=','Male')], fields=['name', 'gender'], groupby=['gender'])
        print(f"***************************{get_value}***************************")
        return get_value

    def _compute_display_name(self):
        for vals in self:
            vals.display_name = f"[{vals.name} {vals.gender}]"
