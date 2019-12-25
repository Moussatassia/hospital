# -*- encoding: utf-8 -*-
from odoo import models, fields,api
class Patient(models.Model):
    _name = 'nutrition.patient'
    _rec_name = 'nom'
    _description = 'Patient du nombre des enfants'
    _order = 'nom desc, numero'

    nom = fields.Char(string='Nom',required =True)
    prenom = fields.Char(string='Prénom',required =True)
    numero = fields.Integer(string='Numero de dossier',required =True)
    date_naissance = fields.Date(string='Date de naissance',required =True)
    age = fields.Integer(string='Âge complet',required =True)
    sexe = fields.Selection([('Masculin','Masculin'),('Féminin','Féminin')],string='Sexe')
    adress = fields.Text(string='Adresse complet',required =True)
    groupe = fields.Selection([('A','A+'),('A','A-'),('B','B+'),('B','B-'),('AB','AB-')
                               ,('AB','AB+'),('O','O-'),('O','O+')],string='Groupe S')
    tel = fields.Integer(string='Tel',size=10, required=True)
    assurer = fields.Char(string='Assurance', required=True)
    photo = fields.Binary()
    estconsulter = fields.One2many('nutrition.consultation','patient_id')
    @api.constrains('date_naissance')
    def verification_date(self):
        for record in self:
            if (record.date_naissance and
                    record.date_naissance > fields.Date.today()):
                raise models.ValidationError(
                    'La date est trés recente'
                )
    @api.constrains('age')
    def verifier_date(self):
        for rec in self:
            if rec.age >14:
                raise models.ValidationError(
                    "L\'age du patient doit etre supperieure à" %rec.age)
            print("Vous devez en revoir l'age")
