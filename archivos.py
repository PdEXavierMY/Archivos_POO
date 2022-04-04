import csv
#se entinde que los ordinarios son las repeteciones de los parciales(ordinario1 del 1 y ordinario2 del 2)
#en base a esta premisa tomaré los mismos porcentajes paar los parciales que para los ordinarios
#también asumimos que si se repite un exámen se toma la nota del repetido(ordinaria), aunque sea menor

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
                    dic.setdefault(parametros[i],linea[i])
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
        if valores[0] != "":
            if int(valores[0]) < 5:
                if valores[2] != "":
                    notasporcentajes.append(int(valores[2]))
            else:
                notasporcentajes.append(int(valores[0]))
        else:
            if valores[2] != "":
                    notasporcentajes.append(int(valores[2]))
            else:
                notasporcentajes.append(0)
        n = notasporcentajes[0]*0,3 + notasporcentajes[1]*0,3 + notasporcentajes[2]*0,4
        dic.setdefault("Nota Final", n)