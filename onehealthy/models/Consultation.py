# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
class Consultation(models.Model):
    _name = 'oh.consultation'
    _description = u'Consultation'
    _order = "date desc, id desc"
    _rec_name = "patient_id"

    def default_company(self):
        return self.env.user.company_id.id

    def default_user(self):
        return self.env.user

    @api.multi
    def name_get(self):
        res = super(Consultation, self).name_get()
        data = []
        for consultation in self:
            display_value = ''
            display_value += consultation.patient_id.name or ""
            display_value += ' - '
            display_value += consultation.date or ""
            data.append((consultation.id, display_value))
        return data

    user_id = fields.Many2one('res.users', 'Médecin', default=default_user,readonly=True)
    company_id = fields.Many2one('res.company', 'Cabinet médicale', default=default_company,readonly=True)
    company_currency_id = fields.Many2one('res.currency',related="company_id.currency_id",readonly=True)
    date = fields.Datetime(string="Date", default=fields.Datetime.now, required=True)
    state = fields.Selection([
        ('ouverte', "Ouverte"),
        ('ferme', "Fermée"),], default='ouverte',string="État",copy=False)
    def button_confirmer(self):
        ligne = self.env['oh.historique_poids_taille']
        if self.taille and self.poids:
            a = ligne.create({
                        'patient_id' :self.patient_id.id ,
                        'date': self.date,
                        'poids': self.poids,
                        'taille': self.taille,
                        'consultation_id':self.id,
                        })
            self.write({'state': 'ferme'})
        else:
            raise ValidationError("Merci de saisir le poids et la taille du patient.")
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
################################## Informations sur la consultation #########################################
    diagnostic_ids = fields.Many2many('oh.diagnostic',string='Diagnostic')
    motif_consultation_ids = fields.Many2many('oh.motif_consultation',string="Motif de consultation")
    examen_clinique_ids = fields.Many2many('oh.examen_clinique',string="Examen clinique")
    poids = fields.Char('Poids')
    taille = fields.Char('Taille')
    pc = fields.Char('P.C.')
    dspoids = fields.Char('DS Poids')
    dstaille = fields.Char('DS Taille')
    dspc = fields.Char('DS P.C.')
    pa = fields.Char('P A')
    imc = fields.Char('IMC',compute="calculer_imc")
    t = fields.Char('T°')
    description = fields.Text(string='Observation')

    @api.one
    @api.depends('poids','taille')
    def calculer_imc(self):
        if self.poids and self.taille:
            taille = float(self.taille) / 100
            imc = float(self.poids) / (taille * taille)
            self.imc = round(imc, 2)
################################## Prescription médicale #########################################
    prescription_medicale_ids = fields.One2many('oh.prescription_medicale','consultation_id',string="Prescription médicale")
    lait_id = fields.Many2many('oh.lait', string='Lait')
    examen_medical_ids = fields.One2many('oh.examen_medical_consultation','consultation_id',string="Examen médical")
    examen_biologique_ids = fields.One2many('oh.examen_biologique_consultation','consultation_id',string="Examen biologique")
    radiographie_ids = fields.One2many('oh.radiographie_consultation','consultation_id',string="Radiographie")
################################## Méthode #########################################
    @api.multi
    def get_ancien_consultation(self):
        return {
            'name': 'Consultations',
            'type': 'ir.actions.act_window',
            'res_model': 'oh.consultation',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'context': {'default_patient_id': self.patient_id.id},
        }

    @api.multi
    def new_rdv(self):
        return {
            'name': 'Rendez-vous',
            'type': 'ir.actions.act_window',
            'res_model': 'oh.rdv',
            'view_mode': 'form',
            'context': {'default_patient_id': self.patient_id.id,
                        'default_date': False},
            'target': 'new',
        }

    @api.multi
    def get_attachement(self):
        return {
            'name': 'Attachement',
            'type': 'ir.actions.act_window',
            'res_model': 'oh.attachment',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'context': {'default_patient_id': self.patient_id.id},
        }

    @api.multi
    def get_regime(self):
        return {
            'name': 'Régime',
            'type': 'ir.actions.act_window',
            'res_model': 'oh.regime',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'context': {'default_patient_id': self.patient_id.id},
        }

    @api.multi
    def get_radiologie(self):
        return {
            'name': 'Radiologie',
            'type': 'ir.actions.act_window',
            'res_model': 'oh.radiographie_consultation',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'context': {'default_patient_id': self.patient_id.id},
        }
    
    @api.multi
    def get_examen_biologique(self):
        return {
            'name': 'Examen biologique',
            'type': 'ir.actions.act_window',
            'res_model': 'oh.examen_biologique_consultation',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'context': {'default_patient_id': self.patient_id.id},
        }

    @api.multi
    def get_antecedent(self):
        return {
            'name': 'Antécédent',
            'type': 'ir.actions.act_window',
            'res_model': 'oh.antecedent_patient',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'context': {'default_patient_id': self.patient_id.id},
        }
