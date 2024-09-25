from odoo import fields, models, api


class GraphView(models.Model):
    _name = "ma.graph.view"
    _description = "This is graph view."

    name = fields.Char(string="Enter Your Name")
    std = fields.Integer(string="Enter Your Standard")
    students = fields.Integer(string="School Students", readonly=True, compute="_compute_students", store=False)
    school = fields.Selection(
        [("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")],
        string="Select Your School",
        default="a",
        required=True
    )

    @api.depends('school')
    def _compute_students(self):
        school_count = self.env['ma.graph.view'].read_group(
            [('school', '!=', False)],
            ['school'],
            ['school']
        )
        student_counts = {record['school']: record['school_count'] for record in school_count}
        for record in self:
            record.students = student_counts.get(record.school, 0)

    @api.model
    def create(self, vals):
        # Create the record
        record = super(GraphView, self).create(vals)
        return record

    def write(self, vals):
        # Update the student count if the school is changed
        for record in self:
            old_school = record.school
            if 'school' in vals and vals['school'] != old_school:
                # Decrement the count for the old school
                self._decrement_student_count(old_school)
                # Increment the count for the new school
                self._increment_student_count(vals['school'])

        return super(GraphView, self).write(vals)

    def _increment_student_count(self, school):
        # Logic to increment the student count for the given school
        # This could include a more complex logic if needed, like logging

        # In this case, we do not maintain a count explicitly, as it can be fetched via compute method
        pass

    def _decrement_student_count(self, school):
        # Logic to decrement the student count for the given school
        # Similar to the increment logic

        # Again, the actual counts are handled by the compute method
        pass
