# -*- coding: utf-8 -*-

from odoo import models, fields, api



class tags(models.Model):
    _name = 'tags'

    name=fields.Char('Name')

class Copartner(models.Model):
    _name = 'copartner'
    _description = 'Copartners'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    country = fields.Char(string='Country')
    joining_date = fields.Date(string='Joining Date')
    tags = fields.Many2many('tags', string='Tags')
    customer_ids = fields.Many2many('res.partner', string='Customers')
    company_id = fields.Many2one('res.company', string='Company', required=True)
    notes = fields.Text(string='Notes')
    comments = fields.Char(string='Comments')