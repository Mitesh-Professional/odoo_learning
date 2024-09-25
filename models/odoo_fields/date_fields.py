from odoo import fields,models

class DateField(models.Model):
    _name = "ma.date.field"
    _description = "This is Char Date"

    enter_today_date = fields.Date(string='Enter Today Date:-')