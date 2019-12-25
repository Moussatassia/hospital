# -*- encoding: utf-8 -*-
from odoo import models, fields
class Regime(models.Model):
    _name = 'nutrition.regime'
    _rec_name = 'nom'
    _description = 'regime dedié à un enfant'
    _order = 'quantite desc, nom'

    nom = fields.Char(string='Nom',required =True)
    quantite = fields.Char(string='Quantité',required =True)
    typologie = fields.Selection([('Enfant','0 à 3 ans'),
                                  ('Petit','3 à 12 ans'),('Grand','12 à 14 ans')],string='Categorie à qui')
    medicament_id = fields.Many2one('nutrition.medicament', string='Medicament')
    typealiment =fields.Char(string='Type d\'aliment',required =True)
    ration = fields.Text(string='La ration alimentaire',required =True)
    conseilethique = fields.Text(string='Conseil ethique',required =True)
    patient_id =fields.Many2one('nutrition.patient',string='Patient')
    maladie_id =fields.Many2one('nutrition.maladie',string='La maladie')
    nouriture_id =fields.Many2one('nutrition.nourriture',string='La Nourriture')


