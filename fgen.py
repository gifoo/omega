# coding=utf-8
"""doc"""
import random


class FirstGeneration(object):
    """
    Assign values and load error handler. Use self.create_generation
    for getting the first generation.
    """
    def __init__(self, persons, group_size, gen_size):
        """
        :type persons: list
        :param persons: filled with Person(object)
        :type group_size: int
        :param group_size: to how many groups we want to divide persons
        :type gen_size: int
        :param gen_size: the size of a generation
        """
        self.__persons = persons
        self.__cache = persons[:]
        self.__group_size = group_size
        self.__gen_size = gen_size
        self.__error_handler()

    def create_generation(self):
        """
        Create starting point for the evolutionary algorithm.

        :rtype: list
        :return: filled with possible groupings
        """
        return [self.__grouping() for index in range(self.__gen_size)]

    def __grouping(self):
        """
        Assign persons to group. Yield result.

        :rtype: dict
        :return: keys - group_index; values - Person(object)
        """
        coeval = {index: [] for index in range(self.__group_size)}
        while self.__persons:
            group_index = random.randint(0, self.__group_size - 1)
            person_index = random.randint(0, len(self.__persons) - 1)
            coeval[group_index].append(self.__persons.pop(person_index))
        self.__persons = self.__cache[:]
        return coeval

    def __error_handler(self):
        """
        Handle errors.

        :raises: IOError: - persons are empty
                 ValueError: - group size is smaller/equal to zero
                 ValueError: - generation size is smaller/equal to 10
        """
        if not self.__persons:
            raise IOError('Empty persons. Probably did not loaded persons')
        if self.__group_size <= 0:
            raise ValueError('Number of groups smaller/equall than 0.')
        # TODO make it modifiable in web app
        if self.__gen_size <= 10:
            raise ValueError('Generation size smaller/equall than 10.')
