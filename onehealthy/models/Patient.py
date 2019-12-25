# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
class Patient(models.Model):
    _name = 'oh.patient'
    _description = u'Patient'
    _order = "name asc"
    _rec_name = "name"

################################## Informations personnelles #########################################
    def get_default_country(self):
        return self.env['res.country'].search([('currency_id','=','DZD')])
    
    name = fields.Char('Patient', required=True)
    gender = fields.Selection([('Masculin', 'Masculin'), ('Feminin', 'Féminin')], 'Sexe')
    nationality_id = fields.Many2one('res.country', string='Nationalité', default=get_default_country)
    date_of_birth = fields.Date(string='Date de naissance', required=True)
    birthplace = fields.Many2one('res.country.state',string='Lieu de naissance',domain="[('country_id','=',nationality_id)]")
    age = fields.Char(string='Âge', compute='get_age')
    age_mois = fields.Integer(string='Âge en mois', compute='get_age')
    description = fields.Text(string='Description')

    @api.one
    @api.constrains('date_of_birth')
    def check_dates(self):
        now = datetime.now()
        date_of_birth = fields.Datetime.from_string(self.date_of_birth)
        if now < date_of_birth:
            raise ValidationError("La date de naissance ne peut pas dépasser la date d’aujourd’hui.")

    @api.one
    @api.constrains('gender')
    def check_gender(self):
        if not self.gender:
            raise ValidationError("Veuillez d'abord choisir un sexe pour ce patient s'il vous plait.")

    @api.onchange('nationality')
    def onchange_nationalite(self):
        self.birthplace = False

    @api.one
    def get_age(self):
        now = datetime.now()
        if self.date_of_birth:
            date_of_birth = fields.Datetime.from_string(self.date_of_birth)
            delta = relativedelta(now, date_of_birth)
            years_months_days = str(delta.years) + _(' ans  ') + str(delta.months) + _(' mois  ') + str(delta.days) + _(' jours')
            years = delta.years
            mois = delta.months
            self.age = years_months_days
            self.age_mois = (years*12) + mois
################################## Adresse #########################################
    address_pays = fields.Many2one('res.country', string='Pays')
    address_wilaya = fields.Many2one('res.country.state', string='Wilaya')
    address_daira = fields.Many2one('res.commune', string='Commune')
    address_cite = fields.Char(string='Adresse') 
    adresse_cp = fields.Char(string='Code postal')

    @api.onchange('address_daira')
    def get_address_daira(self):
        self.address_wilaya = False
        self.adresse_cp = False
        self.address_pays = False
        if self.address_daira :
            self.address_wilaya = self.address_daira.state_id
            self.address_pays = self.address_daira.state_id.country_id
            self.adresse_cp = str(self.address_daira.state_id.code)+"000"
################################## Informations complémentaires #########################################
    assurance_maladie = fields.Selection([('Oui', 'Oui'), ('Non', 'Non')], string='Assurance maladie')
    maladie_enfance_id = fields.Many2many('oh.maladie_enfance',string="Maladie de l'enfance")
    groupe_sanguin = fields.Selection([('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'),('B-','B-'),('O-','O-'),('AB-','AB-')], string='Groupe Sanguin')
    parent_ids = fields.One2many('oh.parent','patient_id',string='Parents')
    lieu_ids = fields.One2many('oh.lieu','patient_id',string='Lieu de résidence')
    diagnostic_ids = fields.Many2many('oh.diagnostic','diagnostic_patient','patient_id','diagnostic_id',compute="compute_diagnostic",store=True, string='Diagnostics')
    antecedent_ids = fields.One2many('oh.antecedent_patient','patient_id',string="Antécédents")
    historique_poids_taille_ids = fields.One2many('oh.historique_poids_taille','patient_id',string='Historique poids / taille')
    medecin_traitant_ids = fields.One2many('oh.medecin_traitant','patient_id',string='Médecin traitant')
    rdv_ids = fields.One2many('oh.rdv','patient_id',string='Rendez-vous')
    attachment_ids = fields.One2many('oh.attachment','patient_id',string='Attachement')

    @api.one
    @api.depends('consultation_ids','consultation_ids.diagnostic_ids')
    def compute_diagnostic(self):
        diagnostic = []
        for s in self.consultation_ids:
            for m in s.diagnostic_ids:
                if m.id not in diagnostic:
                    diagnostic.append(m.id)
        self.diagnostic_ids = [(6, 0, diagnostic)]
################################## Méthode #########################################
    consultation_ids = fields.One2many('oh.consultation','patient_id',string='Consultation')
    nbr_consultation = fields.Integer(compute="_compute_nbr_consultation", string="Nombre de consultation")

    @api.one
    @api.depends('consultation_ids')
    def _compute_nbr_consultation(self):
        a=0
        for c in self.consultation_ids:
            a=a+1
        self.nbr_consultation=a
