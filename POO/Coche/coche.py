class Coche:
    ruedas=4
    largo=260
    ancho=120
    arrancado= False
    
    def arrancar(self):
        self.arrancado=True
    
    def estadoCoche(self):
        return "Coche esta Arrancado " if self.arrancado else "Coche esta Frenado"

mazda= Coche()
renault= Coche()   
print(mazda.ancho)
print(renault.estadoCoche())
renault.arrancar()
print(renault.estadoCoche())