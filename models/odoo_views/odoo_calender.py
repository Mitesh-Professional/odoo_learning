from odoo import models, fields

class CalenderView(models.Model):
    _name = "ma.calender.view"
    _description = "This is Calendar View"
    _rec_name = "task_name"

    task_name = fields.Char(string="Enter Task Name:-")
    date = fields.Date(string="Enter Task Date")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")

    color = fields.Selection([
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
    ], string="Event Color", default='blue')
