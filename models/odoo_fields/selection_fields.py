from odoo import fields,models

class SelectionField(models.Model):
    _name = "ma.selection.field"
    _description = "This is Char Fields"

    city_name = fields.Selection([("patan","Patan"),("mehsana","Mehsana"),("ahmedabad","Ahmedabad")], string='Enter Your Name:-',)