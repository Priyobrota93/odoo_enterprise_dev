{
    'name': 'Access_Updated_HRx',
    'author': 'CLAREx',
    'license': 'LGPL-3',
    'depends': ['hr','hr_attendance','base','hr_expense','hr_holidays'],
    'data': [
        'views/hr_menuitem.xml',
        'views/hr_mobile_access_portal.xml',
        'views/attendance_request_view.xml',
        'views/attendance_request.xml',
        'security/ir.model.access.csv',
        # 'data/scheduled_actions.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}



