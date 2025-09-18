class AreaCalculator:
    def __init__(self):
        self.result = 0

    def area_triangulo(self):
        print("Cálculo del área de un triángulo:")
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        self.result = 0.5 * base * altura

    def area_rectangulo(self):
        print("Cálculo del área de un rectángulo:")
        largo = float(input("Introduce la longitud del rectángulo: "))
        ancho = float(input("Introduce el ancho del rectángulo: "))
        self.result = largo * ancho

    def area_circulo(self):
        print("Cálculo del área de un círculo:")
        radio = float(input("Introduce el radio del círculo: "))
        self.result = 3.14159 * radio * radio

    def resultado(self):
        print(f"El área calculada es: {self.result}")


