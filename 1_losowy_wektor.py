# Adrian Startek, 110956
# Temat 1. Losowy wektor
# Kod dostępny również na GitHub: https://github.com/adriancodeimperium/DM110956

# Nie wyspecyfikowano typu danych, zakresu i rozkładu.
# Przyjmuję domyślnie typ float, rozkład jednostajny i zakres [0, 100]

import random
from collections import namedtuple
from typing import List

Bounds = namedtuple('Bounds', ['lower', 'upper'])
DEFAULT_BOUNDS: Bounds = Bounds(lower=0, upper=100)


def random_vector_of_length_n(n: int, bounds: Bounds = DEFAULT_BOUNDS) -> List[float]:
    """
    Tworzy wektor (listę) o długości n zawierający liczby zmiennoprzecinkowe
    z zakresu określonego przez bounds
    :param n: Liczba elementów do wygenerowania
    :param bounds: Ograniczenie dolne i górne na liczby losowe
    :return: Wektor (lista) n elementów z zakresu bounds
    """
    return [random.uniform(*bounds) for _ in range(n)]


if __name__ == "__main__":
    random_vector_7_elements: List[float] = [random.uniform(*DEFAULT_BOUNDS) for _ in range(7)]
    print("Losowy wektor o 7 elementach: {}".format(random_vector_7_elements))

    lengths_to_generate: List[int] = [2, 5, 10, 20]
    for length in lengths_to_generate:
        random_vector: List[float] = random_vector_of_length_n(length)
        print("Losowy wektor o {} elementach: {}".format(length, random_vector))
