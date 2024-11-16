def divide():
    
    try:
        op1=(float(input("Primer numero")))
        op2=(float(input("Primer numero")))
        print("Resultado" +  str(op1/op2))
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("No es correcto ningun valor") 
    except:
        print("Cualquier otro error")  
    else:
        print("Se entra dentro siempre que no haya una excepción") 
    finally:
        print("Se lanza haya o no excepcion")
        
divide()

print("Calculo Finalizado")