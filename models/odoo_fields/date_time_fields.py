from odoo import fields,models

class DateTimeField(models.Model):
    _name = "ma.date.time.field"
    _description = "This is Date Time Fields"

    enter_date_time = fields.Datetime(string='Enter Today Date and Time:-')