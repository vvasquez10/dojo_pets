from Ninja import Ninja
from Mascota import Mascota
from Pez import Pez


pet1 = Mascota("Misha", "Gato Europeo", "Miau!", ["paté de res","atún"])
pet2 = Pez("Dory", "Piraña", "Glu Glu", "dorado")

ninja1 = Ninja("Victor", "Vasquez", 1, "Mimascot", pet1)
ninja2 = Ninja("Carolina", "Rodriguez", 0, "PezFav", pet2)

ninja1.alimentar()
ninja1.caminar()
ninja1.bañar()

ninja2.alimentar()
ninja2.caminar()