from podatki import *
from funkcije_ostalo import *

#dodamo rojstni dan v podatke
dodaj_rojstni_dan('podatki')

#združimo vse datoteke
zdruzi_csv('podatki', 'tabela_podatki.csv')

#med podatke dodamo še horoskop
dodaj_horoskop_v_datoteko('tabela_podatki.csv')