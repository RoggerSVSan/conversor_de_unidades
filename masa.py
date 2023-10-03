"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
def kilogramos_a_gramos(kg):
    gr = kg * 1000
    return gr

def kilogramos_a_toneladas(kg):
    t = kg / 1000
    return t

def gramos_a_kilogramos(gr):
    kg = gr / 1000
    return kg

def gramos_a_toneladas(gr):
    t = gr / 1000000
    return t

def toneladas_a_kilogramos(t):
    kg = t * 1000
    return kg

def toneladas_a_gramos(t):
    g = t * 1000000
    return g