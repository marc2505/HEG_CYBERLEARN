/* ----------------------------------------------------------------------------
Script : 04-Soirees-Insert.sql                      Auteur : Christian Stettler
Objet  : Insertion des donn�es, et test des contraintes d'int�grit�
---------------------------------------------------------------------------- */

-- a) insertion des donn�es initiales
INSERT INTO heg_entreprise VALUES (1, 'Acer',  'contact@acer.ch', 'Lausanne');
INSERT INTO heg_entreprise VALUES (2, 'DELL',  'info@dell.ch', 'Gen�ve');
INSERT INTO heg_entreprise VALUES (3, 'SUN',   'contact@sun.com', 'Carouge');
INSERT INTO heg_entreprise VALUES (4, 'Oracle','admin@oracle.ch', 'Gen�ve');
INSERT INTO heg_entreprise VALUES (5, 'IBM',   'client@ibm.com', 'Lausanne');
INSERT INTO heg_entreprise VALUES (6, 'Nokia', 'user@nokia.ch', 'gen�ve');
INSERT INTO heg_entreprise VALUES (7, 'Apple', 'contact@apple.com', NULL);
COMMIT; 


INSERT INTO heg_personne VALUES ( 1, 'REMORD', 'Yves',    'M', 'yr@heg.ch', 3, NULL);
INSERT INTO heg_personne VALUES ( 2, 'VANBUS', 'Hillary', 'F', 'hv@heg.ch', 5, NULL);
INSERT INTO heg_personne VALUES ( 3, 'CARRE', 'Otto',     'M', 'oc@eig.ch', NULL, NULL);
INSERT INTO heg_personne VALUES ( 4, 'VAISSELLE', 'Aude', 'F', 'av@hes.ch', 2, NULL);
INSERT INTO heg_personne VALUES ( 5, 'TERIEUR', 'Alex',   'M', 'at@eig.ch', 3, NULL);
INSERT INTO heg_personne VALUES ( 6, 'HOCHON', 'paul',    'M', 'ph@hes.ch', 2, NULL);
INSERT INTO heg_personne VALUES ( 7, 'DORSA', 'Elsa',     'F', 'ed@heg.ch', 2, NULL);
COMMIT; 

INSERT INTO heg_soiree (soi_no, soi_nom, soi_date, soi_inscr, soi_lieu, soi_prix) VALUES (1, 'Soir�e IGS','28/09/2019','26/09/2019','Battelle',15);
INSERT INTO heg_soiree (soi_no, soi_nom, soi_date, soi_inscr, soi_lieu, soi_prix) VALUES (2, 'Soir�e IGS','26/10/2019','24/10/2019','Battelle',20);
INSERT INTO heg_soiree (soi_no, soi_nom, soi_date, soi_inscr, soi_lieu, soi_prix) VALUES (3, 'Soir�e Profs','26/10/2019',NULL,'Carouge',50);
COMMIT;

-- b) modifications & compl�ments :

-- le couple suivant :
INSERT INTO heg_personne (per_no, per_nom, per_prenom, per_sexe, per_ent_no) VALUES (8, 'DOEUF', 'John', 'M', 3);
INSERT INTO heg_personne (per_no, per_nom, per_prenom, per_sexe, per_ent_no, per_per_no) VALUES (9, 'ITION', 'Aude', 'F', 3, 8);
UPDATE heg_personne SET per_per_no = 9 WHERE per_no = 8;
COMMIT;

