#strings#

my_strings = 'mistring'

print(len(my_strings))
w=['cesar','de la cruz',35]
name, lastname, edad = w
print('mi nombre es {} {} y mi edad {}'.format(name,lastname,edad))
print('mi nombre es %s %s y mi edad es %d'%(name,lastname,edad))
# la mejor forma

print(f'mi nombre es {name} {lastname} y mi edad es {edad}')

#funciones 
variable = 'cesar'
print(variable.capitalize())# primera letra con mayuscula
print(variable.upper()) # todo con mayuscula
print(variable.lower())# todo minuscula
print(variable.count("e"))# cuantas letras "e" tiene 
print(name.isnumeric())# El método isnumeric() devuelve «Verdadero» si todos los caracteres de la string son caracteres numéricos; de lo contrario, devuelve «Falso».
print(variable.islower())#Las funciones MAYUSCULA isupper() e MINIUSCULA islower() devuelven el valor booleano True si todos los caracteres de la string están en mayúsculas o minúsculas respectivamente
print(type(edad))

print(variable.isupper())
