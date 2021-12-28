# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lab7Bug(models.Model):
    _name = 'lab7.bug'
    _description = '程式臭虫(Bug)'

    name = fields.Char(string='Bug簡述', required=True)
    detail = fields.Text(string='詳細說明', size=150)
    is_closed = fields.Boolean(string='是否關閉')
    close_reason = fields.Selection([('changed', '已修改'), ('cannot', '無法修改'), ('delay', '延遲')],
                                    string='關閉理由')
    user_id = fields.Many2one('res.users', string='程式設計師')
    follower_ids = fields.Many2many('res.partner', string='關注者')
    #follower_ids = fields.Many2many('lab7.follower','lab_bug_follower_rel','bug_id','follower_id', string='關注者')

    @api.multi
    def do_close(self):
        for item in self:
            item.is_closed = True
            return True