-- ainsi que le fait que ....
INSERT INTO heg_participe (par_per_no, par_soi_no) VALUES (5, 1);
INSERT INTO heg_participe (par_per_no, par_soi_no) VALUES (5, 2);
INSERT INTO heg_participe (par_per_no, par_soi_no) VALUES (5, 3);
INSERT INTO heg_participe (par_per_no, par_soi_no) VALUES (6, 1);
INSERT INTO heg_participe (par_per_no, par_soi_no) VALUES (8, 3);
INSERT INTO heg_participe (par_per_no, par_soi_no) VALUES (9, 3);
UPDATE heg_personne SET per_ent_no = 2 WHERE per_no = 5;
UPDATE heg_personne SET per_per_no = 1, per_nom = 'REMORD-DORSA' WHERE per_no = 7;
UPDATE heg_personne SET per_per_no = 7 WHERE per_no = 1;
UPDATE heg_soiree SET soi_prix = soi_prix + 3 WHERE UPPER(soi_lieu) = 'BATTELLE';
UPDATE heg_participe SET par_soi_no = 2 WHERE par_per_no = 8 AND par_soi_no = 3;
-- ou: DELETE FROM heg_participe WHERE par_per_no = 8 AND par_soi_no = 3;  INSERT INTO heg_participe (par_per_no, par_soi_no) VALUES (8, 2);
COMMIT;


/* ----------------------------------------------------------------------------
Test des contraintes d'int�grit� : Cl� primaire / �trang�re / unique / check / nn
---------------------------------------------------------------------------- */

-- PK: D�montrer le fonctionnement des CL�S PRIMAIRES
--     Message retourn�: ORA-00001: violation de contrainte unique (SYSTEM.PK_HEG_PERSONNE)
INSERT INTO heg_personne VALUES (1, 'Test', 'PK', 'M', 'xx@heg.ch', 1, NULL);
INSERT INTO heg_entreprise VALUES (1, 'Test PK', 'xx@heg.ch', NULL);
INSERT INTO heg_soiree VALUES (1, 'Test PK','01/10/2019','01/10/2019','Battelle',10);
INSERT INTO heg_participe VALUES (5, 1);

-- FK: D�montrer le fonctionnement des CL�S �TRANG�RES
--     Message retourn�: ORA-02291: violation de contrainte d'int�grit� (SYSTEM.FK_HEG_PERSONNE_ENTREPRISE) - cl� parent introuvable
INSERT INTO heg_personne VALUES (20, 'Test FK', 'Test FK entreprise', 'M', 'xx@heg.ch', 99, NULL);
INSERT INTO heg_personne VALUES (20, 'Test FK', 'Test FK conjoint', 'M', 'xx@heg.ch', 1, 99);
INSERT INTO heg_participe VALUES (99, 1);
INSERT INTO heg_participe VALUES (1, 99);

-- NN: D�montrer le fonctionnement des noms OBLIGATOIRES
--     Message retourn�: ORA-01400: impossible d'ins�rer NULL dans ("SYSTEM"."HEG_PERSONNE"."SOI_NOM")
INSERT INTO heg_personne VALUES (20, NULL, 'Test nom vide', 'M', 'xx@heg.ch', 1, NULL);
INSERT INTO heg_entreprise VALUES (20, '', 'Test nom vide', NULL);
INSERT INTO heg_soiree VALUES (20, NULL,'01/10/2019','01/10/2019','Test nom vide',10);

-- UK: D�montrer le fonctionnement des valeurs UNIQUES: nom d'entreprise / nom&date soir�e
--     Message retourn�: ORA-00001: violation de contrainte unique (SYSTEM.UK_ENT_NOM)
INSERT INTO heg_entreprise VALUES (20, 'SUN', 'Test nom existant', NULL);
INSERT INTO heg_soiree VALUES (20, 'Soir�e IGS','28/09/2019','01/09/2019','Nom et date existe d�j�',10);

-- CH: Contraintes de check: per_sexe='M'ou'F' / soi_prix>=0 / soi_inscr<=soi_date
--     Message retourn�: ORA-02290: violation de contraintes (SYSTEM.CH_PER_SEXE) de v�rification
INSERT INTO heg_personne VALUES (20, 'Sexe X', 'Test Check sexe', 'X', 'xx@heg.ch', 1, NULL);
INSERT INTO heg_soiree VALUES (20, 'Prix n�gatif','01/10/2019','01/10/2019','Test prix erron�',-10);
INSERT INTO heg_soiree VALUES (20, 'Dates erron�es','01/10/2019','05/10/2019','Test dates erron�es',10);
