"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
assert config
from time import process_time 


"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def comparePeliculas (nombre_pelicula, pelicula):
    if (nombre_pelicula == pelicula['original_title'] ):
        return 0
    else:
        return 1
def compareDirectactores (nombre, director):
    if (nombre == director['Nombre'] ):
        return 0
    else:
        return 1
    
def compareDirectores(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    Directorentry = me.getKey(director)
    if (keyname == Directorentry):
        return 0
    elif (keyname > Directorentry):
        return 1
    else:
        return -1
def compareActores(keyname, actor):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    actorentry = me.getKey(actor)
    if (keyname == actorentry):
        return 0
    elif (keyname > actorentry):
        return 1
    else:
        return -1
def compareProductoras(keyname, Productora):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    Productoraentry = me.getKey(Productora)
    if (keyname == Productoraentry):
        return 0
    elif (keyname > Productoraentry):
        return 1
    else:
        return -1
            
def compareGeners(keyname, genero):
    
    Generoentry = me.getKey(genero)
    if (keyname == Generoentry):
        return 0
    elif (keyname > Generoentry):
        return 1
    else:
        return -1
def comparePaises(keyname, pais):
    
    paisentry = me.getKey(pais)
    if (keyname == paisentry):
        return 0
    elif (keyname > paisentry):
        return 1
    else:
        return -1

def newCatalog():
   
    catalog = {'Peliculas': None,
               'Directores': None,
               'Generos': None,
               "Productoras":None}

    catalog['Peliculas'] = lt.newList('ARRAY_LIST', cmpfunction=comparePeliculas)
    catalog['Directores'] =  mp.newMap(42967,
                                   maptype='CHAINING',
                                   loadfactor=2,
                                   comparefunction=compareDirectores)
    catalog['Productoras'] =  mp.newMap(17999,
                                   maptype='CHAINING',
                                   loadfactor=2,
                                   comparefunction=compareProductoras)

    catalog['Generos'] = mp.newMap(21,
                                   maptype='CHAINING',
                                   loadfactor=2,
                                   comparefunction=compareGeners)
    catalog['Paises'] = mp.newMap(119,
                                   maptype='CHAINING',
                                   loadfactor=2,
                                   comparefunction=comparePaises)
    
    catalog['Actores'] = mp.newMap(45777,
                                   maptype='CHAINING',
                                   loadfactor=2,
                                   comparefunction=compareActores)


    return catalog

def nuevo_director(nombre):
    
    director = {'Nombre': "", "Peliculas": None,  "Vote_average": 0,"Info_casting":0 }
    director['Nombre'] = nombre
    director['Peliculas'] = lt.newList('ARRAY_LIST')
    director["Info_casting"]=lt.newList('ARRAY_LIST')

    return director

def nueva_productora(nombre_productora):

    Productora={'Nombre': "", "Peliculas": None,  "Vote_average": 0}
    Productora["Nombre"]=nombre_productora
    Productora["Peliculas"]= lt.newList("ARRAY_LIST")
    return Productora

def nuevo_pais(nombre_pais):

    pais={'Nombre': "", "Peliculas": None,  "Vote_average": 0}
    pais["Nombre"]=nombre_pais
    pais["Peliculas"]= lt.newList("ARRAY_LIST")
    pais["Directores"]= []
    return pais

def nuevo_genero(nombre_genero):
    
    genero = {'Nombre_genero': "", "Peliculas_genero": None, "Vote_average": 0}
    genero["Nombre_genero"]= nombre_genero
    genero["Peliculas_genero"]=lt.newList("ARRAY_LIST")
    return genero 

def nuevo_Actor(nombre):
    
    Actor = {'Nombre': "", "Peliculas_genero": None, "Vote_average": 0, "Directores": None}
    Actor["Nombre"]= nombre
    Actor["Peliculas"]=lt.newList("ARRAY_LIST")
    Actor["Directores"]=lt.newList("ARRAY_LIST",cmpfunction=compareDirectactores)
    return Actor 

def nuevo_director_actor(nombre_director):
    director = {'Nombre': "", "Cantidad":0}
    director["Nombre"]=nombre_director
    return director


def addPeliculaDirector(catalog, director_lista, pelicula ):
    ya=False
    nombre_director=director_lista["director_name"]
    id1=director_lista["id"]
    id2=pelicula["\ufeffid"]
    
    if id1==id2:
        Directores = catalog['Directores']
        existe_director = mp.contains(Directores,nombre_director)
        if existe_director:
            entry = mp.get(Directores,nombre_director)
            director= me.getValue(entry)
        else:
            director = nuevo_director(nombre_director)
            mp.put(Directores,nombre_director,director)   

        lt.addLast(director['Peliculas'], pelicula)
        
        lt.addLast(director["Info_casting"],director_lista)
        directorav = director['Vote_average']
        pelicualav = pelicula['vote_average']

        if (directorav == 0.0):
            director['Vote_average'] = float(pelicualav)
        else:
            director['Vote_average'] = (directorav + float(pelicualav)) / 2
        ya=True 
    return ya 
def addPeliculaPais(catalog, director_lista, pelicula ):
    
    nombre_director=director_lista["director_name"]
    id1=director_lista["id"]
    id2=pelicula["\ufeffid"]
    Pais=pelicula["production_countries"]
    if id1==id2:
        Paises = catalog['Paises']
        existe_pais= mp.contains(Paises,Pais)
        if existe_pais:
            entry = mp.get(Paises,Pais)
            paises= me.getValue(entry)
        else:
            paises = nuevo_pais(Pais)
            mp.put(Paises,Pais,paises)   

        lt.addLast(paises['Peliculas'], pelicula)
        paises['Directores'].append(nombre_director)
        paisrav = paises['Vote_average']
        pelicualav = pelicula['vote_average']
        if (paisrav  == 0.0):
            paises['Vote_average'] = float(pelicualav)
        else:
            paises['Vote_average'] = (paisrav  + float(pelicualav)) / 2
        
    return


def addPeliculaActor(catalog, director_lista, pelicula ):
    
    nombre_director=director_lista["director_name"]
    id1=director_lista["id"]
    id2=pelicula["\ufeffid"]
    
    if id1==id2:
        for i in range (1,6):
            actor=director_lista["actor"+str(i)+"_name"]
            Actores = catalog['Actores']
            existe_Actor= mp.contains(Actores,actor)

            if existe_Actor:
                entry = mp.get(Actores,actor)
                actoris= me.getValue(entry)
            else:
                actoris = nuevo_Actor(actor)
                mp.put(Actores,actor,actoris)   

            lt.addLast(actoris['Peliculas'], pelicula)
            directores=actoris["Directores"]
            esta_director= lt.isPresent(directores,nombre_director)
            if esta_director > 0:
                dire=lt.getElement(directores,esta_director)
                dire["Cantidad"]+=1
            else:
                dire=nuevo_director_actor(nombre_director)
                lt.addLast(actoris["Directores"],dire)
                dire["Cantidad"]+=1
            actorav = actoris['Vote_average']
            pelicualav = pelicula['vote_average']
            if (actorav  == 0.0):
                actoris['Vote_average'] = float(pelicualav)
            else:
                actoris['Vote_average'] = (actorav  + float(pelicualav)) / 2
        
     



def addProductora(catalog, pelicula ):
    
    Productora=pelicula["production_companies"]
    productoracatalog=catalog["Productoras"]
    existe_productora= mp.contains(productoracatalog,Productora)
    if existe_productora:
        entry= mp.get(productoracatalog,Productora)
        productoraes= me.getValue(entry)
    else:
        productoraes= nueva_productora(Productora)
        mp.put(productoracatalog,Productora,productoraes)

    lt.addLast(productoraes["Peliculas"],pelicula)
    Productoraav= productoraes["Vote_average"]
    pelicualav = pelicula['vote_average']
    if (Productoraav == 0):
        productoraes["Vote_average"]= float(pelicualav)
    else:
        productoraes["Vote_average"]= (Productoraav+float(pelicualav)) / 2


def addGenero(catalog,pelicula):
    generos=pelicula["genres"]
    generos_lista=generos.split("|")
    for genero in generos_lista:
        generoscat=catalog["Generos"]
        existe_genero= mp.contains(generoscat,genero)
        if existe_genero:
            entry= mp.get(generoscat,genero)
            generoes= me.getValue(entry)
        else:
            generoes= nuevo_genero(genero)
            mp.put(generoscat,genero,generoes)
        lt.addLast(generoes["Peliculas_genero"],pelicula)
        generoav= generoes["Vote_average"]
        pelicualav = pelicula['vote_average']
        if (generoav == 0):
            generoes["Vote_average"]= float(pelicualav)
        else:
            generoes["Vote_average"]= (generoav+float(pelicualav)) / 2
                


def darAutor(catalog,nombre_director):
    
    directores=catalog["Directores"]
    entry= mp.get(directores,nombre_director)
    if entry:
        return me.getValue(entry)
    else:
        return 1

def darGenero(catalog,nombre_genero):
    t1=process_time()
    entry= mp.get(catalog["Generos"],nombre_genero)
    genero=None
    if entry:
        genero= me.getValue(entry)
        t2=process_time()
    return genero

def darproductora(catalog,nombre_productora):

    
    entry= mp.get(catalog["Productoras"],nombre_productora)
    if entry:
        return me.getValue(entry)
    else:
        return 1
def darpais(catalog,nombre_pais):
    
    entry= mp.get(catalog["Paises"],nombre_pais)
    
    if entry:
        return me.getValue(entry)
    else:
        return 1

def darActor(catalog,nombre):
    entry= mp.get(catalog["Actores"],nombre)
    actor=None
    if entry:
        actor=me.getValue(entry)
        directores=actor["Directores"]
        mayor=0
        mejor=None
        iterador=it.newIterator(directores)
        while it.hasNext(iterador):
            element= it.next(iterador)
            if element["Cantidad"]>= mayor:
                mayor=element["Cantidad"]
                mejor=element["Nombre"]

        return actor,mejor
    else:
        return 1

def buscar_actor(nombre,catalog):
    Actor={"Peliculas": lt.newList("ARRAY_LIST"),"Directores": lt.newList("ARRAY_LIST",cmpfunction=compareDirectactores)}
    peliculas=catalog["Peliculas"]
    Directores=catalog["Directores"]
    LLaves=mp.keySet(Directores)
    Iterador=it.newIterator(peliculas)
    while it.hasNext(Iterador):
        pelicula=it.next(Iterador)
        id_pelicula=pelicula["id"]
        Iterador2=it.newIterator(LLaves)
        es_pelicula=False
        while it.hasNext(Iterador2) and not es_pelicula:
            Director=it.next(Iterador2)
            entry= mp.get(Directores,Director)
            director_info=me.getValue(entry)
            director_info_casting=director_info["Info_casting"]
            Iterador3=it.newIterator(director_info_casting)
            
            while it.hasNext(Iterador3) and not es_pelicula:
                Info=it.next(Iterador3) 
                id_casting=Info["id"]
                if id_pelicula==id_casting:
                    encontro=False 
                    i=1
                    while i<=5 and not encontro:
                        actor=Info["actor"+str(i)+"_name"]
                        if actor==nombre:
                            encontro=True
                            lt.addLast(Actor["Peliculas"],pelicula)
                            esta_director= lt.isPresent(Actor["Directores"],Director)
                            if esta_director > 0:
                                dire=lt.getElement(Actor["Directores"],esta_director)
                                dire["Cantidad"]+=1
                            else:
                                dire=nuevo_director_actor(Director)
                                lt.addLast(Actor["Directores"],dire)
                                dire["Cantidad"]+=1
                            encontro=True
                        i+=1
                    es_pelicula=True
    return Actor






   

# Funciones para agregar informacion al catalogo

# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================


