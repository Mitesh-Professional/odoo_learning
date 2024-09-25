from odoo import models, fields, api

class MyWizard(models.TransientModel):
    _name = 'my.wizard'
    _description = 'My Wizard'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

    uploaded_file = fields.Binary(string='Upload Your File')
    file_name = fields.Char("File Name")

    def action_confirm(self):
        pass
