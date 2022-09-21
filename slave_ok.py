#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:29:41 2021

@author: kimpapaulin
"""

import sys
import hashlib
import socket
import subprocess
import time
import os 



## Ce slave lancera les differents phases, le map en suite le shefful, et en fin le reduise ...
## Ainsi en fonction du mode, un des trois fonctions serons lancer ....


mode = sys.argv[1]

if len(sys.argv) > 2 :
    doc = sys.argv[2]

    
# def mapper(mode, doc):
#    df1 = open("/tmp/kimpa-20/split/"+ doc,'r')
#    lines = df1.readlines()
#    print("je continue")
#    print("voici lines : @@@@@@@@@", lines)
#    for i in lines:
#        line = i.lstrip()
#        w = line.split()
#        print(" voici w &&&&&&&&&&&&&&&&&", w)
#    for j in w:
#        m = doc.split(".")[0]
#        n = m.split("S")[1]
#        print(n)
#        fichier = open("/tmp/kimpa-20/map/UM"+str(n)+".txt",'a')
#        fichier.write('%s %s\n' % (j,1))
#        fichier.close()  
       
#    return




def mapper(mode, doc):
   df1 = open("/tmp/kimpa-20/split/"+ doc,'r')
   lines = df1.readlines()
   for i in lines:
       line = i.lstrip()
       w = line.split()
       for j in w:
           n= doc.split(".")[0].split("S")[1]
           fichier = open("/tmp/kimpa-20/map/UM"+str(n)+".txt",'a')
           fichier.write('%s %s\n' % (j,1))
           fichier.close()  
   print("le contenu du map est : .........")
   t_fichier = open("/tmp/kimpa-20/map/"+"UM"+str(n)+".txt",'r')
   t_lines = t_fichier.readlines()
   print(t_lines)

       
def shuffle(mode, doc):
    df2 = open("/tmp/kimpa-20/map/"+doc, 'r')
    #df2 = open("un1.txt",'r')
    lines = df2.readlines()
    mach = socket.gethostname()
    print(lines)
    for i in lines:
        w=i.split()[0] ## Ici on selectionne la ligne 'i' et on retire les espaces potentiels ...
        h=str(int.from_bytes(hashlib.sha256(w.encode('utf-8')).digest()[:4],'little'))
        fichier = open("/tmp/kimpa-20/shuffle/"+h+"-"+str(mach)+".txt" ,'a')
        #fichier = open("UN"+h+str(mach)+".txt", 'a')
        fichier.write('%s %s\n' %(w,1))
        #fichier.write(line)
        fichier.close()
    #print("le contenu du sheffle est : ssssssss.........")
    #t_fichier = open("/tmp/kimpa-20/map/"+"UM0.txt",'r')
    #t_lines = t_fichier.readlines()
   # print(t_lines)
        
        
if mode == str(0):
    mapper(mode, doc)
    

## La fonction ci dessous permettra de creer les repertoires shufflesreceived et y copier les fichiers correspondant ...

## On commence par creer les repertoires shufflesreceived ....

r_sh_re = True ## Cette variable permet de confirmer ou pas si le repertoire a été creer ou pas ....
def rep_shu_rec(command, rsh_r):
    listproc = []
    timer=5
    login="kimpa-20"
    machine = "tp-4b01-1"+str(rsh_r)
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
          print("le repertoire {} a été creer  avec succès sur le serveur {}".format(command.split()[-1],"kimpa-20@tp-4b01-1"+str(rsh_r)))
          
    else : 
          r_sh_re = False
          print(str(i)+" err:'{}'".format(err))
    print(" ")
   # print("attente 3 secondes avant creation du repertoire sur la machine suivante...")
    #time.sleep(3)
    #print("  ") 
 
    
 
## La fonction ci dessous permet de creer le repertoire shufflesreceived pour y copier les h_nam.txt.....
# for rsh_r in [0,1,2]:
#     rep_shu_rec("mkdir -p /tmp/kimpa-20/shufflesreceived",rsh_r)
#     print("Creation du repertoire sur la machine tp-4b01-1"+str(rsh_r))
    
## Ci dessous confirmation de la creation du repertoire shufflesreceived ....
# if r_sh_re == False : 
#     print("Le repertoire shufflesreceived n'a pas pu etre creer, le calcul va s'arreter ...")
#     sys.exit()
    

## Creation des sous repertoires pour la reception des shuffles avants de les envoyés dans le dossier shufflesreceived.......

# r_sh_mach = True ## Cette variable permet de confirmer ou pas si le repertoire a été creer ou pas ....
# def rep_shu_mach(command, rsh_s):
#     listproc = []
#     timer=5
#     login="kimpa-20"
#     machine = "tp-4b01-1"+str(rsh_s)
#     proc = subprocess.Popen(["ssh",login+"@"+machine ,command],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
#     listproc.append(proc)
#     i=0
#     try:
#          out, err = listproc[i].communicate(timeout=timer)
#     except subprocess.TimeoutExpired:
#             listproc[i].kill()
#             print(str(i)+" timeout")
    
#     code = listproc[i].returncode
#     if code == 0 : 
#           print("le repertoire {} a été creer  avec succès sur le serveur {}".format(command.split()[-1],"kimpa-20@tp-4b01-1"+str(rsh_s)))
          
#     else : 
#           print(str(i)+" err: '{}'".format(err))
#           r_shuffle = False
#     print(" ")
#     print("attente 3 secondes avant creation du repertoire sur la machine suivante...")
#     time.sleep(3)
#     print("  ") 

# for rsh_s in [0,1,2]:
#     rep_shu_mach("mkdir -p /tmp/kimpa-20/shuffle/tb-4b01-10-"+str(rsh_s),rsh_s)

# for rsh_s in [0,1,2]:
#     rep_shu_mach("mkdir -p /tmp/kimpa-20/shuffle/tb-4b01-11-"+str(rsh_s),rsh_s)
    
# for rsh_s in [0,1,2]:
#     rep_shu_mach("mkdir -p /tmp/kimpa-20/shuffle/tb-4b01-12-"+str(rsh_s),rsh_s)

  

## La fonction ci dessous permet de copier les differents fichier issu du shuffle dans les machines correspondantes .....


def scp_h_f(distantPath):
    
    chemin = "/tmp/kimpa-20/shuffle"
    liste_fichier = os.listdir(chemin)
    j=0

    for i in liste_fichier :
        new_h = int(i.split("-tp")[0])
        nu_mach = new_h%3
        machine = "tp-4b01-1"+str(nu_mach)
        login="kimpa-20"
        listproc = []
        timer=200
        proc = subprocess.Popen(["scp",chemin+"/"+i,login+"@"+machine +":" +distantPath],stdin=subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        listproc.append(proc)
        
        out, err = listproc[j].communicate(timeout=timer)
        
       
        #try:
           #out, err = listproc[j].communicate(timeout=timer)
        #except subprocess.TimeoutExpired:
            #listproc[j].kill()
            #print(str(j)+" timeout")
        code = listproc[j].returncode
        
        if code !=0: 
            print("le est : {}".format(err))
              #print("le fichier {} n'a pas pu etre copier dans le repertoire {} de la machine {}".format(i,"/tmp/kimpa-20/shufflesreceived", machine))


if mode==str(1):
    
    shuffle(mode,doc)
    
    for rsh_r in [0,1,2]:
        rep_shu_rec("mkdir -p /tmp/kimpa-20/shufflesreceived",rsh_r)
        print("Creation du repertoire shufflesrec sur la machine tp-4b01-1"+str(rsh_r))
        
    # if r_sh_re == False : 
    #     print("Le repertoire shufflesreceived n'a pas pu etre creer, le calcul va s'arreter ...")
    #     sys.exit()

    scp_h_f("/tmp/kimpa-20/shufflesreceived")
    
## Ci dessous autre idées pour faciliter les échanges entre les repertoires shuffle....
## Pour chaque fichier shuffle le copier dans un sous repertoire correspodant au numero de la machine où il sera envoyés ....  


## La fonctio ci dessous permet de creer un repertoire reduce dans chacune des machines ....

r_red = True ## Cette variable permet de confirmer ou pas si le repertoire a été creer ou pas ....
def rep_red(command, rrd):
    listproc = []
    timer=200
    login="kimpa-20"
    machine = "tp-4b01-1"+str(rrd)
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
          print("le repertoire {} a ete creer  avec succes sur le serveur {}".format(command.split()[-1],"kimpa-20@tp-4b01-1"+str(rrd)))
          
    else : 
          r_red = False
          print(str(i)+" err: '{}'".format(err))
    print(" ")
    
## Cette fonction calcul la phse du reduce .....

def reduce(mode):
    chemin = "/tmp/kimpa-20/shufflesreceived"
    liste_fichier = os.listdir(chemin)
    dic_h = {}
    count = 0
    for fichier in liste_fichier:
        h_fichier = str(fichier.split("-tp")[0])
        if h_fichier not in dic_h: 
            dic_h[h_fichier] = count
           
    for fichier in liste_fichier:
        h_fichier = str(fichier.split("-tp")[0]) 
        df1 = open("/tmp/kimpa-20/shufflesreceived/"+fichier, "r")
        lines = df1.readlines()
        for line in lines :
            line = line.lstrip()
            word =line.split()[0]
            dic_h[h_fichier] +=1
            file = open("/tmp/kimpa-20/reduces/"+h_fichier+".txt","w")
            file.write('%s %s\n' % (word,dic_h[h_fichier]))
            file.close()
    return

## La fonction ci dessous permet de combiner tous les fichiers reduces obtenues ...

if mode ==str(2):
    for rrd in [0,1,2]:
        rep_red ("mkdir -p /tmp/kimpa-20/reduces",rrd)
        print("le repertoire reduces a été creer ")
        
    reduce(mode)
    

        

