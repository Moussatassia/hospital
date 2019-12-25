# -*- encoding: utf-8 -*-
from odoo import models, fields
class Prescription(models.Model):
    _name = 'nutrition.prescription'
    _rec_name = 'nom'
    _description = 'Prescription pour un malade donné'
    _order = 'quantite desc, nom'

    nom = fields.Char(string='Nom',required =True)
    quantite = fields.Char(string='Quantité',required =True)
    marge = fields.Selection([('Enfant','Enfant'),
                                  ('Adulte','Adulte'),('Veuillard','Veuillard')],string='Prescrit à qui')
    posologie = fields.Char(string = 'Posologie',required =True)
    medicament_id = fields.Many2one('nutrition.medicament', string='Medicament')
