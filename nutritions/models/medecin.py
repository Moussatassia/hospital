# -*- encoding: utf-8 -*-
from odoo import models, fields
class Medecin(models.Model):
    _name = 'nutrition.medecin'
    _rec_name = 'nom'
    _description = 'medecin et specialiste'
    _order = 'specialite desc, nom'

    nom = fields.Char(string='Nom',required =True)
    prenom = fields.Char(string='Prénom',required =True)
    specialite = fields.Selection([('Neorologue','Neorologue'),('Radiologue','Radiologue')
                                   ,('Psycholoque','Psycholoque'),('Generaliste'
                                   ,'Generaliste'),('detecticien','detecticien')],string='Specialité')
    grade = fields.Selection([('MaitreAssistant','MaitreAssistant')])
    sexe = fields.Selection([('Masculin','Masculin'),('Féminin','Féminin')],string='Sexe')
    patient_id = fields.One2many('nutrition.patient','adress', string='Décision')
    listo = fields.Many2many('nutrition.rdv','nom',string='Liste des rendez-vous')
    consulter = fields.One2many('nutrition.consultation','medecin_id')
