import csv

def leggi_csv_liste(nome_file, delimiter=","):
    """
    Legge un file CSV e inserisce i dati in un due liste
    :param nome_file: nome del file
    :param delimiter: separatore utilizzato nel file
    :return: dati letti dal file
    """
    with open(nome_file, 'r', newline='') as csv_file:
        data = csv.reader(csv_file, delimiter=';')
        for row in data:
            l = row[1:9]
            l.append(row[48])
            world_deaths.append(l)
            l2 = row[35:39]
            l2.append(row[1])
            l2.append(row[2])
            l2.append(row[3])
            world_vacc.append(l2)
        return data

def total_deaths_estraction_location(dati,location):
    """
    Legge una lista e inserisce i dati richiesti in una singola lista
    dati: dati che si desidera estrarre
    location : nome della stringa del Paese oggetto di analisi
    return: lista contenente il valore oggetti di analisi
    """
    location = str(location)
    location_total_deaths = []
    for row in dati:
        if row[1] == location:
            total_deaths_string = row[7]
            total_deaths = total_deaths_string[:-2]
            location_total_deaths.append(total_deaths)

    for i in range(len(location_total_deaths)):
        if location_total_deaths[i] == '':
            location_total_deaths[i] = 0
        elif isinstance(location_total_deaths[i], str):
            location_total_deaths[i] = int(location_total_deaths[i])
    return location_total_deaths

def total_cases_estraction_location(dati,location):
    """
    Legge una lista e inserisce i dati richiesti in una singola lista
    dati: dati che si desidera estrarre
    location : nome della stringa del Paese oggetto di analisi
    return: lista contenente il valore oggetti di analisi
    """
    location = str(location)
    location_total_cases = []
    for row in dati:
        if row[1] == location:
            total_cases_string = row[4]
            total_cases = total_cases_string[:-2]
            location_total_cases.append(total_cases)

    for i in range(len(location_total_cases)):
        if location_total_cases[i] == '':
            location_total_cases[i] = 0
        elif isinstance(location_total_cases[i], str):
            location_total_cases[i] = int(location_total_cases[i])
    return location_total_cases

def total_people_vaccinated(dati,location):
    """
    Legge una lista e inserisce i dati richiesti in una singola lista
    dati: dati che si desidera estrarre
    location : nome della stringa del Paese oggetto di analisi
    return: lista contenente il valore oggetti di analisi
    """
    location = str(location)
    location_total_people_vacc = []
    for row in dati:
        if row[5] == location:
            total_people_vacc_string = row[0]
            total_people_vacc = total_people_vacc_string[:-2]
            location_total_people_vacc.append(total_people_vacc)

    for i in range(len(location_total_people_vacc)):
        if location_total_people_vacc[i] == '':
            location_total_people_vacc[i] = 0
        elif isinstance(location_total_people_vacc[i], str):
            location_total_people_vacc[i] = int(location_total_people_vacc[i])
    return location_total_people_vacc

def total_deaths_estraction_continent(dati,continent):
    """
    Legge una lista e inserisce i dati richiesti in una singola lista
    dati: dati che si desidera estrarre
    continent : nome della stringa del Continente oggetto di analisi
    return: lista contenente il valore oggetti di analisi
    """
    continent = str(continent)
    continent_total_deaths = []
    for row in dati:
        if row[0] == continent:
            total_deaths_string = row[7]
            total_deaths = total_deaths_string[:-2]
            continent_total_deaths.append(total_deaths)

    for i in range(len(continent_total_deaths)):
        if continent_total_deaths[i] == '':
            continent_total_deaths[i] = 0
        elif isinstance(continent_total_deaths[i], str):
            continent_total_deaths[i] = int(continent_total_deaths[i])
    return continent_total_deaths

def total_population_estraction_continent(dati,continent):
    """
    Legge una lista e inserisce i dati richiesti in una singola lista
    dati: dati che si desidera estrarre
    continent : nome della stringa del Continente oggetto di analisi
    return: lista contenente il valore oggetti di analisi
    """
    continent = str(continent)
    continent_population = []
    for row in dati:
        if row[0] == continent:
            population_string = row[8]
            population = population_string[:-2]
            continent_population.append(population)

    for i in range(len(continent_population)):
        if continent_population[i] == '':
            continent_population[i] = 0
        elif isinstance(continent_population[i], str):
            continent_population[i] = int(continent_population[i])
    return continent_population

