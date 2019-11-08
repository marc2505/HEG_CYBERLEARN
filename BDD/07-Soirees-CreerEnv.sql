/* ----------------------------------------------------------------------------
Script : 07-Soirees-CreerEnv.sql                    Auteur : Christian Stettler
Objet  : Création et remplissage des tables du modèle Soirées
---------------------------------------------------------------------------- */

ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY';

DROP TABLE heg_participe;
DROP TABLE heg_soiree;
DROP TABLE heg_personne;
DROP TABLE heg_entreprise;

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
   per_sexe   VARCHAR2(1),
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

INSERT INTO heg_entreprise VALUES (1, 'Acer',  'contact@acer.ch', 'Lausanne');
INSERT INTO heg_entreprise VALUES (2, 'DELL',  'info@dell.ch', 'Genève');
INSERT INTO heg_entreprise VALUES (3, 'SUN',   'contact@sun.com', 'Carouge');
INSERT INTO heg_entreprise VALUES (4, 'Oracle','admin@oracle.ch', 'Genève');
INSERT INTO heg_entreprise VALUES (5, 'IBM',   'client@ibm.com', 'Lausanne');
INSERT INTO heg_entreprise VALUES (6, 'Nokia', 'user@nokia.ch', 'genève');
INSERT INTO heg_entreprise VALUES (7, 'Apple', 'contact@apple.com', NULL);
COMMIT; 

INSERT INTO heg_personne VALUES ( 1, 'REMORD', 'Yves',     'M', 'yr@heg.ch', 3, NULL);
INSERT INTO heg_personne VALUES ( 2, 'VANBUS', 'Hillary',  'F', 'hv@heg.ch', 5, NULL);
INSERT INTO heg_personne VALUES ( 3, 'CARRE', 'Otto',      'M', 'oc@eig.ch', NULL, NULL);
INSERT INTO heg_personne VALUES ( 4, 'VAISSELLE', 'Aude',  'F', 'av@hes.ch', 2, NULL);
INSERT INTO heg_personne VALUES ( 5, 'TERIEUR', 'Alex',    'M', 'at@eig.ch', 3, NULL);
INSERT INTO heg_personne VALUES ( 6, 'HOCHON', 'paul',     'M', 'ph@hes.ch', 2, NULL);
INSERT INTO heg_personne VALUES ( 7, 'DORSA', 'Elsa',      'F', 'ed@heg.ch', 2, NULL);
INSERT INTO heg_personne VALUES ( 8, 'DOEUF', 'John',      'M', 'sd@heg.ch', 3, NULL);
INSERT INTO heg_personne VALUES ( 9, 'ITION', 'Aude',      'F', 'sd@hem.ch', 3, NULL);
INSERT INTO heg_personne VALUES (10, 'DISSOIRE', 'Sam',    'M',  NULL,       1, NULL);
INSERT INTO heg_personne VALUES (11, 'ROUTE', 'Otto',      'M', 'or@hes.ch', 7, NULL);
INSERT INTO heg_personne VALUES (12, 'PROVISTE', 'Alain',  'M', 'ap@heg.ch', 5, NULL);
INSERT INTO heg_personne VALUES (13, 'DESIE', 'Géo',       'M',  NULL,       3, NULL);
INSERT INTO heg_personne VALUES (14, 'TERIEUR', 'Alain',   'M', 'at@hes.ch', 7, NULL);
INSERT INTO heg_personne VALUES (15, 'LOGIE', 'Géo',       'm', 'gl@Hes.ch', NULL, NULL);
INSERT INTO heg_personne VALUES (16, 'AITERIE', 'Marc',    'M', 'ma@hem.ch', 3, NULL);
INSERT INTO heg_personne VALUES (17, 'GRAPHE', 'Géo',      'M', 'gg@hes.ch', 1, NULL);
INSERT INTO heg_personne VALUES (18, 'GRAPHIE', 'Géo',     'M', 'gg@Heg.ch', 2, NULL);
INSERT INTO heg_personne VALUES (19, 'SUE', 'alain',       'M', 'as@hem.ch', NULL, NULL);
INSERT INTO heg_personne VALUES (20, 'METRE', 'géo',       'M', 'gm@eig.ch', NULL, NULL);
INSERT INTO heg_personne VALUES (21, 'DE LUNE', 'Claire',  'F', 'cd@hem.ch', 1, NULL);
INSERT INTO heg_personne VALUES (22, 'HITMIEUX', 'Elmer',  'M',  NULL,       3, NULL);
INSERT INTO heg_personne VALUES (23, 'TIM', 'Vincent',     'M', 'vt@HEG.ch', 2, NULL);
INSERT INTO heg_personne VALUES (24, 'ATAN', 'Charles',    'M', 'ca@heg.ch', 5, NULL);
INSERT INTO heg_personne VALUES (25, 'DEBORD', 'Elvire',   'F', 'ed@hem.ch', 4, NULL);
INSERT INTO heg_personne VALUES (26, 'ASSIN', 'Marc',      'M',  NULL,       NULL, NULL);
INSERT INTO heg_personne VALUES (27, 'AVULEUR', 'Edith',   'f', 'ea@hes.ch', 3, NULL);
INSERT INTO heg_personne VALUES (28, 'CICODE', 'David',    'm',  NULL,       5, NULL);
INSERT INTO heg_personne VALUES (29, 'AIRE', 'Axel',       'M', 'aa@hes.ch', 5, NULL);
INSERT INTO heg_personne VALUES (30, 'POSTEUR', 'Alain',   'M', 'ap@Heg.ch', 5, NULL);
INSERT INTO heg_personne VALUES (31, 'SLEIGHT', 'Bob',     'M', 'bs@hem.ch', 1, NULL);
INSERT INTO heg_personne VALUES (32, 'NÉMARD', 'Jean',     'M', 'jn@eig.ch', NULL, NULL);
INSERT INTO heg_personne VALUES (33, 'POSITION', 'Paul',   'M', 'pp@heg.ch', 3, NULL);
INSERT INTO heg_personne VALUES (34, 'ONYME', 'Anne',      'F',  NULL,       5, NULL);
INSERT INTO heg_personne VALUES (35, 'HONNETE', 'Camille', 'M', 'ch@hem.ch', 3, NULL);
COMMIT; 
UPDATE heg_personne SET per_per_no =  1 WHERE per_no =  7;
UPDATE heg_personne SET per_per_no =  7 WHERE per_no =  1;
UPDATE heg_personne SET per_per_no =  9 WHERE per_no =  8;
UPDATE heg_personne SET per_per_no =  8 WHERE per_no =  9;
UPDATE heg_personne SET per_per_no = 21 WHERE per_no = 22;
UPDATE heg_personne SET per_per_no = 22 WHERE per_no = 21;
UPDATE heg_personne SET per_per_no = 34 WHERE per_no = 12;
UPDATE heg_personne SET per_per_no = 12 WHERE per_no = 34;
COMMIT; 

