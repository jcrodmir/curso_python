class Persona():
    #atributos clase
    especie="Mamiferos"
    #atributos instancia solo necesarios si no hay constructor
    __nombre=""
    __apellido=""
    __edad=0
    __genero="Sin definir"
    
    def __init__(self,nom,ap,edad,genero):
        self.__nombre=nom
        self.__apellido=ap
        self.__edad=edad
        self.__genero=genero
    
    def habla(self):
        return "La persona llamada " + self.__nombre + " esta hablando"
    
    def caminar(self):
        return "La persona llamada " + self.__nombre + " esta caminando"
    
    def propiedades(self):
        return "Nombre " + self.__nombre  + " Apellidos:" + self.__apellido + \
        " Edad " + str(self.__edad) + " Genero: " + self.__genero
    
    def setEdad(self,edad):
        self.__edad=edad    
        
p1 = Persona("Carlos","Rodríguez",34,"Masculino")

print(p1.propiedades())
p1.setEdad(15)
print(p1.propiedades())
print("Las personas son " + p1.especie)
print("Las personas son " + Persona.especie)
    
    