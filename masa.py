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

if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de masa:")
    print("20kg a gramos:", kilogramos_a_gramos(20))
    print("10kg a toneladas:", kilogramos_a_toneladas(10))
    print("4500gr a kilogramos:", gramos_a_kilogramos(4500))
    print("3000000gr a toneladas:", gramos_a_toneladas(3000000))
    print("2t a kilogramos:", toneladas_a_kilogramos(2))
    print("1t a gramos:", toneladas_a_gramos(1))
