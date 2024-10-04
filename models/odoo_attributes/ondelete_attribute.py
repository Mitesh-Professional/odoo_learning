from odoo import models, fields


class Library(models.Model):
    _name = 'ma.ondelete.library.attribute'
    _description = 'Library'

    name = fields.Char(string='Library Name', required=True)
    book_ids = fields.One2many('ma.ondelete.book.attribute', 'library_id', relation="library_table",  string='Books')


class Book(models.Model):
    _name = 'ma.ondelete.book.attribute'
    _description = 'Book'

    name = fields.Char(string='Book Title', required=True)
    library_id = fields.Many2one('ma.ondelete.library.attribute',relation="library_table", string='Library', ondelete='cascade')

# ondelete have Other Method cascade, set null, restrict, set default