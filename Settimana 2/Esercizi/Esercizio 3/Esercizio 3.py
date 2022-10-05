"""
Esercizio 3:
Un multiset è una collezione di elementi con la loro frequenza. Esempio: multiset con due banane e 3 mele.
Un multiset può essere implementato come dizionario (le chiavi sono gli elementi, i valori sono le frequenze).
Scrivi un programma con le funzioni unione, intersezione e differenza che ricevono in input due multiset
e restituiscono in output il multiset unione (somma delle frequenze),
il multiset intersezione (il minimo tra le frequenze)
e infine quello differenza (differenza tra le frequenze, non deve essere minore di zero).
Visualizza il risultato.
"""

# m_1 e m_2 sono i multiset su cui eseguire le operazioni
m_1 = {"apple": 3, "orange": 7, "banana": 4}
m_2 = {"apple": 9, "banana": 9}
keys = list(dict.fromkeys(list(m_1.keys()) + list(m_2.keys())))
print (keys)

def union_ms(d1, d2, keys):
    d_union = {}
    for k in keys:
        if d2.get(k,None) is not None and d1.get(k,None) is not None:
            d_union[k] = d1[k] +d2[k]
        elif d2.get(k,None) is not None:
            d_union[k] = d2[k]
        else:
            d_union[k] = d1[k]
    return d_union

def intersect_ms(d1, d2, keys):
    d_intersect = {}
    for k in keys:
        if d2.get(k, None) is not None and d1.get(k, None) is not None:
            if d2[k] > d1[k]:
                d_intersect[k] = d1[k]
            else:
                d_intersect[k] = d2[k]
        elif d2.get(k, None) is not None:
            d_intersect[k] = d2[k]
        else:
            d_intersect[k] = d1[k]
    return d_intersect

def diff_ms(d1, d2, keys):
    d_diff = {}
    for k in keys:
        if d2.get(k,None) is not None and d1.get(k,None) is not None:
            d_diff[k] = abs(d1[k] - d2[k])
        elif d2.get(k,None) is not None:
            d_diff[k] = d2[k]
        else:
            d_diff[k] = d1[k]
    return d_diff

print("il multiset unione è:", union_ms(m_1, m_2, keys))
print("il multiset differenza è:", diff_ms(m_1, m_2, keys))
print("il multiset intersezione è:", intersect_ms(m_1, m_2, keys))

