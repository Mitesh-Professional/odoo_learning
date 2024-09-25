from odoo import fields,models

class HtmlField(models.Model):
    _name = "ma.html.field"
    _description = "This is Char Fields"

    text_value = fields.Html(string='Enter Notes :-')