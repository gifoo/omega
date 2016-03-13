# coding=utf-8
from person import Person
from fgen import FirstGeneration
from fitness import FitnessCalculator
from copy import deepcopy
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
        """"""
        roulette = self.__roulette_by_fitness(generation)
        chosen = self.weighted_choice(roulette)
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

    @staticmethod
    def weighted_choice(roulette) -> dict:
        """Choose a survivor from roulette (also represents current
        generation).

        Args:
            roulette (list): [(chance, coeval),...]
        Returns:
            (dict): coeval, contains people appointed to groups
        """
        # error bacause of rounding, get more and less than 100%
        max_percents = sum(chance for chance, coeval in roulette)
        pick = random.uniform(0, max_percents)
        current = 0
        for chance, coeval in roulette:
            current += chance
            if current > pick:
                return coeval


class Mutate(object):
    """docstring
    """

    def __init__(self, mutation_rate, mutation_type_chance):
        self.mutation_rate = mutation_rate
        self.mutation_type = mutation_type_chance
        self.roulette = [(100-mutation_rate, False), (mutation_rate, True)]

    def start(self, original_coeval):
        """docstring

        Args:
            original_coeval (dict):
        """
        coeval = deepcopy(original_coeval)
        mutate = Evolve.weighted_choice(self.roulette)
        if not mutate:
            return coeval
        else:
            mutation_type = Evolve.weighted_choice(self.mutation_type)
            if mutation_type:
                return self.__switch_two_persons(coeval)
            else:
                pass

    def __switch_two_persons(self, coeval) -> dict:
        """Switch two persons in a coeval.

        Args:
            coeval (dict): deep copied value, allows to swap elements
        Return:
            (dict): modified coeval, switched 'gens'/persons
        """
        first, second = self.__two_random_choices(coeval)
        g_one = coeval[first]
        g_two = coeval[second]
        # select random person from group
        if len(g_one) and len(g_two):
            p_one = random.randrange(0, len(g_one))
            p_two = random.randrange(0, len(g_two))
            g_one[p_one], g_two[p_two] = g_two[p_two], g_one[p_one]
        return coeval

    @staticmethod
    def __two_random_choices(coeval) -> int:
        """Returns two selected groups. While for two different values.

        Args:
            coeval(dict): deep copied value
        Returns:
            (int), (int):
        """
        choice_one = random.choice(list(coeval.keys()))
        choice_two = random.choice(list(coeval.keys()))
        # if same selected, try selecting another
        while choice_one == choice_two:
            choice_two = random.choice(list(coeval.keys()))
        return choice_one, choice_two



if __name__ == "__main__":
    crit = [
        ['group_size', None, 1],
        ["gender", "Male", 1],
    ]
    Evolve(PERSONS, crit, 20, 100).start()
