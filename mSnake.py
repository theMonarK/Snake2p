# -*- coding: cp1252 -*-

import mMap
import mCase
import pygame
import mJoueur
import mMain
import mJeu
from pygame.locals import*


# Module Snake

#Constructeur

# Creer snake

def creerSnake(x,y):
    """
    Creation d'une liste caracterisant le snake
    """
    assert type(x) is int
    assert type(y) is int
    snake=[]    
    snake=[(x,y)]
    return snake

def creerSnakeInit(x,y):
    assert type(x) is int
    assert type(y) is int
    snake=[(x,y)]
    for i in range(9):
        snake.append((x+i,y))
    return snake


#Accesseur

#Recuperer x

def getxSnake(snake,num):
    """
    Recuperation de x d'une partie d'un snake
    """
    assert type(snake) is list
    assert type(num) is int
    x=snake[num][0]
    return x

#Recuperer y

def getySnake(snake,num):
    """
    Recuperation de y d'une partie d'un snake
    """
    assert type(snake) is list
    assert type(num) is int
    y=snake[num][1]
    return y



# Changer Snake

def setSnake(snake,x,y,num):
    """
    mise en place du snake d'un joueur
    """
    assert type(snake) is list
    assert type(x) is int
    assert type(y) is int
    assert type (num) is int

    snake[num]=(x,y)
    return snake

# Opérateur
def imprimerSnake(carte, snake, numjoueur):
    """
    Affichage du snake dans la map non graphique
    """
    assert type(snake) is list
    assert type(carte) is list
    assert type(numjoueur) is int
    for case in snake:
        etat = "vide"
        if numjoueur == 1:
            etat = "snake1"
        elif numjoueur == 2:
            etat = "snake2"
    for i in range (len(snake)):
        x=snake[i][0]
        y=snake[i][1]
        mMap.setCaseC(carte, x,y, etat)


#déplacer snake (fonction qui déplace le snake d'une case)

def deplacerSnake1(depSnake1,snake1,joueur):
    """
    deplacement du snake1
    """
    assert type (depSnake1) is list
    assert type (snake1) is list
    assert type(joueur) is list
    joueur1=joueur
    
    if (depSnake1[0]=="VD" and depSnake1[1]=="VH") or (depSnake1[0]=="VG" and depSnake1[1]=="VH") or (depSnake1[0]=="VH" and depSnake1[1]=="VH"):
        #Monter                                       
        for j in range(len(snake1)):

                if j==len(snake1)-1:
                        x1=getxSnake(snake1,j)
                        y1=getySnake(snake1,j)
                        setSnake(snake1,x1,y1+1,j)
                        x1,y1=getxSnake(snake1,j),getySnake(snake1,j)
                        
                else:
                        snake1[j]=snake1[j+1]
                        x1=getxSnake(snake1,j)
                        y1=getySnake(snake1,j)
                        
                mJoueur.setSnakeJ(joueur1,snake1)

    if (depSnake1[0]=="VD" and depSnake1[1]=="VB") or (depSnake1[0]=="VG" and depSnake1[1]=="VB") or (depSnake1[0]=="VB" and depSnake1[1]=="VB"):
        #Descendre                                        
        for j in range(len(snake1)):

                if j==len(snake1)-1:
                        x1=getxSnake(snake1,j)
                        y1=getySnake(snake1,j)
                        setSnake(snake1,x1,y1-1,j)
                        x1,y1=getxSnake(snake1,j),getySnake(snake1,j)
                        
                else:
                        snake1[j]=snake1[j+1]
                        x1=getxSnake(snake1,j)
                        y1=getySnake(snake1,j)

                mJoueur.setSnakeJ(joueur1,snake1)

    if (depSnake1[0]=="VH" and depSnake1[1]=="VG") or (depSnake1[0]=="VB" and depSnake1[1]== "VG") or (depSnake1[0]=="VG" and depSnake1[1]=="VG"):
        #Gauche                              
        for j in range(len(snake1)):

                if j==len(snake1)-1:
                        x1=getxSnake(snake1,j)
                        y1=getySnake(snake1,j)
                        setSnake(snake1,x1-1,y1,j)
                        x1,y1=getxSnake(snake1,j),getySnake(snake1,j)
                        
                else:
                        snake1[j]=snake1[j+1]
                        x1=getxSnake(snake1,j)
                        y1=getySnake(snake1,j)
                mJoueur.setSnakeJ(joueur1,snake1)

    if (depSnake1[0]==("VH") and depSnake1[1]== "VD") or (depSnake1[0]== "VB" and depSnake1[1]== "VD") or (depSnake1[0]== "" and depSnake1[1]== "VD" or (depSnake1[0]=="VD" and depSnake1[1]=="VD")):
        # Droite       
        for j in range(len(snake1)):

                if j==len(snake1)-1:
                        x1=getxSnake(snake1,j)
                        y1=getySnake(snake1,j)
                        
                        setSnake(snake1,x1+1,y1,j)
                        x1,y1=getxSnake(snake1,j),getySnake(snake1,j)
                        
                else:
                        snake1[j]=snake1[j+1]
                        x1=getxSnake(snake1,j)
                        y1=getySnake(snake1,j)

                mJoueur.setSnakeJ(joueur1,snake1)
    return depSnake1


