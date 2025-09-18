# Ejemplo de uso
from Clases.areas import AreaCalculator
if __name__ == "__main__":
    calculator = AreaCalculator()
    while True:
        print("\nOpciones:")
        print("1. Calcular el área de un triángulo")
        print("2. Calcular el área de un rectángulo")
        print("3. Salir")
        option = input("Selecciona una opción: ")

        if option == "1":
            calculator.area_triangulo()
            calculator.resultado()
        elif option == "2":
            calculator.area_rectangulo()
            calculator.resultado()
        elif option == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")