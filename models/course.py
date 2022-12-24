# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = "husni_academy.course"
    _description = "Data Course"

    name = fields.Char(string="Nama Kursus", required=True, help="Fill course name...")

    description = fields.Text(string="Penjelasan")

    active = fields.Boolean(string="Active", default=True)

    category_id = fields.Many2one(
        comodel_name="husniacademy.course.category", 
        string="Category"
        )
    