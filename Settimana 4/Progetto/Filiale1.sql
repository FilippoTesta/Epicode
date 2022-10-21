CREATE DATABASE `filiale1`
use filiale1;



CREATE TABLE `regione` (
  `id_regione` tinyint(4) NOT NULL AUTO_INCREMENT,
  `matricola` varchar(50) DEFAULT NULL,
  `nome_regione` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_regione`)
) ENGINE=InnoDB;


CREATE TABLE `dipendente` (
  `matricola` varchar(50) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `cognome` varchar(50) DEFAULT NULL,
  `dt_nascita` DATE,
  `dt_assunzione` DATE,
  `eta` tinyint(3) DEFAULT NULL,
  `anz_lavoro` tinyint(3) DEFAULT NULL,
  `id_regione` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`matricola`)
) ENGINE=InnoDB;


CREATE TABLE `stipendio` (
  `matricola` varchar(50) NOT NULL,
  `stipendio` float NOT NULL DEFAULT 0,
  PRIMARY KEY (`matricola`,`stipendio`)
) ENGINE=InnoDB;


CREATE TABLE `prodotto` (
  `id_prodotto` tinyint(4) NOT NULL,
  `nome_prodotto` varchar(100) DEFAULT NULL,
  `categoria_prodotto` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_prodotto`)
) ENGINE=InnoDB;


