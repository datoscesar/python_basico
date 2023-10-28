my_dic= dict()
# si ponemos los datos {} y coma son SET}
my_other_dic = dict()

my_dic = {"nombre":"cesar","apellido":"de la cruz",
          "edad":35,1:"python"}
# se agrupan por pares de clave:valor
# ES UNA ESTRUCUTRA llave(CLAVE) -  VALOR
my_other_dic = {"nombre":"cesar","apellido":"de la cruz",
                "edad":35,"lenguaje":{"python","SQL","LINUX"}}


print(my_other_dic)
print(type(my_other_dic))

print(len(my_other_dic)) #4
print(my_other_dic["nombre"]) # recuerda que se llama los valores de las llaves con corchete


my_other_dic["apellido"]= 'tapia'# asi se actualizan las llaves con otros valores

my_other_dic["nombre"]= "pedro"
print(my_other_dic)


#AGREGAR UNA NUEVA LLAVE CON VALOR AL DICCIONARIO
my_other_dic["calle"]="dalias 2"
print(my_other_dic)
#ELIMINAAR ELEMENTOS CON DEL
del my_other_dic["calle"]
print(my_other_dic)
print("apellido" in my_other_dic) # llama solo llave valor buleano

print(my_other_dic.items()) # describe todo lo que contiene el diccionario
print(my_other_dic.keys()) # muestras las llaves
print(my_other_dic.values()) # muestras los valores
print(my_other_dic.fromkeys(("nombre","edad"))) # crea un diccionario nuevo sin valores pero si con llaves

new_dicc = dict.fromkeys(my_other_dic)


new_dicc['name'] = 'alejandro'
new_dicc['nombre'] = 'EDUARDO'
print(new_dicc) # jala las llaves de otro lado  pero sin valores
print("holamundo")



