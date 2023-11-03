my_set = set()
my_other_set = {}
print(type(my_other_set))
print(type(my_set))
my_other_set={"wanda",35,35,35,35}
print(my_other_set)
print(len(my_other_set))
#print(my_other_set[0])# esto es para llamar un elemento solo funciona en LISTA y TUPLA
my_other_set.add('cesar')
my_other_set.add("janneth") # agregar un cadena de texto
my_other_set.add(452.2) # solo se puede agregar un elemento a la vez
print(my_other_set) #un set no es una extructura ordenada

my_other_set.add('cesar')# un set no admite repetidos

print("cesar" in my_other_set) # se bota un valor buleano
my_other_set.remove("cesar")# remueve un dato
print(my_other_set)
#my_other_set.clear()  limpia todo el set
print(my_other_set)

# del(my_other_set) NameError: name 'my_other_set' is not defined



my_set={"huancayo",457.2,"shirleys"}
print(my_set)

my_new_set = my_other_set.union(my_set).union({1})
print(my_new_set)


new_set2 = set()
new_set2 ={1,'HOLA'}
print(new_set2.difference(my_new_set)) #es una operacion aritmetica de diferencia


