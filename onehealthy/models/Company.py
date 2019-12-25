# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class Company(models.Model):
    _inherit = 'res.company'

    name_ar = fields.Char(string='Service')
    fixe = fields.Char(string='Tél. Fixe')
    websitee = fields.Char(string='Site web')
    phonee = fields.Char(string='Portable')
    faxe = fields.Char(string='Faxe')
    emaile = fields.Char(string='E-mail')
    address_daira = fields.Many2one('res.commune', string='Commune')
    user_id = fields.Many2one('res.users', 'Responsable')
    specialite = fields.Text(string='Spécialité')
    specialite_ar = fields.Text(string='Spécialité AR')
