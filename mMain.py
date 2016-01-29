# -*- coding: cp1252 -*-

import pygame
from pygame.locals import*
from pygame.mixer import*
import mSnake
import mParametre 
import mMap
import mJoueur
import mJeu
import mGraphique 
import mChargerFichier 
import mCase
import random


def creerPartie(para):
        vitesse = mParametre.getVitesseJeu(para)
        formeCarte = mParametre.getForme(para)
        carte = []
        if formeCarte == "rectangulaire":
                coordonnes = mParametre.getTailleRect(para)
                carte = mMap.creerRectangulaire(coordonnes[0], coordonnes[1])
        elif formeCarte == "triangulaire":
                coordonnes = mParametre.getTailleTrian(para)
                carte = mMap.creerTriangulaire(coordonnes[0][0], coordonnes[0][1],coordonnes[1][0], coordonnes[1][1], coordonnes[2][0], coordonnes[2][1])
        elif formeCarte == "croix":
                carte = mMap.creerCroix(mParametre.getTailleCroix(para))
        #positionnement initiale des deux snakes et du bonbon
        lcarte, hcarte = mMap.getTailleEcran(carte)
        y1init = int(hcarte/2+1)
        y2init = int(hcarte/2-1)
        x1init,x2init=0,0
        
        xb = random.randint(1,lcarte-1)
        yb = random.randint(1,hcarte-1)
        mMap.getEtatCase(carte,xb,yb)
        while carte[xb][yb] !=1:
                xb = random.randint(1,lcarte-1)
                yb = random.randint(1,hcarte-1)

        for i in range(len(carte[0])-1) : #Recherche d'une case "vide" sur l'axe x
                xi=carte[i][y1init]     # Positionne le point sur la map par rapport a (x,y)
                etatxr = mCase.getCase(xi) # Recupere etat de la case
                if etatxr=="vide":
                        x1init=i
                        break # On arrete la boucle quand on a trouvé une case vide
        for j in range(len(carte[0])-1) : 
                xi=carte[j][y2init]
                etatxr = mCase.getCase(xi)
                if etatxr=="vide":
                        x2init=j
                        break # On arrete la boucle quand on a trouvé une case vide
           
        #creation des deux snakes initiaux de longeur 10
        snake1 = mSnake.creerSnakeInit(int(x1init), int(y1init))
        joueur1 = mJoueur.creerJoueur(mParametre.getCouleurJoueur(para,1), mParametre.getNomJoueur(para, 1), snake1)
        snake2 = mSnake.creerSnakeInit(int(x2init), int(y2init))
        joueur2 = mJoueur.creerJoueur(mParametre.getCouleurJoueur(para,2), mParametre.getNomJoueur(para, 2), snake2)
        bonbon = mMap.setCaseC(carte,xb,yb,"bonbon")

        jeu = mJeu.creer(vitesse, carte, joueur1, joueur2)
        return jeu,xb,yb,lcarte,hcarte

# Jouer
def jouer(depSnake,jeu,screen,numJ,carte):               
        #Mise en mouvement du Snake1
        snake=mJoueur.getSnake(mJeu.getJoueur(jeu,numJ))
        joueur=mJeu.getJoueur(jeu,numJ)
        xd,yd=mSnake.getxSnake(snake,0),mSnake.getySnake(snake,0)
        mMap.setCaseC(mJeu.getMap(jeu),xd,yd,"vide")#Suprime état précedent du snake
        if numJ==1:
                depSnake=mSnake.deplacerSnake1(depSnake,snake,joueur)
        if numJ==2:
                depSnake=mSnake.deplacerSnake2(depSnake,snake,joueur)
        x=mSnake.getxSnake(snake,len(snake)-1)
        y=mSnake.getySnake(snake,len(snake)-1)

        #Delimitation du terrain
        snake,joueur1=mMap.sortiCarte(mJoueur.getSnake(mJeu.getJoueur(jeu,numJ)),depSnake,mJeu.getJoueur(jeu,numJ),carte,x,y)
        
        # Affichage et actualisation de la map
        mSnake.imprimerSnake(mJeu.getMap(jeu),mJoueur.getSnake(mJeu.getJoueur(jeu,numJ)),numJ)
        mGraphique.afficherMap(jeu, screen) # Affiche la map graphique
        # Décomenter pour afficher la carte non graphique et les joueurs
        #mMap.affichageMap(mJeu.getMap(jeu),jeu) 
        x=mSnake.getxSnake(snake,len(snake)-1)
        y=mSnake.getySnake(snake,len(snake)-1)
        return depSnake,x,y,snake,joueur

def finPartie(run,parametres,joueur1,joueur2,collision,sperdant):
        # Obtention du joueur gagnant, fin du jeu et affichage du gagnant
        finPartie=mParametre.getFinJeu(parametres)
        if len(mJoueur.getSnake(joueur1))==finPartie:
                print(mJoueur.getNom(joueur1),"gagne")
                run=False
                pygame.time.delay(2000)
        if len(mJoueur.getSnake(joueur2))==finPartie:
                print(mJoueur.getNom(joueur2),"gagne")
                run=False
                pygame.time.delay(2000)
        if collision==True and sperdant=="snake1":
                print(mJoueur.getNom(joueur2),"gagne")
                run=False
                pygame.time.delay(2000)
        if collision==True and sperdant=="snake2":
                print(mJoueur.getNom(joueur1),"gagne")
                run=False
                pygame.time.delay(2000)
        return run

