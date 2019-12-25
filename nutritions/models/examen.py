# -*- encoding: utf-8 -*-
from odoo import models, fields,api
class Examen(models.Model):
    _name = 'nutrition.examen'
    _rec_name = 'numero'
    _description = 'L\'examen propre à un enfant'
    numero = fields.Integer(string = 'Numero',required =True)
    taille = fields.Float(string = 'Taille',required =True)
    poids =fields.Float(string = 'Poids',required =True)
    imc = fields.Float(compute='calcule')
    @api.depends('taille','poids')
    def calcule(self):
        for rec in self:
            rec.imc = rec.poids/(rec.taille*rec.taille)
   # @api.depends('','')
   #  def onchange(self, imc, taille, poids):
   #      self.imc = self.poids/(self.taille*taille)
   #      if self.imc <18:
   #          return {
   #              'warning': {
   #                  'title': "Le patient est en danger",
   #                  'message':"son indice de massse corporel est depassé"
   #              },
   #          }
   #  def calculer(self,imc, taille, poids):
   #      self.imc = self.poids / (self.taille * taille)
   #      if self.imc <18:
   #          return {
   #              'warning': {
   #                  'title': "Le patient est en danger",
   #                  'message':"son indice de massse corporel est depassé"
   #              },
   #          }
   #  taille = fields.Integer(calculer(self=taille))
    cout = fields.Selection([('dec','200.00 Da'),('cind','500.00 Da'),('mill','1000.00 Da')
                                ,('kinz','1500.00 Da'),('demil','2000.00 Da'),('dcink','2500.00 Da')
                                ,('trois','3000.00 Da'),('troiscik','3500.00 Da'),('qatre','4000.00 Da'),
                             ('katrci','4500.00 Da')],string='Coût de la consultation')
    consultation_id = fields.One2many('nutrition.consultation','examen_id',string='Consultation')
