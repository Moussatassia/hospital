# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class ExamenBiologique(models.Model):
    _name = "oh.examen_biologique"
    _description = u"Examen biologique"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Examen biologique", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Examen biologique exist déjà !")
    ]
####################################################################################
class ExamenBiologiqueConsultation(models.Model):
    _name = 'oh.examen_biologique_consultation'
    _description = u"Examen biologique"
    _rec_name = 'examen_biologique_id'
    _order ='date desc, id desc'
    
    examen_biologique_id = fields.Many2one('oh.examen_biologique',string='Examen biologique',required=True)
    consultation_id = fields.Many2one('oh.consultation',string='Consultation')
    patient_id = fields.Many2one('oh.patient',string='Patient',required=True)
    date = fields.Date(string="Date",required=True)
    note = fields.Char(string='Bilan')
