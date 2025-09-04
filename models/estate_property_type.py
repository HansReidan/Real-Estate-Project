from odoo import api, fields, models

class EstatePropretyType(models.Model):
    _name = 'estate.property.type'
    _rec_name = 'property_type'
    # Il rec name serve perchè altrimenti odoo si va aprendere il model_id per visualizzarlo, al posto
    # di property type

    property_type = fields.Char(string='Property Type', required=True)