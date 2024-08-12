# Projektna naloga 
Avtor: Jasmina Mazej

## Uvod
Za projektno nalogo sem se odločila analizirati podatke na spletni strani (https://www.famousbirthdays.com/), ki vsebuje znane osebnosti in njihove poklice/vlogo, rojene na nek datum.

## Navodila za uporabo
Za delovanje funkcij mora imeti uporabnik naložene knjižice re, requests, BeautifulSoup, pandas, csv, os in matplotlib.pyplot.
V csv-ju pri nekaterih osebah pod poklic piše Family Member, saj niso znani zaradi specifičnega razloga.

## Opis datotek
- funkcije_zajem.py in funkcije_ostalo.py vsebujeta funkcije,
 ki so uporabljene v ostalih datotekah
- pridobivanje_podatkov.py iz spletnih strani po 
mesecih pobere html in izlušči željene podatke (ime, starost in poklic) 
in shrani podatke v datoteke
- zdruzi_csv.py med podatke doda rojstne dneve in horoskope ter vse datoteke 
združi v csv tabelo
- analiza.ipynb predstavi zbrane podatke z grafi in histogrami