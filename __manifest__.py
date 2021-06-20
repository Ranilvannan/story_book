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
        'data/category.xml',
        'security/story_security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/story_view.xml',
        'views/category_view.xml',
        'views/tag_view.xml',
        'views/gallery_view.xml',
        'views/language_view.xml',
        'views/history_view.xml',
        'views/project_site1_view.xml',
        'views/project_site2_view.xml',
        'views/project_site3_view.xml',
        'views/project_site4_view.xml',
        'views/project_site5_view.xml',
        'views/project_site6_view.xml',
        'views/project_site7_view.xml',
        'wizard/crawl_service.xml',
        'wizard/publish_service.xml',
        'wizard/control_service.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