def main():

        choix=int(input("Charger une partie (0) ou Nouvelle partie (1) :\n"))
        if choix==1:
                # charger le fichier
                parametres = mChargerFichier.chargerFichier("defsnake2j.xml")
                # Construire la partie
                jeu,xb,yb,lcarte,hcarte = creerPartie(parametres)
                #Initialisation graphique et affichage carte
                carte = mJeu.getMap(jeu)
                hauteur, largeur = mMap.getTailleEcran(carte)
                screen = mGraphique.initGraphique(hauteur*20, largeur*20,"mMain.py")

                collision=False # Variable de collision
                sperdant="" # Snake perdant
                run = True # Variable principale
                depSnake1=["","VD"] #Variable de déplacement du Snake1
                depSnake2=["","VD"] #Variable de déplacement du Snake1
                
        if choix==0:
                parametres = mChargerFichier.chargerPara("sauvegarde")
                print(parametres)
                # Construire la partie
                jeu,xb,yb,lcarte,hcarte = creerPartie(parametres)
                snake1, snake2 = mParametre.getSnakes(parametres)
                mJoueur.setSnakeJ(mJeu.getJoueur(jeu,1),snake1)
                mJoueur.setSnakeJ(mJeu.getJoueur(jeu,2),snake2)
                #Initialisation graphique et affichage carte
                carte = mJeu.getMap(jeu)
                hauteur, largeur = mMap.getTailleEcran(carte)
                screen = mGraphique.initGraphique(hauteur*20, largeur*20,"mMain.py")

                collision=False
                sperdant=""
                run = True # Variable principale
                depSnake1, deSnake2 = mParametre.getDepSnakes(parametres)
                depSnake1=["","VD"] #Variable de déplacement du Snake1
                depSnake2=["","VD"] #Variable de déplacement du Snake2
                
                
        
        #Boucle principale
        while run:
                #déplace le snake 1 (fonctionne et passe par les bordures)
                depSnake1,x1,y1,snake1,joueur1=jouer(depSnake1,jeu,screen,1,carte)
                snake1,joueur1,xb,yb = mMap.bonbon(xb,yb,x1,y1,snake1,joueur1,lcarte,hcarte,carte,1,depSnake1)
                #déplace le snake 2 (fonctionne et passe par les bordures)
                depSnake2,x2,y2,snake2,joueur2=jouer(depSnake2,jeu,screen,2,carte)
                snake2,joueur2,xb,yb = mMap.bonbon(xb,yb,x2,y2,snake2,joueur2,lcarte,hcarte,carte,2,depSnake2)
                #verification que les deux snake ne se sont pas percutte                
                collision,sperdant=mMap.collisionSnakes(snake1,x1,y1,x2,y2,snake2,joueur1,joueur2,jeu,1,collision,sperdant)
                collision,sperdant=mMap.collisionSnakes(snake1,x1,y1,x2,y2,snake2,joueur1,joueur2,jeu,2,collision,sperdant)
                #Verification que le snake ne s'est pas percutte lui meme
                collision,sperdant=mMap.collisionSnake(snake1,x1,y1,joueur1,jeu,1,collision,sperdant)
                collision,sperdant=mMap.collisionSnake(snake2,x2,y2,joueur2,jeu,2,collision,sperdant)
                #ecrit la fin de partie
                run = finPartie(run,parametres,joueur1,joueur2,collision,sperdant)
                #lecture clavier
                for event in pygame.event.get(): 
                        if event.type == KEYDOWN: # Acquisition de l'appuie sur une touche
                                mSnake.clavierSnake1(depSnake1,event) # Touche clavier du snake1
                                mSnake.clavierSnake2(depSnake2,event) # Touche clavier du snake2
                                if event.key == K_p: #met en pause le jeu 5 secondes quand appuit sur p.
                                        pygame.time.delay(5000)
                                if event.key == K_e: #sauvegarde des parametres
                                        mParametre.setSnakes(parametres, mJoueur.getSnake(mJeu.getJoueur(jeu,1)), mJoueur.getSnake(mJeu.getJoueur(jeu,2)))
                                        mParametre.setDepSnakes(parametres, depSnake1, depSnake2)
                                        mChargerFichier.sauverPara(parametres,"sauvegarde")
                                        run=False

                        if event.type == QUIT:
                                run=False
                vitesse=mParametre.getVitesseJeu(parametres)
                pygame.time.delay(vitesse) # Definit la vitesse du jeu  (en milisec)

        #ferme la fenetre pygame
        pygame.time.delay(1000)
        pygame.quit()
        # Sauver la partie
##        choix=int(input("Sauver la partie ? oui (1), non (0):\n"))
##        if choix==1:
##                # sauver la partie
##                mParametre.setSnakes(parametres, mJoueur.getSnake(mJeu.getJoueur(jeu,1)), mJoueur.getSnake(mJeu.getJoueur(jeu,2)))
##                mParametre.setDepSnakes(parametres, depSnake1, depSnake2)
##                mChargerFichier.sauverPara(parametres,"sauvegarde")
        




#####################################################################################################

if __name__ == '__main__': main() # Verification des erreurs      