def deplacerSnake2(depSnake2,snake2,joueur2):
    """
    deplacement du snake2
    """
    assert type (depSnake2) is list
    assert type (snake2) is list
    assert type (joueur2) is list
    
    if (depSnake2[0]=="VD" and depSnake2[1]=="VH") or (depSnake2[0]=="VG" and depSnake2[1]=="VH") or (depSnake2[0]=="VH" and depSnake2[1]=="VH"):
        #Monter                                       
        for j in range(len(snake2)):

                if j==len(snake2)-1:
                        x2=getxSnake(snake2,j)
                        y2=getySnake(snake2,j)
                        setSnake(snake2,x2,y2+1,j)
                        x,y=getxSnake(snake2,j),getySnake(snake2,j)
                        
                else:
                        snake2[j]=snake2[j+1]
                        x=getxSnake(snake2,j)
                        y=getySnake(snake2,j)
                        
                mJoueur.setSnakeJ(joueur2,snake2)

    if (depSnake2[0]=="VD" and depSnake2[1]=="VB") or (depSnake2[0]=="VG" and depSnake2[1]=="VB") or (depSnake2[0]=="VB" and depSnake2[1]=="VB"):
        #Descendre                                        
        for j in range(len(snake2)):

                if j==len(snake2)-1:
                        x2=getxSnake(snake2,j)
                        y2=getySnake(snake2,j)
                        setSnake(snake2,x2,y2-1,j)
                        x2,y2=getxSnake(snake2,j),getySnake(snake2,j)
                        
                else:
                        snake2[j]=snake2[j+1]
                        x2=getxSnake(snake2,j)
                        y2=getySnake(snake2,j)

                mJoueur.setSnakeJ(joueur2,snake2)

    if (depSnake2[0]=="VH" and depSnake2[1]=="VG") or (depSnake2[0]=="VB" and depSnake2[1]== "VG") or (depSnake2[0]=="VG" and depSnake2[1]=="VG"):
        #Gauche                              
        for j in range(len(snake2)):

                if j==len(snake2)-1:
                        x=getxSnake(snake2,j)
                        y=getySnake(snake2,j)
                        setSnake(snake2,x2-1,y2,j)
                        x2,y2=getxSnake(snake2,j),getySnake(snake2,j)
                        
                else:
                        snake2[j]=snake2[j+1]
                        x2=getxSnake(snake2,j)
                        y2=getySnake(snake2,j)
                mJoueur.setSnakeJ(joueur2,snake2)

    if (depSnake2[0]==("VH") and depSnake2[1]== "VD") or (depSnake2[0]== "VB" and depSnake2[1]== "VD") or (depSnake2[0]== "" and depSnake2[1]== "VD" or (depSnake2[0]=="VD" and depSnake2[1]=="VD")):
        # Droite       
        for j in range(len(snake2)):

                if j==len(snake2)-1:
                        x2=getxSnake(snake2,j)
                        y2=getySnake(snake2,j)
                        setSnake(snake2,x2+1,y2,j)
                        x2,y2=getxSnake(snake2,j),getySnake(snake2,j)
                        
                else:
                        snake2[j]=snake2[j+1]
                        x2=getxSnake(snake2,j)
                        y2=getySnake(snake2,j)

                mJoueur.setSnakeJ(joueur2,snake2)
    return depSnake2

def clavierSnake1(depSnake1,event):
    """
    lecture clavier du snake1
    """
    assert type(depSnake1) is list
    
    if event.key == K_RIGHT:
        if depSnake1[1]=="VG":
                depSnake1[1]= "VG"
        else:
                depSnake1[0]=depSnake1[1]
                depSnake1[1]= "VD"
        
    if event.key == K_UP:

            if depSnake1[1]=="VB":
                    depSnake1[1]= "VB"
            else:
                    depSnake1[0]=depSnake1[1]
                    depSnake1[1]= "VH"

    if event.key == K_DOWN:

            if depSnake1[1]=="VH":
                    depSnake1[1]= "VH"
            else:
                    depSnake1[0]=depSnake1[1]
                    depSnake1[1]= "VB"

    if event.key == K_LEFT:

            if depSnake1[1]=="VD":
                    depSnake1[1]= "VD"
            else:
                    depSnake1[0]=depSnake1[1]
                    depSnake1[1]= "VG"
    else:
        return

    return

def clavierSnake2(depSnake2,event):
    assert type(depSnake2) is list
    """
    lecture clavier du snake1
    """    
    if event.key == K_c:
        if depSnake2[1]=="VG":
            depSnake2[1]= "VG"
        else:
            depSnake2[0]=depSnake2[1]
            depSnake2[1]= "VD"
        
    if event.key == K_s:
        if depSnake2[1]=="VB":
            depSnake2[1]= "VB"
        else:
            depSnake2[0]=depSnake2[1]
            depSnake2[1]= "VH"

    if event.key == K_x:
        if depSnake2[1]=="VH":
            depSnake2[1]= "VH"
        else:
            depSnake2[0]=depSnake2[1]
            depSnake2[1]= "VB"

    if event.key == K_z: # Correspond au w en QWERTY
        if depSnake2[1]=="VD":
            depSnake2[1]= "VD"
        else:
            depSnake2[0]=depSnake2[1]
            depSnake2[1]= "VG"
    return

def appSnake(snake,depSnake):
    """
    Rajoute une case au snake d'un joueur
    """
    assert type(snake) is list
    if depSnake[1]=="VD":
        x=snake[0][0]-1
        y=snake[0][1]
    if depSnake[1]=="VG":
        x=snake[0][0]+1
        y=snake[0][1]
    if depSnake[1]=="VH":
        x=snake[0][0]
        y=snake[0][1]-1
    if depSnake[1]=="VB":
        x=snake[0][0]
        y=snake[0][1]+1
    snake.insert(0,(x,y))
    return snake

def ressusciteSnake(snake,joueur,jeu):
    """
    ressuscite snake apres collision
    """
    assert type(snake) is list
    assert type(joueur) is list

    for j in reversed(range(10)):        
        mMap.setCaseC(mJeu.getMap(jeu),snake[j][0],snake[j][1],"vide")
        snake.remove(snake[j])
    mJoueur.setSnakeJ(joueur,snake)
    return snake
    


