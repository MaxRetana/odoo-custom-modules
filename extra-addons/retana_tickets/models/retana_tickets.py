from odoo import models, fields, api

class RetanaTickets(models.Model):
    _name = 'retana.tickets'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tickets de Soporte'
    
    name = fields.Char(string='Ticket', default='Nuevo', tracking=True)
    equipment_id = fields.Many2one('retana.tickets.equipment', string='Equipo Relacionado', tracking=True)
    user_reported_id = fields.Many2one('res.users', string='Usuario que Reporta', tracking=True)
    user_assigned_id = fields.Many2one('res.users', string='Usuario Asignado', tracking=True)
    description = fields.Text(string='Descripción del Problema', tracking=True)
    priority = fields.Selection([
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
        ('critical', 'Crítica'),
    ], string='Prioridad', default='medium', tracking=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_revision', 'En Revisión'),
        ('in_progress', 'En Progreso'),
        ('resolved', 'Resuelto'),
        ('cancel', 'Cancelado'),
    ], string='Estado', default='draft', tracking=True)
    
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals.get('name') == 'Nuevo':
                # Buscar si existe la secuencia, si no existe la crea
                sequence = self.env['ir.sequence'].search([('code', '=', 'retana.tickets')], limit=1)
                if not sequence:
                    sequence = self.env['ir.sequence'].create({
                        'name': 'Retana Ticket Sequence',
                        'code': 'retana.tickets',
                        'prefix': 'RT',
                        'padding': 4,
                        'number_next': 1,
                        'number_increment': 1,
                    })
                
                # Generar el siguiente número
                next_number = self.env['ir.sequence'].next_by_code('retana.tickets') or '0001'
                vals['name'] = f"{next_number}"
        return super().create(vals_list)