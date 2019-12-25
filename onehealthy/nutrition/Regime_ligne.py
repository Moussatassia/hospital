# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from odoo import exceptions
from odoo.exceptions import UserError, AccessError

class RegimeLigne(models.Model):
    _name = 'oh.regime_ligne'
    _order = "id asc"
    _rec_name = "temps_repas_id"

    regime_id = fields.Many2one('oh.regime', string=u'Régime', required=True)
    patient_id = fields.Many2one('oh.patient',string='Patient', required=True)
    date = fields.Date(string=u'Date', required=True)
    temps_repas_id = fields.Many2one('oh.temps_repas', string=u'Temps du repas', required=True)
    detail_ids = fields.One2many('oh.regime_detail_ligne', 'regime_id', string='Détails')
    regimes = fields.Char(string="Régime", compute="compute_regime",store=True)

    @api.one
    @api.depends('detail_ids','detail_ids.nourriture_id','detail_ids.qte')
    def compute_regime(self):
        regimes = ''
        for s in self.detail_ids:
            if regimes == '':
                regimes = s.nourriture_id.name
            else:
                regimes = s.nourriture_id.name + ' , ' + regimes
        self.regimes = regimes
#####################################################################
class RegimeDetailLigne(models.Model):
    _name = 'oh.regime_detail_ligne'
    _order = "id asc"
    _rec_name = "temps_repas_id"

    regime_id = fields.Many2one('oh.regime_ligne',string=u'Régime', required=True)
    nourriture_id = fields.Many2one('oh.nourriture',string=u'Nourriture', required=True)
    qte = fields.Char(string=u'Quantité')
    patient_id = fields.Many2one('oh.patient',string='Patient', required=True)
    date = fields.Date(string=u'Date', required=True)
    temps_repas_id = fields.Many2one('oh.temps_repas', string=u'Temps du repas', required=True)
