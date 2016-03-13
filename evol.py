# coding=utf-8
from person import Person
from fgen import FirstGeneration
from fitness import FitnessCalculator
from mutate import Mutate
import pprint
import random

PERSONS = [
    Person(['A', 'Vieden', 'Male', 'Computer Science',
            'NonSlavic', 'Commuting']),
    Person(['B', 'Vieden', 'Male', 'Computer Science',
            'NonSlavic', 'Commuting']),
    Person(['C', 'Ljubljana', 'Female', 'Human studies',
            'Slavic', 'Staying']),
    Person(['D', 'Zagreb', 'Female', 'Other', 'Slavic',
            'Staying']),
    Person(['E', 'Ljubljana', 'Female', 'Computer Science',
            'Slavic', 'Staying']),
    Person(['F', 'Vieden', 'Female', 'Human studies',
            'NonSlavic', 'Staying']),
    Person(['G', 'Zagreb', 'Male', 'Human studies',
            'Slavic', 'Staying']),
    Person(['H', 'Ljubljana', 'Female', 'Human studies',
            'Slavic', 'Staying']),
    Person(['I', 'Ljubljana', 'Male', 'Human studies',
            'Slavic', 'Staying']),
    Person(['J', 'Zagreb', 'Female', 'Other',
            'Slavic', 'Staying']),
    Person(['K', 'Zagreb', 'Male', 'Other', 'Slavic', 'Staying']),
    Person(['L', 'Vieden', 'Male', 'Human studies',
            'Slavic', 'Commuting']),
]
per = PERSONS[:]


def weighted_choice(roulette) -> type:
    """Choose a survivor from roulette (also represents current
    generation).

    Args:
        roulette (list): [(chance, coeval),...]
    Returns:
        (type): return second value from tuple in roulette
    """
    # error bacause of rounding, get more and less than 100%
    max_percents = sum(chance for chance, coeval in roulette)
    pick = random.uniform(0, max_percents)
    current = 0
    for chance, coeval in roulette:
        current += chance
        if current > pick:
            return coeval


class Evolve(object):
    """docstring

    Args:
    """

    def __init__(self, persons, criteria, num_of_generations, mutation):
        self.persons = persons[:]
        self.criteria = criteria
        self.num_of_generations = num_of_generations
        self._mutation = mutation
        self.starting_gen = FirstGeneration(persons, 3, 11). \
            create_generation()
        self.p = pprint.PrettyPrinter()

    def start(self):
        """docstring"""
        gen = FitnessCalculator(self.persons, 3).calculate_fitness(
            self.starting_gen, self.criteria)
        self.__handle_data(gen)
        # print(pick)

    def __handle_data(self, generation):
        """docstring"""
        roulette = self.__roulette_by_fitness(generation)
        chosen = weighted_choice(roulette)
        Mutate(self._mutation, [(80, True), (20, False)]).start(chosen)

    def __roulette_by_fitness(self, generation) -> list:
        """Set chance of selection based on fitness.

        Args:
            generation (list): tuple(fitness(float), coeval(dict))
        Returns:
            (list): [(chance, coeval), ...]
        """
        _sum = self.sum_of_fitness(generation)
        roulette = []
        for fitness, coeval in generation:
            roulette.append(((fitness / _sum) * 100, coeval))
        return roulette

    @staticmethod
    def sum_of_fitness(generation) -> float:
        """Sum of fitness in generation.

        Args:
            generation (list): (fitness(float), coeval(dict))
        Returns:
            (float): sum fitness
        """
        result = 0
        for fitness, coeval in generation:
            result += fitness
        return result


if __name__ == "__main__":
    crit = [
        ['group_size', None, 1],
        ["gender", "Male", 1],
    ]
    Evolve(PERSONS, crit, 20, 100).start()
