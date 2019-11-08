/* ----------------------------------------------------------------------------
Script : 00-CreerEnv.sql                            Auteur : Christian Stettler
Objet  : Création et remplissage des tables d'exemple
---------------------------------------------------------------------------- */

DROP TABLE exe_employe;
DROP TABLE exe_dept;

CREATE TABLE exe_dept (
   dep_no       NUMBER(5)    CONSTRAINT pk_exe_dept PRIMARY KEY,
   dep_nom      VARCHAR2(20)
);

CREATE TABLE exe_employe (
   emp_no       NUMBER(5)    CONSTRAINT pk_exe_employe PRIMARY KEY,
   emp_prenom   VARCHAR2(20),
   emp_nom      VARCHAR2(20) CONSTRAINT nn_emp_nom     NOT NULL,
   emp_email    VARCHAR2(25) CONSTRAINT uk_emp_email   UNIQUE,
   emp_embauche DATE DEFAULT SYSDATE CONSTRAINT nn_emp_embauche NOT NULL,
   emp_salaire  NUMBER(8,2)  CONSTRAINT ch_emp_salaire CHECK (emp_salaire > 0),
   emp_emp_no   NUMBER(5)    CONSTRAINT fk_exe_employe_chef REFERENCES exe_employe (emp_no),
   emp_dep_no   NUMBER(4)    CONSTRAINT fk_exe_employe_dept REFERENCES exe_dept (dep_no)
);

INSERT INTO exe_dept VALUES (1,'RH');
INSERT INTO exe_dept VALUES (2,'Achat');
INSERT INTO exe_dept VALUES (3,'Vente');
INSERT INTO exe_dept VALUES (4,'Marketing');
INSERT INTO exe_dept VALUES (5,'Production');
COMMIT; 

INSERT INTO exe_employe VALUES (1,'Jean', 'BON',      'jb@heg.ch', '01.01.2000',5000,NULL,1);
INSERT INTO exe_employe VALUES (2,'Yves', 'REMORD',    NULL,       '01.08.2008',4000,1,3);
INSERT INTO exe_employe VALUES (3,'Alex', 'TERIEUR',  'at@heg.ch', '01.03.2003',6000,1,NULL);
INSERT INTO exe_employe VALUES (4,'Alain','PROVISTE', 'ap@heg.ch', '01.02.2002',8000,1,4);
INSERT INTO exe_employe VALUES (5,'Alain','TERIEUR',  'it@heg.ch', '01.06.2006',5000,1,5);
INSERT INTO exe_employe VALUES (6,'Sam',  'DISSOIRE',  NULL,        DEFAULT,    5000,2,4);
INSERT INTO exe_employe VALUES (7,'Elsa', 'DORSA',    'ed@heg.ch', '01.02.2002',7000,3,3);
INSERT INTO exe_employe VALUES (8,'alain','POSTEUR',  'as@heg.ch', '01.08.2008',NULL,5,5);
INSERT INTO exe_employe VALUES (9,'Anne', 'ONYME',    'ao@heg.ch', '01.04.2004',6000,4,5);
COMMIT;