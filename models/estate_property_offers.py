from odoo import api, fields, models

class EstatePropretyOffers(models.Model):
    _name = 'estate.property.offers'

    prezzo = fields.Float(string="Prezzo")
    status = fields.Selection([('rifiutata', 'Rifiutata'), ('accettata', 'Accettata')], nocopy=True)
    partner_id = fields.Many2one('res.partner', string='Compratore', required=True)
    property_id = fields.Many2one('estate.property', string='Proprietà', required=True)
