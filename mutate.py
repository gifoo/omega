# coding=utf-8
import random
from copy import deepcopy
from evol import weighted_choice


class Mutate(object):
    """Handle mutation of coeval. Using deepcopy, because of dict.

    Args:
        mutation_rate (int): chance of mutation in %
        type_chance (list): [(80,False), (20, True)]
                            - false will not mutate
                            - true will mutate
    """

    def __init__(self, mutation_rate, type_chance):
        self.__type_chance = type_chance
        self.__mutation = [(100 - mutation_rate, False), (mutation_rate, True)]

    def start(self, original_coeval):
        """Mutate based on a weighted choice.

        Args:
            original_coeval (type): original input of coeval
        Returns:
            not mutate (dict): unmodified original_coeval
            mutate (dict): modified/mutated original_coeval
        """
        coeval = deepcopy(original_coeval)
        mutate = weighted_choice(self.__mutation)
        if not mutate:
            return coeval
        elif mutate:
            mutation_type = weighted_choice(self.__type_chance)
            return self.__mutation_start(coeval, mutation_type)

    def __mutation_start(self, coeval, mutation_type) -> dict:
        """Mutate based on mutation_type. If true switch two persons, if
        false push one person.

        Args:
            coeval (dict): deep copied dict of input
            mutation_type (type): False/True
        Returns:
            (dict): mutated coeval
        """
        first, second = self.__two_random_choices(coeval)
        if len(coeval[first]) and len(coeval[second]):
            if mutation_type:
                self.__switch_two_persons(coeval[first], coeval[second])
            elif not mutation_type:
                self.__push_one_person(coeval[first], coeval[second])
        return coeval

    @staticmethod
    def __two_random_choices(coeval) -> int:
        """Returns two selected groups. While for two different values.

        Args:
            coeval(dict): deep copied value
        Returns:
            (int), (int): chosen keys from coeval (group index in dict)
        """
        choice_one = random.choice(list(coeval.keys()))
        choice_two = random.choice(list(coeval.keys()))
        while choice_one == choice_two:
            choice_two = random.choice(list(coeval.keys()))
        return choice_one, choice_two

    @staticmethod
    def __switch_two_persons(first, second):
        """Swap two persons in a dictionary.

        Args:
            first (list): first chosen group
            second (list): second chosen group
        """
        p_one = random.randrange(0, len(first))
        p_two = random.randrange(0, len(second))
        first[p_one], second[p_two] = second[p_two], first[p_one]

    @staticmethod
    def __push_one_person(first, second):
        """Push person from group to a different group. Delete from first
        group.

        Args:
            first (list): first chosen group
            second (list): second chosen group
        """
        p_one = random.randint(0, len(first) - 1)
        second.append(first[p_one])
        del first[p_one]
