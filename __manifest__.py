# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'fidar task ',
    'version' : '1.0',
    'summary': 'custom sale for fidar task',
    'sequence': 0,
    'description': '''fidar task  ''',
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'license': 'LGPL-3',
    # 'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['sale',
                 'mail',
                 'contacts'
                 ],
    'data': [
        'security/ir.model.access.csv',


    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}