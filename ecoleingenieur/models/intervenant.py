from datetime import datetime
from odoo import models, fields, api


class Intervenant(models.Model):
    _name = "ecoleingenieur.intervenant"
    _description = "Un intervenant"
    _sql_constraints=[
        ("nom_unique","UNIQUE(name)","le nom d'un intervenant doit étre unique !")
    ]
    name = fields.Char(
        string="Nom",
    )
    prenom = fields.Char(
        string="Prénom"
    )
    telephone_a = fields.Char(
        string="Téléphone 1"
    )
    telephone_b = fields.Char(
        string="Téléphone 2"
    )
    telephone_c = fields.Char(
        string="Téléphone 3"
    )
    cours_ids = fields.One2many(
        "ecoleingenieur.cours",
        "intervenant_id",
        string="Cours",
    )
    bureau_id = fields.Many2one(
        "ecoleingenieur.bureau",
        string="Bureau", 
    )
    specialite_ids = fields.Many2many(
        "ecoleingenieur.specialite",
        string="Specialite", 
    )
    

   
        