def turn(liste):
  #on trourne de 90 degres le tableau 
  new_liste=[]
  new_liste.append(liste[2])
  new_liste.append(liste[5])
  new_liste.append(liste[8])
  new_liste.append(liste[1])
  new_liste.append(liste[4])
  new_liste.append(liste[7])
  new_liste.append(liste[0])
  new_liste.append(liste[3])
  new_liste.append(liste[6])
  return new_liste
  
def verification(liste,perso):
  #verifie si un joueur a gagne
  nvl=liste
  for i in range(4):
    nvl=turn(nvl)
    if nvl[0]==perso and nvl[1]==perso and nvl[2]==perso :
      return True
    if nvl[1]==perso and nvl[4]==perso and nvl[7]==perso :
      return True
    elif nvl[0]==perso and nvl[4]==perso and nvl[8]==perso :
      return True
    elif nvl[0]==perso and nvl[3]==perso and nvl[6]==perso :
      return True
  return False

def ia(liste):

  #fonction qui choisie une case aléatoire
  def rdc(liste):
    print("ia: choix d'une case aléatoire")
    for i in range(len(liste)):
      if liste[i] !="  o  " and liste[i] !="  x  ":
        print(i)
        return i

  perso="  o  "
  perso_j="  x  "
  nvl=liste
  t=False

  print("ia: verification des coups finaux")
  #on verifie si on peut terminer le jeu ce coup si
  for i in range(4):
    nvl=turn(nvl)
    #premiere ligne
    if nvl[0]==perso and nvl[1]==perso and nvl[2]!=perso_j:
      a=nvl[2]
      t=True
    elif nvl[1]==perso and nvl[2]==perso and nvl[0]!=perso_j:
      a=nvl[0] 
      t=True
    elif nvl[0]==perso and nvl[2]==perso and nvl[1]!=perso_j:
      a=nvl[1]
      t=True
    #seconde ligne
    elif nvl[3]==perso and nvl[4]==perso and nvl[5]!=perso_j:
      a=nvl[5]
      t=True
    elif nvl[4]==perso and nvl[5]==perso and nvl[3]!=perso_j:
      a=nvl[3]
      t=True
    elif nvl[3]==perso and nvl[5]==perso and nvl[4]!=perso_j:
      a=nvl[4]
      t=True
    #diagonale
    elif nvl[0]==perso and nvl[4]==perso and nvl[8]!=perso_j:
      a=nvl[8]
      t=True
    elif nvl[4]==perso and nvl[8]==perso and nvl[0]!=perso_j:
      a=nvl[0]
      t=True
    elif nvl[0]==perso and nvl[8]==perso and nvl[4]!=perso_j:
      a=nvl[4]
      t=True
  if t:
    nvl[nvl.index(a)]="  o  "
    return nvl
  
  print("ia: cherche a bloquer l'adversaire")
  #on essaye de bloquer l'adversaire
  for i in range(4):
    nvl=turn(nvl)
    if nvl[0]==perso_j and nvl[1]==perso_j:
      a=nvl[2]
      t=True
    elif nvl[1]==perso_j and nvl[2]==perso_j:
      a=nvl[0]
      t=True
    elif nvl[0]==perso_j and nvl[2]==perso_j:
      a=nvl[1]
      t=True  
    elif nvl[3]==perso_j and nvl[4]==perso_j:
      a=nvl[5]
      t=True
    elif nvl[4]==perso_j and nvl[5]==perso_j:
      a=nvl[3]
      t=True
    elif nvl[3]==perso_j and nvl[5]==perso_j:
      a=nvl[4]
      t=True
    elif nvl[0]==perso_j and nvl[4]==perso_j:
      a=nvl[8]
      t=True
    elif nvl[4]==perso_j and nvl[8]==perso_j:
      a=nvl[0]
      t=True
    elif nvl[0]==perso_j and nvl[8]==perso_j:
      a=nvl[4]
      t=True
  if t:
    nvl[nvl.index(a)]="  o  "
    return nvl  
  

  #on compte le nombre de case occupé par chaque joueur
  x=0
  y=0
  for element in liste:
    if element=="  o  ":y+=1
    if element=="  x  ":x+=1
  total=x+y
  print("ia: j'occupe ",x," cases")
  print("ia: tu occupe ",y," cases")
  print("ia: il y a donc ",total," cases occupées")
  #Si le bot jou le premier coup, il joue au milieu
  if total==0:
    print("ia: c'est le premier coup")
    liste[4]=perso
    return liste
  #Si le bot joue le dernier coup, il joue la seule case libre
  if total==8:
    print("ia: c'est le dernier coup")
    for i in range(len(liste)):
      if liste[i] !="  o  " and liste[i] !="  x  ":
        liste[i]=perso
        return liste
  liste[rdc(liste)]=perso
  return liste

    

