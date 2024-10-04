from odoo import fields, models

class RelatedAttribute(models.Model):
    _name = "ma.related.attribute"
    _description = "This is a Related attribute"

    user = fields.Many2one('ma.domain.attribute',string='Gender', required=True)
    gender_value = fields.Selection(string='Name', required=True, readonly=True, related='user.gender')


# Related field check other side same field type like applied related field on char you can be related with integer
# Suppliers
# └── Supplier A
#     ├── Contact Number: 123-456-7890
#     ├── Address: 123 Main St
# └── Supplier B
#     ├── Contact Number: 987-654-3210
#     ├── Address: 456 Elm St
#
# Products
# └── Product 1
#     ├── Name: Widget A
#     ├── Supplier: Supplier A
#     └── Supplier Contact Number: 123-456-7890 (related field)
#
# └── Product 2
#     ├── Name: Gadget B
#     ├── Supplier: Supplier B
#     └── Supplier Contact Number: 987-654-3210 (related field)
