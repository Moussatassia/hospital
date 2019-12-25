# -*- encoding: utf-8 -*-
from odoo import models, fields
class Motif(models.Model):
    _name = 'nutrition.motifconsultation'
    _rec_name = 'nom'
    _description = 'Le motif de la consultation'
    _order = 'nom desc, typologie'

    numero = fields.Integer(string='Numero du motif',required =True)
    nom = fields.Char(string='Motif',required =True)
    typologie = fields.Char(string='Type',required =True)
    consultation_ids = fields.Many2many('nutrition.consultation','motif_id',string='Consultation')
