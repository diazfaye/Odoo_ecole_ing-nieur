from datetime import datetime
from datetime import timedelta
from odoo import models, fields, api


class Cours(models.Model):
    _name = "ecoleingenieur.cours"
    _description = "Cours"
    _sql_constraints=[
        ("an_unique","UNIQUE(name,numero)","la clé primaire pour un cours doit étre unique !")
    ]
    
    @api.depends("date_debut")
    def _compute_dateFin(self):
        for record in self:
            if record.date_debut:
                record.date_fin = record.date_debut + timedelta(days = 5)
            else:
                record.date_fin = False

    name = fields.Integer(
        string="Annee Cours",
    )
    numero = fields.Integer(
        string="Numéro du cours"
    )
    titre =fields.Char(
        string='Titre'
    )
    autype = fields.Selection(selection=[("C", "C"),("TD", "TD"),("TP","TP"),], string="Type", default="C")
    date_debut = fields.Date(
        string="Date début cours"
    )
    date_fin = fields.Date(
        string="Date fin cours", compute="_compute_dateFin"
    )
    intervenant_id = fields.Many2one(
        "ecoleingenieur.intervenant",
        string="Intervenant", 
    )
   
   
        