INSERT INTO heg_soiree VALUES ( 1, 'Soirée IGS',      '27/09/2019','25/09/2019','Battelle',15);
INSERT INTO heg_soiree VALUES ( 2, 'Soirée Disco',    '22/11/2019','17/11/2019','Carouge',15);
INSERT INTO heg_soiree VALUES ( 3, 'Pasta Party',     '18/10/2019',NULL,'Veyrier',20);
INSERT INTO heg_soiree VALUES ( 4, 'Soirée IGS',      '15/11/2019','15/11/2019','Battelle',10);
INSERT INTO heg_soiree VALUES ( 5, 'Dance Night',     '06/12/2019','06/12/2019','Lancy',30);
INSERT INTO heg_soiree VALUES ( 6, 'Soirée Profs',    '18/10/2019',NULL,'carouge',50);
INSERT INTO heg_soiree VALUES ( 7, 'Pasta Party',     '06/12/2019','01/12/2019','Carouge',20);
INSERT INTO heg_soiree VALUES ( 8, 'Soirée IGS',      '25/10/2019','16/10/2019','Battelle',20);
INSERT INTO heg_soiree VALUES ( 9, 'Soirée Tropicale','17/01/2020','10/01/2020','Battelle',25);
INSERT INTO heg_soiree VALUES (10, 'Soirée Disco',    '25/01/2020','31/12/2019','Lancy',15);
INSERT INTO heg_soiree VALUES (11, 'Soirée Profs',    '22/11/2019',NULL,'Troinex',60);
INSERT INTO heg_soiree VALUES (12, 'Soirée IGS',      '13/12/2019','10/12/2019','battelle',10);
INSERT INTO heg_soiree VALUES (13, 'Pasta Party',     '21/04/2020',NULL,'Carouge',25);
INSERT INTO heg_soiree VALUES (14, 'Dance Night',     '17/03/2020',NULL,'carouge',15);
INSERT INTO heg_soiree VALUES (15, 'Soirée IGS',      '07/05/2020','03/03/2020','Veyrier',15);
INSERT INTO heg_soiree VALUES (16, 'Pasta Party',     '25/03/2020',NULL,'Troinex',15);
INSERT INTO heg_soiree VALUES (17, 'Soirée Profs',    '28/04/2020',NULL,'Troinex',45);
INSERT INTO heg_soiree VALUES (18, 'Pasta Party',     '13/12/2019',NULL,'Carouge',20);
INSERT INTO heg_soiree VALUES (19, 'Choucroute Party','31/10/2019','22/10/2019','Carouge',35);
INSERT INTO heg_soiree VALUES (20, 'Dance Night',     '11/11/2019',NULL,'Lancy',30);
INSERT INTO heg_soiree VALUES (21, 'Pasta Party',     '15/05/2020',NULL,'Carouge',20);
INSERT INTO heg_soiree VALUES (22, 'Soirée Profs',    '13/12/2019',NULL,'Troinex',75);
INSERT INTO heg_soiree VALUES (23, 'Dance Night',     '21/04/2020','15/04/2020','Carouge',25);
COMMIT;

