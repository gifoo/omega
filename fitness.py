# coding=utf-8
class FitnessCalculator(object):
    """Class for calculation of fitness of a generation. Sort the result
    by fittest at the top. Also can be used for static data creation about
    persons.

    Args:
        persons (list): filled with Person(object)
        group_size (int): to how many groups we want to divide the persons
    """

    def __init__(self, persons, group_size):
        self.__persons = persons
        self.__group_size = group_size
        self.__persons_stats = self.__statistic_data_about_persons()

    @property
    def persons_stats(self) -> dict:
        """Returns: (dict): static table data about persons"""
        return self.__persons_stats

    def __statistic_data_about_persons(self) -> dict:
        """Represent data about persons and count the number of
        different criterias.

        Returns:
            (dict): persons data as a tree representation
        """

        def __fill_data(crit, data):
            """Fill static_data; enumerate values. Using dict.setdefault()

            Args:
                crit (str): defines allocated keys for criteria
                data (object.value): value from Person(object)
            """
            static_data.setdefault(crit, dict()).setdefault(data, 0)
            static_data[crit][data] += 1

        static_data = dict()
        for person in self.__persons:
            __fill_data("gender", person.gender)
            __fill_data("study", person.study)
            __fill_data("university", person.university)
            __fill_data("nationality", person.nationality)
            __fill_data("transport", person.transport)
        return static_data

    def calculate_fitness(self, generation, criteria) -> list:
        """Calculate the fitness of generation. Sorted by fittest at top.

        Args:
            generation (list): input, filled with coeval(dict)
            criteria (list): contains (list) filled with:
                             [criteria(str), specific_criteria(str)]
        Returns:
            (list): calculated fitness of generation, sorted by fittest
                    at top
        """
        result = []
        for coeval in generation:
            penalty = 0
            for crit in criteria:
                penalty += self.__fitness_of_coeval(coeval, crit)
            # 1/(penalty+1) - keeps the fitness between <0, 1>
            fitness_of_coeval = round(1 / (penalty + 1), 4)
            result.append((fitness_of_coeval, coeval))
        result.sort(key=lambda tup: tup[0], reverse=True)
        return result

    def __fitness_of_coeval(self, coeval, criteria) -> int:
        """Calculate penalty of coeval, based on one criteria.

        Args:
            coeval (dict): random grouping of persons
            criteria (list): two values [criteria(str),
                                         specific criteria(str),
                                         weight value(float)<0, 1>]
        Returns:
            (int): penalty for coeval
        """
        if criteria[0] != 'group_size':
            counted = self.__evaluate_by_criteria(coeval, criteria)
            return self.__calculate_by_criteria(counted, criteria)
        elif criteria[0] == 'group_size':
            return self.__calculate_by_criteria(coeval, criteria)
        elif criteria[0] == 'dist_matrix':
            #TODO implement dist_matrix calculation
            pass

    def __calculate_by_criteria(self, counted, criteria) -> int:
        """Calculate penlaty based on criteria. Selected by user.

        Args:
            counted (list): filled with (int), people with needed criteria
                            in group
            criteria (list): two values [criteria(str),
                                         specific criteria(str),
                                         weight value(float)<0, 1>]

        Returns:
            (int): weighted penalty - one criteria
        """
        penalty = 0
        for value in counted:
            div = self.persons_stats[criteria[0]][criteria[1]] / \
                  self.__group_size
            penalty += abs(div - value)
        return penalty * criteria[2]

    def __calculate_by_group_size(self, coeval, criteria) -> int:
        """Calculate panlty of coeval, based on group size.

        Args:
            coeval (dict): grouping of people
            criteria (list): two values [criteria(str),
                                         specific criteria(str),
                                         weight value(float)<0, 1>]

        Returns:
            (int): weighted penalty - group size
        """
        penalty = 0
        for group in coeval.values():
            median = len(self.__persons)/self.__group_size
            if len(group) != median:
                penalty += abs(median - len(group))
        return penalty * criteria[2]

    @staticmethod
    def __evaluate_by_criteria(coeval, criteria) -> list:
        """Evaluate how are the criterias divided between groups
        in coeval. Based on one criteria.

        Args:
            coeval (dict): random grouping of persons
            criteria (list): two values [criteria(str),
                                         specific criteria(str),
                                         weight value(float)<0, 1>]

        Returns:
            (list): how many persons with needed criteria in group;
                    index in list corresponds to index of group in
                    coeval
        """
        arranged = []
        for group in coeval.values():
            index = 0
            for person in group:
                if criteria[0] == "gender":
                    if person.gender == criteria[1]:
                        index += 1
                elif criteria[0] == "study":
                    if person.study == criteria[1]:
                        index += 1
                elif criteria[0] == "university":
                    if person.university == criteria[1]:
                        index += 1
                elif criteria[0] == "nationality":
                    if person.nationality == criteria[1]:
                        index += 1
                elif criteria[0] == "transport":
                    if person.transport == criteria[1]:
                        index += 1
            arranged.append(index)
        return arranged



