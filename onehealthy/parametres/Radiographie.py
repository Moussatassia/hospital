# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class Radiographie(models.Model):
    _name = "oh.radiographie"
    _description = u"Radiographie"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Radiographie", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Radiographie exist déjà !")
    ]
####################################################################################
class RadiographieConsultation(models.Model):
    _name = 'oh.radiographie_consultation'
    _description = u"Radiographie"
    _rec_name = 'radiographie_id'
    _order ='date desc, id desc'
    
    radiographie_id = fields.Many2one('oh.radiographie',string='Radiographie',required=True)
    consultation_id = fields.Many2one('oh.consultation',string='Consultation')
    patient_id = fields.Many2one('oh.patient',string='Patient',required=True)
    date = fields.Date(string="Date",required=True)
    note = fields.Char(string='Bilan')
