"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import os
import csv
import datetime

from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_linear_probing as lp

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'crimes': None,
                'dateIndex': None
                }

    analyzer['crimes'] = al.new_list()
    analyzer['dateIndex'] = bst.new_map()
    
    return analyzer

# Funciones para realizar la carga

def load_data(analyzer, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    crimesfile = data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"),
                                delimiter=",")
    for crime in input_file:
        add_crime(analyzer, crime)
    return analyzer



# Funciones para agregar informacion al analizador


def add_crime(analyzer, crime):
    """
    funcion que agrega un crimen al catalogo
    """
    al.add_last(analyzer['crimes'], crime)
    update_date_index(analyzer['dateIndex'], crime)
    return analyzer


def update_date_index(map, crime):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = crime['OCCURRED_ON_DATE']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = bst.get(map, crimedate.date())
    if entry is None:
        datentry = {'lstcrimes': None,
                    'offenseIndex': None}
        
        datentry['lstcrimes'] = al.new_list()
        datentry['offenseIndex'] = lp.new_map(20, 0.7)
        bst.put(map, crimedate.date(), datentry)
    else:
        datentry = entry
    
    add_date_index(datentry, crime)
    return map


def add_date_index(datentry, crime):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstcrimes']
    al.add_last(lst, crime)
    offenseIndex = datentry['offenseIndex']
    offentry = lp.get(offenseIndex, crime['OFFENSE_CODE_GROUP'])
    if (offentry is None):
        # TODO Realice el caso en el que no se encuentre el tipo de crimen
        lp.put(offenseIndex, crime['OFFENSE_CODE_GROUP'], datentry['lstcrimes'])
    else:
        # TODO Realice el caso en el que se encuentre el tipo de crimen
        al.add_last(offentry, crime)
    return datentry


def new_data_entry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = lp.new_map(num_elements=30,
                                        load_factor=0.5)
    entry['lstcrimes'] = al.new_list()
    return entry


def new_offense_entry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = al.new_list()
    return ofentry


# ==============================
# Funciones de consulta
# ==============================


def crimes_size(analyzer):
    """
    Número de crimenes
    """
    return al.size(analyzer['crimes'])


def index_height(analyzer):
    """
    Altura del arbol
    """
    return bst.height(analyzer['dateIndex'])


def index_size(analyzer):
    """
    Numero de elementos en el indice
    """
    return analyzer['crimes']['size']


def min_key(analyzer):
    """
    Llave mas pequena
    """
    return bst.left_key(analyzer['dateIndex'])


def max_key(analyzer):
    """
    Llave mas grande
    """
    return bst.right_key(analyzer['dateIndex'])


def get_crimes_by_range(analyzer, initialDate, finalDate):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    return bst.keys(analyzer['dateIndex'], initialDate, finalDate)


def get_crimes_by_range_code(analyzer, initialDate, offensecode):
    """
    Para una fecha determinada, retorna el numero de crimenes
    de un tipo especifico.
    """
    crimedate = bst.get(analyzer['dateIndex'], initialDate)
    if crimedate == None: return 0
    
    crimes = lp.get(crimedate, offensecode)
    if crimes == None: return 0
    
    return crimes['size']
