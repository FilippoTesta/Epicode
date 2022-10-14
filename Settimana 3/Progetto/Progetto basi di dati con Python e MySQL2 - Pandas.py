from sqlalchemy import create_engine
import pandas as pd


def connection_database(user, password, host, database):
    """
    Permette di connettersi ad un database indicato
    :param user:Inserisci il nome dell'utente
    :param password: Inserisci la password
    :param host: Inserisci l'host
    :param database: Inserisci nome del database
    :return: Connessione al database
    """
    db_connection_str = 'mysql+pymysql://' + user + ':' + password + '@' + host + '/' + database
    return db_connection_str

#Interrogazioni su Pandas


db_connection = create_engine(connection_database('root', 'root', '127.0.0.1', 'ecommerce'))


#01) Categorie di prodotto più ordinate
prodotto = pd.read_sql("prodotto", db_connection)
categoria = pd.read_sql("categoria", db_connection)
orpr01 = pd.read_sql("orpr01", db_connection)

df_prodotto = pd.DataFrame(prodotto)
df_categoria = pd.DataFrame(categoria)
df_orpr01 = pd.DataFrame(orpr01)


df01_merged = pd.merge(df_categoria, df_prodotto, on='cid')
df01_merged2 = pd.merge(df01_merged, df_orpr01, on='pid')
df01_grouped = df01_merged2.groupby([('nome_x')]).sum()
df01_grouped.sort_values(by='quantita_y', ascending=False, inplace=True)
TopCat = df01_grouped.loc[:, ['quantita_y']]

#print(TopCat)


#02) Dieci prodotti più acquistati

df02 = df_orpr01.groupby('pid')['quantita', 'prezzo'].sum()
df02.sort_values(by='quantita', ascending=False, inplace=True)
df02.head(10).reset_index(inplace=True)
df_merged03 = pd.merge(df02, df_prodotto, on='pid')
TopPr = df_merged03[['nome', 'quantita_x']]

#print(TopPr)


#03 Città da dove arrivano più ordini

indirizzo = pd.read_sql("indirizzo", db_connection)
ordine = pd.read_sql("ordine", db_connection)

df_indirizzo = pd.DataFrame(indirizzo)
df_ordine = pd.DataFrame(ordine)


df03_merged = pd.merge(df_indirizzo, df_ordine, on='inid')
df03_grouped = df03_merged.groupby([('citta')]).count()
df03_grouped.sort_values(by='citta', ascending=False, inplace=True)
Citta = df03_grouped[['nome']]

#print(Citta)


#04 Numero utenti iscritti alla newsletter

utente = pd.read_sql("utente", db_connection)
df_utente = pd.DataFrame(utente)

df04 = df_utente.loc[df_utente['newsletter'] == 1]
df04_count = df04.count()
Newsletter = df04_count['newsletter']

#print(Newsletter)


#05 Modalità di pagamento più usate
pagamento = pd.read_sql("pagamento", db_connection)
pasp01 = pd.read_sql("pasp01", db_connection)

df_pagamento = pd.DataFrame(pagamento)
df_pasp = pd.DataFrame(pasp01)

df05_merged = pd.merge(df_pagamento, df_pasp, on='paid')
df05_merged2 = pd.merge(df05_merged, df_ordine, on='paspid')
df05_grouped = df05_merged2.groupby([('nome')]).count()
ModPag = df05_grouped.loc[:, ['paid']]

#print(ModPag)


#06 Marca prodotto più ordinata
marca = pd.read_sql("marca", db_connection)

df_marca = pd.DataFrame(marca)

df06_merged = pd.merge(df_marca, df_prodotto, on='mid')
df06_merged2 = pd.merge(df06_merged, df_orpr01, on='pid')
df06_grouped = df06_merged2.groupby([('nome_x')]).sum()
df06_grouped.sort_values(by='quantita_y', ascending=False, inplace=True)
Marca = df06_grouped.loc[:, ['quantita_y']]
#print(Marca)


#07 Tipo di spedizione preferita
spedizione = pd.read_sql("spedizione", db_connection)
pasp01 = pd.read_sql("pasp01", db_connection)

df_spedizione = pd.DataFrame(spedizione)
df_pasp01 = pd.DataFrame(pasp01)

df07_merged = pd.merge(df_spedizione, df_pasp01, on='spid')
df07_merged2 = pd.merge(df07_merged, df_ordine, on='paspid')
df07_grouped = df07_merged2.groupby([('nome')]).count()
Spedizione = df07_grouped.loc[:, ['spid']]

#print(Spedizione)


#08 Numero di ordini da parte di utenti liberi professionisti

df_merged_08 = pd.merge(df_ordine, df_utente, on='uid')
df08_count= df_merged_08.count()
pIVA = df08_count['piva']
#print(pIVA)

#print(data['c'])


#09 Prodotto più costoso ordinato
prezzo = pd.read_sql("prezzo", db_connection)

df_prezzo = pd.DataFrame(prezzo)

df09_merged = pd.merge(df_prezzo, df_prodotto, on='pid')
df09_merged2 = pd.merge(df09_merged, df_orpr01, on='pid')
df09_grouped = df09_merged2.groupby([('prezzo')]).max()
df09_grouped.sort_values(by='prezzo', ascending=False, inplace=True)
Costo = df09_grouped.loc[:, ['nome']]

#print(Costo)


#10 Utenti che hanno effettuato più ordini
utente = pd.read_sql("utente", db_connection)

df_utente = pd.DataFrame(utente)


df10_merged = pd.merge(df_utente, df_ordine, on='uid')
df10_grouped = df10_merged.groupby([('nome'), ('cognome')]).count()
df10_grouped.sort_values(by='uid', ascending=False, inplace=True)
Ordini = df10_grouped.loc[:, ['inid']]

#print(Ordini)
