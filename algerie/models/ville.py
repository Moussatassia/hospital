# -*- encoding: utf-8 -*-
from openerp import models, fields, api

class ResCommune(models.Model):
    _name = 'res.commune'
    _descritpion = 'Commune'
    _order = 'name,id'

    state_id = fields.Many2one('res.country.state', string='Wilaya', required=True)
    name = fields.Char(string='Commune', required=True)
