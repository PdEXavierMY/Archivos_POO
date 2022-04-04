import csv

def diccionarioprueba():
    with open("calificaciones.csv", newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for linea in reader:
            print(linea)
    file.close()

def diccionario():
    with open("calificaciones.csv", newline='') as file:
        reader = csv.reader(file, delimiter=';')
        lista = []
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
                    dic.setdefault(parametros[i],linea[i])
                lista.append(dic)
    file.close()
    return lista

def ordenardic(lista):
    apellidos = []
    for elemento in lista:
        apellidos.append(elemento["Apellidos"])
    sorted(apellidos)


l = diccionario()
print(l)
ordenardic(l)