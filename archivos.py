
import csv

def diccionarioprueba():
    with open("calificaciones.csv", newline='') as file:
        reader = csv.reader(file)
        for linea in reader:
            print(linea)
    file.close()

diccionario()