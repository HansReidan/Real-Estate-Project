from odoo import api, fields, models

class EstatePropretyTag(models.Model):
    _name = 'estate.property.tag'
    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(string='Tag Proprietà')

    _sql_constraints = [
        ('property_tga_unico',
         'UNIQUE(name)',
         'Il nome del tag di proprietà deve essere univoco.')
    ]