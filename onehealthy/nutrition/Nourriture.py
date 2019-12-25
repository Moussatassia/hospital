# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class Nourriture(models.Model):
    _name = "oh.nourriture"
    _description = u"Nourriture"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Nourriture", required=True)
    type_nourriture_id = fields.Many2one('oh.type_nourriture', string="Type nourriture", required=True)
    calorie = fields.Char("Calorie", required=True)
    lipide = fields.Char("Lipide", required=True)
    glucide = fields.Char("Glucide", required=True)
    proteine = fields.Char("Protéine", required=True)
    valeur_nutritionnelle_ids = fields.One2many('oh.valeur_nutritionnelle_ligne', 'nourriture_id', string="Valeur nutritionnelle")
    vitamine_ids = fields.One2many('oh.vitamine_ligne', 'nourriture_id', string="Vitamine")
    mineral_ids = fields.One2many('oh.mineral_ligne', 'nourriture_id', string="Minéral")
    photo = fields.Binary()


    _sql_constraints = [
    ('name', 'unique(name)', "Nourriture exist déjà !")
    ]
