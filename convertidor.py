"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """
import temperatura
import masa
import tiempo

def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1] Convertir de celsius a fahrenheit")
        print("[2] Convertir de celsius a kelvin")
        print("[3] Convertir de fahrenheit a celsius")
        print("[4] Convertir de fahrenheit a kelvin")
        print("[5] Convertir de kelvin a celsius")
        print("[6] Convertir de kelvin a fahrenheit")
        print("[7] Convertir de kilogramos a gramos")
        print("[8] Convertir de kilogramos a toneladas")
        print("[9] Convertir de gramos a kilogramos")
        print("[10] Convertir de gramos a toneladas")
        print("[11] Convertir de toneladas a kilogramos")
        print("[12] Convertir de toneladas a gramos")
        print("[13] Convertir de segundos a minutos")
        print("[14] Convertir de segundos a horas")
        print("[15] Convertir de minutos a segundos")
        print("[16] Convertir de minutos a horas")
        print("[17] Convertir de horas a segundos")
        print("[18] Convertir de horas a minutos")
        print("[0] Salir")
        
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")

        valor_inicial = int(input("Ingrese valor inicial: "))
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                respuesta = temperatura.celsius_a_fahrenheit(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 2:
                respuesta = temperatura.celsius_a_kelvin(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 3:
                respuesta = temperatura.fahrenheit_a_celsius(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 4:
                respuesta = temperatura.fahrenheit_a_kelvin(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 5:
                respuesta = temperatura.kelvin_a_celsius(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 6:
                respuesta = temperatura.kelvin_a_fahrenheit(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 7:
                respuesta = masa.kilogramos_a_gramos(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 8:
                respuesta = masa.kilogramos_a_toneladas(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 9:
                respuesta = masa.gramos_a_kilogramos(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 10:
                respuesta = masa.gramos_a_toneladas(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 11:
                respuesta = masa.toneladas_a_kilogramos(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 12:
                respuesta = masa.toneladas_a_gramos(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 13:
                respuesta = tiempo.segundos_a_minutos(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 14:
                respuesta = tiempo.segundos_a_horas(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 15:
                respuesta = tiempo.minuto_a_segundo(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 16:
                respuesta = tiempo.minuto_a_hora(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 17:
                respuesta = tiempo.horas_a_segundos(valor_inicial)
                print("Resultado es: ", respuesta)
            elif opcion == 18:
                respuesta = tiempo.horas_a_minutos(valor_inicial)
                print("Resultado es: ", respuesta)
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()