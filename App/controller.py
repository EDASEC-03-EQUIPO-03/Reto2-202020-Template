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

import config as cf
from App import model
import csv
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from time import process_time 


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

def compareDirectores (Nombre_director, director):
    return  (Nombre_director == director['Nombre'] )

def iniciarcatalog():
    catalogo=model.newCatalog()
    return catalogo


def loadDirectores1():
    lst=[]
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(  cf.data_dir + "AllMoviesCastingRaw.csv", encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lst.append(elemento)
    return lst

def loadmovies(catalog):
    t1= process_time()
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(  cf.data_dir + "AllMoviesDetailsCleaned.csv", encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for pelicula in row: 
            lt.addLast(catalog["Peliculas"],pelicula)
            
            model.addProductora(catalog,pelicula)
    t2=process_time()
    
                   
    

def load_Directores_peliculas1(catalog,lista):
    t1= process_time()
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(  cf.data_dir + "AllMoviesDetailsCleaned.csv", encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        i=0
        j=0
        for pelicula in row: 
            ya=False
            while i<len(lista) and not ya:
                element=lista[i]
                ya=model.addPeliculaActor(catalog,element,pelicula)
                i+=1
            j+=1
            i=j
    t2=process_time()
      


def loadDatos(catalog):
    lista=loadDirectores1()
    loadmovies(catalog)
    load_Directores_peliculas1(catalog,lista)
    
def darDirector(catalog,nombre_director):
    director=model.darAutor(catalog,nombre_director)
    return director

def darGenero(catalog,nombre_genero):
    model.darGenero(catalog,nombre_genero)

def darProductora(catalog,nombre_productora):
    productora=model.darproductora(catalog,nombre_productora)
    return productora
# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