world_deaths = list()
world_vacc = list()

leggi_csv_liste('owid-covid-data.csv')


#Creo seconde copie della lista World per uso futuro
china_deaths = world_deaths.copy()                  #CHN
china_vacc = world_vacc.copy()

india_deaths = world_deaths.copy()                  #IND
india_vacc = world_vacc.copy()

#Creo liste Cina
del china_deaths[1:40731]
del china_deaths[989:]

del china_vacc[1:40731]
del china_vacc[989:]
#for row in range (0,10):
#    print(china_deaths[row])

#Creo liste India
del india_deaths[1:90966]
del india_deaths[981:]

del india_vacc[1:90966]
del india_vacc[981:]
#for row in range (0,10):
#  print(india_vacc[row])

#[01] Probabilità di morire se è stato contratto il COVID-19 [Total_Deaths/Total_Cases]

#CHN
#china_total_deaths = list()
#china_total_cases = list()

total_deaths_estraction_location(china_deaths,'China')                          #Estraggo valore Total Deaths Cina
sum(total_deaths_estraction_location(china_deaths,'China'))
#print(sum(total_deaths_estraction_location(china_deaths,'China')))



total_cases_estraction_location(china_deaths, 'China')                          #Estraggo valore Total Cases Cina

sum(total_cases_estraction_location(china_deaths, 'China'))

china_death_prob = sum(total_deaths_estraction_location(china_deaths,'China')) / \
                   sum(total_cases_estraction_location(china_deaths, 'China')) * 100
#print(china_death_prob)  #0.39%


#IND
india_total_deaths = list()
india_total_cases = list()

total_deaths_estraction_location(india_deaths,'India')                           #Estraggo valore Total Deaths India

sum(total_deaths_estraction_location(india_deaths,'India')) 
#print(sum(total_deaths_estraction_location(india_deaths,'India')))


total_cases_estraction_location(india_deaths, 'India')                           #Estraggo valore Total Cases India

sum(total_cases_estraction_location(india_deaths, 'India'))
india_death_prob = sum(total_deaths_estraction_location(india_deaths,'India'))  / \
                   sum(total_cases_estraction_location(india_deaths, 'India')) * 100
#print(india_death_prob)  #1.16%


#[02] Percentuale di popolazione contagiata da COVID-19 [Total_Cases/Population]

china_population = (china_deaths[1][8])                                           #Ricavo valore Popolazione Cina
#print(int(float(china_population)))

india_population = (india_deaths[1][8]   )                                          #Ricavo dato Popolazione India
#print(int(float(india_population)))

china_infected_pop = sum(total_cases_estraction_location(china_deaths, 'China')) / (float(china_population))*100  #0.06%
#print(china_infected_pop)

india_infected_pop = sum(total_cases_estraction_location(india_deaths, 'India')) / (float(india_population))*100  #3.16%
#print(india_infected_pop)


#[03] Percentuale di popolazione con almeno una dose di vaccino contro COVID-19 [Total_vaccinations/Population]

#CHN
china_total_people_vacc = list()

total_people_vaccinated(china_vacc, 'China')                               #Estraggo valore People Vaccinated Cina

#china_people_vacc_percent = max(total_people_vaccinated(china_vacc, 'China')) / int(float(china_population))*100 #91.36%
#print(china_people_vacc_percent)


#IND
total_people_vaccinated(india_vacc, 'India')                               #Estraggo valore People Vaccinated India


#india_people_vacc_percent = total_people_vaccinated(india_vacc, 'India')  / int(float(china_population))*100 #72.92%
#print(india_total_people_vacc)


#[04] Continenti con tasso di morte da COVID-19 più elevato rispetto alla popolazione [Max[Total_Deaths/Population]

#Africa
total_deaths_estraction_continent(world_deaths,'Africa')                   #Estraggo valore Total Deaths Africa

#print(sum(total_deaths_estraction_continent(world_deaths,'Africa')))


total_population_estraction_continent(world_deaths,'Africa')               #Estraggo valore Popolazione Africa

#print(sum(total_population_estraction_continent(world_deaths,'Africa')))

africa_tasso_morte_pop = sum(total_deaths_estraction_continent(world_deaths,'Africa')) / \
                         sum(total_population_estraction_continent(world_deaths,'Africa'))  # 1.95
