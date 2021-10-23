import datetime
from datetime import datetime as dt
from functools import reduce
from math import floor, sqrt
from random import randrange, uniform
from statistics import mean
from typing import Union


def mean_age(i, j, k, x, y) -> float:
    """
    Teste 1 \n
    Dada as idades I, J, K, X, Y. Faça um algoritmo para
    calcular a média das idades.
    """
    return float(mean([i, j, k, x, y]))


def average_consumption(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Teste 2 \n
    Dada a distância A e o combustível gasto B,
    faça um algoritmo para calcular o consumo médio.
    """
    return round(float(a / b), 2)


def smallest_number(a, b, c) -> Union[int, float]:
    '''
    Teste 3 \n
    Dados três números (a, b, c), faça um algoritmo
    para mostrar o menor número.
    '''
    return min([a, b, c])


def to_fahrenheit(temp_celsius: Union[int, float]) -> float:
    '''
    Teste 4 \n
    Faça um algoritmo que converta a temperatura de C para F.
    '''
    return round((temp_celsius * 9 / 5) + 32, 2)


def is_multiple(num1: Union[int, float], num2: Union[int, float]) -> bool:
    '''
    Teste 5 \n
    Faça um algoritmo para apresentar se dois números são múltiplos.
    PS: A função retornará True se "num1" for multiplo de "num2" apenas.
    PS2: Por definição matemática, 0 é multiplo de todos os reais != 0.
    '''

    # 0 não é fator de nenhum número
    return num2 != 0 and num1 % num2 == 0


def match_duration(a: str, b: str) -> datetime.timedelta:
    '''
    Teste 6 \n
    Uma partida de futebol iniciou na hora A e terminou na hora B.
    Faça um algoritmo que calcule o tempo que durou a partida.
    PS: Horário deve seguir norma ISO 8601
    '''
    _format = '%H:%M:%S'
    return dt.strptime(b, _format) - dt.strptime(a, _format)


def even_list(a: list) -> list:
    '''
    Teste 7 \n
    Dada uma lista de números A[1,2,3,...], faça um algoritmo
    que retorne uma lista somente com os números pares.
    '''
    return [num for num in a if num % 2 == 0]


def is_prime(x: int) -> bool:
    '''
    Teste 8 \n
    Faça um algoritmo que receba um número e retorne
    se o número é primo ou não.
    '''
    if x <= 0:
        return False
    _limit = floor(sqrt(x))  # Maior valor a ser checado
    for div in range(2, _limit + 1):
        if x % div == 0:
            return False
    return True


def mult_table(x: Union[int, float]) -> list:
    '''
    Teste 9 \n
    Faça um algoritmo que receba um número e retorne a tabuada desse número.
    '''
    return [round(x * mult, 2) for mult in range(1, 11)]


def factorial(x: int) -> int:
    '''
    Teste 10 \n
    Faça um algoritmo que receba um número e retorne o Fatorial desse número.
    '''
    return reduce(lambda x, y: x * y, range(1, x + 1))


def intersection(a: list[int], b: list[int]) -> list[int]:
    '''
    Teste 11 \n
    Dada duas listas de números A[1,2,3,4] e B[1,2,5,8], faça um algoritmo
    que retorne a intersecção das listas.
    '''
    return [x for x in a if x in b]


def concatenation(a: list[int], b: list[int]) -> list[int]:
    '''
    Teste 12 \n
    Dada duas listas de números A[1,2,3,4] e B[1,2,5,8], faça um algoritmo
    que retorne a concatenação das listas.
    '''
    # return a.append(b)
    return a + b


def matrix_printer(matrix: list[list[int]]) -> list:
    '''
    Teste 13 \n
    Faça um algoritmo que receba uma matriz[i,z] como parâmetro e imprima
    todos os valores dessa matriz.
    '''
    for i in range(len(matrix)):
        for z in range(len(matrix[0])):
            print(matrix[i][z], end=' ')


def is_palindrome(palavra: str) -> bool:
    '''
    Teste 14 \n
    Faça um algoritmo que recebe uma palavra e retorne se a palavra \
    é palíndromo. (Palavra que se pode ler, indiferentemente, da esquerda \
    para direita ou vice-versa. Ex: osso, Ana e etc).
    '''
    return palavra == palavra[::-1]


def _title(val: str):
    print(f"########################################\n"
          f"## {val}{' ' * (35 - len(val))}##\n"
          f"########################################")


if __name__ == "__main__":
    # Teste 1
    _title('Teste 1 - mean_age()')
    for i in range(5):
        age = [randrange(0, 100) for i in range(5)]
        print(
            f"A média de idade entre as pessoas de {', '.join(map(str, age))}"
            f" anos é {mean_age(age[0], age[1], age[2], age[3], age[4])} anos")
    print()

    # Teste 2
    _title('Teste 2 - average_consumption()')
    for i in range(5):
        km = round(uniform(10, 50), 2)
        litro = round(uniform(1, 10), 2)
        print(f"Percorrendo {km} km com {litro} L, um carro tem seu consumo"
              f" médio aferido em {average_consumption(km, litro)} km/l")
    print()

    # Teste 3
    _title('Teste 3 - smallest_number()')
    for i in range(5):
        a = randrange(-50, 50)
        b = randrange(-50, 50)
        c = randrange(-50, 50)
        print(f"O menor número dentre {a}, {b} e {c} "
              f"é {smallest_number(a, b, c)}")
    print()

    # Teste 4
    _title('Teste 4 - to_fahrenheit()')
    for i in range(5):
        celsius = round(uniform(-273.15, 1000), 2)
        print(f"{celsius} C° equivalem a {to_fahrenheit(celsius)} F°")
    print()

    # Teste 5
    _title('Teste 5 - is_multiple()')
    for i in range(5):
        a, b = randrange(0, 10), randrange(0, 5)
        if is_multiple(a, b):
            print(f"{a} é multiplo de {b}")
        else:
            print(f"{a} não é multiplo de {b}")
    print()

    # Teste 6
    _title('Teste 6 - match_duration()')
    for i in range(5):
        a = f"{randrange(16, 18)}:{randrange(0, 59)}:{randrange(0, 59)}"
        b = f"{randrange(18, 20)}:{randrange(0, 59)}:{randrange(0, 59)}"
        print(f"A partida aconteceu entre as {a} e {b},"
              f" durando {match_duration(a, b)}")
    print()

    # Teste 7
    _title('Teste 7 - even_list()')
    for i in range(5):
        num_list = [randrange(0, 100) for i in range(randrange(4, 11))]
        print(f"Os elementos pares de {num_list} são {even_list(num_list)}")
    print()

    # Teste 8
    # Testando pequenos e grandes valores
    _title('Teste 8 - is_prime()')
    for i in range(5):
        num = randrange(1, 100000000000)
        if is_prime(num):
            print(f"{num} é primo.")
        else:
            print(f"{num} não é primo.")
    for i in range(5):
        num = randrange(1, 100)
        if is_prime(num):
            print(f"{num} é primo.")
        else:
            print(f"{num} não é primo.")
    print()

    # Teste 9
    # Testando inteiros e floats
    _title('Teste 9 - mult_table()')
    for i in range(3):
        x = randrange(1, 20)
        print(f"A tabuada de {x} é {mult_table(x)}")
    for i in range(2):
        x = round(uniform(1, 20), 2)
        print(f"A tabuada de {x} é {mult_table(x)}")
    print()

    # Teste 10
    _title('Teste 10 - factorial()')
    for i in range(5):
        x = randrange(2, 10)
        print(f"{x}! = {factorial(x)}")
    print()

    # Teste 11
    _title('Teste 11 - intersection()')
    a = [1, 2, 3, 4]
    b = [1, 2, 5, 8]
    print(f"A intersecção de {a} e {b} é {intersection(a, b)}")
    print()

    # Teste 12
    _title('Teste 12 - concatenation()')
    a = [1, 2, 3, 4]
    b = [1, 2, 5, 8]
    print(f"Concatenar {a} e {b} resulta em {concatenation(a, b)}")
    print()

    # Teste 13
    _title('Teste 13 - matrix_printer()')
    for i in range(5):
        # Gerador de matriz com i, z e valores aleatórios
        # List comprehension aninhada
        i = randrange(2, 5)
        z = randrange(2, 5)
        matrix = [[randrange(0, 10) for x in range(z)] for y in range(i)]

        # Criando matriz legível
        printable_matrix = '\n'.join(
            [' '.join([str(z) for z in i]) for i in matrix])

        print(
            f"A Matriz M({i}, {z}) = \n"
            f"{printable_matrix}\n"
            f"tem os seguintes elementos: ",
            end='')
        matrix_printer(matrix)
        print(end="\n\n")
    print()

    # Teste 14
    _title('Teste 14 - is_palindrome()')
    words = ["pedro", "ovo", "anilina", "redania", "osso"]

    for word in words:
        if is_palindrome(word):
            print(f"{word} é palíndromo.")
        else:
            print(f"{word} não é palíndromo.")
    print()
