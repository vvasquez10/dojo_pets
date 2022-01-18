class Mascota:
    # implementa __init__( name , tipo , golosinas ):
    def __init__(self, nombre , raza ,sonido, golosinas=[]):
        self.nombre=nombre
        self.raza=raza
        self.golosinas=golosinas     
        self.sonido = sonido
        self.salud = 100
        self.energia = 100

    # implementa los siguientes métodos:
    # dormir() - incrementa la energía de la mascota en 25
    # comer() - incrementa la energía de la mascota en 5 y la salud en 10
    # jugar() - incrementa la salud de la mascota en 5
    # ruido() - imprime el sonido que produce la mascota

    def dormir(self):
        print("A", self.nombre, "le gusta dormir en el sofá del dojo.")
        self.energia += 25
        return self
    
    def comer(self):
        self.energia += 5
        self.salud += 10
        return "a "+ self.nombre + " le gusta comer mucho, sobre todo depués de una larga siesta."
    
    def jugar(self):
        self.energia -= 10
        self.salud += 5
        return "a "+ self.nombre+ " le gusta jugar con otros perros."
    
    def ruido(self):
        return self.sonido