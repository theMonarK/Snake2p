# -*- coding: cp1252 -*-

import marshal

#Fonction de chargement des donnés du fichier .xml

def chargerFichier(fichier):
    assert type(fichier) is str
    #Importation du module python de lecture de fichier .xml
    from xml.dom.minidom import parse;
    #Importation du fichier .xml
    doc = parse(fichier);
    #Récupération de la racine du fichier
    rootElement = doc.documentElement;

    #importaion du module de chargement des parametres
    import mParametre as mPa
    para = mPa.creer()

    #chargement des nom et couleurs des joueurs
    couleur=[0,0]
    nom=[1,1]
    joueurNode = rootElement.getElementsByTagName("joueurs");#joueurNode est une liste
    joueurSize = joueurNode.length;
    for i in range(joueurSize):
        joueurxNode = rootElement.getElementsByTagName("joueur1");#joueurxNode est une liste
        joueurxSize = joueurxNode.length;
        for i in range(joueurxSize):
            couleurNode = rootElement.getElementsByTagName("couleur");
            couleurSize = couleurNode.length;
            for i in range(couleurSize):
                node = couleurNode[i];
                couleur[i]= str(node.firstChild.nodeValue)
            nomNode = rootElement.getElementsByTagName("nom");
            nomSize = nomNode.length;
            for i in range(nomSize):
                node = nomNode[i];
                nom[i]= str(node.firstChild.nodeValue)

    mPa.setNomsJoueurs(para, nom[0], nom[1])
    mPa.setCouleursJoueurs(para, couleur[0], couleur[1])

    #Chargement forme de la carte
    formeNode = rootElement.getElementsByTagName("forme");#carteNode est une liste
    formeSize = formeNode.length;
    for i in range(formeSize):
        node = formeNode[i];
        forme = str(node.firstChild.nodeValue)
    mPa.setForme(para, forme)

    #Chargement carte rectangulaire
    rectanNode = rootElement.getElementsByTagName("rectangulaire");#rectanNode est une liste
    rectanSize = rectanNode.length;
    for i in range(rectanSize):
        node = rectanNode[i];
        if node.hasAttributes():
            hauteur = node.getAttribute("hauteur");
            largeur = node.getAttribute("largeur");
            mPa.setTailleRect(para, mPa.convertirEnInt(hauteur), mPa.convertirEnInt(largeur))

    #Chargement carte triangulaire
    triNode = rootElement.getElementsByTagName("triangulaire");#triNode est une liste
    triSize = triNode.length;
    for i in range(triSize):
        node = triNode[i];
        if node.hasAttributes():
            x1 = node.getAttribute("x1");
            y1 = node.getAttribute("y1");
            x2 = node.getAttribute("x2");
            y2 = node.getAttribute("y2");
            x3 = node.getAttribute("x3");
            y3 = node.getAttribute("y3");
            #convertion en int
            x1 = mPa.convertirEnInt(x1)
            y1 = mPa.convertirEnInt(y1)
            x2 = mPa.convertirEnInt(x2)
            y2 = mPa.convertirEnInt(y2)
            x3 = mPa.convertirEnInt(x3)
            y3 = mPa.convertirEnInt(y3)
            mPa.setTailleTrian(para, x1, y1, x2, y2, x3, y3)

    #Chargement carte croix
    croixNode = rootElement.getElementsByTagName("croix");#croixNode est une liste
    croixSize = croixNode.length;
    for i in range(croixSize):
        node = croixNode[i];
        if node.hasAttributes():
            longueurcote = node.getAttribute("longueurcote");
            mPa.setTailleCroix(para, mPa.convertirEnInt(longueurcote))

    #Chargement de la vitesse de déroulement du jeu
    vjeuNode = rootElement.getElementsByTagName("vitessejeu");#vjeuNode est une liste
    vjeuSize = vjeuNode.length;
    for i in range(vjeuSize):
        node = vjeuNode[i];
        if node.hasAttributes():
            vitessejeu = node.getAttribute("vitessejeu")
            mPa.setVitesseJeu(para, mPa.convertirEnInt(vitessejeu))

    #Chargement du sccore a atteindre pour gagner
    finjeuNode = rootElement.getElementsByTagName("finjeu");#finjeuNode est une liste
    finjeuSize = finjeuNode.length;
    for i in range(finjeuSize):
        node = finjeuNode[i];
        if node.hasAttributes():
            finjeu = node.getAttribute("finjeu")
            mPa.setFinJeu(para, mPa.convertirEnInt(finjeu))
    return para

#Sauver une partie

def sauverPara(para,nomFichier):
    assert type(nomFichier) is str
    assert type(para) is list
    import mParametre as mPa
    marshal.dump(para, open(nomFichier,"wb"))


# Charger une partie

def chargerPara(nomFichier):
    assert type(nomFichier) is str
    para = marshal.load(open(nomFichier,"rb"))
    return para
























    

