# coding=utf-8
from person import Person
from fgen import FirstGeneration
from fitness import FitnessCalculator
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
    """docstring

    Args:
    """
    def __init__(self):
        pass

if __name__ == '__main__':
    criteria = [
        ['gender', 'Male', 1],
    ]
    fg = FirstGeneration(PERSONS, 3, 11)
    generation = fg.create_generation()
    p = pprint.PrettyPrinter()
    PERSONS = per
    fc = FitnessCalculator(PERSONS, 3)
    p.pprint(fc.calculate_fitness(generation, criteria))

