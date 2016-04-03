# coding=utf-8
import random
import pprint
import string
import itertools
from person import Person
from evol import Evolve


def _nine_persons_evol_by_gender():
    """
    Testing 9 people. Evolve by gender.
    """
    input = [
        Person(['A', 'Vieden', 'Male', 'Computer Science', 'NonSlavic',
                'Commuting']),
        Person(['B', 'Vieden', 'Male', 'Computer Science', 'NonSlavic',
                'Commuting']),
        Person(['C', 'Ljubljana', 'Female', 'Human studies', 'Slavic',
                'Staying']),
        Person(['D', 'Zagreb', 'Female', 'Other', 'Slavic', 'Staying']),
        Person(['E', 'Ljubljana', 'Female', 'Computer Science', 'Slavic',
                'Staying']),
        Person(['F', 'Vieden', 'Female', 'Human studies', 'NonSlavic',
                'Staying']),
        Person(['G', 'Zagreb', 'Male', 'Human studies', 'Slavic', 'Staying']),
        Person(['H', 'Ljubljana', 'Female', 'Human studies', 'Slavic',
                'Staying']),
        Person(
            ['I', 'Ljubljana', 'Male', 'Human studies', 'Slavic', 'Staying']),
        Person(['J', 'Zagreb', 'Female', 'Other', 'Slavic', 'Staying']),
        Person(['K', 'Zagreb', 'Male', 'Other', 'Slavic', 'Staying']),
        Person(
            ['L', 'Vieden', 'Male', 'Human studies', 'Slavic', 'Commuting']),
    ]
    crit = [["gender", "Male", 1], ['group_size', None, 1]]
    number_of_generations = 100
    chance_of_mutation = 20
    split_to = 3
    coevals = 11
    mutation_type_config = [(80, True), (20, False)]
    freq_print = 25
    conf = [number_of_generations, chance_of_mutation, split_to, coevals,
            mutation_type_config, freq_print]
    e = Evolve(input, crit, conf)
    pprint.PrettyPrinter().pprint(e.persons_stats)
    e.start()


def choose(_from):
    return random.choice(_from)


def _twenty_persons_by_gender():
    abc = list(string.ascii_uppercase)
    gender = ['Male', 'Female']
    uni = ['Vieden', 'Ljubljana', 'Zagreb']
    study = ['Computer Science', 'Human studies', 'Other']
    nat = ['Slavic', 'NonSlavic']
    tran = ['Staying', 'Commuting']
    persons = []
    for index in range(20):
        p = Person([abc[index], choose(uni), choose(gender), choose(study),
                    choose(nat), choose(tran)])
        persons.append(p)
    crit = [["gender", "Male", 1], ['group_size', None, 1],
            ['study', 'Computer Science', 1]]
    number_of_generations = 200
    chance_of_mutation = 20
    split_to = 5
    coevals = 20
    mutation_type_config = [(80, True), (20, False)]
    freq_print = 100
    conf = [number_of_generations, chance_of_mutation, split_to, coevals,
            mutation_type_config, freq_print]
    e = Evolve(persons, crit, conf)
    pprint.PrettyPrinter().pprint(e.persons_stats)
    e.start()


def _twenty_persons_by_gender():
    abc = list(string.ascii_uppercase)
    gender = ['Male', 'Female']
    uni = ['Vieden', 'Ljubljana', 'Zagreb']
    study = ['Computer Science', 'Human studies', 'Other']
    nat = ['Slavic', 'NonSlavic']
    tran = ['Staying', 'Commuting']
    persons = []
    for index in range(20):
        p = Person([abc[index], choose(uni), choose(gender), choose(study),
                    choose(nat), choose(tran)])
        persons.append(p)
    crit = [["gender", "Male", 1], ['group_size', None, 1],
            ['study', 'Computer Science', 1]]
    number_of_generations = 200
    chance_of_mutation = 20
    split_to = 5
    coevals = 20
    mutation_type_config = [(80, True), (20, False)]
    freq_print = 100
    conf = [number_of_generations, chance_of_mutation, split_to, coevals,
            mutation_type_config, freq_print]
    e = Evolve(persons, crit, conf)
    pprint.PrettyPrinter().pprint(e.persons_stats)
    e.start()


def _hundred_persons():
    abc = list(itertools.permutations('ABCDE'))
    gender = ['Male', 'Female']
    uni = ['Vieden', 'Ljubljana', 'Zagreb']
    study = ['Computer Science', 'Human studies', 'Other']
    nat = ['Slavic', 'NonSlavic']
    tran = ['Staying', 'Commuting']
    persons = []
    for index in range(120):
        p = Person([''.join(abc[index]), choose(uni), choose(gender),
                    choose(study), choose(nat), choose(tran)])
        persons.append(p)
    crit = [["gender", "Male", 1], ['group_size', None, 1],
            ['study', 'Computer Science', 1]]
    number_of_generations = 1000
    chance_of_mutation = 20
    split_to = 5
    coevals = 20
    mutation_type_config = [(80, True), (20, False)]
    freq_print = 250
    conf = [number_of_generations, chance_of_mutation, split_to, coevals,
            mutation_type_config, freq_print]
    e = Evolve(persons, crit, conf)
    pprint.PrettyPrinter().pprint(e.persons_stats)
    e.start()


if __name__ == '__main__':
    _nine_persons_evol_by_gender()
    #_twenty_persons_by_gender()
    #_hundred_persons()
