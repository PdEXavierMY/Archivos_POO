# Archivos_POO
<h1 align="center">Archivos(de manera básica) en POO</h1>

En este [repositorio](https://github.com/Xavitheforce/Archivos_POO) queda resuelto el ejercicio del csv.

El código lee un csv y devuleve una lista de diccionarios(diccionario por línea) y una lista de diccionarios ordenada. A esa última lista la añade un valor más a cada diccionario(Nota Final) y finalmente devuelve dos listas con los aprobados y suspensos siguiendo los criterios establecidos en el enunciado del ejercicio.

El código empleado para resolverlo es el siguiente:

```python
import csv
#se entinde que los ordinarios son las repeteciones de los parciales(ordinario1 del 1 y ordinario2 del 2)
#en base a esta premisa tomaré los mismos porcentajes paar los parciales que para los ordinarios
#también asumimos que si se repite un exámen se toma la nota del repetido(ordinaria), aunque sea menor
class Calificaciones:
    def diccionario():
        with open("calificaciones.csv", newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            lista = []
            global parametros
            parametros = []
            n = 0
            for linea in reader:
                n+=1
                if n == 1:
                    for valor in linea:
                        parametros.append(valor)
                else:
                    dic = {}
                    for i in range(9):
                        a = linea[i].replace(",", ".")
                        dic.setdefault(parametros[i],a)
                    lista.append(dic)
        file.close()
        return lista

    def ordenardic(lista):
        global apellidos
        apellidos = []
        lista_dicordenada = []
        for elemento in lista:
            apellidos.append(str(elemento["Apellidos"]))
        apellidosordenados = sorted(apellidos)
        for nombre in apellidosordenados:
            for i in lista:
                if nombre == i["Apellidos"]:
                    lista_dicordenada.append(i)
                    break
        return lista_dicordenada

    def notafinal(lista):
        for dic in lista:
            valores = []
            for i in range(3, 9):
                valores.append(dic[parametros[i]])
            notasporcentajes = []
            Calificaciones.comprobarnumeros(valores, notasporcentajes, 0, 2)
            Calificaciones.comprobarnumeros(valores, notasporcentajes, 1, 3)
            Calificaciones.comprobarnumeros(valores, notasporcentajes, 4, 5)
            n = round((float(notasporcentajes[0])*0.3) + (float(notasporcentajes[1])*0.3) + (float(notasporcentajes[2])*0.4), 2)
            dic.setdefault("Nota Final", n)
        return lista

    def comprobarnumeros(lista1, lista2, a, b):
        if lista1[a] != "":
                if float(lista1[a]) < 5.0:
                    if lista1[b] != "":
                        lista2.append(float(lista1[b]))
                    else:
                        lista2.append(float(lista1[a]))
                else:
                    lista2.append(float(lista1[a]))
        else:
            if lista1[b] != "":
                    lista2.append(float(lista1[b]))
            else:
                lista2.append(0)
 #comprueba si los parciales tienen nota, si no miran las ordinarias y si están en blanco cogen un 0, y si no, la nota de las ordinarias
 #si los parciales tienen nota, comprueba si es >5, si lo es cogen la nota, si no buscan en la ordinaria(igual que antes)

    def apto(lista):
        aprobados = []
        suspensos = []
        for dic in lista:
            valores = []
            for i in range(3, 9):
                valores.append(dic[parametros[i]])
            notasporcentajes = []
            Calificaciones.comprobarnumeros(valores, notasporcentajes, 0, 2)
            Calificaciones.comprobarnumeros(valores, notasporcentajes, 1, 3)
            Calificaciones.comprobarnumeros(valores, notasporcentajes, 4, 5)
            if (dic["Asistencia"]>="75%" or dic["Asistencia"]=="100%") and dic["Nota Final"]>=5.0 and notasporcentajes[0]>=4.0 and notasporcentajes[1]>=4.0 and notasporcentajes[2]>=4.0:
                aprobados.append(dic["Nombre"]+" "+dic["Apellidos"])
            else:
                suspensos.append(dic["Nombre"]+" "+dic["Apellidos"])
        print("APROBADOS:\n")
        for persona in aprobados:
            print(persona)
        print("\nSUSPENSOS:\n")
        for persona in suspensos:
            print(persona)
        return aprobados, suspensos
```
Su UML es el siguiente:

<br>
<img height="250" src="UML/archivos_POO.jpg" />
<br>
