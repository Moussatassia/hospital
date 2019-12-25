# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class MedecinTraitant(models.Model):
	_name = "oh.medecin_traitant"
	_description = u"Médecin traitant"
	_order = "patient_id asc"
	_rec_name = "patient_id"

	patient_id = fields.Many2one('oh.patient', string="Patient", required=True)
	medecin_id = fields.Char(string="Médecin", required=True)
	wilaya = fields.Many2one('res.country.state', string='Wilaya', required=True)
	numero_telephone = fields.Char(string='Numéro de téléphone')
	adresse_electronique = fields.Char(string='Adresse électronique')
	autre = fields.Char(string='Autres informations')
