# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
class CertificatMedical(models.Model):
    _name = 'oh.certificat_medical'
    _description = u"Certificat médical"
    _order = "date desc, id desc"
    _rec_name = "patient_id"

    def default_company(self):
        return self.env.user.company_id.id

    def default_user(self):
        return self.env.user

    user_id = fields.Many2one('res.users', 'Médecin', default=default_user,readonly=True)
    company_id = fields.Many2one('res.company', 'Cabinet médicale', default=default_company,readonly=True)
    date = fields.Date(string="Date", default=fields.Datetime.now, required=True)
################################## Informations sur le patient #########################################
    patient_id = fields.Many2one('oh.patient',string='Patient', required=True)
    date_of_birth = fields.Date(string='Date de naissance',store=True,related='patient_id.date_of_birth',readonly=True)
    age = fields.Char(string='Âge',store=True,related='patient_id.age',readonly=True)
    diagnostic_ids = fields.Many2many('oh.diagnostic',string='Diagnostic')
    date_admission = fields.Date(string="Date d'admission")
    date_sortie = fields.Date(string="Date de sortie")
    motif_repos = fields.Char(string="Nécessite un arrêt de travail / un repos de")
    type = fields.Selection([('Sante', 'Certificat médical de bonne santé'), ('Travail', "Certificat médical d'arrêt de travail / de repos")], 'Type', required=True)

    @api.onchange('type')
    def onchange_type(self):
        self.motif_repos = False
        self.date_admission = False
        self.date_sortie = False
        self.diagnostic_ids = False
