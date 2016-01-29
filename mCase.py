# -*- coding: cp1252 -*-

#Module case

#Constructeur
def creer(etat) :
    assert type(etat) is str
    entier=0
    if etat == "rien":
        entier=0
    elif etat == "vide":
        entier=1
    elif etat == "bonbon":
        entier=2
    elif etat == "snake1":
        entier=3
    elif etat == "snake2":
        entier=4
    return entier

#Accesseur
def getCase(x):
    '''(case)'''
    assert type(x) is int
    etat="bug"
    if x==0:
        etat="rien"
    elif x==1:
        etat="vide"
    elif x==2:
        etat="bonbon"
    elif x==3:
        etat="snake1"
    elif x==4:
        etat="snake2"
    return etat

def setCase(etat):
    '''etat'''
    assert type(etat) is str
    entier = 0
    if etat == "rien":
        entier=0
    elif etat == "vide":
        entier=1
    elif etat == "bonbon":
        entier=2
    elif etat == "snake1":
        entier = 3
    elif etat == "snake2":
        entier = 4
    #print entier
    return entier


def getCaseX(x, etat):
    '''(case, etat)'''
    assert type(x) is int
    assert type(etat) is str
    return getCase(x)== etat









