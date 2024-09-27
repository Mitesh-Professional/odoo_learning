from odoo import fields, models

class CohortView(models.Model):
    _name="ma.cohort.view"

    start_date= fields.Date("Enter Starting Date")
    end_date= fields.Date("Enter Ending Date")