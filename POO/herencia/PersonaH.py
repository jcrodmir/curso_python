class Persona():
    
    def __init__(self,nom,ap,edad) :
        self.__nombre=nom
        self.__apellido=ap
        self.__edad=edad
    
    def getDatosPesonales(self):
        return "Nombre " + self.__nombre  + " Apellidos:" + self.__apellido + \
        " Edad " + str(self.__edad) 
    
    def habla(self):
        return "La persona llamada " + self.__nombre + " esta hablando"
    
    def caminar(self):
        return "La persona llamada " + self.__nombre + " esta caminando"


class Trabajador(Persona):
    
    def __init__(self,nom,ap,edad,empresa) :
        Persona.__init__(self,nom,ap,edad)
        self.empresa=empresa
    
    def trabaja(self):
        
        return "Estoy trabajando" 
    
    def getDatosPesonales(self):
        return super().getDatosPesonales() +  " Empresa " + self.empresa

class Estudiante(Persona):
    
    def __init__(self,nom,ap,edad,centro) :
        Persona.__init__(self,nom,ap,edad)
        self.centro=centro
    
    def estudia(self):
        
        return "Estoy estudiando" 
    
    def getDatosPesonales(self):
        return super().getDatosPesonales() +  " Centro " + self.centro


class Director(Trabajador,Estudiante):
    
    def __init__(self,nom,ap,edad,empresa,centro,bonus) :
        Trabajador.__init__(self,nom,ap,edad,empresa)
        Estudiante.__init__(self,nom,ap,edad,centro)
        self.bonus=bonus
    
    def dirige(self):
        
        return "Estoy Dirigiendo" 
    
    def getDatosPesonales(self):
        return super().getDatosPesonales() +  " Bonus " + str(self.bonus)
        
p1= Persona("A","B",13)
e1 = Estudiante("B","C",16,"Arco Iris")
d1 = Director("C","D",16,"Arco Iris","Rex",500)
print(p1.getDatosPesonales())
print(e1.getDatosPesonales())
print(d1.getDatosPesonales())
#Clases que implementa
print(Estudiante.__mro__)
#Nombre Clases que implementa
print(Estudiante.__name__)
#Metodos propios
print(Estudiante.__dict__)
#Metodos heredados
print(dir(Estudiante))
print(help(Estudiante))