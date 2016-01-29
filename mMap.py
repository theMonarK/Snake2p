# -*- coding: cp1252 -*-

#Module map

import mCase
import mJeu
import mSnake
import mJoueur
import random
import mGraphique

#Constructeur

def creerEncadrement(carte):
    cartef = []
    for i in range(len(carte)+2):
        cartef.append([])
        for j in range(len(carte[0])+2):
            if i==0 or i==len(carte)+1 or j==0 or j==len(carte[0])+1:
                cartef[i].append(mCase.creer("rien"))
            else:
                cartef[i].append(carte[i-1][j-1])
    return cartef
            

#Rectangulaire
def creerRectangulaire(hauteur, largeur):
    assert type(hauteur) is int
    assert type(largeur) is int
    carte = []
    for i in range(largeur):
        carte.append([])
        for j in range(hauteur):
            carte[i].append(mCase.creer("vide"))
    return creerEncadrement(carte)

    

#Triangulaire
def creerTriangulaire(x1, y1, x2, y2, x3, y3):
    assert type(x1) is int
    assert type(y1) is int
    assert type(x2) is int
    assert type(y2) is int
    assert type(x3) is int
    assert type(y3) is int
    # decalage de l'origine du repere et passage en flotants
    ox = min(x1,x2,x3)
    oy = min(y1,y2,y3)
    x1, x2, x3 = float(x1-ox),float(x2-ox),float(x3-ox)
    y1, y2, y3 = float(y1-oy),float(y2-oy),float(y3-oy)
    # tri des points selon leurs absisses
    l=[[x1,y1]]
    if x2 >= x1:
        l.append([x2,y2])
    else:
        l.insert(0,[x2,y2])
    if x3 >= x2:
        l.append([x3,y3])
    else:
        if x3 >= x1:
            l.insert(1,[x3,y3])
        else :
            l.insert(0,[x3,y3])
    x11,x22,x33 = l[0][0],l[1][0],l[2][0]#enregistrement des points triés
    y11,y22,y33 = l[0][1],l[1][1],l[2][1]
    #equations des droites :
    if (x11-x33) == 0:#droite passant par les points 11 et 33
        a11 = 10000
        b11 = x11
    else:
        a11 = (y11-y33)/(x11-x33)
        b11 = y11 - a11*x11
    if (x22-x11) == 0: #droite passant par les points 11 et 22
        a22 = 10000
        b22 = x22
    else:
        a22 = (y22-y11)/(x22-x11)
        b22 = y22 - a22*x22
    if (x33-x22) == 0: #droite passant par les points 22 et 33
        a33 = 10000
        b33 = x33
    else:
        a33 = (y33-y22)/(x33-x22)
        b33 = y33 - a33*x33
    #trois cas de triangles possibles
    #cas du triangle trop plat...
    deltaY = max(y11, y22, y33)-min(y11, y22, y33)
    deltaX = max(x11, x22, x33)-min(x11, x22, x33)
    if deltaY <=2 or deltaX<= 2 :
        return creerRectangulaire(int(max(x11,x22,x33))+3,int(max(y11,y22,y33))+3)
    else:
        #creation d'une carte rectangulaire de rien
        carte = []
        for i in range(int(max(x11,x22,x33))+1):
            carte.append([])
            for j in range(int(max(y11,y22,y33))+1):
                carte[i].append(mCase.creer("rien"))

        #cas int(y2) < int(y1(x2)
        if int(y22) < int(a11*x22+b22-1):
            for i in range(len(carte)):
                y = int(a11*i+b11)
                while y >= int(max(a22*i+b22,a33*i+b33)):
                    carte[i][y] = mCase.setCase("vide")
                    y = y-1
            cartefinie = carte
                
        #cas int(y2) > int(y1(x2)
        elif int(y22) > int(a11*x22+b22+1):
            for i in range(len(carte)):
                y = int(a11*i+b11)
                while y <= int(min(a22*i+b22,a33*i+b33)):
                    carte[i][y] = mCase.setCase("vide")
                    y = y+1
            cartefinie = carte
        #cas du triangle trop plat... (prévention des erreurs)
        else :
            cartefinie = creerRectangulaire(int(max(x11,x22,x33)),int(max(y11,y22,y33)))
    return creerEncadrement(cartefinie)

#croix
def creerCroix(a):
    assert type(a) is int
    xmin = a/3
    xmax = a-a/3
    ymin, ymax = xmin, xmax
    carte = []
    for i in range(a):
        carte.append([])
        for j in range(a):
            if (i<xmin and ( j<ymin or j>=ymax)) or (i>=xmax and ( j<ymin or j>=ymax)):
                carte[i].append(mCase.creer("rien"))
            else :
                carte[i].append(mCase.creer("vide"))
    
    return creerEncadrement(carte)


#Accesseur

def getCaseC(carte,x,y):
    assert type(x) is int
    assert type(y) is int
    assert type(carte) is list
    return mCase.getCase(carte[x][y])

def getEtatCase(carte,x,y):
    assert type(x) is int
    assert type(y) is int
    assert type(carte) is list
    etat=""
    x=carte[x][y]
    return mCase.getCase(x)
    
                
    
def setCaseC(carte,x,y, etat):
    assert type(x) is int
    assert type(y) is int
    carte[x][y] = mCase.setCase(etat)
    return

