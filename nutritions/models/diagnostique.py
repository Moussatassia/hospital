# -*- encoding: utf-8 -*-
from odoo import models, fields
class Diagnostique(models.Model):
    _name = 'nutrition.diagnostique'
    _rec_name = 'nom'
    _description = 'Les diagnostiques pour chaque malade'
    _order = 'date desc, nom'

    numero = fields.Integer(string='Numéro de la diagnostique:',required =True)
    nom = fields.Char(string= 'Nom de la diagnostique:',required =True)
    date = fields.Date(string='Date d apparition:',required =True)
    consultation_ids = fields.One2many('nutrition.consultation','patient_id',string='Consultation')
