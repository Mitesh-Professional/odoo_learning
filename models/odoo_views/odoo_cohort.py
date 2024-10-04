from odoo import fields, models

class CohortView(models.Model):
    _name="ma.cohort.view"
    _description = "The cohort view in Odoo visually analyzes data trends over time or groups, helping users assess metrics like retention and behavior patterns."
    start_date= fields.Date("Enter Starting Date")
    end_date= fields.Date("Enter Ending Date")