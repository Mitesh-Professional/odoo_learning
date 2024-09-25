from odoo import fields,models

class YourDetails(models.Model):
    _name="ma.details"
    _description = "This is Give Form View"

    user_name = fields.Char(string="Enter Your Name")

class Inherits(models.Model):
    _name = "ma.inherits"
    _description =  "This field is Inherits Example."
    _inherits = {"ma.details": "details_id"}
    details_id = fields.Many2one("ma.details", required=True, ondelete="cascade")
    user_email = fields.Char(string="Enter Your Email")
    user_password = fields.Char(string="Enter Your Password")