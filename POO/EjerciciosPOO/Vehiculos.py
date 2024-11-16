class Vehiculo():
    def __init__(self,color,ruedas,asientos,ancho,alto):
        self.color=color
        self.ruedas=ruedas
        self.asientos=asientos
        self.alto=alto
        self.ancho=ancho
        
    def arrancar(self):
        return " Arrancamos"
    
    def acelerar(self):
        return " Aceleramos"
    
    def frenar(self):
        return " Frenamos"
    
    def girar(self):
        return " Girar"
    
    def marchaAtras(self):
        return " Estas dando marcha atras"

class Coche(Vehiculo):
    def __init__(self,color,ruedas,asientos,ancho,alto,marchas):
        super().__init__(color,ruedas,asientos,ancho,alto)
        self.marchas=marchas
        
        
    def getMarcha(self):
        return self.marchas
    
    def getDerrapar(self):
        return "Estoy Derrapando"
    
class Furgoneta(Vehiculo):
    def __init__(self,color,ruedas,asientos,ancho,alto,marchas,carga, aire):
        super().__init__(color,ruedas,asientos,ancho,alto)
        self.marchas=marchas
        self.carga=carga
        self.aire=aire
        
    def getMarcha(self):
        return self.marchas
    def getCarga(self):
        return self.carga
        
    def cargar(self):
        return "Cargamos "
    
class Moto(Vehiculo):
    def __init__(self,color,ruedas,asientos,ancho,alto,marchas,cilindrada):
        super().__init__(color,ruedas,asientos,ancho,alto)
        self.marchas=marchas
        self.cilindrada=cilindrada
        
    def getMarcha(self):
        return self.marchas

    
class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,asientos,ancho,alto):
        super().__init__(color,ruedas,asientos,ancho,alto)
      
        
    def getSaltar(self):
        return "Salto "
    
