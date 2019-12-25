# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class HistoriquePoidsTaille(models.Model):
	_name = "oh.historique_poids_taille"
	_description = u"Historqiue poids / taille"
	_order = "patient_id asc"
	_rec_name = "patient_id"

	patient_id = fields.Many2one('oh.patient', string="Patient", required=True)
	consultation_id = fields.Many2one('oh.consultation', string="Consultation")
	date = fields.Date(string='Date', required=True)
	poids = fields.Char('Poids')
	taille = fields.Char('Taille')
	age = fields.Char(string='Âge',store=True,compute='get_age',readonly=True)
	age_mois = fields.Integer(string='Âge en mois',store=True,compute='get_age',readonly=True)

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
