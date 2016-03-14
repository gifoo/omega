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
        self._gen_size = 11
        self.starting_gen = FirstGeneration(persons, 3, self._gen_size). \
            create_generation()
        self.p = pprint.PrettyPrinter()
        self.fc = FitnessCalculator(self.persons, 3)
        self.gen = self.fc.calculate_fitness(
            self.starting_gen, self.criteria)
        self.mut_type = [(80, True), (20, False)]

    def start(self):
        """docstring"""
        for index in range(self.num_of_generations):
            new_gen = self.__select_survivors_and_mutate()
            self.gen = self.fc.calculate_fitness(new_gen, self.criteria)
            if index % 20 == 0:
                temp_res = self.fc.calculate_fitness(new_gen, self.criteria)
                temp_res.sort(key=lambda tup: tup[0], reverse=True)
                self.p.pprint(temp_res)

    def __select_survivors_and_mutate(self):
        """
        Create new generation. Roulette values are defined by fitness.
        With weighted choice choose one survivor. Apply mutation.
        Fill up descendants.

        :rtype: list
        :return: descendants of previous generation
        """
        descendants = []
        while len(descendants) < self._gen_size:
            roulette = self.__roulette_by_fitness(self.gen)
            chosen = weighted_choice(roulette)
            mutate = Mutate(self._mutation, self.mut_type)
            result_of_mutation = mutate.start(chosen)
            descendants.append(result_of_mutation)
        return descendants

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
            # *100 to know how much percents from 100%
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
    Evolve(PERSONS, crit, 100, 20).start()
