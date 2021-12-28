# -*- coding: utf-8 -*-
{
    'name': "Lab7(Bug Manage除錯管理)",

    'summary': "Odoo12_BugManage",

    'description': "介吾測試",

    'author': "蘇介吾",
    'website': "http://afgn.cc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/bug_manage_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bug.xml',
        'views/follower.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}