#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:05:18 2023

@author: pierreaudisio
"""

import os
import touch

# Répertoire où se trouvent les fichiers L1C
directory = '/mnt/NasespaceSentinel/Sentinel2/L1C/Caledonie'
folders = os.listdir(directory)

list_L1C = []

for i in folders:
    if str(2022) in i : 
        if not "zip" in i :
            a = "\n" + "/home/pierreaudisio/Sen2Cor-02.11.00-Linux64/bin/L2A_Process" + "  " + directory + "/" + str(i)
            list_L1C.append(a)

touch.touch("L1C_processing.sh")

f = open("L1C_processing.sh","w")
f.writelines(list_L1C)
f.close

##################################################################################################################################
#%%

import os
import touch

os.remove("L1C_processing.sh")
touch.touch("L1C_processing.sh")

f = open("L1C_processing.sh", "a")

path = '/home/pierreaudisio/Bureau/Mangrove/python_script/peps_download-master'
folders = os.listdir( path )


list_L1C = []
for i in folders:
    a =  "/home/pierreaudisio/Sen2Cor-02.11.00-Linux64/bin/L2A_Process" + " " + path + "/" +str(i)
    f.writelines(a + "\n")
f.close()

#open and read the file after the appending:
f = open("L1C_processing.sh", "r")
print(f.read())