CREATE TABLE `fatturato` (
  `fid` tinyint(4) NOT NULL AUTO_INCREMENT,
  `data` DATE,
  `m_venditore` varchar(50) NOT NULL,
  `categoria_merce` varchar(50),
  `id_prodotto` tinyint(4) NOT NULL,
  `fatturato` float DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB;

INSERT INTO `regione`
VALUES ("1",'B01755800','Lazio'),
       ("2","B01755801","Abruzzo"),
       ("3","B01755802","Toscana"),
       ("4","B01755803","Campania"),
       ("5","B01755804","Lazio"),
	   ("6","B01755805","Abruzzo"),
       ("7","B01755806","Toscana"),
       ("8","B01755807","Campania"),
       ("9","B01755808","Lazio"),
       ("10","B01755809","Abruzzo"),
       ("11","B01755810","Toscana"),
       ("12","B01755811","Campania"),
       ("13","B01755812","Lazio"),
       ("14","B01755813","Abruzzo"),
       ("15","B01755814","Toscana");


INSERT INTO `dipendente`
VALUES ("B01755800","Federico","Paninucci",11/09/1977,20/10/2020,45,2,1),
       ("B01755801","Iole","Lombardo",27/11/1961, 20/10/1990,60,32,2),
       ("B01755802","Valter","Colombo",04/04/1996, 14/02/2019,26,3,3),
       ("B01755803","Benvenuto","Napolitano",31/12/1997, 14/02/2020,24,2,4),
       ("B01755804","Ciro","Colombo",17/03/1976, 22/02/1991,46,31,5),
	   ("B01755805","Anna","Trentini",09/10/1961, 22/06/1993,46,29,6),
       ("B01755806","Beata","Ricci",13/01/1990, 11/02/2021,32,1,7),
       ("B01755807","Gennaro","Licata",30/11/1971, 16/12/2021,50,1,8),
       ("B01755808","Isabella","Fiorentini",21/12/1997, 16/05/2019,24,3,9),
       ("B01755809","Serena","Gallo",16/04/1978, 07/01/1995,44,27,10),
       ("B01755810","Isabella","Cremonesi",31/05/1985, 07/01/1999,44,23,11),
       ("B01755811","Debora","Serpico",06/06/1981, 20/10/2020,41,2,12),
       ("B01755812","Claudio","Russo",11/04/1978, 11/07/2018,44,4,13),
       ("B01755813","Davide","Isauro",13/08/1965, 13/03/2016,57,6,14),
       ("B01755814","Enrico","Selrizzi",28/11/1981, 20/10/2014,40,8,15);

INSERT INTO `stipendio`
VALUES ("B01755800",2218.88),
       ("B01755801",1633.59),
       ("B01755802",1936.51),
       ("B01755803",2256.9),
       ("B01755804",1255.27),
	   ("B01755805",2451.93),
       ("B01755806",1977.17),
       ("B01755807",1971.96),
       ("B01755808",1775.12),
       ("B01755809",1566.21),
       ("B01755810",1460.93),
       ("B01755811",2019.1),
       ("B01755812",1177.0),
       ("B01755813",1775.25),
       ("B01755814",2463.85);


INSERT INTO `prodotto`
VALUES ("1","MOUSE LOGITECH MX MASTER 3","accessori_pc"),
       ("2","TAPPETINO PER MOUSE COLORE ROSSO CON POGGIAPOLSI IN GEL","accessori_pc"),
       ("3","Apolo Arte Set Pennelli Per Dipingere","pennelli"),
       ("4","Pattex Nastro Adesivo Americano Rotolo 50x25mm","nastri"),
       ("5","STABILO BOSS ORIGINAL Desk-Set","evidenziatori");

       SELECT *
       FROM fatturato;

       DELETE
       FROM fatturato
       WHERE fid = 1;

INSERT INTO `fatturato`
VALUES ("1",04/07/2020,"B01755800","Cancelleria",4,6457),
("2",26/08/2020,"B01755800","Cancelleria",3,11659),
("3",18/08/2020,"B01755805","Informatica",2,3091),
("4",09/09/2020,"B01755808","Cancelleria",3,517),
("5",04/09/2020,"B01755812","Informatica",2,9487),
("6",24/07/2020,"B01755814","Cancelleria",4,5294),
("7",04/09/2020,"B01755814","Informatica",1,3601),
("8",11/08/2020,"B01755814","Cancelleria",4,3884),
("9",03/07/2020,"B01755813","Informatica",1,6093),
("10",08/08/2020,"B01755813","Informatica",1,2955),
("11",14/09/2020,"B01755813","Informatica",2,3903),
("12",27/08/2020,"B01755813","Cancelleria",4,8667),
("13",11/07/2020,"B01755813","Cancelleria",4,1252),
("14",18/07/2020,"B01755801","Cancelleria",4,1992),
("15",07/09/2020,"B01755812","Cancelleria",3,601),
("16",10/07/2020,"B01755812","Cancelleria",4,3252),
("17",14/09/2020,"B01755812","Informatica",1,7233),
("18",12/08/2020,"B01755812","Cancelleria",3,7911),
("19",30/08/2020,"B01755812","Informatica",1,9949),
("20",11/09/2020,"B01755811","Informatica",1,1368),
("21",21/08/2020,"B01755811","Informatica",1,3989),
("22",18/07/2020,"B01755801","Cancelleria",3,11918),
("23",13/09/2020,"B01755811","Cancelleria",4,221),
("24",01/08/2020,"B01755811","Informatica",2,10003),
("25",21/08/2020,"B01755811","Cancelleria",3,11713),
("26",08/09/2020,"B01755810","Informatica",2,3606),
("27",23/07/2020,"B01755810","Cancelleria",3,5588),
("28",08/09/2020,"B01755810","Informatica",1,11578),
("29",07/09/2020,"B01755801","Cancelleria",4,7479),
("30",16/07/2020,"B01755810","Cancelleria",4,2930),
("31",07/07/2020,"B01755810","Cancelleria",3,4559),
("32",31/07/2020,"B01755801","Informatica",1,4803),
("33",30/06/2020,"B01755810","Informatica",1,7713),
("34",25/08/2020,"B01755810","Cancelleria",3,123),
("35",14/07/2020,"B01755810","Informatica",2,8487),
("36",12/07/2020,"B01755809","Informatica",2,4643),
("37",29/08/2020,"B01755809","Informatica",2,10939),
("38",01/09/2020,"B01755809","Cancelleria",3,7820),
("39",30/06/2020,"B01755801","Cancelleria",3,9521),
("40",20/07/2020,"B01755809","Informatica",1,368),
("41",26/07/2020,"B01755809","Cancelleria",3,11611),
("42",08/09/2020,"B01755809","Cancelleria",3,1623),
("43",13/08/2020,"B01755809","Informatica",2,11535),
("44",27/06/2020,"B01755809","Informatica",1,11501),
("45",15/08/2020,"B01755809","Informatica",2,3726),
("46",05/09/2020,"B01755809","Cancelleria",3,2053),
("47",29/06/2020,"B01755809","Informatica",1,6578),
("48",30/08/2020,"B01755809","Informatica",3,5911),
("49",21/07/2020,"B01755809","Informatica",2,10539),
("50",27/06/2020,"B01755801","Cancelleria",3,2164),
("51",21/08/2020,"B01755808","Informatica",2,3758),
("52",30/08/2020,"B01755808","Cancelleria",3,9155),
("53",02/08/2020,"B01755808","Informatica",1,8843),
("54",01/08/2020,"B01755808","Informatica",2,1860),
("55",03/07/2020,"B01755808","Informatica",2,2472),
("56",22/07/2020,"B01755808","Cancelleria",4,1409),
("57",14/08/2020,"B01755808","Cancelleria",4,112),
("58",03/08/2020,"B01755808","Cancelleria",3,6997),
("59",12/08/2020,"B01755808","Cancelleria",3,6028),
("60",02/07/2020,"B01755807","Informatica",2,9685),
("61",17/07/2020,"B01755807","Informatica",1,6830),
("62",12/08/2020,"B01755807","Informatica",2,2362),
("63",17/09/2020,"B01755807","Cancelleria",4,10916),
("64",24/07/2020,"B01755807","Cancelleria",3,9564),
("65",28/08/2020,"B01755807","Cancelleria",4,8968),
("66",27/08/2020,"B01755807","Cancelleria",3,1647),
("67",26/07/2020,"B01755806","Informatica",2,9294),
("68",09/07/2020,"B01755806","Informatica",2,3681),
("69",03/07/2020,"B01755806","Cancelleria",4,10772),
("70",22/08/2020,"B01755806","Cancelleria",4,9542),
("71",12/08/2020,"B01755806","Cancelleria",3,8008),
("72",06/07/2020,"B01755806","Informatica",2,10658),
("73",26/06/2020,"B01755806","Informatica",1,9436),
("74",11/09/2020,"B01755806","Cancelleria",4,3926),
("75",12/09/2020,"B01755801","Cancelleria",3,1787),
("76",01/07/2020,"B01755805","Informatica",1,5710),
("77",07/09/2020,"B01755805","Informatica",1,2489),
("78",13/07/2020,"B01755805","Cancelleria",4,4483),
("79",06/09/2020,"B01755805","Cancelleria",4,335),
("80",19/08/2020,"B01755805","Informatica",2,5958),
("81",01/09/2020,"B01755805","Cancelleria",3,4733),
("82",21/08/2020,"B01755805","Cancelleria",3,4404),
("83",07/07/2020,"B01755804","Cancelleria",4,6146),
("84",04/07/2020,"B01755804","Cancelleria",4,2125),
("85",06/07/2020,"B01755804","Informatica",2,1569),
("86",11/09/2020,"B01755804","Cancelleria",4,8418),
("87",21/08/2020,"B01755804","Informatica",2,9499),
("88",08/07/2020,"B01755804","Cancelleria",4,9739),
("89",28/08/2020,"B01755804","Cancelleria",4,8020),
("90",22/08/2020,"B01755804","Cancelleria",4,4792),
("91",14/08/2020,"B01755804","Informatica",2,7537),
("92",05/07/2020,"B01755803","Cancelleria",3,11274),
("93",03/09/2020,"B01755803","Informatica",1,11712),
("94",30/06/2020,"B01755803","Cancelleria",3,10624),
("95",31/07/2020,"B01755803","Cancelleria",3,10366),
("96",16/07/2020,"B01755802","Informatica",1,6935),
("97",30/07/2020,"B01755802","Cancelleria",4,11764),
("98",11/08/2020,"B01755802","Cancelleria",3,6872),
("99",27/08/2020,"B01755801","Informatica",1,2795);


ALTER TABLE `dipendente`
ADD
FOREIGN KEY (`id_regione`) REFERENCES `regione` (`id_regione`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `fatturato`
ADD
FOREIGN KEY (`id_prodotto`) REFERENCES `prodotto` (`id_prodotto`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `fatturato`
ADD
FOREIGN KEY (`m_venditore`) REFERENCES `dipendente` (`matricola`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `stipendio`
ADD
FOREIGN KEY (`matricola`) REFERENCES `dipendente` (`matricola`) ON DELETE CASCADE ON UPDATE CASCADE;