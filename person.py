# coding=utf-8
"""doc"""


class Person():
    def __init__(self, information):
        if len(information) != 6:
            raise ValueError('Some informations are lacking, check Person obj')
        self.name = information[0]
        self.university = information[1]
        self.gender = information[2]
        self.study = information[3]
        self.nationality = information[4]
        self.transport = information[5]
        self.info = information[1:]

    def __repr__(self):
        return self.name
        #+ '|' + self.gender + '|' + self.study + '|' + \
        #self.nationality + '|' + self.transport + '|' + self.university