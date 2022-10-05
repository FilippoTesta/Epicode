"""
Esercizio 1
Scrivi un programma che trasforma in maiuscolo tutte le consonanti di una stringa in input da tastiera.
Costruisci un dizionario le cui chiavi sono le lettere minuscole ed i cui valori sono tuple di parole
che contengono quella lettera.

"""

stringa=(input("Inserisci una frase?"))
print("La frase è:",stringa)
stringa=stringa.upper()
# sostituzione vocali maiuscole con vocali minuscole
new_stringa=stringa.replace('A','a').replace('E','e').replace('I','i').replace('O','o').replace('U','u')
print(new_stringa)


parole = new_stringa.split(' ')
vocali = ['a','e','i','o','u']
#creo il dizionario vuoto
d = {'a':(),'e':(),'i':(),'o':(),'u':()}

for p in parole:
    for v in vocali:
        i = p.find(v)
        if i >= 0:
            t = d[v] #tupla associata alla lettera "chiave"
            t_upd = t + (p,)
            d[v] = t_upd
print ('Il dizionario finale è:',d)
print (t)