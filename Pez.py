from Mascota import Mascota

class Pez(Mascota):
    def __init__(self, nombre, raza, sonido, color):
        super().__init__(nombre, raza, sonido)
        self.color = color
    
    def getColor(self):
        return self.nombre+" es de color "+self.color
    
    def jugar(self):
        self.energia -= 10
        self.salud += 5
        return "a "+ self.nombre+ " no le gusta jugar, es un pez."

    def comer(self):
        self.energia -= 10
        self.salud += 5
        return "a "+ self.nombre+ " le gusta comer muuy lento."

    