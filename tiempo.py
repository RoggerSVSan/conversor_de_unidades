"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
def segundos_a_minutos(s):
    m = s / 60
    return m

def segundos_a_horas(s):
    h = s / 3600
    return h

def minuto_a_segundo(m):
    s = m * 60
    return s

def minuto_a_hora(m):
    h =  m / 60
    return h

def horas_a_segundos(h):
    s = h * 3600
    return s

def horas_a_minutos(h):
    m =  h * 60
    return m