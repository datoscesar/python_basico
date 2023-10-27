class Coche: 
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        
    def arrancado(self):
      
       print(f'el {self.marca} {self.modelo} se ha arrancado')

    def parado(self):
        
        print(f'el {self.marca} {self.modelo} se ha parado')
      

laguna = Coche("tico","cesar23")
tesla = Coche("tesla","modelo 3")

print(type(laguna))
print(type(tesla))


laguna.arrancado()
tesla.arrancado()


laguna.parado()
tesla.parado()
