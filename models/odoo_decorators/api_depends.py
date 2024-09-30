from odoo import fields, models, api
from odoo.exceptions import ValidationError

class ApiDepends(models.Model):
    _name = "ma.api.depends"
    _description = "This is a Depends"

    name = fields.Char(string="Student Name")
    marks = fields.Integer(string="Enter Marks", default=0)
    student_std = fields.Selection([("10", "10"), ("11", "11"), ("12", "12")], string="Select Standard", default="10")
    student_class = fields.Selection([("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")], string="Select Class", default="a")
    student_rank = fields.Char(string="Student Rank", compute='_calculate_rank', store=True)

    @api.depends("marks", "student_std")
    def _calculate_rank(self):
        for record in self:
            students = self.search([
                ('student_std', '=', record.student_std),
                ('student_class', '=', record.student_class),
            ])
            marks_list = [mark.marks for mark in students]
            greater_count = sum(1 for mark in marks_list if mark > record.marks)
            rank = greater_count + 1
            record.student_rank = rank

    @api.onchange("marks", "student_std")
    def change_value(self):
        for record in self:
            students = self.search([
                ('student_std', '=', record.student_std),
                ('student_class', '=', record.student_class),
            ])
            marks_list = [mark.marks for mark in students]
            greater_count = sum(1 for mark in marks_list if mark > record.marks)
            rank = greater_count + 1
            record.student_rank = rank











    # @api.model_create_multi()
    # if self.marks == 0:
    #     if len_student == 0:
    #         self.student_rank = (sum_of_marks / 1)
    #     # else:
    #     #     self.student_rank = len_student
    # else:
    #     self.student_rank = int(sum_of_marks / self.marks)

    # for record in self:
    #     if record.student_std == "10":
    #         if record.marks >= 90:
    #
    #             record.student_rank = "A"
    #         elif record.marks >= 75:
    #             record.student_rank = "B"
    #         elif record.marks >= 50:
    #             record.student_rank = "C"
    #         else:
    #             record.student_rank = "D"
    #     elif record.student_std == "11":
    #         if record.marks >= 85:
    #             record.student_rank = "A"
    #         elif record.marks >= 70:
    #             record.student_rank = "B"
    #         elif record.marks >= 50:
    #             record.student_rank = "C"
    #         else:
    #             record.student_rank = "D"
    #     elif record.student_std == "12":
    #         if record.marks >= 80:
    #             record.student_rank = "A"
    #         elif record.marks >= 65:
    #             record.student_rank = "B"
    #         elif record.marks >= 50:
    #             record.student_rank = "C"
    #         else:
    #             record.student_rank = "D"
    #     else:
    #         record.student_rank = "Not Ranked"
