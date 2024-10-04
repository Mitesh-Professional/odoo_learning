from odoo import fields, models, api

class ColumnAttribute(models.Model):
    _name = "ma.column.attribute"
    _description = "This is a column attribute"
    name = fields.Char("Enter Name")
    name_value = fields.Many2many("ma.domain.attribute", string="Data",column1="name",column2="gender")