INSERT INTO heg_participe VALUES ( 5, 1);
INSERT INTO heg_participe VALUES ( 5, 2);
INSERT INTO heg_participe VALUES ( 5, 3);
INSERT INTO heg_participe VALUES ( 6, 10);
INSERT INTO heg_participe VALUES ( 8, 3);
INSERT INTO heg_participe VALUES ( 2, 6);
INSERT INTO heg_participe VALUES ( 9, 3);
INSERT INTO heg_participe VALUES ( 7, 3);
INSERT INTO heg_participe VALUES ( 6, 6);
INSERT INTO heg_participe VALUES ( 4, 7);
INSERT INTO heg_participe VALUES (13, 2);
INSERT INTO heg_participe VALUES (12, 7);
INSERT INTO heg_participe VALUES (15, 3);
INSERT INTO heg_participe VALUES ( 7, 4);
INSERT INTO heg_participe VALUES ( 9, 5);
INSERT INTO heg_participe VALUES ( 8, 2);
INSERT INTO heg_participe VALUES (11, 1);
INSERT INTO heg_participe VALUES (13, 6);
INSERT INTO heg_participe VALUES (15, 7);
INSERT INTO heg_participe VALUES (22, 5);
INSERT INTO heg_participe VALUES (31, 4);
INSERT INTO heg_participe VALUES (30, 6);
INSERT INTO heg_participe VALUES (31, 6);
INSERT INTO heg_participe VALUES (27, 9);
INSERT INTO heg_participe VALUES (25, 2);
INSERT INTO heg_participe VALUES (22, 1);
INSERT INTO heg_participe VALUES (18, 5);
INSERT INTO heg_participe VALUES (30, 4);
INSERT INTO heg_participe VALUES (33, 3);
INSERT INTO heg_participe VALUES (27, 8);
INSERT INTO heg_participe VALUES (22, 6);
INSERT INTO heg_participe VALUES (24, 6);
INSERT INTO heg_participe VALUES (11, 7);
INSERT INTO heg_participe VALUES (14, 2);
INSERT INTO heg_participe VALUES (22, 3);
INSERT INTO heg_participe VALUES (35, 4);
INSERT INTO heg_participe VALUES (11, 3);
INSERT INTO heg_participe VALUES ( 6, 5);
INSERT INTO heg_participe VALUES (13, 3);
INSERT INTO heg_participe VALUES (22, 2);
INSERT INTO heg_participe VALUES (13, 1);
INSERT INTO heg_participe VALUES (19, 5);
INSERT INTO heg_participe VALUES (23, 4);
INSERT INTO heg_participe VALUES ( 6, 4);
INSERT INTO heg_participe VALUES ( 7, 2);
INSERT INTO heg_participe VALUES (19, 3);
INSERT INTO heg_participe VALUES (20, 6);
INSERT INTO heg_participe VALUES (19, 6);
INSERT INTO heg_participe VALUES (28, 2);
INSERT INTO heg_participe VALUES (30, 3);
INSERT INTO heg_participe VALUES ( 2, 4);
INSERT INTO heg_participe VALUES (31, 7);
INSERT INTO heg_participe VALUES (26, 5);
INSERT INTO heg_participe VALUES (28, 8);
INSERT INTO heg_participe VALUES (25, 6);
INSERT INTO heg_participe VALUES (11, 2);
INSERT INTO heg_participe VALUES ( 6, 8);
INSERT INTO heg_participe VALUES ( 3, 6);
INSERT INTO heg_participe VALUES ( 4, 2);
INSERT INTO heg_participe VALUES (11, 6);

INSERT INTO heg_participe VALUES (11, 10);
INSERT INTO heg_participe VALUES (18, 10);
INSERT INTO heg_participe VALUES (22, 10);
INSERT INTO heg_participe VALUES (24, 10);
INSERT INTO heg_participe VALUES (30, 10);
INSERT INTO heg_participe VALUES (33, 10);
INSERT INTO heg_participe VALUES (18, 15);
INSERT INTO heg_participe VALUES (30, 14);
INSERT INTO heg_participe VALUES (33, 13);
INSERT INTO heg_participe VALUES (22, 16);
INSERT INTO heg_participe VALUES (24, 16);
INSERT INTO heg_participe VALUES (11, 17);
INSERT INTO heg_participe VALUES (22, 13);
INSERT INTO heg_participe VALUES (35, 14);
INSERT INTO heg_participe VALUES (11, 13);
INSERT INTO heg_participe VALUES ( 6, 15);
INSERT INTO heg_participe VALUES (13, 13);
INSERT INTO heg_participe VALUES (19, 15);
INSERT INTO heg_participe VALUES (23, 14);
INSERT INTO heg_participe VALUES ( 6, 14);
INSERT INTO heg_participe VALUES (19, 13);
INSERT INTO heg_participe VALUES (20, 16);
INSERT INTO heg_participe VALUES (19, 16);
INSERT INTO heg_participe VALUES (30, 13);
INSERT INTO heg_participe VALUES ( 2, 14);
INSERT INTO heg_participe VALUES (31, 17);
INSERT INTO heg_participe VALUES (26, 15);
INSERT INTO heg_participe VALUES (25, 16);
INSERT INTO heg_participe VALUES ( 3, 16);
INSERT INTO heg_participe VALUES (11, 16);
COMMIT;
