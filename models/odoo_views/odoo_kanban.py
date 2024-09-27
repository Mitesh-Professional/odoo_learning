from odoo import fields, models


class KanbanView(models.Model):
    _name = "ma.kanban.view"
    _description = "This is Kanban View"
    _rec_name = "patient"
    patient = fields.Char(string="Enter Patient Name")
    appointment_date = fields.Datetime(string="Enter Patient Appointment")
    doctor = fields.Selection([("a","A"), ("b","B"), ("c","C"), ("d","D")],string="Doctor Chose")



