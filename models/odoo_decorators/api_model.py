from odoo import fields, models, api

class ApiModel(models.Model):
    _name = "ma.api.model"
    _description = "this is model Decorators"

    user_value = fields.Integer(string="Number", default=0)
    user_result = fields.Char(string="Result", readonly=True)

    @api.model
    def calculate_sum(self, number1):
        return number1 % 2 == 0

    def action_calculate(self):
        result_value = self.calculate_sum(self.user_value)
        if result_value:
            self.user_result = f"{self.user_value} is Even"
        else:
            self.user_result = f"{self.user_value} is Odd"
        print(f"***************************************{self}***************************************")
    def action_reset(self):
        self.user_value = 0
        self.user_result = ""