/* ----------------------------------------------------------------------------
Script : 03-Soirees-Constraint.sql                  Auteur : Christian Stettler
Objet  : Rajout des contraintes de validation particulières
---------------------------------------------------------------------------- */

-- Ajout des contraintes suivantes :
--    - toutes les PK (clés primaires)
--    - toutes les FK (clés étrangères)

-- les contraintes de validation suivantes :
--    - tous les noms (personne, entreprise, soirée) sont obligatoires
--    - le nom d'une entreprise doit être unique
--    - le sexe d'une personne est soit M, soit F
--    - le prix des soirées ne peut pas être négatif
--    - il ne peut jamais y avoir deux soirées qui ont exactement le même nom à la même date
--    - la date limite d'inscription à une soirée est obligatoirement antérieure à la date de cette soirée

-- ----------------------------------------------------------------------------

--    - toutes les PK (clés primaires)
ALTER TABLE heg_entreprise MODIFY ent_no CONSTRAINT pk_heg_entreprise PRIMARY KEY;
ALTER TABLE heg_personne   MODIFY per_no CONSTRAINT pk_heg_personne PRIMARY KEY;
ALTER TABLE heg_soiree     MODIFY soi_no CONSTRAINT pk_heg_soiree PRIMARY KEY;
ALTER TABLE heg_participe  ADD CONSTRAINT pk_heg_participe PRIMARY KEY(par_per_no, par_soi_no);

--    - toutes les FK (clés étrangères)
ALTER TABLE heg_personne ADD (
   CONSTRAINT fk_heg_personne_entreprise FOREIGN KEY(per_ent_no) REFERENCES heg_entreprise(ent_no),
   CONSTRAINT fk_heg_personne_conjoint   FOREIGN KEY(per_per_no) REFERENCES heg_personne(per_no)
);

ALTER TABLE heg_participe ADD (
   CONSTRAINT fk_heg_participe_personne FOREIGN KEY(par_per_no) REFERENCES heg_personne(per_no),
   CONSTRAINT fk_heg_participe_soiree   FOREIGN KEY(par_soi_no) REFERENCES heg_soiree(soi_no)
);

-- les contraintes de validation suivantes :
ALTER TABLE heg_personne   MODIFY per_nom CONSTRAINT nn_per_nom NOT NULL;
ALTER TABLE heg_entreprise MODIFY ent_nom CONSTRAINT nn_ent_nom NOT NULL;
ALTER TABLE heg_soiree     MODIFY soi_nom CONSTRAINT nn_soi_nom NOT NULL;

ALTER TABLE heg_entreprise MODIFY ent_nom CONSTRAINT uk_ent_nom UNIQUE;
-- ou ALTER TABLE heg_entreprise ADD CONSTRAINT uk_ent_nom UNIQUE(ent_nom);

ALTER TABLE heg_personne ADD CONSTRAINT ch_per_sexe CHECK(per_sexe IN ('M', 'F'));

ALTER TABLE heg_soiree ADD (
   CONSTRAINT ch_soi_prix CHECK(soi_prix >= 0),
   CONSTRAINT uk_soi_nom_date UNIQUE(soi_nom, soi_date),
   CONSTRAINT ch_soi_date CHECK(soi_inscr <= soi_date)
);

-- ----------------------------------------------------
/* A la création des tables, on aurait du faire ainsi :

CREATE TABLE heg_entreprise (
   ent_no     NUMBER(5)    CONSTRAINT pk_heg_entreprise PRIMARY KEY,
   ent_nom    VARCHAR2(20) CONSTRAINT nn_ent_nom NOT NULL CONSTRAINT uk_ent_nom UNIQUE,
   ent_mail   VARCHAR2(20),
   ent_ville  VARCHAR2(20)
);

CREATE TABLE heg_personne (
   per_no     NUMBER(5)    CONSTRAINT pk_heg_personne PRIMARY KEY,
   per_nom    VARCHAR2(20) CONSTRAINT nn_per_nom NOT NULL,
   per_prenom VARCHAR2(20),
   per_sexe   VARCHAR2(1)  CONSTRAINT ch_per_sexe CHECK(per_sexe IN ('M', 'F')),
   per_mail   VARCHAR2(20),
   per_ent_no NUMBER(5)    CONSTRAINT fk_heg_personne_entreprise REFERENCES heg_entreprise(ent_no),
   per_per_no NUMBER(5)    CONSTRAINT fk_heg_personne_conjoint REFERENCES heg_personne(per_no)
);

CREATE TABLE heg_soiree (
   soi_no     NUMBER(5)    CONSTRAINT pk_heg_soiree PRIMARY KEY,
   soi_nom    VARCHAR2(25) CONSTRAINT nn_soi_nom NOT NULL,
   soi_date   DATE,
   soi_inscr  DATE,
   soi_lieu   VARCHAR2(25),
   soi_prix   NUMBER(5,2)  CONSTRAINT ch_soi_prix CHECK(soi_prix >= 0),
   CONSTRAINT uk_soi_nom_date UNIQUE(soi_nom, soi_date),
   CONSTRAINT ch_soi_date CHECK(soi_inscr <= soi_date)
);

CREATE TABLE heg_participe (
   par_per_no NUMBER(5) CONSTRAINT fk_heg_participe_personne REFERENCES heg_personne(per_no),
   par_soi_no NUMBER(5) CONSTRAINT fk_heg_participe_soiree   REFERENCES heg_soiree(soi_no),
   CONSTRAINT pk_heg_participe PRIMARY KEY(par_per_no, par_soi_no)
);
*/
