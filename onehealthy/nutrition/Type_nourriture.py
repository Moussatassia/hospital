# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class TypeNourriture(models.Model):
    _name = "oh.type_nourriture"
    _description = u"Type nourriture"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Type nourriture", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Type nourriture exist déjà !")
    ]
