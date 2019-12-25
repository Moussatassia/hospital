# -*- encoding: utf-8 -*-
from odoo import models, fields
class Maladie(models.Model):
    _name = 'nutrition.maladie'
    _rec_name = 'nom'
    _description = 'La maladie ou ration pour un enfant'
    _order = 'numero desc, pathologie'
    nom = fields.Char(string='Nom', required=True)
    numero = fields.Integer(string = 'Numero',required =True)
    description = fields.Text(string='description',required=True)
    pathologie = fields.Char(string='Pathologie',required =True)
    consulter = fields.Many2one('nutrition.consultation')
