from odoo import models, fields, api

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    department_id = fields.Many2one('hr.department', string='Department')

class FleetVehicleRequest(models.Model):
    _name = 'fleet.vehicle.request'
    _description = 'Vehicle Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    requested_by = fields.Many2one('res.users', string='Requested By', default=lambda self: self.env.user, readonly=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', compute='_compute_employee', store=True)
    department_id = fields.Many2one('hr.department', string='Department', related='employee_id.department_id', store=True)
    purpose = fields.Text(string='Purpose of Request', required=True)
    request_date = fields.Date(string='Request Date', default=fields.Date.today, readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)

    @api.depends('requested_by')
    def _compute_employee(self):
        for record in self:
            record.employee_id = self.env['hr.employee'].search([('user_id', '=', record.requested_by.id)], limit=1)

    def action_submit(self):
        self.state = 'submitted'

    def action_approve(self):
        self.state = 'approved'

    def action_reject(self):
        self.state = 'rejected'