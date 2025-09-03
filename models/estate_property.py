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
    postcode = fields.Char()
    date_availability = fields.Date(default=fields.Date.add(today, months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('nord', 'Nord'), ('sud', 'Sud'), ('est', 'Est'), ('ovest', 'Ovest')])
    active = fields.Boolean(default=True)
