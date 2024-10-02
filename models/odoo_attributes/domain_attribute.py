from odoo import fields, models

class DomainAttribute(models.Model):
    _name = "ma.domain.attribute"
    _description = "This is a domain attribute"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([("Male","Male"), ("Female","Female"), ("Other","Other"),],string='Gender')


