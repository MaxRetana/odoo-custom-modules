{
    "name": "Tickets",
    "summary": "Este modulo permitira gestionar tickets de soporte",
    "description": 
        """
        Este módulo permite gestionar tickets de soporte dentro de Odoo.
        Con este módulo, los usuarios pueden crear tickets de soporte, asignarlos a técnicos, y hacer seguimiento de su estado.
        """,
    "author": ["MaxRetana"],
    "category": "base",
    "version": "17.0.0.0",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "depends": ["base", "mail"],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/retana_tickets_views.xml",
        "views/retana_tickets_equipment_views.xml",
        "views/retana_tickets_equipment_brand_views.xml",
        "views/retana_tickets_equipment_type_views.xml",
    ],
}
