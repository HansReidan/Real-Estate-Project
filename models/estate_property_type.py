from odoo import api, fields, models


class EstatePropretyType(models.Model):
    _name = 'estate.property.type'
    _rec_name = 'property_type'
    _order = 'property_type ASC'

    # Il rec name serve perchè altrimenti odoo si va aprendere il model_id per visualizzarlo, al posto
    # di property type

    property_type = fields.Char(string='Property Type', required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id')
    _sql_constraints = [
        ('property_type_name_unique',
         'UNIQUE(name)',
         'Il nome del tipo di proprietà deve essere univoco.')
    ]
