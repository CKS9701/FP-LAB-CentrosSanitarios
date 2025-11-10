import csv
import math 
import folium
from typing import NamedTuple

# Creación de un tipo de namedtuple para las coordenadas
# type: Coordenadas(float, float)
Coordenadas = NamedTuple('Coordenadas', [('latitud',float), ('longitud', float)])

def calcular_distancia(coord1: Coordenadas, coord2: Coordenadas) -> float:
    '''
    calcular_distancia: recibe dos coordenadas de tipo 
    Coordenadas(float, float) y devuelve un float que 
    representa la distancia euclídea entre esas dos coordenadas.
    '''
    return math.sqrt((coord1.latitud-coord2.latitud)**2 + (coord1.longitud-coord2.longitud)**2)

def calcular_media_coordenadas(lista: list[Coordenadas]) -> Coordenadas:
    '''
    calcular_media_coordenadas: recibe una lista de Coordenadas(float, float)
    y devuelve una tupla de tipo Coordenadas(float, float) cuya latitud es 
    la media de las latitudes de la lista y cuya longitud es la media de las 
    longitudes de la lista.
    '''
    x, y = (0,0)
    for latitud, longitud in lista:
        x += latitud
        y += longitud

    return Coordenadas(x/len(lista), y/len(lista))