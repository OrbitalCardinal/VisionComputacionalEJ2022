from segmentation import main as blasco
from PIAVC import main as lopezgarcia
from mainf import main as pydipati
print('1. Blasco 2007 . Detección de defectos en las cascaras de frutas con segmentación. (Segmentación basada en color)')
print('2. Lopez Garcia 2010. Detección de defectos en la superficie de las frutas con análisis de textura (Segmentación basado en textura).')
print('3. Pydipati 2006. Demo de detección de daño por enfermedad en los citricos con caracteristicas de color y texuta (Segmentación basado en color y textura).')
option = int(input('Ingrese la opción del método a aplicar: '))
if option == 1:
    path = input('Ingrese la ruta de la imagen: ')
    print('Este método utiliza un algoritmo de K-means.')
    k = input('Ingrese la cantidad de K centros: ')
    blasco(path, k)
elif option == 2:
    path = input('Ingrese la ruta de la imagen: ')
    lopezgarcia(path)
elif option == 3:
    pydipati()
else:
    print('Opción invalida')
