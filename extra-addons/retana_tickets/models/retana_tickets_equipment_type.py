from odoo import models, fields, api

class RetanaTicketsEquipmentType(models.Model):
    _name = 'retana.tickets.equipment.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tipo de Equipo para Tickets de Soporte'
    
    name = fields.Char(string='Nombre del Tipo de Equipo', tracking=True)