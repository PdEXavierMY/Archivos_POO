from introducir import solicitar_introducir_numero, solicitar_introducir_numero_extremo
from archivos import Calificaciones as C

if __name__ == "__main__":
    elección = solicitar_introducir_numero("¿Desea mostrar la lista de diccionarios del archivo csv(1), mostrar la lista de diccionarios del archivo csv con las notas finales(2), o mostrar los alumnos aprobados y suspendos(3)?(cualquier otro número para salir)")
    if elección == 1:
        bonito = solicitar_introducir_numero_extremo("¿Desea ver la lista de dic(1), o los diccionarios por línea(más limpio pero sin la lista)(2)?: (eliga", 1, 2)
        if bonito == 2:
            notas = C.diccionario()
            print("\nLa lista de diccionarios tal cuál está el archivo es la siguiente:\n")
            for elemento in notas:
                print(str(elemento)+"\n")
            notasord = C.ordenardic(notas)
            print("La lista de diccionarios ordenada por apellidos es la siguiente:\n")
            for elemento in notasord:
                print(str(elemento)+"\n")
        else:
            notas = C.diccionario()
            print("\nLa lista de diccionarios tal cuál está el archivo es la siguiente:\n")
            print(str(notas)+"\n")
            notasord = C.ordenardic(notas)
            print("La lista de diccionarios ordenada por apellidos es la siguiente:\n")
            print(str(notasord)+"\n")
    elif elección == 2:
        bonito = solicitar_introducir_numero_extremo("¿Desea ver la lista de dic(1), o los diccionarios por línea(más limpio pero sin la lista)(2)?: (eliga", 1, 2)
        if bonito == 2:
            notas = C.diccionario()
            notasord = C.ordenardic(notas)
            notasfinales = C.notafinal(notasord)
            print("\nLa lista de diccionarios con las notas finales es la siguiente:\n")
            for elemento in notasfinales:
                print(str(elemento)+"\n")
        else:
            notas = C.diccionario()
            notasord = C.ordenardic(notas)
            notasfinales = C.notafinal(notasord)
            print("\nLa lista de diccionarios con las notas finales es la siguiente:\n")
            print(str(notasfinales)+"\n")
    elif elección == 3:
        notas = C.diccionario()
        notasord = C.ordenardic(notas)
        notasfinales = C.notafinal(notasord)
        print("\nLos aprobados y suspensos siguiendo los criterios establecidos son los siguientes:\n")
        C.apto(notasfinales)
    else:
        print("Ha seleccionado la opción de salir.")