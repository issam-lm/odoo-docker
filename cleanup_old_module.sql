-- Script pour nettoyer toutes les références à l'ancien module tp_gestion_projets
-- À exécuter dans la base de données PostgreSQL

-- Supprimer les vues de l'ancien modèle
DELETE FROM ir_ui_view WHERE model = 'tp.projet';

-- Supprimer les actions associées à l'ancien modèle
DELETE FROM ir_actions_act_window WHERE res_model = 'tp.projet';

-- Supprimer les menus associés à l'ancien module
DELETE FROM ir_ui_menu WHERE name LIKE '%Projets TP%' OR name LIKE '%Gestion des Projets%';

-- Supprimer les règles d'accès de l'ancien modèle
DELETE FROM ir_model_access WHERE name LIKE '%tp_projet%';

-- Supprimer les données du modèle (si elles existent)
DELETE FROM tp_projet;

-- Supprimer le modèle lui-même de la table ir_model
DELETE FROM ir_model WHERE model = 'tp.projet';

-- Supprimer les champs du modèle
DELETE FROM ir_model_fields WHERE model = 'tp.projet';

