# -*- coding: cp1252 -*-

#Module Parametre

#Constructeur
def creer():
    #[forme, [hauteur, largeur], [x1,y1,x2,y2,x3,y3],largeur cote map croix
    #     "nomJ1", "nomJ2","couleuJ1","couleurJ2",vitessejeu,finjeu, snake1, snake2, sens de deplacement snake1, sens de deplacement snake2]
    return ["forme",[0,0],[0,0,0,0,0,0],0,"nomJ1", "nomJ2","couleuJ1","couleurJ2",0,0, "snake1", "snake2", "depsnake1", "depsnake2"]

#Accesseurs :
def setForme(para, forme):
    assert type(forme) is str
    para[0]=forme

def setTailleRect(para, hauteur, largeur):
    assert type(hauteur) is int
    assert type(largeur) is int
    para[1][0]=hauteur
    para[1][1]=largeur

def setTailleTrian(para, x1, y1, x2, y2, x3, y3):
    assert type(x1) is int
    assert type(y1) is int
    assert type(x2) is int
    assert type(y2) is int
    assert type(x3) is int
    assert type(y3) is int
    para[2][0]=x1
    para[2][1]=y1
    para[2][2]=x2
    para[2][3]=y2
    para[2][4]=x3
    para[2][5]=y3

def setTailleCroix(para, largeurcote):
    assert type(largeurcote) is int
    para[3]=largeurcote

def setNomsJoueurs(para, nomJ1, nomJ2):
    assert type(nomJ1) is str
    assert type(nomJ2) is str
    para[4]=nomJ1
    para[5]=nomJ2


def setCouleursJoueurs(para, couleurJ1, couleurJ2):
    assert type(couleurJ1) is str
    assert type(couleurJ2) is str
    para[6]=couleurJ1
    para[7]=couleurJ2

def setVitesseJeu(para, vitessejeu):
    assert type(vitessejeu) is int
    para[8]=vitessejeu

def setFinJeu(para, finjeu):
    assert type(finjeu) is int
    para[9]=finjeu

def setSnakes(para, snake1,snake2):
    assert type(snake1) is list
    assert type(snake2) is list
    para[10], para[11] = snake1, snake2

def setDepSnakes(para, depsnake1, depsnake2):
    assert type(depsnake1) is list
    assert type(depsnake2) is list
    para[12], para[13] = depsnake1, depsnake2    

def getForme(para):
    return para[0]

def getTailleRect(para):
    return [para[1][0],para[1][1]]

def getTailleTrian(para):
    return [[para[2][0],para[2][1]], [para[2][2],para[2][3]], [para[2][4],para[2][5]]]

def getTailleCroix(para):
    return para[3]

def getNomJoueur(para, numjoueur):
    if numjoueur==1:
        return para[4]
    elif numjoueur==2:
        return para[5]

def getCouleurJoueur(para, numjoueur):
    if numjoueur==1:
        return para[6]
    elif numjoueur==2:
        return para[7]

def getVitesseJeu(para):
    return para[8]

def getFinJeu(para):
    return para[9]

def getSnakes(para):
    return para[10], para[11]

def getDepSnakes(para):
    return para[12], para[13]


def convertirEnInt(chaine):
    nombre = 0;
    try:
        nombre = int(chaine)
    except ValueError:
        nombre = -1;
    return nombre;

