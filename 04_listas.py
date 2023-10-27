
# el len es para contar los elementos de una lista
# count es para contar un elemento especial
my_first_list=list()
my_first_list = ['cesar',35,1.65,23221,23202,78]
print(my_first_list)
print(len(my_first_list))
print(my_first_list.count(35))
print(type(my_first_list))

my_new_list=list()
my_new_list =[24,24,24]
print(my_new_list.count(24))
# llamar elementos

print(my_first_list[0])
print(my_first_list[1])
print(my_first_list[2])
print(my_first_list[-2])

name,edad,altura,dinero,decimales,other = my_first_list

print(altura) #1.65



#lista es para agregar elementos

my_list = list()
my_other_list = list()

my_list = ['A',1,2,3]

my_other_list = ['cesar', 24, 1.65]
print(len(my_list))
print(my_list)
my_list.append("cama") # agregar mas elementos
my_list.insert(0,"alejandro") #agreagar un dato con ubicacion 
my_list.remove('cama') # remover
print(my_list.pop(0)) # para eliminar un elemento con una posicion 
print(my_list)

my_other_list.append("janneth")# agrega en cualqueir sitio
my_other_list.insert(0,"perrito")
print(my_other_list.pop(0))

my_other_list.insert(0,'cesar')

print(my_other_list)














del my_other_list[3]# ELIMINA CON NUMERO DE UBICACION

print(my_other_list)
y = my_list.copy() # copiar datos
print(y)
y.reverse() # cambiar orden
print(y)
y.pop(3)
y.sort() # ordenar de menor  mayor
print(y)
y.insert(3,'A')
print(y)
y[0]=2#agrega defrente 
print(y)
print(my_list+my_other_list) # concatenado

z = my_list + my_other_list

print(z)
print(z.index('cesar'))
