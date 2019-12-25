# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class Regime(models.Model):
    _name = "oh.regime"
    _description = u"Régime"
    _order = "date desc, id desc"
    _rec_name = "patient_id"

    def default_company(self):
        return self.env.user.company_id.id

    def default_user(self):
        return self.env.user

    @api.multi
    def name_get(self):
        res = super(Regime, self).name_get()
        data = []
        for regime in self:
            display_value = ''
            display_value += regime.patient_id.name or ""
            display_value += ' - '
            display_value += regime.date or ""
            data.append((regime.id, display_value))
        return data

    user_id = fields.Many2one('res.users', 'Médecin', default=default_user,readonly=True)
    company_id = fields.Many2one('res.company', 'Cabinet médicale', default=default_company,readonly=True)
    date = fields.Datetime(string="Date", default=fields.Datetime.now, required=True)
################################## Informations sur le patient #########################################
    patient_id = fields.Many2one('oh.patient',string='Patient', required=True)
    date_of_birth = fields.Date(string='Date de naissance',store=True,related='patient_id.date_of_birth',readonly=True)
    age = fields.Char(string='Âge',store=True,compute='get_age',readonly=True)
    age_mois = fields.Integer(string='Âge en mois',store=True,compute='get_age',readonly=True)
    ancien_diagnostic_ids = fields.Many2many('oh.diagnostic',related='patient_id.diagnostic_ids',readonly=True,string='Anciens diagnostics')
    assurance_maladie = fields.Selection([('Oui', 'Oui'), ('Non', 'Non')], string='Assurance maladie')

    @api.one
    @api.depends('patient_id.date_of_birth','date')
    def get_age(self):
        now = datetime.now()
        if self.patient_id.date_of_birth:
            date_of_birth = fields.Datetime.from_string(self.patient_id.date_of_birth)
            date = fields.Datetime.from_string(self.date)
            delta = relativedelta(date, date_of_birth)
            years_months_days = str(delta.years) + _(' ans  ') + str(delta.months) + _(' mois  ') + str(delta.days) + _(' jours')
            years = delta.years
            mois = delta.months
            self.age = years_months_days
            self.age_mois = (years*12) + mois

    @api.onchange('patient_id')
    def get_assurance_maladie(self):
        self.assurance_maladie = False
        if self.patient_id:
            self.assurance_maladie = self.patient_id.assurance_maladie
################################## Informations sur le régime #########################################
    date_debut = fields.Date(string='Date de début', required=True)
    date_fin = fields.Date(string='Date de fin', required=True)
    duree = fields.Char(string="Durée", compute="compute_duration")
    regime_ids = fields.One2many('oh.regime_ligne', 'regime_id', string='Régime')

    @api.one
    @api.depends('date_debut','date_fin')
    def compute_duration(self):
        if self.date_debut and self.date_fin:
            dd = fields.Datetime.from_string(self.date_debut)
            df = fields.Datetime.from_string(self.date_fin)
            if df < dd:
                raise ValidationError("Date de début ne peut pas dépasser la date de fin.")
            else:
                date_debut = datetime.strptime(self.date_debut,'%Y-%m-%d')
                date_fin = datetime.strptime(self.date_fin,'%Y-%m-%d')
                dt = date_debut
                day_count = 0
                while dt < date_fin:
                    day_count+=1
                    dt += timedelta(days=1)
                self.duree = str(day_count) + _(' jours ')
