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

    def __init__(self, persons, criteria, config):
        """
        :type persons: list
        :param persons:
        :type criteria: list
        :param criteria:
        :type config: list
        :param config:  0 - number of generations
                        1 - mutation rate in %
                        2 - to how many groups are we splitting
                        3 - how many coevals in a generation
                        4 - occurance of mutation type
        """
        self.criteria = criteria
        (self.gen_num, self.mut, self.grp_size, self.gen_size,
         self.mut_type) = config
        fg = self.__first_generation(persons)
        self.fc = self.__fitness_calculator(persons)
        self.first_gen = fg.create_generation()
        self.gen = self.fc.calculate_fitness(self.first_gen)

    def __first_generation(self, persons):
        """
        :type persons: list
        :param persons: input persons, used for copying
        :rtype FirstGeneration
        """
        copy = persons[:]
        return FirstGeneration(copy, self.grp_size, self.gen_size)

    def __fitness_calculator(self, persons):
        """
        :type persons: list
        :param persons: input persons, used for copying
        :rtype: FitnessCalculator
        """
        copy = persons[:]
        return FitnessCalculator(copy, self.grp_size, self.criteria)

    def start(self, frequency):
        """
        Run evolve as many number of generations specified by user. Also
        checks for print out.

        :type frequency: int
        :param frequency: how often print out result of evol. algorithm
        """
        for index in range(self.gen_num):
            descendants = self.__select_survivors_and_mutate()
            self.gen = self.fc.calculate_fitness(descendants)
            if index % frequency == 0:
                self.__print_result(descendants)

    def __select_survivors_and_mutate(self):
        """
        Create new generation. Roulette values are defined by fitness.
        With weighted choice choose one survivor. Apply mutation.
        Fill up descendants.

        :rtype: list
        :return: descendants of previous generation
        """
        descendants = []
        while len(descendants) < self.gen_size:
            roulette = self.__roulette_by_fitness(self.gen)
            chosen = weighted_choice(roulette)
            mutate = Mutate(self.mut, self.mut_type)
            result_of_mutation = mutate.start(chosen)
            descendants.append(result_of_mutation)
        return descendants

    def __roulette_by_fitness(self, generation):
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
    def sum_of_fitness(generation):
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

    def __print_result(self, descendants):
        """
        Handles print of result during evolve. Also sort result for fittest
        at top.

        :type descendants: list
        :param descendants: new generation, sort them and print out
        """
        res = self.fc.calculate_fitness(descendants)
        res.sort(key=lambda tup: tup[0], reverse=True)
        self.p = pprint.PrettyPrinter()
        self.p.pprint(res)


if __name__ == "__main__":
    crit = [
        ['group_size', None, 1],
        ["gender", "Male", 1],
    ]
    conf = [100, 20, 3, 11, [(80, True), (20, False)]]
    Evolve(PERSONS, crit, conf).start(20)
