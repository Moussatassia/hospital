# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class Lait(models.Model):
    _name = "oh.lait"
    _description = u"Lait"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Lait", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Lait exist déjà !")
    ]
