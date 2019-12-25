# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class MotifConsultation(models.Model):
    _name = "oh.motif_consultation"
    _description = u"Motif de consultation"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Motif de consultation", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Motif de consultation exist déjà !")
    ]