def affichageMap(carte,jeu):
    hauteur = len(carte[0])
    largeur = len(carte)
    print ("joueur1", mJeu.getJoueur(jeu,1))
    print ("joueur2", mJeu.getJoueur(jeu,2))
    for a in reversed(range(hauteur)):
        MapNum=[]
        for b in range(largeur):
            MapNum.append(carte[b][a])
        print(MapNum,'\n')
    l=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1]

            
            

def getTailleEcran(carte):
    hauteur = len(carte)
    largeur = len(carte[0])
    return hauteur, largeur

def sortiCarte(snake,depSnake,joueur,carte,x,y):
    
    # "Capteurs" de sorti
    etatSortie = getEtatCase(carte,x,y)    
    if etatSortie == "rien" :
        if depSnake[1]=="VD":# Sort par la droite
            for i in range(len(carte[1])) : #Recherche d'une case "vide" sur l'axe x dans le sens du snake
                xr=carte[i][y]
                etatxr = mCase.getCase(xr)
                if etatxr=="vide" :
                    mSnake.setSnake(snake,i,y,len(snake)-1) # Replace le snake sur la carte
                    mJoueur.setSnakeJ(joueur,snake)
                    x,y=mSnake.getxSnake(snake,len(snake)-1),mSnake.getySnake(snake,len(snake)-1)
                    break # on arrete la boucle

        if depSnake[1]=="VH":# Sort par le haut
            for i in range(len(carte)-1) :
                yr=carte[x][i]
                etatyr = mCase.getCase(yr)
                if etatyr=="vide" :                                                
                    mSnake.setSnake(snake,x,i,len(snake)-1)
                    mJoueur.setSnakeJ(joueur,snake)
                    x,y=mSnake.getxSnake(snake,len(snake)-1),mSnake.getySnake(snake,len(snake)-1)
                    break

        if depSnake[1]=="VG":# Sort par la Gauche
          for i in reversed(range(len(carte)-1)) :
            xr=carte[i][y]
            etatxr = mCase.getCase(xr)
            if etatxr=="vide":                                                
                mSnake.setSnake(snake,i,y,len(snake)-1)
                mJoueur.setSnakeJ(joueur,snake)
                x,y=mSnake.getxSnake(snake,len(snake)-1),mSnake.getySnake(snake,len(snake)-1)
                break

        if depSnake[1]=="VB":# Sort par le bas
            for i in reversed(range(len(carte[0])-1)) :
                yr=carte[x][i]
                etatyr = mCase.getCase(yr)
                if etatyr=="vide":
                    mSnake.setSnake(snake,x,i,len(snake)-1)
                    mJoueur.setSnakeJ(joueur,snake)
                    x,y=mSnake.getxSnake(snake,len(snake)-1),mSnake.getySnake(snake,len(snake)-1)
                    break
    return snake,joueur

def bonbon(xb,yb,x,y,snake,joueur,lcarte,hcarte,carte,numJ,depSnake):
    
        if x==xb and y==yb:
            mSnake.appSnake(snake)
            mGraphique.playSound() # Joue la musique quand on est sur le bonbon            
            mJoueur.setSnakeJ(joueur,snake)
            xb = random.randint(1,lcarte-1) # position au hasard de x
            yb = random.randint(1,hcarte-1)# position au hasard de y
            getEtatCase(carte,xb,yb)
            print('score de ', mJoueur.getNom(joueur), ' : ', len(snake))#affiche le score
            while carte[xb][yb] !=1: # Verification que l'on est sur la carte
                xb = random.randint(1,lcarte-1)
                yb = random.randint(1,hcarte-1)
        bonbon = setCaseC(carte,xb,yb,"bonbon")
        return snake,joueur,xb,yb

def collisionSnakes(snake1,x1,y1,x2,y2,snake2,joueur1,joueur2,jeu,numJ,collision,sperdant):
    
    if numJ==1:
        for i in range(len(snake2)-1):
            if x1==snake2[i][0] and y1==snake2[i][1]:
                if len(snake1)>10: # si le snkae est encore assez grand
                    mSnake.ressusciteSnake(snake1,joueur1,jeu)
                    collision=False
                    sperdant=""
                    return collision, sperdant
                if len(snake1)<=10: #Si le snake est trop petit, il perd
                    collision=True
                    sperdant="snake1"          
    if numJ==2:
        for j in range(len(snake1)-1):
            if x2==snake1[j][0] and y2==snake1[j][1]:
                if len(snake2)>10:
                    mSnake.ressusciteSnake(snake2,joueur2,jeu)
                    collision=False
                    sperdant=""
                    return collision, sperdant
                if len(snake2)<=10:
                    collision=True
                    sperdant="snake2" 
    return collision,sperdant

def collisionSnake(snake,x,y,joueur,jeu,numJ,collision,sperdant):
    for i in reversed(range(len(snake)-1)):
        #print snake
        #print "i=", i
        if x==snake[i][0] and y==snake[i][1] :
            if len(snake)>10:
                mSnake.ressusciteSnake(snake,joueur,jeu)
                collision = False
                sperdant=""
                return collision,sperdant
            if len(snake)<=10 and numJ==1:
                collision=True
                sperdant="snake1"
            if len(snake)<=10 and numJ==2:
                collision=True
                sperdant="snake2"
                break

    return collision,sperdant


    


