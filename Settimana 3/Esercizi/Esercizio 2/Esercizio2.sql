-- I cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D';

SELECT NomeCantante
FROM CANTANTE JOIN ESECUZIONE ON
        CANTANTE.CodiceReg = ESECUZIONE.CodiceReg
        JOIN AUTORE ON ESECUZIONE.TitoloCanz = AUTORE.TitoloCanzone
WHERE Nome = NomeCantante AND Nome LIKE 'D%';

-- I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione;

SELECT TitoloAlbum
FROM DISCO JOIN CONTIENE ON
        DISCO.NroSerie = CONTIENE.NroSerieDisco
        JOIN ESECUZIONE ON CONTIENE.CodiceReg = ESECUZIONE.CodiceReg
WHERE ESECUZIONE.Anno IS NULL;


-- I cantanti che non hanno mai registrato una canzone come solisti;

SELECT NomeCantante
FROM CANTANTE
WHERE NomeCantante NOT IN
                     (SELECT C1.NomeCantante
                      FROM CANTANTE AS C1
                      WHERE CodiceReg NOT IN
                                        (SELECT CodiceReg
                                         FROM CANTANTE AS C2
                      WHERE C2.NomeCantante <> C1.NomeCantante));


-- I cantanti che hanno sempre registrato una canzone come solisti;

SELECT NomeCantante
FROM CANTANTE
WHERE NomeCantante NOT IN
                     (SELECT C1.NomeCantante
                      FROM CANTANTE AS C1 JOIN ESECUZIONE ON
                      ESECUZIONE.CodiceReg = C1.CodiceReg
                      JOIN CANTANTE AS C2 ON
                           ESECUZIONE.CodiceReg = C2.CodiceReg)
                      WHERE C1.NomeCantante <> C2.NomeCantante);

