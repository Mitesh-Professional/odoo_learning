from odoo import fields, models

class StudentDetails(models.Model):
    _name = "ma.student.field"
    _description = "This is Student Fields"

    name = fields.Char("Enter your Name")
    std = fields.Integer("Enter your Standard")
    school_ids = fields.Many2many('ma.many2many.field', string="School Data")  # Ensure this matches the XML

class SchoolDetails(models.Model):
    _name = "ma.many2many.field"
    _description = "This is School Fields"
    _rec_name = "school_name"
    school_name = fields.Char("Enter School Name")
    school_student_ids = fields.Many2many("ma.student.field", string="Student Data")  # Ensure this matches the XML
