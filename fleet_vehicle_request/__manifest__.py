{
    'name': 'Fleet Vehicle Request',
    'version': '1.0',
    'category': 'Human Resources/Fleet',
    'summary': 'Vehicle Request Workflow for Employees',
    'description': """
        This module allows HR users and Department Heads to create vehicle requests.
        Fleet Managers can approve or reject these requests.
    """,
    'author': 'Your Name',
    'depends': ['hr', 'fleet', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
        'views/fleet_vehicle_request_views.xml',
    ],
    'installable': True,
    'application': False,
}