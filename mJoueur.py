# -*- coding: cp1252 -*-

# Module Joueur

#Constructeur

# Creer joueur

def creerJoueur(couleur,nom,snake):
    """
    Création d'une liste caractérisant le joueur
    """
    joueur=[]
    assert type(couleur) is str
    assert type(nom) is str
    assert type(snake) is list
    joueur=[couleur,nom,snake]
    return joueur

#Accesseur

#Récupérer sa couleur

def getCouleur(joueur):
    """
    Récupération de la couleur d'un joueur
    """
    assert type(joueur) is list
    couleur=""
    couleur=joueur[0]
    return couleur

#Récupérer le nom

def getNom(joueur):
    """
    Récupération du nom d'un joueur
    """
    nom=""
    assert type(joueur) is list

    nom=joueur[1]
    return nom

# Récupérer son snake

def getSnake(joueur):
    """
    Récupération du snake d'un joueur
    """
    snake=[]
    assert type(joueur) is list

    snake=joueur[2]
    return snake

# Mise en place d'un joueur

def setSnakeJ(joueur,snake):
    """
    Met en place le snake d'un joueur
    """
    assert type(joueur) is list
    assert type(snake) is list

    joueur[2]=snake

    return joueur
  
