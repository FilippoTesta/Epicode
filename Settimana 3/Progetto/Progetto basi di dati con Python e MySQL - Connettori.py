import mysql.connector


def connection_database(user, password, host, database):
    """
    Permette di connettersi ad un database indicato, attraverso un connettore
    :param user: Inserisci il nome dell'utente
    :param password: Inserisci la password
    :param host: Inserisci l'host
    :param database: Inserisci nome del database
    :return: Connessione al database tramite connettore
    """
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host,
                                       database=database)
        return conn
    except mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None


def close_connection(connection):
    """
    Chiude la connessione
    :param connection: Inserisci il nome della variabile data alla connessione
    :return: Chiusura della connessione
    """
    connection.close()


def execute_query(cursor, query):
    """
    Permette di eseguire un'interrogazione di qualsiasi tipo associata al cursore
    :param cursor: Inserisci il cursore
    :param query: Inserisci l'interrogazione
    :return: Esecuzione dell'interrogazione
    """
    return cursor.execute(query)


def print_result(cursor):
    """
    Recupera le righe nel result set dell'interrogazione e permette la visualizzazione
    :param cursor: Inserisci il cursore
    :return: Visualizzazione dell'interrogazione
    """
    for i in cursor.fetchall():
        print(i)


def select_from(column, table):
    """
    Permette di svolgere una selezione di una o più colonne da una tabella di un database
    :param column: Inserisci nome colonna
    :param table: Inserisci nome tabella
    :return: Ritorna una stringa dell'interrogazione richiesta
    """
    return "SELECT %s FROM %s" % (column, table)


def where(condition):
    """
    Permette di esprimere una condizione durante un'interrogazione
    :param condition: Inserisci la condizione
    :return: Ritorna una stringa dell'interrogazione richiesta
    """
    return " WHERE %s" % (condition)


def groupby(column):
    """
    Permette di raggruppare dati identici in gruppi a partire da una colonna indicata
    :param column: Inserisci la colonna
    :return: Ritorna una stringa dell'interrogazione richiesta
    """
    return " GROUP BY %s" % (column)


def orderby(column):
    """
    Permette di ordinare una tabella basandosi su una o più colonne
    :param column: Inserisci la colonna
    :return: Ritorna una stringa dell'interrogazione richiesta
    """
    return " ORDER BY %s" % (column)


def join(tables, field):
    """
    Permette di combinare i valori di due tabelle attraverso una regola di confronto espressa nel parametro campo
    :param tables: Inserisci il nome delle tabelle
    :param field: Inserisci il valore su cui effettuare l'unione
    :return: Ritorna una stringa dell'interrogazione richiesta
    """
    return " JOIN %s ON %s" % (tables, field)


def limit(row_number):
    """
    Permette di limitare il risultato di un'interrogazione
    :param row_number: Numero di righe che si desidera visualizzare nell'interrogazione
    :return: Ritorna una stringa dell'interrogazione richiesta
    """
    return " LIMIT %s" % (row_number)


conn = connection_database('root', 'root', '127.0.0.1', 'ecommerce')
cursor = conn.cursor()

#Interrogazioni con connettore MySQL

#01) Prime cinque categorie di prodotto più ordinate

sql = select_from('c.nome AS categoria,SUM(o.quantita) AS quantita_ordinata', 'categoria AS c') \
      + join('prodotto AS p', 'c.cid = p.cid') + join('orpr01 AS o', 'p.pid = o.pid') + groupby('categoria') \
      + orderby('quantita_ordinata desc') + limit('5;')

execute_query(cursor, sql)
result = print_result(cursor)


#02) Dieci prodotti più acquistati

sql2 = select_from('p.nome AS prodotto, SUM(o.quantita) AS quantita_ordinata','prodotto AS p') \
       + join('orpr01 AS o','p.pid = o.pid') + groupby('prodotto') + orderby('quantita_ordinata desc') + limit('10;')

execute_query(cursor, sql2)
result2 = print_result(cursor)


#03) Città da dove arrivano più ordini

sql3 = select_from('COUNT(citta) AS numero_ordini, citta','indirizzo AS i') \
       + join('ordine AS o','i.inid=o.inid') + groupby('citta') + orderby('numero_ordini desc;')

execute_query(cursor,sql3)
result3 = print_result(cursor)


#04) Numero di utenti iscritti alla newsletter

sql4 = select_from('COUNT(nome)','utente') + where('nome NOT IN (') + select_from('nome','utente') \
       + where('newsletter = 0);')

execute_query(cursor,sql4)
result4 = print_result(cursor)


#05) Modalità di pagamento più usate

sql5 = select_from('pag.nome as modalita_pagamento, COUNT(pag.nome) as quantita','pagamento pag') \
       + join('pasp01 pas','pag.paid = pas.paid') + join('ordine o','pas.paspid = o.paspid') \
       + groupby('modalita_pagamento') + orderby('quantita desc;')
execute_query(cursor,sql5)
result5 = print_result(cursor)


#06) Marca di prodotti più ordinata

sql6 = select_from('m.nome AS marca, SUM(o.quantita) AS quantita_ordinata','marca m') \
       + join('prodotto p','m.mid = p.mid') + join('orpr01 o','p.pid = o.pid') + groupby('marca') \
       + orderby('quantita_ordinata desc;')
execute_query(cursor,sql6)
result6 = print_result(cursor)


#07) Tipo di spedizione preferita

sql7 = select_from('s.nome as modalita_spedizione, COUNT(s.nome) as quantita','spedizione AS s') \
       + join('pasp01 AS p','s.spid = p.spid') + join('ordine AS o ','p.paspid = o.paspid') \
       + groupby('modalita_spedizione') + orderby('quantita desc;')
execute_query(cursor,sql7)
result7 = print_result(cursor)


#08) Numero di ordini da parte di utenti liberi professionisti

sql8 = select_from('COUNT(ordine.oid) AS numero_ordini','ordine') + join('utente','ordine.uid = utente.uid') \
       + where('piva IS NOT NULL;')
execute_query(cursor,sql8)
result8 = print_result(cursor)


#09) Prodotti più costosi ordinati

sql9 = select_from('MAX(prezzo), prodotto.nome','prezzo') + join('prodotto','prezzo.pid = prodotto.pid') \
       + join('orpr01', 'orpr01.pid = prodotto.pid') + groupby('prodotto.nome') + orderby('MAX(prezzo) desc') \
       + limit('3;')
execute_query(cursor, sql9)
result9 = print_result(cursor)


#10) Utenti che hanno effettuato più ordini

sql10 = select_from\
        ("COUNT(ordine.uid) AS numero_ordini, CONCAT(utente.nome,' ',utente.cognome) AS nome_utente", 'utente, ordine') \
        + where('utente.uid = ordine.uid') + groupby('nome_utente') + orderby('COUNT(ordine.uid) desc;')
execute_query(cursor, sql10)
result10 = print_result(cursor)

close = close_connection(conn)
