# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital patient Model just for testing...."

    name = fields.Char(required=True)
