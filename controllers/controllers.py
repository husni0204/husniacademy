# -*- coding: utf-8 -*-
# from odoo import http


# class Husniacademy(http.Controller):
#     @http.route('/husniacademy/husniacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/husniacademy/husniacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('husniacademy.listing', {
#             'root': '/husniacademy/husniacademy',
#             'objects': http.request.env['husniacademy.husniacademy'].search([]),
#         })

#     @http.route('/husniacademy/husniacademy/objects/<model("husniacademy.husniacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('husniacademy.object', {
#             'object': obj
#         })
