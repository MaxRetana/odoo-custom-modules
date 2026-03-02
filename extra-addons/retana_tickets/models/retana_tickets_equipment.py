from odoo import models, fields, api

class RetanaTicketsEquipment(models.Model):
    _name = 'retana.tickets.equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Equipo para Tickets de Soporte'
    
    name = fields.Char(string='Nombre del Equipo', tracking=True)
    code = fields.Char(string='Código Interno', tracking=True)
    equipment_type_id = fields.Many2one('retana.tickets.equipment.type', string='Tipo de Equipo', tracking=True)
    equipment_brand_id = fields.Many2one('retana.tickets.equipment.brand', string='Marca del Equipo', tracking=True)
    user_assigned_id = fields.Many2one('res.users', string='Usuario Asignado', tracking=True)
    date_purchase = fields.Date(string='Fecha de Compra', tracking=True)
    state = fields.Selection([
        ('new', 'Nuevo'),
        ('in_use', 'En Uso'),
        ('in_repair', 'En Reparación'),
        ('fall', 'Baja'),
    ], string='Estado', default='new', tracking=True)