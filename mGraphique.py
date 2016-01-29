# -*- coding: cp1252 -*-

import pygame
from pygame.locals import*
from pygame.mixer import*
import mCase
import mJoueur
import mJeu

#Module graphique

def initGraphique(hauteur,largeur,nomfichier):
    #Initialiser ecran        
    screen = pygame.display.set_mode((hauteur,largeur)) # Taille ecran
    pygame.display.set_caption(nomfichier)
    background = pygame.Surface(screen.get_size()) # récupere taille de l'écran
    background = background.convert() # converti le fond dans pygame
    background.fill((250,250,250)) # Fond blanc
    pygame.init() # Initialisation Pygame
    #initialisation son
    pygame.mixer.init()
    pygame.mixer.music.load("votai.wav")
    return screen


def chargerFichierCouleurJoueur(couleur):
    if couleur == "bleu":
        joueurcoul = pygame.image.load("corps_snake_bleu.jpg")
    elif couleur == "jaune":
        joueurcoul = pygame.image.load("corps_snake_jaune.jpg")
    elif couleur == "noir":
        joueurcoul = pygame.image.load("corps_snake_noir.jpg")
    elif couleur == "orange":
        joueurcoul = pygame.image.load("corps_snake_orange.jpg")
    elif couleur == "rouge":
        joueurcoul = pygame.image.load("corps_snake_rouge.jpg")
    elif couleur == "vert":
        joueurcoul = pygame.image.load("corps_snake_vert.jpg")
    elif couleur == "violet":
        joueurcoul = pygame.image.load("corps_snake_violet.jpg")
    return joueurcoul


def afficherMap(jeu, screen):
    carte = mJeu.getMap(jeu)
    caseVide = pygame.image.load("case_carte_vide.jpeg")
    caseRien = pygame.image.load("case_carte_rien.jpeg")
    caseBonbon = pygame.image.load("case_carte_bonbon.jpeg")
    couleurj1 = mJoueur.getCouleur(mJeu.getJoueur(jeu,1))
    couleurj2 = mJoueur.getCouleur(mJeu.getJoueur(jeu,2))
    if couleurj1=="bleu":
        caseSnake1 = pygame.image.load("corps_snake_bleu.jpg")
    elif couleurj1=="jaune":
        caseSnake1 = pygame.image.load("corps_snake_jaune.jpg")
    elif couleurj1=="noir":
        caseSnake1 = pygame.image.load("corps_snake_noir.jpg")
    elif couleurj1=="orange":
        caseSnake1 = pygame.image.load("corps_snake_orange.jpg")
    elif couleurj1=="rouge":
        caseSnake1 = pygame.image.load("corps_snake_rouge.jpg")
    elif couleurj1=="vert":
        caseSnake1 = pygame.image.load("corps_snake_vert.jpg")
    elif couleurj1=="violet":
        caseSnake1 = pygame.image.load("corps_snake_violet.jpg")
        
    if couleurj2=="bleu":
        caseSnake2 = pygame.image.load("corps_snake_bleu.jpg")
    elif couleurj2=="jaune":
        caseSnake2 = pygame.image.load("corps_snake_jaune.jpg")
    elif couleurj2=="noir":
        caseSnake2 = pygame.image.load("corps_snake_noir.jpg")
    elif couleurj2=="orange":
        caseSnake2 = pygame.image.load("corps_snake_orange.jpg")
    elif couleurj2=="rouge":
        caseSnake2 = pygame.image.load("corps_snake_rouge.jpg")
    elif couleurj2=="vert":
        caseSnake2 = pygame.image.load("corps_snake_vert.jpg")
    elif couleurj2=="violet":
        caseSnake2 = pygame.image.load("corps_snake_violet.jpg")
    hauteur = len(carte[0])
    largeur = len(carte)
    for i in range(largeur):
        for j in range(hauteur):
            etat = mCase.getCase(carte[i][hauteur-j-1])
            if etat == "vide":
                screen.blit(caseVide,(i*20,j*20))
            elif etat == "rien":
                screen.blit(caseRien,(i*20,j*20))
            elif etat == "bonbon":
                screen.blit(caseBonbon,(i*20,j*20))
            elif etat == "snake1":
                screen.blit(caseSnake1,(i*20,j*20))
            elif etat == "snake2":
                screen.blit(caseSnake2,(i*20,j*20))
    pygame.display.flip()

def playSound():
    pygame.mixer.music.play() #joue votai
























