#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:28:25 2023

@author: pierreaudisio
"""

import os
import datetime
from sentinelsat import SentinelAPI

# Fonction permettant d'écrire une date sous la forme YYYYmmdd
def numConcat(num1, num2, num3):
       
        # Convert both the numbers to
        # strings
        if (num2<10 and num3<10):
            num1 = str(num1)
            num2 = str(0)+str(num2)
            num3 = str(0)+str(num3) 
        
        elif (num3<10):
            num1 = str(num1)
            num2 = str(num2)
            num3 = str(0)+str(num3) 
            
        elif (num2<10):
            num1 = str(num1)
            num2 = str(0)+str(num2)
            num3 = str(num3) 
        
        else:
            num1 = str(num1)
            num2 = str(num2)
            num3 = str(num3) 
        
        
        # Concatenate the strings
        num1 += num2+num3
          
        return int(num1)


# Renvoie le nom de la tuile associé auc coordonnées fournis en entrée
def S2tile_fromLATLON (lat,lon):
    
    USER = "pierre_545"
    PASSWORD = "Zoomzoom05!"
    
    # query scenes
    api = SentinelAPI(USER, PASSWORD, 'https://scihub.copernicus.eu/dhus')
    
    footprint = 'POINT(%s %s)' % (lon, lat)
    
  
    product = api.query(footprint, 
                    date=('20210101', '20211201'), 
                    platformname='Sentinel-2', 
                    producttype= 'S2MSI1C', 
                    area_relation='Contains',
                    )
    # get tile
    tiles=[]
    for value in product.values():
        tile = value['tileid']
        if len(tiles)==0:
            print(tile)
            tiles.append(tile)
        aux=0
        for j in range(0,len(tiles)):
            if tile==tiles[j]:
                aux=1
        if aux==0:
            print(tile)
            tiles.append(tile)
              
    return tiles


# Définir de quelle date à quelle date nous voulons télécharger les produits
d_start = "2022-01-01"
d_end = "2023-01-01"
d_day = []

start = datetime.datetime.strptime(d_start , "%Y-%m-%d")
end = datetime.datetime.strptime(d_end , "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for i in range (len(date_generated)):
    d_day.append(numConcat(date_generated[i].year, date_generated[i].month, date_generated[i].day))
    
# Répertoire où les produits seront téléchargés
directory = '/home/pierreaudisio/Bureau/Mangrove/python_script/Sentinel-download-master2'
folders = os.listdir(directory)

# Définition du répertoire de travail, ce répertoire doit contenir le code pour le téléchargement
os.chdir(directory)

# Coordonnées des éléments d'intérêts que l'on veut télécharger
lat = [-20.32916, -21.27183, -21.80389, -20.85374, -20.59686]
long = [164.43567, 165.36655, 165.77037, 164.54991, 165.20855]


#Démarrage du téléchargement et vérification que le produit n'est pas déjà présent
for j in range (len(d_day)):
    print()
    print(d_day[j])
    print()
    for i in range (len(lat)):
        
        # Recherche du nom de la tuile selon les coordonnées fournis
        tiles = S2tile_fromLATLON(lat[i],long[i])
        
        # Recherche dans le dossier d'arrivé si le fichier est déja existant
        for fname in folders:
            if "tiles" and str(d_day[j]) in fname:
                pass
            else:
                os.system("./Sentinel_download.py --lat %s --lon %s -a apihub.txt -d %s -f %s -s S2" % (lat[i], long[i], d_day[j], d_day[j]))
    	
print(os.getcwd())


