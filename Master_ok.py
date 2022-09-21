#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:13:33 2021

@author: kimpapaulin
"""


import subprocess
import time
import sys
import os 
import numpy

## le programme ci dessous est notre master .... 

## Cette premiere fonction permettra de vérifier la connectivité sur les machines de l'école. 

def verif_con():
    df = open( 'machine.txt','r')
    lines = df.readlines()
    lines = [line.split('\n')[0] for line in lines]
    listproc = []
    timer=5
    login="kimpa-20"
    
    for i in lines:
        proc = subprocess.Popen(["ssh",login+"@"+i , "hostname"],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        listproc.append(proc)
        
    machine_disp = []
    machine_non_disp=[]
    
    for j in range (0, len(lines)-1): 
        try:
               out, err = listproc[j].communicate(timeout=timer)
        except subprocess.TimeoutExpired:
               listproc[j].kill()
               print(str(j)+" timeout")
        code = listproc[j].returncode
        if code == 0 :
            machine_disp.append(lines[j])
        else : 
           machine_non_disp.append(lines[j])
           
    print("voici la liste des machines disponible : ")
    print("  ")
    print(machine_disp)
    print("   ")
    print("Voici la liste des machines non disponible ....")
    print("  ")
    print(machine_non_disp)
    print("  ")
    
    return machine_disp , machine_non_disp

## la fonction clear permet de netoyer les repertoires dans les quelles nous allons travailler ......

def rm (command , na):
    listproc = []
    timer=50
    login="kimpa-20"
    machine = "tp-4b01-1"+str(na)
    proc = subprocess.Popen(["ssh",login+"@"+machine,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    i=0
    out, err = listproc[i].communicate(timeout=timer)
    try:
        out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
        listproc[i].kill()
        print(str(i)+" timeout")  
        
    code = listproc[i].returncode
    if code == 0 : 
          print("le repertoire {} a eté suprimé avec succès sur le serveur {}".format("/kimpa-20","kimpa-20@tp-4b01-1"+str(na)))
    else : 
         #print(" ")
         print(str(i)+ " err: '{}'".format(err))
         
    #print("attente 3 secondes avant supression du repertoire sur le cerveur suivant: {}".format("kimpa-20@tp-4b01-1"+str(na)))
    #time.sleep(3)
    print("  ")
        

## La fonction ci dessous permet de creer les repertoires dans le tmp avec lesquels nous allons travailler ....
    
def ssh(command,ma):
    listproc = []
    timer=50
    login="kimpa-20"
    machine = "tp-4b01-1"+str(ma)
    proc = subprocess.Popen(["ssh",login+"@"+machine,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    i=0
    try:
         out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
            listproc[i].kill()
            print(str(i)+" timeout")
    
    code = listproc[i].returncode
    if code == 0 : 
          print("le repertoire {} a été creer  avec succès sur le serveur {}".format(command.split()[-1],"kimpa-20@tp-4b01-1"+str(ma)))
    else : 
          print(str(i)+ " err: '{}'".format(err))
    #print(" ")
    #print("attente 6 secondes avant creation du repertoire sur la machine suivante..")
    #time.sleep(3)
    #print("  ")
    
r_split = True
## La fonction ci dessous permets de creer les repertoires des split .....
def rep_split(command, rs):
    listproc = []
    timer=50
    login="kimpa-20"
    machine = "tp-4b01-1"+str(rs)
    proc = subprocess.Popen(["ssh",login+"@"+machine ,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    i=0
    try:
         out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
            listproc[i].kill()
            print(str(i)+" timeout")
    
    code = listproc[i].returncode
    if code == 0 : 
          print("le repertoire {} a été creer  avec succès sur le serveur {}".format(command.split()[-1],"kimpa-20@tp-4b01-1"+str(rs)))

    else : 
          print(str(i)+ " err: '{}'".format(err))
          r_split = False
    print(" ")
    #print("attente 3 secondes avant creation du repertoire sur la machine suivante..")
    #time.sleep(3)
   # print("  ")
    

## La fonction ci dessous permet de creer le repertoire Map....
r_map = True ## Cette variable permettra de confirmer ou pas la creation du repertoire ...
def rep_map(command, rm):
    listproc = []
    timer=50
    login="kimpa-20"
    machine = "tp-4b01-1"+str(rm)
    proc = subprocess.Popen(["ssh",login+"@"+machine ,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    i=0
    try:
         out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
        listproc[i].kill()
        print(str(i)+" timeout")
    
    code = listproc[i].returncode
    if code == 0 : 
          print("le repertoire {} a été creer  avec succès sur le serveur {}".format(command.split()[-1],"kimpa-20@tp-4b01-1"+str(rm)))
    else : 
          print(str(i)+ " err: '{}'".format(err))
          r_map = False
    print(" ")
    #print("attente 3 secondes avant creation du repertoire sur la machine suivante..")
    #time.sleep(3)
    #print("  ")
       
## La fonction ci dessous permets de copiers les fichiers split dans les repertoirs correspondants .....

def scp_split(localPath,distantPath, machine_nber):
    listproc = []
    timer=50
    login="kimpa-20"
    i=0
    
    machine ="tp-4b01-1"+ machine_nber
    proc = subprocess.Popen(["scp",localPath,login+"@"+machine +":" +distantPath],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    
    out, err = listproc[i].communicate(timeout=timer)
    code = listproc[i].returncode
    
    try:
        out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
        listproc[i].kill()
        print(str(i)+" timeout") 
    if code ==0: 
        print("le fichier{} a été copier avec succès dans le repertoire {} de la machine{}".format("./S"+str(j)+".txt","/tmp/kimpa-20/", machine))
    else : 
      print("le fichier{} n'a pas pu etre copier dans le repertoire {} de la machine{}".format("./S"+str(j)+".txt","/tmp/kimpa-20/", machine))
     
    print(" ")
    #print("attente 6 secondes : copie du fichier sur la machine correspondante...")
    #time.sleep(3)
   # print(" ")

## La fonction ci dessous permet de copier le slave.py dans les differents repertoirs ....

def scp_slave(localPath,distantPath, machine_nber):
    listproc = []
    timer=50
    login="kimpa-20"
    i=0
    
    machine ="tp-4b01-1"+ machine_nber
    proc = subprocess.Popen(["scp",localPath,login+"@"+machine +":" +distantPath],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    
    out, err = listproc[i].communicate(timeout=timer)
    code = listproc[i].returncode
    
    try:
        out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
        listproc[i].kill()
        print(str(i)+" timeout") 
    if code ==0: 
        print("le fichier {} a été copier avec succès dans le repertoire {} de la machine {}".format("slave.py","/tmp/kimpa-20/map", machine))
    else : 
      print("le fichier {} n'a pas pu etre copier dans le repertoire {} de la machine{}".format("slave.py","/tmp/kimpa-20/map", machine))
     
    print(" ")
    #print("attente 3 secondes : copie du fichier sur la machine correspondante...")
    #time.sleep(3)
    #print(" ")

## La fonction ce dessous permet de lancer le slave sur les differentes machines 

def runslave(mode,lan):
    listproc = []
    timer=700
    i=0
    login="kimpa-20"
    machine = "tp-4b01-1"+str(lan)
    proc =subprocess.Popen(["ssh",login+"@"+machine, " python3 /tmp/kimpa-20/map"+ "/slave.py " + mode + " S"+str(lan)+".txt"],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    
    out, err = listproc[i].communicate(timeout=timer)
    code = listproc[i].returncode
    try:
        out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
        listproc[i].kill()
        print(str(i)+" timeout")
    if code ==0: 
        print("le lencement du mapper dans le slave.py s'est bien effectuer sur la machine "+machine)
        print("  ")
    else : 
        print("le calcul du map ne s'est fait sur la machine {} et l'erreur:{}".format(machine ,err))
        print("  ")

## La fonction ci dessous permet d'envoyer sur les differents slaves, le fichiers des machines ..

def scp_mach(localPath,distantPath, machine_nber):
  listproc = []
  timer=50
  login="kimpa-20"
  i=0

  machine ="tp-4b01-1"+ machine_nber
  proc = subprocess.Popen(["scp",localPath,login+"@"+machine +":" +distantPath],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
  listproc.append(proc)
    
  out, err = listproc[i].communicate(timeout=timer)
  code = listproc[i].returncode
  try:
      out, err = listproc[i].communicate(timeout=timer)
  except subprocess.TimeoutExpired:
      listproc[i].kill()
      print(str(i)+" timeout") 
  if code ==0: 
      print("le fichier {} a été copier avec succès dans le repertoire {} de la machine{}".format("machines_used.txt","/tmp/kimpa-20/", str(k)))
  else : 
      print("le fichier {} n'a pas pu etre copier dans le repertoire {} de la machine{}".format("machines_used.txt","/tmp/kimpa-20/", str(k)))
     
  print(" ")
  #print("attente 3 secondes : copie du fichier sur la machine correspondante...")
  #time.sleep(3)
  #print(" ")
 
## La fonction ce dessous permet de creer les repertoires shuffles .....

r_shuffle = True ## Cette variable permet de confirmer ou pas si le repertoire a été creer ou pas ....
def rep_shu(command, rsh):
    listproc = []
    timer=50
    login="kimpa-20"
    machine = "tp-4b01-1"+str(rsh)
    proc = subprocess.Popen(["ssh",login+"@"+machine ,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    i=0
    try:
         out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
            listproc[i].kill()
            print(str(i)+" timeout")
    
    code = listproc[i].returncode
    if code == 0 : 
          print("le repertoire {} a été creer  avec succès sur le serveur {}".format(command.split()[-1],"kimpa-20@tp-4b01-1"+str(rsh)))
          
    else : 
          print(str(i)+" err: '{}'".format(err))
          r_shuffle = False
    print(" ")
    #print("attente 3 secondes avant creation du repertoire sur la machine suivante...")
    #time.sleep(3)
    #print("  ") 
  
    
## La fonction ci dessous permet de tourner le shuffle .....
def runshuffle(mode,shan):
    listproc = []
    timer=50
    i=0
    login="kimpa-20"
    machine = "tp-4b01-1"+str(shan)
    proc =subprocess.Popen(["ssh",login+"@"+machine, " python3 /tmp/kimpa-20/map"+ "/slave.py " + mode + " UM"+str(shan)+".txt"],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    
    out, err = listproc[i].communicate(timeout=timer)
    code = listproc[i].returncode
    try:
        out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
        listproc[i].kill()
        print(str(i)+" timeout")
    if code ==0: 
        print("le lencement du shuffle dans le slave.py s'est bien effectuer sur la machine "+machine)
        print("  ")
    else : 
        print("le calcul n'a pas eté faite sur la machine {} et l'erreur:{} et \n !!!!!!!! et out {}".format(machine ,err,out))
        print("  ")
        
        
## La fonction ci dessous permet de lancer la phase du reduce ....        
def runreduce(mode,rdu):
    listproc = []
    timer=60
    i=0
    login="kimpa-20"
    machine = "tp-4b01-1"+str(rdu)
    proc =subprocess.Popen(["ssh",login+"@"+machine, " python3 /tmp/kimpa-20/map"+ "/slave.py " + mode],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    listproc.append(proc)
    
    out, err = listproc[i].communicate(timeout=timer)
    code = listproc[i].returncode
    try:
        out, err = listproc[i].communicate(timeout=timer)
    except subprocess.TimeoutExpired:
        listproc[i].kill()
        print(str(i)+" timeout")
    if code ==0: 
        print("le lencement du reduce dans le slave.py s'est bien effectuer sur la machine "+machine)
        print("  ")
    else : 
        print("le calcul n'a pas eté faite sur la machine {} et l'erreur:{} et \n !!!!!!!! et out {}".format(machine ,err,out))
        print("  ")
        
  
### Premier test plus optimal ....le calcul se fait ici en parallele (combine reduce)

# def red_comb(command):
#     a=""
#     listproc = []
#     timer=600
#     login="kimpa-20"
#     for var in [0,1,2]:
#         machine = "tp-4b01-1"+str(var)
#         proc = subprocess.Popen(["ssh",login+"@"+machine ,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
#         listproc.append(proc)
        
        
#     for j in [0,1,2]:
#         out, err = None, None
#         try:
#             out, err = listproc[j].communicate(timeout=timer)
#         except subprocess.TimeoutExpired:
#              listproc[j].kill()
#              print(str(j)+" timeout")
    
#         code = listproc[j].returncode
#         if code == 0 : 
#           print("la sortie est &&&&&&&&&&&&&&&  ")
#           print(out)
#           print("le fichier est ecrit !!")
          
#         else : 
#               print(str(j)+" err: '{}'".format(err))
#         liste_sort = out.split()
#         print("la liste en sortie est lllllllllllllllllll",liste_sort)
#         for el in liste_sort : 
#             #sortie = str(el)[2:-3]
#             sortie = str(el)
#             print("la sortie !!!!!!!!!!!!!!!!!!!",sortie)
#             #a+=sortie+"\n"
#             a+=sortie
        
#             fichier = open("summary_results.txt","w")
#     #fichier.write("%s \n" % a)
#             fichier.write("%s " % a)
#             fichier.close
#     return 

### autre approche ..................................
# Deuxieme approche pour faire le combine ici le calcul est elementaire....

# def red_comb2(command, var):
#     listproc = []
#     timer=600
    
#     login="kimpa-20"
#     machine = "tp-4b01-1"+str(var)
#     proc = subprocess.Popen(["ssh",login+"@"+machine ,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
#     listproc.append(proc)

#     out, err = None, None
#     try:
#         out, err = listproc[0].communicate(timeout=timer)
#     except subprocess.TimeoutExpired:
#             listproc[0].kill()
#             print(str(err)+" timeout")
#     code = listproc[0].returncode
#     if code == 0 : 
#        print("la sortie est &&&&&&&&&&&&&&& ")
#        print(out)
#        print("le fichier est ecrit !!")    
#     else : 
#        print(" err: '{}'".format(err))
#     sortie = str(out)[2:-3]
#     print("la sortie !!!!!!!!!!!!!!!!!!!",sortie)
       
#     fichier = open("summary_results.txt","a")
#     fichier.write("%s \n" % sortie)
#     #fichier.write("%s " % sortie)
#     fichier.close
#     return


def red_comb2(command , var):
     listproc = []
     timer=600
     login="kimpa-20"
     machine = "tp-4b01-1"+str(var)
     proc = subprocess.Popen(["ssh",login+"@"+machine ,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
     listproc.append(proc)
     
     out, err = None, None
     try:
         out, err = listproc[0].communicate(timeout=timer)
     except subprocess.TimeoutExpired:
             listproc[0].kill()
             print(str(err)+" timeout")
     code = listproc[0].returncode
     if code ==0 : 
         string = out.decode("utf-8")
         liste = string.split("\n")
         #allel = " ".join(liste)
         fichier = open("summary_results.txt","a+")
         for mot in liste : 
             fichier.write("%s \n" % mot)
         fichier.close()   
     else :
        print("ca ne marche pas et l'erreur est @@@@@@@@@@@@@@@@@@: ", err)
        
     return

## La fonction ci dessous permet de splitter un fichiers inputs en entrées en plusieurs petits fichiers ....

def div_files(input_file):
    df1 = open(input_file , 'r')
    listes_ligne = df1.readlines()
    for i in range (0, (len(listes_ligne))//3):
        file = open("S0.txt","a")
        file.write('%s' %listes_ligne[i])
        
    for j in range((len(listes_ligne))//3 , (2*len(listes_ligne))//3):
        file = open("S1.txt","a")
        file.write("%s" %listes_ligne[j])
        
    for k in range((2*len(listes_ligne))//3 , len(listes_ligne)):
        file=open("S2.txt","a")
        file.write("%s" %listes_ligne[k])
        

# def div_files2(input_file):
#     df1 = open(input_file, 'r')
#     listes_ligne = df1.readlines()
#     part0 = list(numpy.array_split(listes_ligne , 3)[0])
#     part1 = list(numpy.array_split(listes_ligne , 3)[1])
#     part2 = list(numpy.array_split(listes_ligne , 3)[2])
    
#     for i in part0:
#          file = open("S0.txt","w")
#          file.write('%s' %i)
         
#     for j in  part1:
#         file = open("S1.txt","w")
#         file.write("%s" %j)
        
#     for k in part2:
#         file=open("S2.txt","w")
#         file.write("%s" %k)
    
## On creet les differents fichiers split....




#div_files("test4.txt")

div_files("test.txt")


## On verifie que les machines avec lesquels nous alons travailler sont bien disponible....

d = verif_con()
machines_dispo =d[0]
machines_non_dispo=d[1]
machine_work=['tp-4b01-10','tp-4b01-11','tp-4b01-12']


for machine in machine_work:
     if machine in machines_dispo : 
         print("La machine {} est disponible et peut etre utiliser pour le calcul".format(machine))
         print("  ")
         T=True
     else : 
         print("La machine {} n'est pas disponible et ne peut etre utiliser pour le calcul".format(machine))
         print("  ")
         print("on ne peut continuer le calcul car l'une des machines necessaires n'est pas disponible. ")
         print("  ")
         print("veillez changer de machine..")
         T=False
         break     
if T==False:
    print(" ")
    print("le master va s'arreter...")
    sys.exit()

## Ci dessous on appel  la fonction pour suppression des repertoires avant de travailler ....
for na in [0,1,2]:
    rm("rm -rf /tmp/kimpa-20/" , na)
       
## Ci dessous on appel la fonction pour creation des fichiers ....
for ma in [0,1,2]:
    ssh("mkdir -p /tmp/kimpa-20", ma)
    
   
## Ce dessous on appele la fonction pour creer le repertoire des splits.   
for rs in [0,1,2]:
    rep_split("mkdir -p /tmp/kimpa-20/split", rs)
    
##Ci desoous on confirme la creation des repertoires splits avant de continuer les calculs ...
## Si le repertoire n'est pas creer le calcul s'interompe....
if r_split == False:
    print("  ")
    print("Le repertoire des splits n'a pas été créer, le calcul ne peut se poursuivre ...")
    sys.exit()
    
print("Confirmation de la creation des repertoires splits....") 
#time.sleep(3)   
  
## Ci dessous la fonction pour creer les fichiers split....



## Ci dessous on appel la fonction pour copier les splits .......
for j in [0,1,2]:
    scp_split("./S"+str(j)+".txt", "/tmp/kimpa-20/split", str(j))
 
## ci dessous la fonction pour creer le dossier Map dans le quel on viendra ecrire les fichiers UMx.txt
for rm in [0,1,2]:
    rep_map("mkdir -p /tmp/kimpa-20/map" , rm)
    
## Confirmation de ca creation du repertoire map, sinon le calcul s'arrete ....
if r_map == False :
    print("  ")
    print("Le repertoire map n'a pas pu etre creer .. le calcul va s'arreter ..")
    sys.exit()
print("  ")
print("Confirmation de la creation des repertoires maps....") 
#time.sleep(5) 
    
## ci dessous on appel la fonction pour copier le slave         
for k in [0,1,2]:
    scp_slave("slave.py", "/tmp/kimpa-20/map", str(k))
       
## Ci dessous on appel la fonction pour lancer le slave 
## On recupere le temps en debut ......
av_map = time.perf_counter()     
for lan in [0,1,2]: 
    runslave(str(0), lan)
    print("phase de Map terminer sur la machine :tp-4b01-1"+str(lan))
ap_map =time.perf_counter()      
print("  ")
print("MAP FINISH......")
print("  ")
print("La durée du map est : ", ap_map - av_map)


## La fonction ci dessous permet de copier le fichier machines_used.txt dans le repertoire indiqué...
for t in [0,1,2]:
    scp_mach("machines_used.txt","/tmp/kimpa-20/", str(t))
    
## La fonction ci dessous permet de creer le repertoire shuffles pour la phase du shuffles.....
for rsh in [0,1,2]:
    rep_shu("mkdir -p /tmp/kimpa-20/shuffle",rsh)
    print("Creation du repertoire sur la machine tp-4b01-1"+str(rsh))
    
## Ci dessous confirmation de la creation du repertoire shuffle ....
if r_shuffle == False : 
    print("Le repertoire shuffle n'a pas pu etre creer, le calcul va s'arreter ...")
    sys.exit()

av_shuf = time.perf_counter()      
for shan in [0,1,2]:
    runshuffle(str(1),shan)
    
ap_shuf = time.perf_counter()  
print("      ")    
print(".............SHUFFLE FINISHE ...........")
print("  ")
print("La durée du shefful est : ", ap_shuf - av_shuf )


av_rd = time.perf_counter()  
for rdu in [0,1,2]:
    runreduce(str(2),rdu)
ap_rd = time.perf_counter()  
print("     ")
print("................REDUCE FINISH............... ")
print("    ")
print("La durée du reduce est : ", ap_rd - av_rd)
print("  ")


for var in [0,1,2]:
    red_comb2("cat /tmp/kimpa-20/reduces/*",var)
    
#for var in [0,1,2]:
#    red_comb2("os.listdir(/tmp/kimpa-20/reduces/)",var)

#red_comb2()
           
