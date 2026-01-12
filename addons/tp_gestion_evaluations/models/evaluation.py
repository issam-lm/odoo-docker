from odoo import models, fields

class TpEvaluation(models.Model):
    _name = "tp.evaluation"
    _description = "Évaluation TP"
    _order = "name"

    name = fields.Char(string="Nom de l'évaluation", required=True)
    responsible = fields.Char(string="Responsable")
    date_debut = fields.Date(string="Date de début")
    statut = fields.Selection([
        ("brouillon", "Brouillon"),
        ("en_cours", "En cours"),
        ("termine", "Terminé"),
    ], string="Statut", default="brouillon")
    description = fields.Text(string="Description")
