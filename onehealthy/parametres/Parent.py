# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class Parent(models.Model):
	_name = "oh.parent"
	_description = u"Parent"
	_order = "name asc"
	_rec_name = "name"

	name = fields.Char("Parent", required=True)
	patient_id = fields.Many2one('oh.patient', string="Patient", required=True)
	date_naissance = fields.Date(string='Date de naissance')
	age = fields.Char(string='Âge', compute='get_age')
	numero_telephone = fields.Char(string='Numéro de téléphone')
	adresse_electronique = fields.Char(string='Adresse électronique')
	etat_sante = fields.Char(string='État de santé')
	type = fields.Selection([(u'Père', u'Père'), (u'Mère', u'Mère')], 'Parent')
	profession_id = fields.Many2one('oh.profession', string="Profession")
	situation = fields.Selection([('Divorce', 'Divorcé(e)'), ('Veuf', 'Veuf(ve)'), ('Décédé(e)', 'Décédé(e)')],string='État civil')
	groupe_sanguin = fields.Selection([('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'),('B-','B-'),('O-','O-'),('AB-','AB-')],string='Groupe Sanguin')
	phenotype_id = fields.Many2one('oh.phenotype',string="Phénotype")
	
	@api.one
	def get_age(self):
		now = datetime.now()
		if self.date_naissance:
			date_naissance = fields.Datetime.from_string(self.date_naissance)
			delta = relativedelta(now, date_naissance)
			years_months_days = str(delta.years) + _(' ans  ') + str(delta.months) + _(' mois  ') + str(delta.days) + _(' jours')
			self.age = years_months_days

class Lieu(models.Model):
	_name = "oh.lieu"
	_description = u"Lieu de résidence"
	_order = "patient_id asc"
	_rec_name = "patient_id"

	patient_id = fields.Many2one('oh.patient', string="Patient", required=True)
	address = fields.Many2one('res.commune', string='Ville', required=True)
	de = fields.Char(string='De', required=True)
	a = fields.Char(string="Jusqu'à", required=True)
	note = fields.Char('Note')
