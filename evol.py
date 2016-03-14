# coding=utf-8
"""doc"""
from person import Person
from fgen import FirstGeneration
from fitness import FitnessCalculator
from w_choice import weighted_choice
from mut import Mutate
import pprint

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


class Evolve(object):
    """
    docstring
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
        m = Mutate(self._mutation, [(80, True), (20, False)]).start(chosen)
        print(chosen)
        print(m)

    def __roulette_by_fitness(self, generation: list) -> list:
        """
        Set chance of selection based on fitness.

        :type generation: list
        :param generation: tuple(fitness(float), coeval(dict))
        :rtype: list
        :return: [(chance, coeval), ...]
        """
        _sum = self.sum_of_fitness(generation)
        roulette = []
        for fitness, coeval in generation:
            roulette.append(((fitness / _sum) * 100, coeval))
        return roulette

    @staticmethod
    def sum_of_fitness(generation: list) -> float:
        """
        Sum of fitness in generation.

        :type generation: list
        :param generation: (fitness(float), coeval(dict))
        :rtype: float
        :return: sum of fitness
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
