from odoo import fields, models, api


class ApiOnchange(models.Model):
    _name = "ma.api.onchange"
    _description = "This is OnChange"

    user_name = fields.Char(string="User Name", required=True)
    user_password = fields.Char(string="User Password", required=True)
    conform_password = fields.Char(string="Conform Password", required=True)
    status = fields.Char(string="Status", readonly=True)

    @api.onchange('user_password', 'conform_password')
    def _check_password_is_match(self):
        if not self.user_password:
            self.status = "Password Is Empty."
        elif not self.conform_password:
            self.status = "Conform Password Is Empty."
        elif self.user_password == self.conform_password:
            self.status = "Password Matched"
        else:
            self.status = "Password Is not Match."
