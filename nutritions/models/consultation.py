# -*- encoding: utf-8 -*-
from odoo import models, fields
class Consultation(models.Model):
    _name = 'nutrition.consultation'
    _rec_name = 'numero'
    _description = 'La consultation dediée à chaque enfant'
    _order = 'numero desc,signecli '

    numero = fields.Integer(string='Numéro Dossier',size =10,required =True)
    date = fields.Date(string='Date de consultation',required =True)
    signecli = fields.Char(string='Signe Clinique',size =12,required =True)
    patient_id = fields.Many2one('nutrition.patient', ondelete='cascade')
    motif_id = fields.Many2many('nutrition.motifconsultation','consultation_ids',string='Motif')
    medecin_id = fields.Many2one('nutrition.medecin', ondelete='cascade',string='Medecin')
    maladie_id = fields.One2many('nutrition.maladie','consulter',string='Maladie')
    examen_id = fields.Many2one('nutrition.examen', ondelete='cascade', string='Examen')

