# -*- coding: utf-8 -*-
{
    'name': "Colis_sur_BL",

    'summary': """
        Numéro de colis sur le Bon de livraison""",

    'description': """
        Ajoute le numéro de colis associé à un article du bon de commande, sur le même article
        dans le bon de livraison.
        S'effectue aussi lors de la création d'un reliquat.
    """,

    'author': "BeProject",
    'website': "https://beproject.fr/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
