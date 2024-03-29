"""
Módulo que agrupa todas las funcionalidades
que permiten solicitar introducir un dato cuya respuesta es VERDADERO/SÍ o FALSO/NO
"""

SI = ("s", "sí", "si", "y", "yes")
VERDADERO = ("v", "verdadero", "t", "true")


def solicitar_introducir_si_o_no(invite):
    """Por defecto, toda respuesta no incluida vale NO"""
    try:
        return input(invite).lower() in SI
    except:
        return False

def solicitar_introducir_verdadero_o_falso(invite):
    """Por defecto, toda respuesta no incluida vale FALSO"""
    try:
        return input(invite).lower() in VERDADERO
    except:
        return False