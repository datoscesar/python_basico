
#funciones
#resolver problema con ella. 
#
def my_function():
    print ("esto es una funcion")


my_function()

def suma_de_numero(x:int,y:int):
    return(x+y)

resultado2= suma_de_numero(7,8)
print(resultado2)
print(suma_de_numero(7,8))
print(suma_de_numero(78854,6767.21))


def suma_de_numero2(values1,values2):
    return values1+values2

resultado=suma_de_numero2(854,76.21)
print(resultado)


def print_name(name,lastname):
    return(f" este es mi nombre: {name} y mi apellido: {lastname}")

z=print_name("cesar","de la cruz")
print(z)


def print_name2(name,lastname,alias="coyote"):
    return(f"nombre:{name} apellido:{lastname} apodo:{alias}")

print(print_name2('janneth','quintana'))

def texts(i):
    return(i)

print(texts('ALEJNADRO'))

lista_x = list()
lista_x = [4,5,'dela']

for i in lista_x:
   print(i)

 