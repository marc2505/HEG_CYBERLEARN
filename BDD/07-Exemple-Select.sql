/* ----------------------------------------------------------------------------
Script : 07-Exemple-Select.sql                      Auteur : Christian Stettler
Objet  : Exemples d'instruction SELECT
---------------------------------------------------------------------------- */

SELECT * FROM exe_employe;                              -- tous les champs de tous les employ�s
SELECT emp_nom, emp_prenom FROM exe_employe;            -- certains champs de tous les employ�s
SELECT * FROM exe_employe WHERE emp_salaire > 5000;     -- tous les champs de certains employ�s
SELECT emp_nom, emp_prenom FROM exe_employe WHERE emp_salaire > 5000; -- certains champs de certains employ�s

SELECT * FROM exe_employe ORDER BY emp_nom, emp_prenom; -- tri� par nom/pr�nom
SELECT * FROM exe_employe ORDER BY emp_salaire DESC;    -- tri� du plus grand au plus petit salaire

SELECT * FROM exe_employe WHERE emp_nom = 'TERIEUR';    -- tous ceux dont le nom = TERIEUR (Attention MAJ/MIN !!)
SELECT * FROM exe_employe WHERE emp_nom LIKE 'T%';      -- tous ceux dont le nom commence par T majuscule
SELECT * FROM exe_employe WHERE emp_nom LIKE '%T%';     -- tous ceux dont le nom contient un T majuscule

SELECT * FROM exe_employe WHERE emp_salaire BETWEEN 5000 AND 6000; -- entre 2 bornes num�riques
SELECT * FROM exe_employe WHERE emp_nom BETWEEN 'C' AND 'P';       -- entre 2 bornes textes

SELECT * FROM exe_employe WHERE emp_dep_no IN (1, 4, 5);           -- dont le d�partement est 1, 4 ou 5

SELECT * FROM exe_employe WHERE emp_email IS NULL;                 -- qui n'ont pas de mail

SELECT emp_nom, emp_prenom FROM exe_employe WHERE ROWNUM <= 5;     -- ne r�cup�re que 5 enregistrements

SELECT * FROM exe_employe WHERE UPPER(emp_prenom) = 'ALAIN';       -- comparaison correcte des strings

SELECT emp_nom, emp_salaire * 12 FROM exe_employe;                 -- champ calcul�
SELECT emp_prenom || ' ' || emp_nom FROM exe_employe;              -- concat�nation de valeurs dans un seul champ
SELECT emp_prenom || ' ' || emp_nom AS "Employ�" FROM exe_employe; -- Alias de colonne (nouveau nom de champ)

/* ----------------------------------------------------------------------------
====================   Les JOINtures   ========================================
---------------------------------------------------------------------------- */

SELECT * FROM exe_employe;   -- TOUS les employ�s
SELECT * FROM exe_dept;      -- TOUS les d�partements

SELECT * FROM exe_employe       JOIN exe_dept ON dep_no=emp_dep_no; -- CHAQUE employe dans SON d�partement (uniquement s'il est rattach� � un d�partement)
SELECT * FROM exe_employe LEFT  JOIN exe_dept ON dep_no=emp_dep_no; -- TOUS les employ�s (m�me si non rattach� � un dpt)
SELECT * FROM exe_employe RIGHT JOIN exe_dept ON dep_no=emp_dep_no; -- TOUS les d�partements (m�me si aucun employ� dedans)
SELECT * FROM exe_employe FULL  JOIN exe_dept ON dep_no=emp_dep_no; -- TOUS les employ�s et TOUS les d�partements
