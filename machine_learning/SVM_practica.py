import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split 
from sklearn.impute import  SimpleImputer
from sklearn.svm import SVC

csv= pd.read_csv("machine_learning/dataset/Phishing.csv")

print(csv.head())


print(csv.describe())

print(csv["URL_Type_obf_Type"].value_counts())

valores_nulos= csv.isna().any()

print(valores_nulos[valores_nulos])

valores_infintos= csv.isin([np.inf,-np.inf]).any()

print(valores_infintos[valores_infintos])

malignas=csv[csv["URL_Type_obf_Type"]=="phishing"]
benignas=csv[csv["URL_Type_obf_Type"]=="benign"]
'''
plt.figure(figsize=(14,8))

plt.scatter(malignas["domainUrlRatio"],malignas["domainlength"],label="Phishing")
plt.scatter(benignas["domainUrlRatio"],benignas["domainlength"],label="Benign")
plt.xlabel("Domain Url Ratio")
plt.ylabel("Domain URL length")

plt.legend()
plt.show()'''

#Dividimos los datos coge datos diferentes cada vez que ejecutamos
#para que sean siempre los mismos  usamos random_state sea usa 42 por convección

train_set, test_set= train_test_split(csv,test_size=0.2,random_state=42)

#Division del conjunto de entrenamiento y validación(80% entrenamiento, 20% validación) del conjunto original

train_set, val_set=train_test_split(train_set,test_size=0.25,random_state=42)

#Separacion de caracteristicas x de las etiquetas y en cada conjunto de datos(entrenamiento,validacion y pruebas)

X_train=train_set.drop("URL_Type_obf_Type",axis=1)
Y_train=train_set["URL_Type_obf_Type"].copy()

X_val=val_set.drop("URL_Type_obf_Type",axis=1)
Y_val=val_set["URL_Type_obf_Type"].copy()

X_test=test_set.drop("URL_Type_obf_Type",axis=1)
Y_test=test_set["URL_Type_obf_Type"].copy()

#Preparacion de datos
# 
#Eliminacion de valores infinitos

X_train= X_train.drop("argPathRatio", axis=1)
X_val= X_val.drop("argPathRatio", axis=1)
X_test= X_test.drop("argPathRatio", axis=1)



#Eliminacion de valores nulos con SimplerInputer


imputer=SimpleImputer(strategy="median")

X_train_prep= imputer.fit_transform(X_train)
X_val_prep= imputer.fit_transform(X_val)
X_test_prep= imputer.fit_transform(X_test)

# Llevar datos a un dataframe

X_train_prep= pd.DataFrame(X_train_prep,columns=X_train.columns, index= Y_train.index)
X_val_prep= pd.DataFrame(X_val_prep,columns=X_val.columns, index= Y_val.index)
X_test_prep= pd.DataFrame(X_test_prep,columns=X_test.columns, index= Y_test.index)



X_trainreduced= X_train_prep[["domainUrlRatio","domainlength"]].copy()


#C 50 es trade off flexibilidad del limite mas valor mas preciso, menos valor mas flexible 
#
limite_decision_linal=SVC(kernel="linear",C=1000)

limite_decision_linal.fit(X_trainreduced, Y_train)


def plot_svc_decission_boundary(svm_clf, X_train_reduced, y_train, xmin, xmax):

    # Parámetros del clasificador (coeficientes y el intercepto)
    w = svm_clf.coef_[0]
    b = svm_clf.intercept_[0]

    # Crear el rango de valores de x0 para el gráfico
    x0 = np.linspace(xmin, xmax, 200)
    decision_boundary = -w[0] / w[1] * x0 - b / w[1]

    # Cálculo del margen (distancia a los vectores de soporte)
    margin = 1 / w[1]
    gutter_up = decision_boundary + margin
    gutter_down = decision_boundary - margin

    # Crear la figura
    plt.figure(figsize=(12, 6))
    
    # Gráfico de los datos de entrenamiento (phishing y benign)
    plt.plot(X_train_reduced.values[:, 0][y_train == "phishing"], 
             X_train_reduced.values[:, 1][y_train == "phishing"], "ro", label="Phishing", zorder=2)
    plt.plot(X_train_reduced.values[:, 0][y_train == "benign"], 
             X_train_reduced.values[:, 1][y_train == "benign"], "bs", label="Benign", zorder=2)

    # Gráfico de los vectores de soporte (ahora en otro color y con zorder más bajo)
    svs = svm_clf.support_vectors_
    plt.scatter(svs[:, 0], svs[:, 1], s=180, facecolors='none', edgecolors='black', zorder=1)

    # Gráfico de la línea de decisión y los márgenes (con zorder más alto para que aparezcan arriba)
    plt.plot(x0, decision_boundary, "k-", linewidth=2, zorder=3)
    plt.plot(x0, gutter_up, "k--", linewidth=2, zorder=3)
    plt.plot(x0, gutter_down, "k--", linewidth=2, zorder=3)

    # Configurar el título y límites del gráfico
    plt.title("$C={}$".format(svm_clf.C), fontsize=16)
    plt.axis([xmin, xmax, -100, 250])
    plt.legend()
    plt.show()
    plt.close()


# Llamar a la función para graficar el límite de decisión
plot_svc_decission_boundary(limite_decision_linal, X_trainreduced, Y_train, X_trainreduced["domainUrlRatio"].min(), X_trainreduced["domainUrlRatio"].max())



