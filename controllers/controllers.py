# -*- coding: utf-8 -*-
from odoo import http

# class Lab7(http.Controller):
#     @http.route('/lab7/lab7/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lab7/lab7/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lab7.listing', {
#             'root': '/lab7/lab7',
#             'objects': http.request.env['lab7.lab7'].search([]),
#         })

#     @http.route('/lab7/lab7/objects/<model("lab7.lab7"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lab7.object', {
#             'object': obj
#         })