/* ----------------------------------------------------------------------------
Script : 04-Soirees-Insert.sql                      Auteur : Christian Stettler
Objet  : Insertion des données, et test des contraintes d'intégrité
---------------------------------------------------------------------------- */

-- a) insertion des données initiales
INSERT INTO heg_entreprise VALUES (1, 'Acer',  'contact@acer.ch', 'Lausanne');
INSERT INTO heg_entreprise VALUES (2, 'DELL',  'info@dell.ch', 'Genève');
INSERT INTO heg_entreprise VALUES (3, 'SUN',   'contact@sun.com', 'Carouge');
INSERT INTO heg_entreprise VALUES (4, 'Oracle','admin@oracle.ch', 'Genève');
INSERT INTO heg_entreprise VALUES (5, 'IBM',   'client@ibm.com', 'Lausanne');
INSERT INTO heg_entreprise VALUES (6, 'Nokia', 'user@nokia.ch', 'genève');
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

INSERT INTO heg_soiree (soi_no, soi_nom, soi_date, soi_inscr, soi_lieu, soi_prix) VALUES (1, 'Soirée IGS','28/09/2019','26/09/2019','Battelle',15);
INSERT INTO heg_soiree (soi_no, soi_nom, soi_date, soi_inscr, soi_lieu, soi_prix) VALUES (2, 'Soirée IGS','26/10/2019','24/10/2019','Battelle',20);
INSERT INTO heg_soiree (soi_no, soi_nom, soi_date, soi_inscr, soi_lieu, soi_prix) VALUES (3, 'Soirée Profs','26/10/2019',NULL,'Carouge',50);
COMMIT;

-- b) modifications & compléments :

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
Test des contraintes d'intégrité : Clé primaire / étrangère / unique / check / nn
---------------------------------------------------------------------------- */

-- PK: Démontrer le fonctionnement des CLÉS PRIMAIRES
--     Message retourné: ORA-00001: violation de contrainte unique (SYSTEM.PK_HEG_PERSONNE)
INSERT INTO heg_personne VALUES (1, 'Test', 'PK', 'M', 'xx@heg.ch', 1, NULL);
INSERT INTO heg_entreprise VALUES (1, 'Test PK', 'xx@heg.ch', NULL);
INSERT INTO heg_soiree VALUES (1, 'Test PK','01/10/2019','01/10/2019','Battelle',10);
INSERT INTO heg_participe VALUES (5, 1);

-- FK: Démontrer le fonctionnement des CLÉS ÉTRANGÈRES
--     Message retourné: ORA-02291: violation de contrainte d'intégrité (SYSTEM.FK_HEG_PERSONNE_ENTREPRISE) - clé parent introuvable
INSERT INTO heg_personne VALUES (20, 'Test FK', 'Test FK entreprise', 'M', 'xx@heg.ch', 99, NULL);
INSERT INTO heg_personne VALUES (20, 'Test FK', 'Test FK conjoint', 'M', 'xx@heg.ch', 1, 99);
INSERT INTO heg_participe VALUES (99, 1);
INSERT INTO heg_participe VALUES (1, 99);

-- NN: Démontrer le fonctionnement des noms OBLIGATOIRES
--     Message retourné: ORA-01400: impossible d'insérer NULL dans ("SYSTEM"."HEG_PERSONNE"."SOI_NOM")
INSERT INTO heg_personne VALUES (20, NULL, 'Test nom vide', 'M', 'xx@heg.ch', 1, NULL);
INSERT INTO heg_entreprise VALUES (20, '', 'Test nom vide', NULL);
INSERT INTO heg_soiree VALUES (20, NULL,'01/10/2019','01/10/2019','Test nom vide',10);

-- UK: Démontrer le fonctionnement des valeurs UNIQUES: nom d'entreprise / nom&date soirée
--     Message retourné: ORA-00001: violation de contrainte unique (SYSTEM.UK_ENT_NOM)
INSERT INTO heg_entreprise VALUES (20, 'SUN', 'Test nom existant', NULL);
INSERT INTO heg_soiree VALUES (20, 'Soirée IGS','28/09/2019','01/09/2019','Nom et date existe déjà',10);

-- CH: Contraintes de check: per_sexe='M'ou'F' / soi_prix>=0 / soi_inscr<=soi_date
--     Message retourné: ORA-02290: violation de contraintes (SYSTEM.CH_PER_SEXE) de vérification
INSERT INTO heg_personne VALUES (20, 'Sexe X', 'Test Check sexe', 'X', 'xx@heg.ch', 1, NULL);
INSERT INTO heg_soiree VALUES (20, 'Prix négatif','01/10/2019','01/10/2019','Test prix erroné',-10);
INSERT INTO heg_soiree VALUES (20, 'Dates erronées','01/10/2019','05/10/2019','Test dates erronées',10);
