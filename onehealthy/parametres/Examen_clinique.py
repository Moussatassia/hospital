# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class ExamenClinique(models.Model):
    _name = "oh.examen_clinique"
    _description = u"Examen clinique"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Examen clinique", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Examen clinique exist déjà !")
    ]
