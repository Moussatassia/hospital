# -*- encoding: utf-8 -*-
from odoo import models, fields
class Medicament(models.Model):
    _name = 'nutrition.medicament'
    _rec_name = 'nom'
    _description = 'Les medicaments pour chaque traitement'
    _order = 'typologie desc, nom'

    nom = fields.Char(string='Nom',required =True)
    photo = fields.Binary('photo')
    prescription_id = fields.One2many('nutrition.prescription','medicament_id',string='Prescrire')
    typologie = fields.Selection([('comprimé','comprimé'),
                                  ('gélule','gélule'),('sirop','sirop')],string='Galenique')
