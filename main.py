from introducir import
from introducir.numero import solicitar_introducir_numero 
from archivos import Calificaciones as C

if __name__ == "__main__":
    elección = solicitar_introducir_numero("¿Desea mostrar la lista de diccionarios del archivo csv(1), mostrar la lista de diccionarios del archivo csv con las notas finales(2), o mostrar los alumnos aprobados y suspendos(3)?")
    notas = C.diccionario()
    notasord = C.ordenardic(notas)
    notasfinales = C.notafinal(notasord)
    if elección == 1:
        print("La lista de diccionarios tal cuál está el archivo es la siguiente:\n")
        print(str(notas)+"\n")
        print("La lista de diccionarios ordenada por apellidos es la siguiente:\n")
        print(notasord+"\n")
    elif elección == 2:
        print("La lista de diccionarios con las notas finales es la siguiente:\n")
        print(notasfinales+"\n")
    elif elección == 3:
        print("Los aprobados y suspensos siguiendo los criterios establecidos son los siguientes:\n")
        C.apto(notasfinales+"\n")
    else: