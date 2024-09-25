from odoo import fields,models,api

class Abstract(models.AbstractModel):
    _name = "ma.abstract.model"
    _description = "This is Abstract Class for a Other Class you want use So you can inherit a Abstract Class"
    name= fields.Char(string="Your Name")

class Test(models.Model):
    _name="ma.test.model"
    _description = "This is Main Class For a Abstract Module if You Can Change some be Careful"
    _inherit = ['ma.abstract.model']
    name_f=fields.Char(string="Enter Name")