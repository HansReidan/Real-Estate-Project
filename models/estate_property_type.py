from odoo import api, fields, models

class EstateProprety(models.Model):
    _name = 'estate.property.type'

    name = fields.Char(string='Property Type', required=True)

    property_type_id = fields.Many2one('estate.property')