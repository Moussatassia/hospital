# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class MaladieEnfance(models.Model):
    _name = "oh.maladie_enfance"
    _description = u"Maladie de l'enfance"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Maladie de l'enfance", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Maladie de l'enfance exist déjà !")
    ]
