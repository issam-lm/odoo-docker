{
    'name': 'TP - Gestion des Évaluations',
    'version': '17.0.1.0.0',
    'category': 'Custom',
    'summary': 'Module de gestion d\'évaluations TP',
    'description': """
        Module de gestion d'évaluations TP
        ===================================
        
        Ce module permet de :
        - Gérer des évaluations avec nom, responsable, date de début et statut
        - Afficher les évaluations en liste et en formulaire
    """,
    'author': 'M. AIT DAOUD',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/evaluation_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
