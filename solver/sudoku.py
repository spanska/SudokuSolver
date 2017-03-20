#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from solver.constraint import *

COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

LINES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def build_problem():

    problem = Problem()

    # build du tableau avec toutes les variables
    for letter in COLS:
        for number in LINES:
            var = letter + number
            problem.addVariable(var, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # tous les éléments des lignes doivent être différents
    for letter in COLS:
        line = [letter + number for number in LINES]
        problem.addConstraint(AllDifferentConstraint(), line)

    # toutes les éléments des colonnes doivent être différents
    for number in LINES:
        column = [letter + number for letter in COLS]
        problem.addConstraint(AllDifferentConstraint(), column)

    # tous les carrés doivent être différents
    for index in [0, 3, 6]:

        for index_2 in [0, 3, 6]:

            square = []

            for i in range(3):
                for j in range(3):

                    cell = COLS[index + j] + LINES[index_2 + i]
                    square.append(cell)

            problem.addConstraint(AllDifferentConstraint(), square)

    return problem


def set_answer(problem, var, value):
    problem.addConstraint(lambda var: var == value, (var,))


def print_first_solution(problem):

    solution = problem.getSolutionIter().__next__()

    for number in LINES:

        row = []

        for letter in COLS:

            var = letter + number
            row.append(str(solution[var]))

        print("|".join(row))
