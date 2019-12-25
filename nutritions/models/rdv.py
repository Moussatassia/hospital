# -*- encoding: utf-8 -*-
from odoo import models, fields
class Rdv(models.Model):
    _name = 'nutrition.rdv'
    _rec_name = 'nom'
    _description = 'les rendez-vous pris'
    _order = 'numero desc, nom'

    numero = fields.Integer(string='N° Rendez-vous :',required =True)
    code = fields.Integer(string='Code patient :', required=True)
    nom = fields.Char(string='Nom prénom du patient :',required =True)
    date = fields.Date(string='Date de rende-vous :',required =True)
    heure = fields.Datetime(string='Heure rende-vous :',required =True)
    motif = fields.Text(string='Motif :',required =True)
    medecin_id = fields.Many2many('nutrition.medecin','listo',string='Medecin')


