class CuentaCorriente():
    
    def __init__(self,numero,titular,saldo) -> None:
        self.numeroCuenta=numero
        self.titular=titular
        self.saldo=saldo
    
    def getDatos(self):
        return "Numero de Cuenta " + self.numeroCuenta  + " Titular:" + self.titular + " Saldo " + str(self.saldo)
    
    def ingresarDinero(self,dinero):
        
        self.saldo += dinero
    
    def retirarDinero(self,dinero):
        
        self.saldo -= dinero
        
cuenta= CuentaCorriente("255","Pepe",2000)
print(cuenta.getDatos())
cuenta.ingresarDinero(500)
print(cuenta.getDatos())
cuenta.retirarDinero(500)
print(cuenta.getDatos())