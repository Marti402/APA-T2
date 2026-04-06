"""primos.py
Tests unitarios (doctest)
=========================

>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
>>> mcm(90, 14)
630
>>> mcd(924, 780)
12
>>> mcm(42, 60, 70, 63)
1260
>>> mcd(840, 630, 1050, 1470)
210
"""


def esPrimo(numero):
    """Devuelve True si numero es primo y False si no lo es.
    """
    if type(numero) != int or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True


def primos(numero):
    """Devuelve una tupla con los números primos menores que numero.
    """
    if type(numero) != int:
        raise TypeError("El argumento debe ser un número entero.")

    resultado = []

    for i in range(2, numero):
        if esPrimo(i):
            resultado.append(i)

    return tuple(resultado)


def descompon(numero):
    """Devuelve una tupla con la descomposición en factores primos de numero.
    """
    if type(numero) != int or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")

    factores = []
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero = numero // divisor
        divisor += 1

    return tuple(factores)


def mcm(*numeros):
    """Devuelve el mínimo común múltiplo de uno o varios números.
    """
    if len(numeros) == 0:
        raise TypeError("Debe indicarse al menos un número.")

    descomposiciones = []

    for numero in numeros:
        if type(numero) != int or numero <= 1:
            raise TypeError("Todos los argumentos deben ser naturales mayores que uno.")
        descomposiciones.append(list(descompon(numero)))

    resultado = 1
    primos_usados = []

    for factores in descomposiciones:
        for factor in factores:
            if factor not in primos_usados:
                maximo = 0
                for otra in descomposiciones:
                    veces = otra.count(factor)
                    if veces > maximo:
                        maximo = veces
                resultado *= factor ** maximo
                primos_usados.append(factor)

    return resultado


def mcd(*numeros):
    """Devuelve el máximo común divisor de uno o varios números.
    """
    if len(numeros) == 0:
        raise TypeError("Debe indicarse al menos un número.")

    for numero in numeros:
        if type(numero) != int or numero <= 1:
            raise TypeError("Todos los argumentos deben ser naturales mayores que uno.")

    comun = list(descompon(numeros[0]))

    for numero in numeros[1:]:
        factores = list(descompon(numero))
        nueva_comun = []

        for factor in comun:
            if factor in factores:
                nueva_comun.append(factor)
                factores.remove(factor)

        comun = nueva_comun

    resultado = 1
    for factor in comun:
        resultado *= factor

    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)