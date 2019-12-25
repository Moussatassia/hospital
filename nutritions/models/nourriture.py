# -*- encoding: utf-8 -*-
from odoo import models, fields
class Nourriture(models.Model):
    _name = 'nutrition.nourriture'
    _rec_name = 'nom'
    _description = 'La nourriture prête à etre consommée'
    _order = 'nom desc, typa'

    nom = fields.Char(string='Nom de la nourriture',required =True)
    typa = fields.Char(string='Type de la nourriture',required =True)
    quantite = fields.Char(string='Quantité',required =True)
    energie = fields.Selection([('Calories', 'Calories'), ('Glucides', 'Glucides')
                                      , ('Lipides', 'Lipides'), ('Proteines'
                                      ,'Proteines')], string='Valeurs energetiques')
    indique = fields.Html(string='Indication')
