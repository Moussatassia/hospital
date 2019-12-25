# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class TempsRepas(models.Model):
    _name = "oh.temps_repas"
    _description = u"Temps du repas"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Temps du repas", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Temps du repas exist déjà !")
    ]
