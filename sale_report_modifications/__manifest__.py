# -*- coding: utf-8 -*-
{
    'name': "Report Modifications",

    'summary': "Adds the Debtor status indicator from accounting to the Conctact and Sales apps.",

    'description': """
        Adds the Debtor status indicator from accounting to the Conctact and Sales apps.
    """,

    'author': "QOC Innovations",
    'website': "http://www.qocinnovations.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.12',

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'account'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        # 'report/invoice_report.xml'
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
