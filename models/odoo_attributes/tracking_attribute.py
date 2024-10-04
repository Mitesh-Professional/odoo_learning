from odoo import fields, models

class TrackingAttribute(models.Model):
    _name = "ma.tracking.attribute"
    _description = "This is a Tracking attribute"
    _inherit = "mail.thread"
    name = fields.Char(string='Name', tracking=True)

