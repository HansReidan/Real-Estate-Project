from odoo import api, fields, models

class EstatePropretyTag(models.Model):
    _name = 'estate.property.tag'
    _rec_name = 'name'

    name = fields.Char(string='Tag Proprietà')