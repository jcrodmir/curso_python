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

class CuentaJoven(CuentaCorriente):
    
    def __init__(self, numero, titular, saldo,bonus):
        
        super().__init__(numero, titular, saldo + bonus)
        self.bonus=bonus
        
    
    def getBonus(self):
        
        return self.bonus
    
    def getDatos(self):
        return super().getDatos() +  " Bonus " + str(self.bonus)
        
cuenta= CuentaCorriente("255","Pepe",2000)
print(cuenta.getDatos())
cuenta.ingresarDinero(500)
print(cuenta.getDatos())
cuenta.retirarDinero(500)
print(cuenta.getDatos())
cuentaJoven= CuentaJoven("300","Paco",5000,500)
print(cuentaJoven.getDatos())
cuentaJoven.ingresarDinero(500)
print(cuentaJoven.getDatos())