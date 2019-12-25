# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class ValeurNutritionnelle(models.Model):
    _name = "oh.valeur_nutritionnelle"
    _description = u"Valeur nutritionnelle"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Valeur nutritionnelle", required=True)
    _sql_constraints = [
    ('name', 'unique(name)', "Valeur nutritionnelle exist déjà !")
    ]

class Vitamine(models.Model):
    _name = "oh.vitamine"
    _description = u"Vitamine"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Vitamine", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Vitamine exist déjà !")
    ]

class Mineral(models.Model):
    _name = "oh.mineral"
    _description = u"Minéral"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Minéral", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Minéral exist déjà !")
    ]
##########################################################################################
class ValeurNutritionnelleLigne(models.Model):
    _name = "oh.valeur_nutritionnelle_ligne"
    _description = u"Valeur nutritionnelle"
    _order = "valeur_nutritionnelle_id asc"
    _rec_name = "valeur_nutritionnelle_id"

    valeur_nutritionnelle_id = fields.Many2one('oh.valeur_nutritionnelle',"Valeur nutritionnelle", required=True)
    portion = fields.Char("Par portion", required=True)
    dv = fields.Char("% DV", required=True)
    nourriture_id = fields.Many2one('oh.nourriture', "Nourriture", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Valeur nutritionnelle exist déjà !")
    ]

class VitamineLigne(models.Model):
    _name = "oh.vitamine_ligne"
    _description = u"Vitamine"
    _order = "vitamine_id asc"
    _rec_name = "vitamine_id"

    vitamine_id = fields.Many2one('oh.vitamine',"Vitamine", required=True)
    portion = fields.Char("Par portion", required=True)
    dv = fields.Char("% DV", required=True)
    nourriture_id = fields.Many2one('oh.nourriture', "Nourriture", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Vitamine exist déjà !")
    ]

class MineralLigne(models.Model):
    _name = "oh.mineral_ligne"
    _description = u"Minéral"
    _order = "mineral_id asc"
    _rec_name = "mineral_id"

    mineral_id = fields.Many2one('oh.mineral', "Minéral", required=True)
    portion = fields.Char("Par portion", required=True)
    dv = fields.Char("% DV", required=True)
    nourriture_id = fields.Many2one('oh.nourriture', "Nourriture", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Minéral exist déjà !")
    ]
