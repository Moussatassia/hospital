# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class Rdv(models.Model):
    _name = 'oh.rdv'
    _description = u'Rendez-vous'
    _order = "date asc"
    _rec_name = "patient_id"

    def default_company(self):
        return self.env.user.company_id.id

    def _get_default_doctor(self):
        return self.env.user.company_id.user_id.id

    user_id = fields.Many2one('res.users',string='Médecin', required=True)
    company_id = fields.Many2one('res.company', 'Cabinet médicale', default=default_company,readonly=True)
    date = fields.Datetime(string='Date',default=fields.Datetime.now, required=True)
################################## Informations sur le patient #########################################
    patient_id = fields.Many2one('oh.patient',string='Patient', required=True)
    date_of_birth = fields.Date(string='Date de naissance',store=True,related='patient_id.date_of_birth',readonly=True)
    age = fields.Char(string='Âge',store=True,related='patient_id.age',readonly=True)
################################## Informations sur le rdv #########################################
    description = fields.Text(string="Description")
    color = fields.Integer('Couleur', compute='_compute_color')

    @api.one
    @api.depends('color')
    def _compute_color(self):
        self.color=self.patient_id.id

    state = fields.Selection([
        ('brouillon', 'Brouillon'),('confirme', 'Confirmé'),("indisponible","Indisponible"),
        ('en_attente', 'En attente'),("en_consultation","En consultation"),('annule', 'Annulé')],
        string='Statut', default='brouillon', readonly=True, required=True,
        copy=False)

    @api.multi
    def button_confirmer(self):
        self.state = 'confirme'

    @api.one
    def button_indisponible(self):
        self.state = 'indisponible'

    @api.multi
    def button_en_attente(self):
        self.state = 'en_attente'

    @api.multi
    def button_annuler(self):
        self.state = 'annule'

    @api.multi
    def button_consultation(self):
        self.state = 'en_consultation'
        now = fields.Datetime.now()
        ligne = self.env['oh.consultation']
        a = ligne.create({
                    'patient_id' :self.patient_id.id ,
                    'date': now,
                    'user_id':self.user_id.id,
                    })
