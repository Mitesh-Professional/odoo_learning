from odoo import fields, models

class NameSearchMethod(models.Model):
    _name = "ma.name.search.method"
    _description = "This is a Name Search Method"
    user_name = fields.Char(string="Username", default="")
    user = fields.Many2one("ma.read.group.method", string='Name', required=True)
    total_entries = fields.Integer(string='Total Entries', default=0)


# Check Out The read_group model This mode in used _rec_name_search method there to send data to this field
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search
# _rec_names_search