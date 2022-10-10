-- Le città con un aeroporto di cui non è noto il numero di piste
SELECT DISTINCT Citta FROM AEROPORTO WHERE NumPiste IS NULL;

-- I tipi di aereo usati nei voli che partono da Torino
SELECT TipoAereo FROM VOLO WHERE CittaPart = 'Torino';

-- Le città da cui partono i voli diretti a Bologna
SELECT CittaPart FROM VOLO WHERE CittaArr = 'Bologna';

-- Le città da cui parte e arriva il volo con codice AZ274
SELECT CittaPart, CittaArr FROM VOLO WHERE IdVolo = 'AZ274';

-- Il tipo di aereo, il giorno della settimana, l'orario di partenza la cui città di partenza inizia per B e contiene O e la cui città di arrivo termina con  A e contiene E
SELECT TipoAereo, GiornoSett, OraPart FROM VOLO WHERE CittaPart LIKE 'B%o%' AND CittaArr LIKE '%e%a';