from datetime import datetime
from odoo import models, fields, api


class Bureau(models.Model):
    _name = "ecoleingenieur.bureau"
    _description = "Un bureau"
    _sql_constraints=[
        ("cl_unique","UNIQUE(name,batiment,centre)","La clé doit étre unique"),
        ("nombre","CHECK(name<=1000)","le numéro du bureau doit étre inférieur à 1000 !")
        
    ]
    name = fields.Integer(
        string="numBureau",
    )
    batiment = fields.Selection(selection=[("A", "A"),("B", "B"),("C","C"),
    ("D", "D"),("E", "E"),("F", "F"),("G", "G"),("H", "H"),("I", "I"),("J", "J"),("K", "K"),
    ("L", "L"),("M", "M"),("N", "N"),("O", "O"),("P", "P"),("Q", "Q"),
    ("R", "R"),("S", "S"),("T", "T"),("U", "U"),("V", "V"),("W", "W"),
    ("X", "X"),("Y", "Y"),("Z", "Z"),], string="Batiment", default="A")
    centre = fields.Selection(selection=[("R", "R"),("BF", "BF"),("PG","PG"),], string="Centre", default="R")
    intervenant_ids = fields.One2many(
        "ecoleingenieur.intervenant",
        "bureau_id",
        string="Intervenant",
    )
   
   
        