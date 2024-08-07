from podatki import *
from funkcije import *

import os
import re
import pandas as pd


#dodamo rojstni dan v podatke
dodaj_rojstni_dan('podatki')

#združimo vse datoteke
zdruzi_csv('podatki', 'tabela.csv')