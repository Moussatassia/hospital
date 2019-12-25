# -*- encoding: utf-8 -*-
from odoo import models, fields
class Infirmiere(models.Model):
    _name = 'nutrition.infirmiere'
    _rec_name = 'nom'
    _description = 'Infirmiere au sein de la Pediatrie'
    _order = 'matricule desc, nom'

    nom = fields.Char(string='Nom',required =True)
    prenom = fields.Char(string='Prénom',required =True)
    matricule = fields.Integer(string='Matricule',required =True)
    grade = fields.Char(string='Grade', required=True)
    emploi = fields.Char(string='Emploi',help='l emploi actuel de l infirmiere', required=True)
    sexe = fields.Selection([('Masculin','Masculin'),('Féminin','Féminin')],string='Sexe')
    patient_id = fields.Many2one('nutrition.patient',string='Patient')
    medecin_ids = fields.Many2one('nutrition.medecin',string='Medecin')
    consultation_ids = fields.One2many('nutrition.consultation','medecin_id',string='Consultation')
