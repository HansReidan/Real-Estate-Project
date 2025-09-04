from email.policy import default

from odoo import api, fields, models

class EstateProprety(models.Model):
    _name = 'estate.property'
    _description = 'Agenzia Immobiliare'
    _inherit = ['mail.thread']

    today = fields.Date.today()

    # HTML FIELD
    address_html = fields.Html(string='Address HTML')

    name = fields.Char(string="Nome Immobile", required=True)
    description = fields.Text()
    property_type = fields.Selection([('casa', 'Casa'), ('appartamento', 'Appartamento'),
                                      ('villa', 'Villa'), ('castello', 'Castello')])
    postcode = fields.Char(string="CAP")
    date_availability = fields.Date(default=fields.Date.add(today, months=3))
    expected_price = fields.Float(string="Prezzo previsto", required=True)
    selling_price = fields.Float(string="Prezzo vendita", readonly=True)
    bedrooms = fields.Integer(string="Camere da letto", default=2)
    living_area = fields.Integer(string="Saloni")
    facades = fields.Integer(string="Facciate")
    garage = fields.Boolean()
    garden = fields.Boolean(string="Giardino")
    garden_area = fields.Integer(string="Area giardino")
    garden_orientation = fields.Selection([('nord', 'Nord'), ('sud', 'Sud'), ('est', 'Est'), ('ovest', 'Ovest')])
    active = fields.Boolean(string="Attivo", default=True)
    state = fields.Selection([('nuova', 'Nuova'), ('offerta ricevuta', 'Offerta Ricevuta'),
                              ('offerta accettata', 'Offerta Accettata'), ('venduta', 'Venduta'),
                              ('cancellata', 'Cancellata')])

    # DOMAIN ---> [('model_id', 'operator', 'value')]
    # '|' '&' '!' or, and, not