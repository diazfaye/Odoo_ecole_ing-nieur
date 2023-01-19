# -*- coding: utf-8 -*-

{
    "name": "Mon ecole d'ingénieur",
    "version": "12.0.1",
    "category": "ECOLEINGENIEUR",
    "summary": """
        Resumé de mon module ecole
    """,
    "description": """Description du module""",
    "author": "DIEGANETdsi",
    "company": "TDSI",
    "maintainer": "Tdsi",
    "website": "https://www.tdsi.sn",
    "depends": ["base","mail","web"],
    "data": [
        # "security/base_security.xml",
        "security/ir.model.access.csv",
        # "data/auth_signup_data.xml",
        # "data/webclient_templates.xml",
        "views/cours_views.xml",
        "views/intervenant_views.xml",
        "views/bureau_views.xml",
        "views/specialite_views.xml",
        "report/ecoleingenieur_report_template.xml",
        "report/ecoleingenieur_reports.xml",
    ],
    "installable": True,
    # 'images': ['static/description/banner.png'],
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",
}
