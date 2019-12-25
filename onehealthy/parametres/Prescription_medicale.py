# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp
import time
import pdb
from datetime import datetime

class PrescriptionMedicale(models.Model):
	_name = "oh.prescription_medicale"
	_description = u"Prescription médicale"
	_order = "medicament_id asc"
	_rec_name = "medicament_id"

	def default_user(self):
		return self.env.user

	consultation_id = fields.Many2one('oh.consultation',string='Consultation', required=True)
	medicament_id = fields.Many2one('oh.medicament',string='Médicament', required=True)
	posologie = fields.Char(string='Posologie')
	quantite = fields.Char(string='Quantité')
