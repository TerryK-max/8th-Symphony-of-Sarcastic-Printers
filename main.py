import os
import subprocess
import colors as color


logo = open('asciiLogo.txt', 'r')
print(color.bcolors.OKGREEN + color.bcolors.BOLD + logo.read() + color.bcolors.ENDC + color.bcolors.WARNING)

cmd = ['lpstat' ,'-p', '-d']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

sortie = str(proc.communicate())
try:
    lignes = sortie.split("\n")
    imprimantes = []
    for index, ligne in lignes :
      if index < (lignes.lenght-1) :
        mots = ligne.split(" ")
        if len(mots) > 1 :
            imprimantes.append(mots[1])

except ValueError:
    mots = sortie.split(" ")
    print(sortie)
    if len(mots) > 1 :
        imprimantes.append(mots[1])

print('\n'+color.bcolors.OKBLUE + color.bcolors.BOLD + str(len(imprimantes)), 'imprimantes détectées :')
print(imprimantes)
a = input("\nQuel fichier voulez vous imprimer ? (.txt et .pdf recommandés)" + color.bcolors.ENDC + color.bcolors.OKCYAN)
b = input(color.bcolors.ENDC + color.bcolors.OKBLUE + color.bcolors.BOLD + "Combien de copies par imprimante souhaitez vous imprimer ?" + color.bcolors.ENDC + color.bcolors.OKCYAN)
try:
  for i in range(len(imprimantes)):
    os.system("lpr -P " + imprimantes[i] + " -# " + b + " templates/" + a)
  print(color.bcolors.OKGREEN + color.bcolors.BOLD +'\n\nImpression réussie !' + color.bcolors.ENDC)

except:
  print(color.bcolors.FAIL + color.bcolors.BOLD + "\n\nERREUR : quelque chose s'est mal passé.\n" + color.bcolors.ENDC)