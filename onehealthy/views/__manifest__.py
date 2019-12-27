# -*- encoding: utf-8 -*-
{
    "name": "Nutrition",
    "version": "1.0",
    "author": "Moussa",
    "website": "http://univ-tlemcen.dz",
    "sequence": 0,
    'category': 'Healthy',
    "license": "LGPL-3",
    "depends": [
        "web","base","algerie","backend_theme_v11","odoo_web_login",
    ],
    "description": """

	""",
    'summary': 'Bien nourir les enfants affamés',
    "data": [
        'views/parametres/Parent.xml',
        'views/parametres/Diagnostic.xml',
        'views/parametres/Motif_consultation.xml',
        'views/parametres/Antecedent.xml',
        'views/parametres/Radiographie.xml',
        'views/parametres/Examen_biologique.xml',
        'views/parametres/Medicament.xml',
        'views/parametres/Lait.xml',
        'views/parametres/Maladie_enfance.xml',
        'views/parametres/Profession.xml',
        'views/parametres/Examen_clinique.xml',
        "views/parametres/Examen_medical.xml",
        "views/parametres/Company.xml",
        "views/nutrition/Nourriture.xml",
        "views/nutrition/Type_nourriture.xml",
        "views/nutrition/Valeur_nutritionnelle.xml",
        "views/nutrition/Vitamine.xml",
        "views/nutrition/Mineral.xml",
        "views/nutrition/Temps_repas.xml",
        "views/nutrition/Regime.xml",
        'report/Ordonnance.xml',
        'report/Radiographie.xml',
        'report/Examen_biologique.xml',
        'report/Certificat_medical_arret_travail.xml',
        'report/Certificat_medical_bon_sante.xml',
        'report/Regime.xml',
        'views/Patient.xml',
        'views/Consultation.xml',
        'views/Rendez_vous.xml',
        'views/Attachement.xml',
        'views/Certificat_medical.xml',
        'Menu.xml',
    ],
    "qweb": [
    ],
    "demo": [
    ],
    "images": [
    ],
    "auto_install": True,
    "installable": True,
    "application": True,
}
