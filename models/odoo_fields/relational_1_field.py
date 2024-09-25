from odoo import fields, models

class ManyToOne(models.Model):
    _name = "ma.many.to.one"
    _description = "This is a Many2one User fields."

    user_name = fields.Char(string="Enter Your Name")
    user_password = fields.Char(string="Enter Your Password")  # Changed label for clarity
    user_email = fields.Char(string="Enter Your Email Id")
    user_product = fields.Many2one("ma.one.to.many", string="Enter Your Product")  # Ensure this model exists

class OneToMany(models.Model):
    _name = "ma.one.to.many"
    _description = "This is One2many Field"

    product_ids = fields.One2many("ma.many.to.one", "user_product", string="Products")  # Reference to the Many2one field
