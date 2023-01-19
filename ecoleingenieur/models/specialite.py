from datetime import datetime
from odoo import models, fields, api


class Specialite(models.Model):
    _name = "ecoleingenieur.specialite"
    _description = "Une specialite"
    _sql_constraints=[
        ("spec_unique","UNIQUE(name,domaine)","la clé primaire d'une spécialité doit étre unique !")
    ]
    name = fields.Char(
        string="Spécialité",
    )
    domaine = fields.Char(
        string="Domaine"
    )
    intervenant_ids = fields.Many2many(
        "ecoleingenieur.intervenant",
        string="Intervenant", 
    )
    
   
   
        