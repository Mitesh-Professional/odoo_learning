from odoo import fields, models

class ComputeAttribute(models.Model):
    _name = "ma.compute.attribute"
    _description = "This is a compute attribute"

    number = fields.Integer(string="Enter Number")
    square_return = fields.Integer(string="Square Of Number", readonly=True, compute='_square_compute_attribute')

    def _square_compute_attribute(self):
        self.square_return = self.number**2