#print(africa_tasso_morte_pop)


# Asia
total_deaths_estraction_continent(world_deaths,'Asia')                      #Estraggo valore Total Deaths Asia

#print(sum(total_deaths_estraction_continent(world_deaths,'Asia')))


total_population_estraction_continent(world_deaths,'Asia')                  #Estraggo valore Popolazione Asia

#print(sum(total_population_estraction_continent(world_deaths,'Asia')))

asia_tasso_morte_pop = sum(total_deaths_estraction_continent(world_deaths,'Asia')) / \
                         sum(total_population_estraction_continent(world_deaths,'Asia'))  # 3.23
#print(asia_tasso_morte_pop)


#Europa
total_deaths_estraction_continent(world_deaths,'Europe')                     #Estraggo valore Total Deaths Europa

#print(sum(total_deaths_estraction_continent(world_deaths,'Europe')))


total_population_estraction_continent(world_deaths,'Europe')                 #Estraggo valore Popolazione Europa

#print(sum(total_population_estraction_continent(world_deaths,'Europe')))

europa_tasso_morte_pop = sum(total_deaths_estraction_continent(world_deaths,'Europe')) / \
                         sum(total_population_estraction_continent(world_deaths,'Europe'))  # 2.67
#print(europa_tasso_morte_pop)


#Nord America
total_deaths_estraction_continent(world_deaths,'North America')               #Estraggo valore Total Deaths Nord America

#print(sum(total_deaths_estraction_continent(world_deaths,'North America')))


total_population_estraction_continent(world_deaths,'North America')           #Estraggo valore Popolazione Nord America

#print(sum(total_population_estraction_continent(world_deaths,'North America')))

na_tasso_morte_pop = sum(total_deaths_estraction_continent(world_deaths,'North America')) / \
                         sum(total_population_estraction_continent(world_deaths,'North America'))  # 2.57
#print(na_tasso_morte_pop)


#Oceania
total_deaths_estraction_continent(world_deaths,'Oceania')               #Estraggo valore Total Deaths Oceania

#print(sum(total_deaths_estraction_continent(world_deaths,'Oceania')))


total_population_estraction_continent(world_deaths,'Oceania')           #Estraggo valore Popolazione Oceania

#print(sum(total_population_estraction_continent(world_deaths,'Oceania')))

oceania_tasso_morte_pop = sum(total_deaths_estraction_continent(world_deaths,'Oceania')) / \
                         sum(total_population_estraction_continent(world_deaths,'Oceania'))  #4.65
#print(oceania_tasso_morte_pop)


#Sud America
total_deaths_estraction_continent(world_deaths,'South America')             #Estraggo valore Total Deaths Sud America

#print(sum(total_deaths_estraction_continent(world_deaths,'South America')))


total_population_estraction_continent(world_deaths,'South America')           #Estraggo valore Popolazione Sud America

#print(sum(total_population_estraction_continent(world_deaths,'South America')))

sa_tasso_morte_pop = sum(total_deaths_estraction_continent(world_deaths,'South America')) / \
                         sum(total_population_estraction_continent(world_deaths,'South America'))  #3.15
#print(sa_tasso_morte_pop)



print('In Cina, la probabilità di morire se è stato contratto il COVID-19 è pari allo',
      china_death_prob,'%.\nLa percentuale di popolazione contagiata da COVID-19 è stata pari allo:',
      china_infected_pop,'% e la percentuale di popolazione con almeno una dose di vaccino è il 91.36%')

print('In India, la probabilità di morire se è stato contratto il COVID-19 è pari allo',
      india_death_prob,'%.\nLa percentuale di popolazione contagiata da COVID-19 è stata pari allo:',
      india_infected_pop,'% e la percentuale di popolazione con almeno una dose di vaccino è il 72.92%')

print('Di seguito un elenco dei continenti ordinati per tasso di morte da COVID-19 più elevato rispetto alla popolazione:\n'
      '1) Oceania:', oceania_tasso_morte_pop,'%\n'
      '2) Asia:', asia_tasso_morte_pop,'%\n'
      '3) Sud America:', sa_tasso_morte_pop,'%\n'
      '4) Europa:',europa_tasso_morte_pop,'%\n'
      '5) Nord America',na_tasso_morte_pop,'%\n'
      '6) Africa', africa_tasso_morte_pop, '%')