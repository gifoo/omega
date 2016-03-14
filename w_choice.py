# coding=utf-8
import random


def weighted_choice(roulette):
    """
    Choose a survivor from roulette (also represents current generation).

    :type roulette: list
    :param roulette: [(chance, coeval),...]
    :rtype: type
    :return: second value from tuple in roulette
    """
    # rounding error, get more and less than 100%
    max_percents = sum(chance for chance, coeval in roulette)
    pick = random.uniform(0, max_percents)
    current = 0
    for chance, coeval in roulette:
        current += chance
        if current > pick:
            return coeval
