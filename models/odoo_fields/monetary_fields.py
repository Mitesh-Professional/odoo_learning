from odoo import models, fields

class MonetaryField(models.Model):
    _name = 'ma.monetary.field'
    _description = 'This is Monetary Fields'

    name = fields.Char(string="Name", required=True)
    amount = fields.Monetary(string="Amount", required=True)
    currency_id = fields.Many2one('res.currency', string="Currency", required=True,
                                   default=lambda self: self.env.company.currency_id)

    def apply_discount(self, discount_percentage):
        for record in self:
            discount_amount = record.amount * (discount_percentage / 100)
            record.amount -= discount_amount
