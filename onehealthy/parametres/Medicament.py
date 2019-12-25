# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class Medicament(models.Model):
    _name = "oh.medicament"
    _description = u"Médicament"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Médicament", required=True)
