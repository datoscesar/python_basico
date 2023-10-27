#tuples##

my_tuple=tuple()

my_other_tuple=tuple()
my_tuple=(35,1.65,"cesar","de la cruz",'cesar')
my_other_tuple=(45822.2,875)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])

print(len(my_tuple))#5

print(my_tuple.count("cesar")) #cuenta cuantas veces se repite
print(my_tuple.index("cesar")) #valor de ubiacion del valor pedido

# la tuplas no se pueden modificar

my_sum_tuples = my_tuple + my_other_tuple
print(my_sum_tuples)
print(my_sum_tuples[5])
print(len(my_sum_tuples))
# my_tuple.insert(0,"cesar")  ESTO ES UN ERROR
print(my_tuple.count(35))


