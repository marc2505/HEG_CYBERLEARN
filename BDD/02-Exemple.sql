/* ----------------------------------------------------------------------------
Script : 02-Exemple-LDD.sql                         Auteur : Christian Stettler
Objet  : Création des tables d'exemple
---------------------------------------------------------------------------- */

-- Suppression des tables pour que le script soit réexecutable

DROP TABLE exe_employe;
DROP TABLE exe_dept;

-- Création des tables

CREATE TABLE exe_dept (
   dep_no       NUMBER(5),
   dep_nom      VARCHAR2(20)
);

CREATE TABLE exe_employe (
   emp_no       NUMBER(5),
   emp_prenom   VARCHAR2(20),
   emp_nom      VARCHAR2(20),
   emp_email    VARCHAR2(25),
   emp_embauche DATE,
   emp_salaire  NUMBER(8,2),
   emp_emp_no   NUMBER(5),
   emp_dep_no   NUMBER(5)
);