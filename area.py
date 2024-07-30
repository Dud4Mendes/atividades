def area_circulo(raio):
    return 3.14159 * raio ** 2

raio = float(input("digite o raio do circulo: "))   
print(f"a area do circulo é: {area_circulo(raio)}")


def area_quadrado(lado):
    return lado ** 2

lado = float(input("digite o comprimento do lado do quadrado:"))
print(f"a area do quadrado é: {area_quadrado(lado)}")    


def area_triangulo(base, altura):
    return 0.5 * base * altura

base = float(input("digite a base do triangulo: "))
altura = float(input("digite a altura do trangulo: "))
print(f"a area do trianulo é: {area_triangulo(base, altura)}")
