# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Story',
    'version': '1.1',
    'summary': 'Story Book',
    'sequence': 15,
    'description': 'Story Book',
    'category': 'New',
    'website': 'https://www.odoo.com/page/billing',
    'images': [],
    'depends': ['base', 'web', 'mail'],
    'data': [
        'data/story.xml',
        'security/story_security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/story_view.xml',
        'views/category_view.xml',
        'views/language_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
