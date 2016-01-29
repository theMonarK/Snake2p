# -*- coding: cp1252 -*-

#Module jeu

#Constructeur
def creer(vitesse, carte, joueur1, joueur2):
    jeu = [vitesse, carte, joueur1, joueur2]
    return jeu


#Accesseur
def getMap(jeu):
    return jeu[1]

def getJoueur(jeu, numjoueur):
    x = numjoueur + 1
    return jeu[x]

def getVitesse(jeu):
    return jeu[0]


