# Pràctica 1: Web scraping

## Descripció

La Pràctica 1 es du a terme per a l'assignatura <b>Tipologia i cicle de vida de les dades</b>. 

S'han d'analitzar, a través d'un cas pràctic, les dades rellevants per a aprendre a identificar-les i 
utilitzar les eines d’extracció de dades.

Hem triat una web open source (Dades Obertes) de la Generalitat de Catalunya (http://governobert.gencat.cat/ca/dades_obertes/). 
L'objectiu d'aquesta activitat serà la creació d'un dataset a partir de les dades obtingudes mitjançant Web Scraping en la següent web: 
(https://analisi.transparenciacatalunya.cat/Salut/Registre-de-casos-de-COVID-19-realitzats-a-Catalun/jj6z-iyrp/data), extreta de la web arrel Govern Obert de la Generalitat de Catalunya.
Les dades de la pàgina web analitzada són el registre de casos de COVID-19 realitzats a Catalunya, per comarques.

## Punts de la Pràctica

<li> <b>Context del dataset.</b> 
<li> Definir un <b>títol descriptiu </b>pel dataset. </li>
<li> <b>Descripció breu del dataset</b></li>
<li> <b>Representació gràfica</b> del dataset</li>
<li> <b>Contingut:</b> explicació dels camps del dataset, el període de temps de les dades i com s'ha recollit. </li>
<li> <b>Agraïments:</b> presentar el propietari del conjunt de dades (citar anàlisis anteriors i/o justificar la cerca amb anàlisis similars). </li>
<li> <b>Inspiració:</b> perquè és interessant el conjunt de dades seleccionat? Quines preguntes es volen respondre? </li>
<li> <b>Llicència seleccionada pel dataset resultant i motivació</b>.</li>
<li> <b>Codi</b> amb el qual s'ha generat el dataset. </li>
<li> <b>Publicació del dataset</b> en format CSV a Zenodo (obtenció del DOI) amb una breu descripció. </li></br>

Tots els punts anteriors, estan desenvolupats en el fitxer Práctica1.PDF

## Descripció dels fitxers

<li> <b>web_scraper.py:</b> conté la implementació dels mètodes per obtenir un conjunt de dades de la web indicada anteriorment. Utilitza les llibreries BeautifulSoup i Selenium. </li>
<li> <b>json_to_csv.py:</b> genera un fitxer en format CSV a partir del JSON obtingut del web scraping. Utilitza la llibreria Pandas. </li>

## Membres del grup de treball

<li>Maria Begoña Felip. </li>
<li>Vicenç Pio. </li>

## Bibliografia i referències digitals

<li> Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC. </li>
<li> Masip, D. El lenguaje Python. Editorial UOC. </li>
<li> Tutorial de Github https://guides.github.com/activities/hello-world. </li>
