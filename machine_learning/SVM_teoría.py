'''SVM puede hacer ambos regresión y logistica, suele usarse más para clasificar.


Hard margin clasification:

Valido con datos separables linealmente
Altamente sensible a datos anómalos

Función de coste es 1 o myor es positivo, -1 o menor es falso


Función hipótesis
Los limites de decisión se optimizan hasta que el coste de error sea 1 y -1


Soft Margin Clasification:

Más flexible que Hard margin clasification
Mentendrá un equilibirio entre mantener el limite de decisión lo mas alejado posible de los datos de entrenamiento
y disminuir la sensibilidad con datos anómalos. Se controla con un parámetro "C".

Regresión polinómica:

Cuando con una linea recta no podemos separar datos positivos de negativos.
Por lo tanto se va añadiendo datos de entra y se elevan al cuadrado, cubo, ... hasta que encontremos la más
adecuada para nuestros datos.

Kernel Gaussiano
Se colocan 3 puntos de referencia (L1,L2,L3) nos permite calcular caracteristicas con disntitas maneras
f1= similitud(x,L(1)) Se coge un punto y se mide la distancia de cada uno de los puntos de referencia
f2= similitud(x,L(2))
f3= similitud(x,L(3))

htheta(f)= 00+01f1 + 02f2 + 03f3

1 si la ecuación si es >=0 y será 0 en caso contrario

'''