# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class Attachment(models.Model):
    _name = 'oh.attachment'
    _description = u'Attachement'
    _order = "date desc, id desc"
    _rec_name = "patient_id"

    def default_company(self):
        return self.env.user.company_id.id

    def default_user(self):
        return self.env.user

    date = fields.Date(string="Date", default=fields.Datetime.now, required=True)
    user_id = fields.Many2one('res.users', 'Médecin', default=default_user,readonly=True)
    company_id = fields.Many2one('res.company', 'Cabinet médicale', default=default_company,readonly=True)
    patient_id = fields.Many2one('oh.patient',string='Patient',required=True)
    datas_fname = fields.Char('Nom de fichier')
    name = fields.Char('Nom de la pièce jointe', required=True)
    description = fields.Text('Description')
    datas = fields.Binary(string='Contenu de fichier', required=True)
    examen_biologique_id = fields.Many2one('oh.examen_biologique_consultation',string='Examen biologique')
    radiographie_id = fields.Many2one('oh.radiographie_consultation',string='Radiographie')
