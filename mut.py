# coding=utf-8
import random
from copy import deepcopy
from w_choice import weighted_choice


class Mutate(object):
    """
    Handle mutation of coeval. Using deepcopy, because of dict.
    """

    def __init__(self, mutation_rate: int, type_chance: list):
        """
        :type mutation_rate: int
        :param mutation_rate: chance of mutation in %
        :type type_chance: list
        :param type_chance: [(80,False), (20, True)] - not mutate or mutate
        """
        self.__type_chance = type_chance
        self.__mutation = [(100 - mutation_rate, False), (mutation_rate, True)]

    def start(self, original_coeval: type) -> dict:
        """
        Mutate based on a weighted choice.

        :type original_coeval: type
        :param original_coeval: original input of coeval
        :rtype: dict
        :return: unmodified/modified original_coeval
        """
        coeval = deepcopy(original_coeval)
        mutate = weighted_choice(self.__mutation)
        if not mutate:
            return coeval
        elif mutate:
            mutation_type = weighted_choice(self.__type_chance)
            return self.__mutation_start(coeval, mutation_type)

    def __mutation_start(self, coeval: dict, mutation_type: type) -> dict:
        """
        Mutate based on mutation_type. If true switch two persons, if
        false push one person.

        :type coeval: dict
        :param coeval: deep copy of original_coeval
        :type mutation_type: type
        :param mutation_type: False/True
        :rtype: dict
        :return: mutated coeval
        """
        first, second = self.__two_random_choices(coeval)
        if len(coeval[first]) and len(coeval[second]):
            if mutation_type:
                self.__switch_two_persons(coeval[first], coeval[second])
            elif not mutation_type:
                self.__push_one_person(coeval[first], coeval[second])
        return coeval

    @staticmethod
    def __two_random_choices(coeval: dict) -> int:
        """
        Returns two selected groups. While for two different values.

        :type coeval: dict
        :param coeval: still using deepcopied for swaping
        :rtype: int & int
        :return: chosen keys from coeval (group index in dict)
        """
        choice_one = random.choice(list(coeval.keys()))
        choice_two = random.choice(list(coeval.keys()))
        while choice_one == choice_two:
            choice_two = random.choice(list(coeval.keys()))
        return choice_one, choice_two

    @staticmethod
    def __switch_two_persons(first: list, second: list):
        """
        Swap two persons in a dictionary.

        :type first: list
        :param first: first chosen group
        :type second: list
        :param second: second chosen group
        """
        p_one = random.randrange(0, len(first))
        p_two = random.randrange(0, len(second))
        first[p_one], second[p_two] = second[p_two], first[p_one]

    @staticmethod
    def __push_one_person(first: list, second: list):
        """
        Push person from group to a different group. Delete from first
        group.

        :type first: list
        :param first: first chosen group
        :type second: list
        :param second: second chosen group
        """
        p_one = random.randint(0, len(first) - 1)
        second.append(first[p_one])
        del first[p_one]
