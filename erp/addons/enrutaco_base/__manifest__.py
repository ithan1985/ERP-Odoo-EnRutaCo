# -*- coding: utf-8 -*-

{
    "name": "EnRutaCo Base",
    "summary": "Módulo base para la plataforma ERP de EnRutaCo.",
    "description": """
EnRutaCo Base
=============

Módulo fundacional que contiene la configuración,
seguridad y componentes comunes para el ERP EnRutaCo.
""",
    "version": "19.0.1.0.0",
    "category": "Operations",
    "author": "EnRutaCo",
    "website": "https://enrutaco.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "mail",
        "contacts",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}