from centros import *

def test_leer_centros(fichero: str) -> list[CentroSanitario]:
    print("Probando leer_centros()...")
    centros = leer_centros(fichero)
    print(f"Los primeros 3 centros son {centros[:3]}")
    print()

def test_calcular_total_camas_centros_accesibles(centros: list[CentroSanitario]) -> None:
    print("Probando calcular_total_camas_centros_accesibles()...")
    camas = calcular_total_camas_centros_accesibles(centros)
    print(f"El numero de camas es {camas}")
    print()

def test_obtener_centros_con_uci_cercanos_a(centros: list[CentroSanitario], coord: Coordenadas, dist: float) -> None:
    print("Probando obtener_centros_con_uci_cercanos_a()...")
    centros_cercanos = obtener_centros_con_uci_cercanos_a(centros, coord, dist)
    print(f"Se tienen {len(centros_cercanos)} centros cercanos")
    print(f"Los tres primeros son {centros_cercanos[:3]}")
    print()


if __name__ == '__main__':
    # centros = test_leer_centros('data/centrosSanitarios.csv')
    centros = leer_centros('data/centrosSanitarios.csv')
    # test_calcular_total_camas_centros_accesibles(centros)
    test_obtener_centros_con_uci_cercanos_a(centros, Coordenadas(36.135051666002795,-5.843455923196172), 0.1)