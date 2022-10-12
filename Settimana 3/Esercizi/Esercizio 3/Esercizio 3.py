import mysql.connector
"""
CREATE DATABASE `discografia` 
/*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- discografia.disco definition

CREATE TABLE `DISCO` (
  `NroSerie` varchar(100) NOT NULL,
  `TitoloAlbum` varchar(100) DEFAULT NULL,
  `Anno` year NOT NULL,
  `Prezzo` float(4,2) NOT NULL,
  PRIMARY KEY (`NroSerie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- discografia.esecuzione definition

CREATE TABLE `ESECUZIONE` (
  `CodiceReg` varchar(100) NOT NULL,
  `TitoloCanzone` varchar(100) NOT NULL,
  `Anno` year NOT NULL,
  PRIMARY KEY (`CodiceReg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- discografia.autore definition

CREATE TABLE `AUTORE` (
  `nome` varchar(100) NOT NULL,
  `TitoloCanzone` varchar(100) NOT NULL,
  PRIMARY KEY (`nome`,`TitoloCanzone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- discografia.contiene definition

CREATE TABLE `CONTIENE` (
  `NroSerieDisco` varchar(100) NOT NULL,
  `CodiceReg` varchar(100) NOT NULL,
  `NroProg` varchar(100) NOT NULL,
  PRIMARY KEY (`NroSerieDisco`,`CodiceReg`),
  KEY `contiene_FK_1` (`CodiceReg`),
  CONSTRAINT `contiene_FK` FOREIGN KEY (`NroSerieDisco`) REFERENCES `disco` (`NroSerie`),
  CONSTRAINT `contiene_FK_1` FOREIGN KEY (`CodiceReg`) REFERENCES `esecuzione` (`CodiceReg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- discografia.canzone definition

CREATE TABLE `CANTANTE` (
  `NomeCantante` varchar(100) NOT NULL,
  `CodiceReg` varchar(100) NOT NULL,
  PRIMARY KEY (`NomeCantante`,`CodiceReg`),
  KEY `canzone_FK` (`CodiceReg`),
  CONSTRAINT `canzone_FK` FOREIGN KEY (`CodiceReg`) REFERENCES `esecuzione` (`CodiceReg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""

def connection_database(user, password, host, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host,
                                       database=database)
        return conn
    except mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None


conn= connection_database('root', 'root', '127.0.0.1', 'discografia')
cursor = conn.cursor()

#Implementare una funzione di inserimento in tabella DISCO


def inserimento_tabella_disco(NroSerie, TitoloAlbum, Anno, Prezzo):
    try:
        query_inserimento = "INSERT INTO disco (NroSerie,TitoloAlbum,Anno,Prezzo) VALUES (%s,%s,%s,%s)"
        dati = (NroSerie, TitoloAlbum, Anno, Prezzo)
        try:
            cursor.execute(query_inserimento, dati)
            conn.commit()
        except:
            conn.rollback()
        print('Dati inseriti con successo nella tabella disco')
    except mysql.connector.errors.DatabaseError as db_error:
        print("Errore durante l'inserimento dei dati")

#inserimento_tabella_disco(1,'Enema of the States',1999,19)
#inserimento_tabella_disco(2,'Master of Puppets',1986,18)
#inserimento_tabella_disco(3,'Ride the Lightning',1984,18)

#Implementare una funzione di cancellazione in tabella DISCO


def cancellazione_tabella_disco_NroSerie(NroSerie):
    try:
        query_cancellazione = "DELETE FROM disco WHERE NroSerie = '%s';"
        dati = (NroSerie)
        try:
            cursor.execute(query_cancellazione)
            conn.commit()
        except:
            conn.rollback()
        print('Dati cancellati con successo nella tabella disco')
    except mysql.connector.errors.DatabaseError as db_error:
        print("Errore durante la cancellazione dei dati")

#cancellazione_tabella_disco_NroSerie('3')

#Riportare le interrogazioni all'interno di funzioni Python


def execute_query(cursor, query):
    return cursor.execute(query)


def print_result(cursor):
    for i in cursor.fetchall():
        print(i)


def selezione_tabella(nome_colonna, nome_tabella):
    query = 'SELECT ' + nome_colonna + 'FROM' + nome_tabella + ';'
    return query


def selezione_tabella_multicolonna(nome_colonna1, nome_colonna2, nome_tabella):
    query = 'SELECT ' + nome_colonna1 + ',' + nome_colonna2 + ' FROM ' + nome_tabella + ';'
    return query


"""
select = selezione_tabella('*',' disco ')
execute_query(cursor,select)
result = print_result(cursor)


select2 = selezione_tabella_multicolonna('TitoloAlbum',' Anno','disco')
print(select2)
execute_query(cursor,select2)
result2 = print_result(cursor)
"""

"""
-- I cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D';

SELECT NomeCantante
FROM CANTANTE JOIN ESECUZIONE ON
        CANTANTE.CodiceReg = ESECUZIONE.CodiceReg
        JOIN AUTORE ON ESECUZIONE.TitoloCanz = AUTORE.TitoloCanzone
WHERE Nome = NomeCantante AND Nome LIKE 'D%';
"""


def interrogazione(select, frm, where1=None, groupby=None, orderby=None, join1=None, join2=None, where2=None):
    stmt = "SELECT %s from %s" % (select, frm)
    if where1 is not None:
        stmt = stmt + "WHERE %s" % where1
    if groupby is not None:
        stmt = stmt + "GROUP BY %s" % groupby
    if orderby is not None:
        stmt = stmt + "ORDER BY %s" % orderby
    if join1 is not None:
        stmt = stmt + "JOIN %s" % join1
    if join2 is not None:
        stmt = stmt + "JOIN %s" % join2
    if where2 is not None:
        stmt = stmt + "WHERE %s" % where2
    stmt = stmt + ";"
    return stmt

join = interrogazione('NomeCantante', 'cantante ', None, None, None,
                      'esecuzione ON cantante.CodiceReg = esecuzione.CodiceReg ',
                      'autore ON esecuzione.TitoloCanzone = autore.TitoloCanzone ',
                      "Nome = NomeCantante AND Nome LIKE 'D%'")
#print(join)
execute_query(cursor, join)
result3 = print_result(cursor)


"""
I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione;

SELECT TitoloAlbum
FROM DISCO JOIN CONTIENE ON
        DISCO.NroSerie = CONTIENE.NroSerieDisco
        JOIN ESECUZIONE ON CONTIENE.CodiceReg = ESECUZIONE.CodiceReg
WHERE ESECUZIONE.Anno IS NULL;
"""


def interrogazione2(select, frm, where1=None, groupby=None, orderby=None, join1=None, join2=None, where2=None):
    stmt = "SELECT %s from %s" % (select, frm)
    if where1 is not None:
        stmt = stmt + "WHERE %s" % where1
    if groupby is not None:
        stmt = stmt + "GROUP BY %s" % groupby
    if orderby is not None:
        stmt = stmt + "ORDER BY %s" % orderby
    if join1 is not None:
        stmt = stmt + "JOIN %s" % join1
    if join2 is not None:
        stmt = stmt + "JOIN %s" % join2
    if where2 is not None:
        stmt = stmt + "WHERE %s" % where2
    stmt = stmt + ";"
    return stmt


join2 = interrogazione2('TitoloAlbum', 'disco ', None, None, None,
                        'contiene ON disco.NroSerie = contiene.NroSerieDisco ',
                        'esecuzione ON contiene.CodiceReg = esecuzione.CodiceReg ', 'esecuzione.Anno IS NULL')
#print(join)
execute_query(cursor, join2)
result4 = print_result(cursor)
