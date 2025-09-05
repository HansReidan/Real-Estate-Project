from odoo import api, fields, models
from odoo.exceptions import ValidationError

class EstateProprety(models.Model):
    _name = 'estate.property'
    _description = 'Agenzia Immobiliare'
    _inherit = ['mail.thread']
    _order = 'id desc'

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
    sequence = fields.Integer(':', default=1)

    total_area = fields.Float(string='Area Totale', digits=0, readonly=True, compute='_compute_totalArea')
    # SERVE ER COMPUTE PER LE DEF IN PYTHON

    best_offer = fields.Float(string='Miglior Offerta', digits=0, readonly=True, compute='_compute_bestOffer')

    name = fields.Char(string="Nome Immobile", required=True)
    description = fields.Text()
    postcode = fields.Char(string="CAP")
    date_availability = fields.Date(default=fields.Date.add(today, months=3))
    expected_price = fields.Float(string="Prezzo previsto", required=True)
    selling_price = fields.Float(string="Prezzo vendita", readonly=True)
    bedrooms = fields.Integer(string="Camere da letto", default=2)
    living_area = fields.Integer(string="Grandezza (mq)")
    facades = fields.Integer(string="Facciate")
    garage = fields.Boolean()
    garden = fields.Boolean(string="Giardino")
    garden_area = fields.Integer(string="Area giardino")
    garden_orientation = fields.Selection([('nord', 'Nord'), ('sud', 'Sud'), ('est', 'Est'), ('ovest', 'Ovest')])
    active = fields.Boolean(string="Attivo", default=True)
    state = fields.Selection([('nuova', 'Nuova'), ('offerta ricevuta', 'Offerta Ricevuta'),
                              ('offerta accettata', 'Offerta Accettata'), ('venduta', 'Venduta'),
                              ('cancellata', 'Cancellata')], tracking=True, readonly=True)

    _sql_constraints = [
        ('expected_price_positive',
         'CHECK(expected_price > 0)',
         'Il prezzo atteso deve essere strettamente positivo.'),
        ('selling_price_non_negative',
         'CHECK(selling_price >= 0)',
         'Il prezzo di vendita non può essere negativo.')
    ]

    # DOMAIN ---> [('model_id', 'operator', 'value')]
    # '|' '&' '!' or, and, not

    def action_vendi(self):
        for rec in self:
            rec.state = 'venduta'

    def action_cancella(self):
        for rec in self:
            rec.state = 'cancellata'

    @api.depends('living_area', 'garden_area')
    def _compute_totalArea(self):
        for rec in self:
            rec.total_area = rec.garden_area + rec.living_area

    @api.depends('offer_ids')
    def _compute_bestOffer(self):
        for rec in self:
            temp = rec.offer_ids.mapped('prezzo')
            rec.best_offer = max(temp) if temp else 0.0

    @api.onchange('garden')
    def _onchange_property_type(self):
            if self.garden:
                self.garden_area = 10
                self.garden_orientation = 'nord'
            else:
                self.garden_area = 0
                self.garden_orientation = False

    @api.constrains('selling_price', 'expected_price')
    def _check_price(self):
        for rec in self:
            # Se è impostato un prezzo di vendita
            if rec.selling_price:
                min_price = rec.expected_price * 0.9
                if rec.selling_price < min_price:
                    raise ValidationError(
                        "Il prezzo di vendita non può essere inferiore al 90% del prezzo previsto.\n"
                        f"Prezzo previsto: {rec.expected_price:.2f} → minimo accettato: {min_price:.2f}"
                    )



