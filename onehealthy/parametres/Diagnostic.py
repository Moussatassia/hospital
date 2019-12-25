# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class Diagnostic(models.Model):
    _name = "oh.diagnostic"
    _description = u"Diagnostic"
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Diagnostic", required=True)
    nombre_patient = fields.Integer('Nombre de patient',readonly=True)
    patient_ids = fields.Many2many("oh.patient",'patient_diagnostic','diagnostic_id','patient_id', string='Patient')

    @api.multi
    def calcul_patient(self):
        self._cr.execute('select count(patient_id) from diagnostic_patient where diagnostic_id=%s',(self.id,))
        self.nombre_patient = self._cr.fetchone()[0]
        self._cr.execute('delete from patient_diagnostic where diagnostic_id=%s',(self.id,))
        self._cr.execute('select patient_id from diagnostic_patient where diagnostic_id=%s',(self.id,))
        for c in list(self._cr.fetchall()):
            self._cr.execute('insert into patient_diagnostic (diagnostic_id,patient_id) values (%s,%s)',(self.id,c[0]))
            self._cr.commit()

    _sql_constraints = [
    ('name', 'unique(name)', "Diagnostic exist déjà !")]
