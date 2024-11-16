#Metodo STR
import datetime
class Persona():
    
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
    
    #TOSTRING
    def __str__(self) -> str:
        return "Nombre: " + self.nombre + "\nEdad: " + str(self.edad)
    
    #Más preciso que str
    def __repr__(self) -> str:
        return "Nombre: " + self.nombre + "\nEdad: " + str(self.edad)
    
    def __len__(self):
        return len(self.nombre)

p1=Persona("Carlos",18)
print(p1)


#De esta manera no seria necesario crear variables
class PersonaKWARGS:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

# Crear una instancia:
persona = PersonaKWARGS(nombre="Juan", edad=30, ocupacion="Ingeniero", ciudad="Madrid")
print(persona.ocupacion)  # Output: Ingeniero
print(persona.ciudad)     # Output: Madrid

hoy= datetime.date.today()
print(str(hoy))
print(len(p1))
print()

