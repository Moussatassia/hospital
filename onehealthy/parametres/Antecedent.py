# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class Antecedent(models.Model):
    _name = "oh.antecedent"
    _description = u"Antécédent"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Antécédent", required=True)
    detail_ids = fields.One2many('oh.antecedent_ligne','antecedent_id',string="Détails")

    _sql_constraints = [
    ('name', 'unique(name)', "Antécédent exist déjà !")
    ]

class AntecedentLigne(models.Model):
    _name = "oh.antecedent_ligne"
    _description = u"Détail antécédent"
    _order = "antecedent_id asc"
    _rec_name = "name"

    name = fields.Char("Détail antécédent", required=True)
    antecedent_id = fields.Many2one('oh.antecedent', string="Antécédent", required=True)

    _sql_constraints = [
    ('name', 'unique(name)', "Antécédent exist déjà !")
    ]

class AntecedentPatient(models.Model):
    _name = "oh.antecedent_patient"
    _description = u"Antécédent patient"
    _order = "antecedent_id asc"
    _rec_name = "antecedent_id"

    patient_id = fields.Many2one('oh.patient', string="Patient", required=True)
    antecedent_id = fields.Many2one('oh.antecedent', string="Antécédent", required=True)
    antecedent_detail_id = fields.Many2one('oh.antecedent_ligne', string="Détail", required=True,domain="[('antecedent_id','=',antecedent_id)]")
    note = fields.Char(string="Note")
