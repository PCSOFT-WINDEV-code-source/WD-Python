# WD Python
# Fichier exemple pour illustrer l'usage de la fonction PythonExécute
from math import *

# Retourne une chaîne
def HelloWorld():
	return "Hello World!"
	
# Retourne une chaîne complétée avec la chaîne reçue en paramètre
def DireBonjour(name):
	return "Hello, %s" % name

# Retourne un entier représentant l'addition entre les deux entiers reçus en paramètres
def AdditionEntier(int1, int2):
    return int1 + int2
		
# Retourne un réel représentant la soustraction entre les deux réels reçus en paramètres
def SoustraireReel(float1, float2):
    return float1 - float2
	
# Retourne un tableau de nombres premiers
def ListePremiers(max):
  tabPrem = list(range(2,max+1))
  k = 2
  nRacine = sqrt(max)
  while k < nRacine:
    tabPrem=[p for p in tabPrem if p <= k or p%k != 0]
    k = tabPrem[tabPrem.index(k) + 1]  # nouveau nombre premier
  return tabPrem

# Retourne un dictionnaire
def LitDictionnaire():
	return { "G. Washington": 1732, "C. de Gaulle": 1890, "Nabuchodonosor II": -642 }
	
# Réceptionne un dictionnaire
def EcritDictionnaire(dict):
	return str(dict)