from odoo import fields,models

class PivotView(models.Model):
    _name = "ma.pivot.view"
    _description = "This is Pivot view."

    employee = fields.Char(string="Enter Employee Name")
    salary = fields.Integer(string="Enter Employee Salary")

