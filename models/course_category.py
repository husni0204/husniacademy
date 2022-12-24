# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = "husniacademy.course.category"
    _description = "Data Course Category"

    name = fields.Char(string="Course Category Name", required=True, help="Fill category name...")

    description = fields.Text(string="Description")

    active = fields.Boolean(string="Active", default=True)

    course_ids = fields.One2many(
        comodel_name="husni_academy.course", 
        inverse_name="category_id", 
        string="Course")
    