from odoo import fields,models

class GanttView(models.Model):
    _name = "ma.gantt.view"
    _description = "This is a Gantt View"

    name = fields.Char("Enter Name")
    age = fields.Integer("Enter Your Number")
    start_date= fields.Date("Enter Starting Date")
    end_date= fields.Date("Enter Ending Date")
