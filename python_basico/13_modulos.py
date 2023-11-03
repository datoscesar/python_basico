# codigo algun lado, externo yq ueremos usarlo usamos MODULO
# ES PARA USAR LIBRERIAS DE MODULOS

import module
module.sumar(1,2)
module.resta(5,8)

from module import sumar,resta
sumar(87,100)
resta(87,100)
#importa una funcion especificada
from modulo_2 import multiplicacion,impresion
multiplicacion(8,10)
impresion(8,10)

# tenemos modulos de python
# el modulo haga trabajos concretos

import math

print(math.pi)
print(math.pow(2,3))

from math import pi
print(pi)