def printm(liste,perso="  x  ",):
  #definition de l'affichage avec les elements de la liste
  affichage="┌─────┬─────┬─────┐\n"+"│"+liste[0]+"│"+liste[1]+"│"+liste[2]+"│\n"+"├─────┼─────┼─────┤\n"+"│"+liste[3]+"│"+liste[4]+"│"+liste[5]+"│\n"+"├─────┼─────┼─────┤\n"+"│"+liste[6]+"│"+liste[7]+"│"+liste[8]+"│\n"+"└─────┴─────┴─────┘\n"
  
  #verification: l'entree utilisateur est un chiffre entre 0 et 8 et si la case est libre
  cond=True
  while cond:
    r=input(affichage)
    if r.isdigit()==True:
      if 0<=int(r)<=8:
        if liste[int(r)]=="  o  "or liste[int(r)]=="  x  ":
          cond=True
        else:
          liste[int(r)]=perso
          cond=False



  #on remplit et renvoi la case designe par l'utilisateur
  liste[int(r)]=perso
  return liste


def partie_2_joueurs():
  liste=["  0  ","  1  ","  2  ","  3  ","  4  ","  5  ","  6  ","  7  ","  8  "]
  fini=False
  i=0
  print("Debut de la partie")
  j1=input("Nom du premier joueur: ")
  perso1="  x  "
  j2=input("Nom du second joueur: ")
  perso2="  o  "

  while fini!=True:
    i+=1
    if i%2==0:
      print("C'est au tour de : "+j1+" de jouer.")
      liste=printm(liste,perso1)
      fini=verification(liste,perso1)
    elif i==10:
      print("Match Nul")
      fini=True
    else:
      print("C'est au tour de : "+j2+" de jouer.")
      liste=printm(liste,perso2)
      fini=verification(liste,perso2)
  if i%2==0 and i!=10:
    print(j1," a gagné !")
  elif i!=10:
    print(j2,"a gagné !")
    
  print("┌─────┬─────┬─────┐\n"+"│"+liste[0]+"│"+liste[1]+"│"+liste[2]+"│\n"+"├─────┼─────┼─────┤\n"+"│"+liste[3]+"│"+liste[4]+"│"+liste[5]+"│\n"+"├─────┼─────┼─────┤\n"+"│"+liste[6]+"│"+liste[7]+"│"+liste[8]+"│\n"+"└─────┴─────┴─────┘\n")
  print("end")

def partie_joueur_vs_ia():
  liste=["  0  ","  1  ","  2  ","  3  ","  4  ","  5  ","  6  ","  7  ","  8  "]
  fini=False
  i=0
  print("Debut de la partie")
  j1=input("Nom du joueur: ")
  perso1="  x  "
  perso2="  o  "
  while fini!=True:
    i+=1
    if i%2==0:
      print("C'est au tour de : "+j1+" de jouer.")
      liste=printm(liste,perso1)
      fini=verification(liste,perso1)
    elif i==10:
      print("Match Nul")
      fini=True
    else:
      print("C'est au tour de l'ia de jouer.")
      liste=ia(liste)
      fini=verification(liste,perso2)
  if i%2==0 and i!=10:
    print(j1," a gagné !")
  elif i!=10:
    print("L'ia a gagné !")
    
  print("┌─────┬─────┬─────┐\n"+"│"+liste[0]+"│"+liste[1]+"│"+liste[2]+"│\n"+"├─────┼─────┼─────┤\n"+"│"+liste[3]+"│"+liste[4]+"│"+liste[5]+"│\n"+"├─────┼─────┼─────┤\n"+"│"+liste[6]+"│"+liste[7]+"│"+liste[8]+"│\n"+"└─────┴─────┴─────┘\n")
  print("end")
