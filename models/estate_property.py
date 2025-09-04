from odoo import api, fields, models

class EstateProprety(models.Model):
    _name = 'estate.property'
    _description = 'Agenzia Immobiliare'
    _inherit = ['mail.thread']

    today = fields.Date.today()

    # The object self.env gives access to request parameters and other useful things:
    # self.env.cr or self._cr is the database cursor object; it is used for querying the database
    # self.env.uid or self._uid is the current user’s database id
    # self.env.user is the current user’s record
    # self.env.context or self._context is the context dictionary
    # self.env.ref(xml_id) returns the record corresponding to an XML id
    # self.env[model_name] returns an instance of the given model

    address_html = fields.Html(string='Address HTML')

    user_id = fields.Many2one('res.users', string='Venditore', required=True, default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Compratore', required=True)
    property_type_id = fields.Many2one('estate.property.type', string='Tipo', required=True)
    property_tag_ids = fields.Many2many('estate.property.tag', string='', required=True)
    offer_ids = fields.One2many('estate.property.offers', 'property_id', string='', required=True)

    name = fields.Char(string="Nome Immobile", required=True)
    description = fields.Text()
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