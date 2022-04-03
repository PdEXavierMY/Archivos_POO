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
                for i in range(9):
                    lista.append({parametros[i]:linea[i]})
        print(lista)
    file.close()

diccionarioprueba()
diccionario()