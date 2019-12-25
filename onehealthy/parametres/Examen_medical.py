# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class ExamenMedical(models.Model):
    _name = "oh.examen_medical"
    _description = u"Examen médical"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Examen médical", required=True)
    prix = fields.Float(digits=(6,2),string=u'Prix', required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Examen médical exist déjà !")
    ]
#######################################################################################################################
class ExamenMedicalConsultation(models.Model):
    _name = 'oh.examen_medical_consultation'
    _description = u'Examen médical'
    _rec_name = 'examen_medical_id'
    _order = "examen_medical_id asc"
    
    consultation_id = fields.Many2one('oh.consultation',string='Consultation')
    examen_medical_id = fields.Many2one('oh.examen_medical',string='Examen médical',required=True)
    prix = fields.Float(digits=(6,2),string=u'Prix', required=True)

    @api.onchange('examen_medical_id')
    def onchange_examen_medical(self):
        self.prix = self.examen_medical_id.prix
