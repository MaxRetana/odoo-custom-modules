from odoo import models, fields, api

class RetanaTicketsEquipmentBrand(models.Model):
    _name = 'retana.tickets.equipment.brand'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Marca de Equipo para Tickets de Soporte'
    
    name = fields.Char(string='Nombre de la Marca', tracking=True)