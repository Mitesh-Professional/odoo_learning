from odoo import fields,models

class SearchView(models.Model):
    _name = "ma.search.view"
    _description = "This is Search View"
    # _rec_name = "task_name"

    name = fields.Char(string="Enter your Name:-")
    password = fields.Char(string="Enter Your Password:-")
    account = fields.Selection([('yes','Yes'), ('no','No')], default="no", string="You Have Account:-")

