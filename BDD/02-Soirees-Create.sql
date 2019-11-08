/* ----------------------------------------------------------------------------
Script : 02-Soirees-Create.sql                      Auteur : Christian Stettler
Objet  : Création des tables du cas Soirees
---------------------------------------------------------------------------- */

-- Suppression des tables pour que le script soit réexecutable

DROP TABLE heg_personne;
DROP TABLE heg_entreprise;
DROP TABLE heg_participe;
DROP TABLE heg_soiree;

-- création des tables

CREATE TABLE heg_personne (
   per_no     NUMBER(5),
   per_nom    VARCHAR2(20),
   per_prenom VARCHAR2(20),
   per_sexe   VARCHAR2(1),
   per_mail   VARCHAR2(20),
   per_ent_no NUMBER(5),
   per_per_no NUMBER(5)
);

CREATE TABLE heg_entreprise (
   ent_no     NUMBER(5),
   ent_nom    VARCHAR2(20),
   ent_mail   VARCHAR2(20),
   ent_ville  VARCHAR2(20)
);

CREATE TABLE heg_participe (
   par_per_no NUMBER(5),
   par_soi_no NUMBER(5)
);

CREATE TABLE heg_soiree (
   soi_no     NUMBER(5),
   soi_nom    VARCHAR2(25),
   soi_date   DATE,
   soi_inscr  DATE,
   soi_lieu   VARCHAR2(25),
   soi_prix   NUMBER(5,2)
);