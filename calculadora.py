# calculadora.py — Alumno: ICO 8vo semestre
# Unidad 4, Actividad 3 — Pipeline CI/CD
def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicar(a, b):
    """Devuelve la multiplicación."""
    return a * b


def dividir(a, b):
    """Devuelve la división."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

# ERROR INTENCIONAL
resultado = sumar(1, 2)
variable_sin_usar = "Este es un error intencional para demostrar el fallo"