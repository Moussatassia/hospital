# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class Profession(models.Model):
    _name = "oh.profession"
    _description = u"Profession"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Profession", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Profession exist déjà !")
    ]
