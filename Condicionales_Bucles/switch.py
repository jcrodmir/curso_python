print("No existe el switch se simula con un diccionario dentro de una funcion")
def opera2(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)
    
print(opera2("multiplica",5,5)())