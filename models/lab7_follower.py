# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Lab7Follower(models.Model):
    _name = 'lab7.follower'
    _description = '關注者'

    _inherit = 'res.partner'
    #bug_ids = fields.Many2many('lab7.bug', string='臭虫')
    # bug_ids = fields.Many2many('lab7.bug','lab_bug_follower_rel','follower_id','bug_id',string='臭虫')
    bug_ids = fields.Many2many('lab7.bug', string='臭虫')

