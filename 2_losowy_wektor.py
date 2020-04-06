# Adrian Startek, 110956
# Temat 2. Losowy wektor
# Kod dostępny również na GitHub: https://github.com/adriancodeimperium/DM110956
import random
import logging
import numpy


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    logger = logging.getLogger(__name__)
    mu: float = 4
    sigma: float = 2
    element_count: int = 100

    logger.info("Generowanie losowego [N({},{})] wektora o dlugosci {}".format(mu, sigma, element_count))
    random_vector = [random.normalvariate(mu, sigma) for _ in range(element_count)]
    logger.debug("Wygenerowano wektor: {}".format(random_vector))
    mean: float = numpy.mean(random_vector)
    std: float = numpy.std(random_vector)
    logger.info("Zakladana srednia: {}. Otrzymana: {}".format(mu, mean))
    logger.info("Zakladane odchylenie standardowe: {}. Otrzymane: {}".format(sigma, std))
