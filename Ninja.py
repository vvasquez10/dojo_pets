import Mascota

class Ninja:
    # implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
    def __init__(self, nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota 

    def caminar(self):
        print("Un ninja caminando junto a su mascota,", self.mascota.jugar())
        return self
    
    def alimentar(self):
        print("Un ninja alimentando a su mascota,", self.mascota.comer())
        return self
    
    def bañar(self):
        print("El ninja esta bañanado a "+ self.mascota.nombre +", "+ self.mascota.ruido())
        return self