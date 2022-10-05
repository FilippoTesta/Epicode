"""
Esercizio 2
Un supermercato vuole ricompensare i suoi clienti giornalieri, mostrando il loro nome su uno schermo all'interno del
supermercato. A tal fine, l'importo degli acquisti è memorizzato in una prima lista ed il nome del cliente in una
seconda lista corrispondente. Scrivi quindi un programma che chiede al cassiere di inserire tutti gli acquisti dei
clienti ed i nomi dei clienti, da inserire in due liste. Implementa la funzionalità che visualizza il nome e l'importo
del cliente che ha speso di più, il nome e l'importo del cliente che ha speso di meno, la media e la mediana della spesa
di tutti i clienti e visualizza il risultato quando il cassiere immette prezzo 0 (valore usato come sentinella).
"""

lista1 = []
lista2 = []
while True:
    j = input('Inserisci nome cliente:')
    i = float(input('Inserisci prezzo spesa:'))
    if j != '0':
        [lista1.append(j)]
    if i != 0:
        [lista2.append(i)]
    if i == 0:
        break

#Spesa massima e nome del cliente corrispettivo
indice_max = lista2.index(max(lista2))
print('Il nome del cliente che ha speso di più è {} per un valore di €{}'.format(lista1[indice_max],lista2[indice_max]))
#Spesa minima e nome del cliente corrispettivo
indice_min = lista2.index(min(lista2))
print('Il nome del cliente che ha speso di meno è {} per un valore di €{}'.format(lista1[indice_min],lista2[indice_min]))
#Media
somma = 0
for prezzo in lista2:
    somma= somma + prezzo
media = somma/len(lista2)
print('La media degli acquisti è',media)
#Mediana
def mediana(lista2):
    lista2.sort()
    half = len(lista2) // 2
    if not len(lista2) % 2:
        return (lista2[half] + lista2[half - 1]) / 2.0
    return lista2[half]
print('La mediana degli acquisti è',mediana(lista2))