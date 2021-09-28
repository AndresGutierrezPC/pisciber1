# -*- coding: utf-8 -*-
# Part of Kiran Infosoft. See LICENSE file for full copyright and licensing details.
{
    'name': "Quick Add Sale Line",
    'summary': """Quickly Add the Sale Order Lines.""",
    'description': """
It will allow to quickly add multiple Sale order lines.
Tags:
order line
sale order line
add line
add order line
add sale order line
quick add
quick add line
    """,
    "version": "1.0",
    "category": "Sale",
    'author': "Kiran Infosoft",
    "website": "http://www.kiraninfosoft.com",
    'license': 'Other proprietary',
    'price': 15.0,
    'currency': 'EUR',
    'images': ['static/description/logo.jpeg'],
    "depends": [
        'sale',
    ],
    "data": [
        'security/ir.model.access.csv',
        'wizard/quick_sale_wizard_view.xml',
        'views/sale_view.xml',
    ],
    "application": False,
    'installable': True,
    
}
