
# un bucle se usa cuando se desea repetir un conjunto de instrucciones varias veces
#while hace que un codigo se repita varias veces en funcion de una condicion
#se utiliza while cuando se desea repetir las instrucciones hasta que se satisfaga el criterio
my_condicional =0
while my_condicional <10:
    
    print(my_condicional)
    my_condicional +=4
else: 
   print("el resultado es mayor que 10")


my_condicional2=0

while my_condicional2 < 20:
    
    print(my_condicional2)
    print("eljuego continua =)")
    my_condicional2 +=5
        
    if my_condicional2==16:
      print(my_condicional2)
      print("se detiene es igual a 15")
      break


#for cumplir una condicion. Ejecuta los elementos. iterar
#un for se va ejecutar cuanto elementos tengamos y llamando a cada elemento
#atado un nuemro finito de elementos
my_list= list()
my_tuple = tuple()
my_other_set =set()
my_other_dic = dict()

my_list = ['A',1]#guardan elementos 1 en 1 en forma ordenada
my_tuple=(35,1.65)#guardan elementos pero no se alteran
my_other_set={'cesar'}#guardan elementos pero no se pueden repetir
my_other_dic = {"nombre":"cesar",'apellido':'tapia'}# elementos clave valor
                
for i in my_list:
   print(i)

for i in my_tuple:
   print(i)

for i in my_other_set:
   print(i)

for i in my_other_dic:
   print(i)

for i in my_other_dic.values():
   print(i)


for i in my_list:
   print(i)
   if i =='A':
      print('estas bien')
      break
     
   


# bucle for es la opcion mas sencilla cuando se sabe cuantas veces se tiene que repetir el bucle
# i es el indice(varible) que es un numero que cambia en cada paso a traves del bucle
# despues de la linea de identificacion viene el grupo de comandos  
#range es una funcion range(0,5) = [0,1,2,3,4]
#range(0,5,2) =[0,2,4]

for i in range(0,10,2):
   print(i**2)
else:
   print('el bucle a finalizado')
# la estructura del bucle for permite recorrer cada microespacio en la memoria generado por un string

frase='python'
for i in frase:
   print(i)
else: 
   print('finalizado')