from segmentation import main as blasco
from PIAVC import main as lopezgarcia
print('1. Blasco 2007 . Detección de defectos en las cascaras de frutas con segmentación. (Segmentación basada en color)')
print('2. Lopez Garcia 2010. Detección de defectos en la superficie de las frutas con análisis de textura (Segmentación basado en textura).')
print('3. Pydipati 2006. Demo de detección de daño por enfermedad en los citricos con caracteristicas de color y texuta (Segmentación basado en color y textura).')
option = int(input('Ingrese la opción del método a aplicar: '))
if option == 1:
    blasco('orange_blasco.png')
elif option == 2:
    lopezgarcia('orange_blasco.png')
elif option == 3:
    from mainf import main as pydipati
else:
    print('Opción invalida')
