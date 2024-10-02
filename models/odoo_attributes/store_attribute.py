from odoo import fields, models

class StoreAttribute(models.Model):
    _name = "ma.store.attribute"
    _description = "This is a store attribute"

    number = fields.Integer(string="Enter Number")
    square_return = fields.Integer(string="Square Of Number", readonly=True, compute='_square_compute_attribute', store=True)

    def _square_compute_attribute(self):
        self.square_return = self.number**2


