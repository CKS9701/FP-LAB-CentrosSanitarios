from coordenadas import *

def test_calcular_distancia(coord1: Coordenadas, coord2: Coordenadas) -> None:
    print("Probando calcular_distancia()...")
    dist = calcular_distancia(coord1, coord2)
    print(f"La distancia es {dist}")
    print()

def test_calcular_media_coordenadas(lista: list[Coordenadas]) -> Coordenadas:
    print("Probando calcular_media_coordenadas()...")
    media = calcular_media_coordenadas(lista)
    print(f"La coordenada media es {media}")
    print()

if __name__ == '__main__':
    # test_calcular_distancia(Coordenadas(0,1), Coordenadas(1,2))
    test_calcular_media_coordenadas([Coordenadas(0,1), Coordenadas(1,2)])