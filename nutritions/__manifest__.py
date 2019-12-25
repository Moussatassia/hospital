{
    'name':'Module nutrition',
     'summary':'Nutrition chez l''enfant',
     'description':'Bien nourir les enfants affamés',
     'sequence':1,
     'author':'Moussa',
     'licence':'GPL-3',
     'website':'http://univ-tlemcen.dz',
     'category':'Santé des enfants',
     'version':'1.0',
     'depends':['base'],
     'data':[
         'views/patient.xml','views/consultation.xml',
'views/diagnostique.xml','views/motifconsultation.xml','views/medicament.xml',
         'views/prescription.xml','views/examen.xml'
,'views/infirmiere.xml','views/medecin.xml','views/nourriture.xml',
         'views/rdv.xml','views/regime.xml','views/maladie.xml'
     ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

