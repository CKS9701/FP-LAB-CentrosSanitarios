from coordenadas import *

# Creación de un tipo de namedtuple para los centros sanitarios
# type: CentroSanitario(str, str, Coordenadas(float, float), str, int, bool, bool)
CentroSanitario = NamedTuple('CentroSanitario',
                             [('nombre',str),
                              ('localidad',str), 
                              ('ubicacion',Coordenadas),
                              ('estado',str),
                              ('num_camas', int), 
                              ('acceso_discapacitados', bool), 
                              ('tiene_uci',bool)
                              ])

def leer_centros(fichero: str) -> list[CentroSanitario]:
    '''
    leer_centros: recibe la ruta de un fichero CSV codificado en UTF-8, 
    y devuelve una lista de tuplas de tipo CentroSanitario(str, str, 
    Coordenadas(float, float), str, int, bool, bool) conteniendo todos 
    los datos almacenados en el fichero.
    '''
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)

        centros = []
        for nombre, localidad, latitud, longitud, estado, num_camas, \
            acceso_discapacitados, tiene_uci in lector:
             # Conversión de datos
             nombre = nombre.strip()
             localidad = localidad.strip()
             ubicacion = Coordenadas(float(latitud), float(longitud))
             estado = estado.strip()
             num_camas = int(num_camas)
             acceso_discapacitados = (acceso_discapacitados.strip() == 'true')
             tiene_uci = (tiene_uci.strip() == 'true')

             centros.append(CentroSanitario(nombre, localidad, ubicacion, estado, \
                                            num_camas, acceso_discapacitados, tiene_uci))
        
        return centros
    
def calcular_total_camas_centros_accesibles(centros: list[CentroSanitario]) -> int:
    '''
    calcular_total_camas_centros_accesibles: recibe una 
    lista de tuplas de tipo CentroSanitario y produce como 
    salida un entero correspondiente al número total de 
    camas de los centros sanitarios accesibles para discapacitados.
    '''
    camas = 0
    for centro in centros:
        if centro.acceso_discapacitados:
            camas += centro.num_camas
    
    return camas

def obtener_centros_con_uci_cercanos_a(centros: list[CentroSanitario], coord: Coordenadas, dist: float) -> list[tuple[str, str, Coordenadas]]:
    '''
    obtener_centros_con_uci_cercanos_a: recibe una lista 
    de tuplas de tipo CentroSanitario; una tupla de tipo 
    Coordenadas, que representa un punto; y un float, que 
    representa un umbral de distancia. Produce como salida 
    una lista de tuplas (str, str, Coordenadas(float, float)) 
    con el nombre, del centro, la localidad y la ubicacion de 
    los centros con uci situados a una distancia de las 
    coordenadas dadas como parámetro menor o igual que el umbral dado.
    '''
    centros_cercanos = []
    for centro in centros:
        if calcular_distancia(centro.ubicacion, coord) <= dist:
            centros_cercanos.append((centro.nombre, centro.localidad, centro.ubicacion))

    return centros_cercanos