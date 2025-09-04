from odoo import api, fields, models
from odoo.tools import date_utils
from datetime import datetime


class EstatePropretyOffers(models.Model):
    _name = 'estate.property.offers'

    today = fields.Date.today()

    prezzo = fields.Float(string="Prezzo")
    status = fields.Selection([('rifiutata', 'Rifiutata'), ('accettata', 'Accettata')], nocopy=True)
    partner_id = fields.Many2one('res.partner', string='Compratore', required=True)
    property_id = fields.Many2one('estate.property', string='Proprietà', required=True)
    validita = fields.Integer(string='Validità')
    date_deadline = fields.Date(default=today, string='Deadline', compute='_compute_deadline',
                                inverse='_inverse_deadline')

    @api.depends('validita', 'create_date')
    def _compute_deadline(self):
        for rec in self:
            # create_date può essere None durante la creazione, fallback a oggi
            create_dt = rec.create_date.date() if rec.create_date else fields.Date.today()
            # validita può essere None o zero, fallback a 0
            validita = rec.validita if rec.validita else 0

            # Calcolo deadline = create_date + validita giorni
            rec.date_deadline = date_utils.add(create_dt, days=validita)

    def _inverse_deadline(self):
        for rec in self:
            # create_date può essere None, fallback a oggi
            create_dt = rec.create_date.date() if rec.create_date else fields.Date.today()
            if rec.date_deadline:
                # Converti date_deadline in datetime.date se è stringa
                if isinstance(rec.date_deadline, str):
                    deadline_date = datetime.strptime(rec.date_deadline, '%Y-%m-%d').date()
                else:
                    deadline_date = rec.date_deadline

                # Calcola differenza giorni tra date_deadline e create_date
                diff_days = (deadline_date - create_dt).days
                # Aggiorna validita (evita valori negativi)
                rec.validita = diff_days if diff_days >= 0 else 0
            else:
                # Se date_deadline è vuoto, reset validita
                rec.validita = 0
