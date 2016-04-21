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
            problem.addVariable(var, [1, 2, 3, 4, 5, 6, 7, 8 , 9])

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


def set_answer(problem, col, line, value):

    var = col + str(line)
    problem.addConstraint(lambda var: var == value, (var,))


def print_first_solution(problem):

    solution = problem.getSolutionIter().__next__()

    for number in LINES:

        row = []

        for letter in COLS:

            var = letter + number
            row.append(str(solution[var]))

        print("|".join(row))


def main():
    problem = build_problem()

    set_answer(problem, 'a', 3, 1)
    set_answer(problem, 'a', 4, 7)
    set_answer(problem, 'a', 5, 2)
    set_answer(problem, 'a', 9, 9)

    set_answer(problem, 'b', 4, 1)
    set_answer(problem, 'b', 6, 3)

    set_answer(problem, 'c', 2, 2)
    set_answer(problem, 'c', 3, 7)
    set_answer(problem, 'c', 4, 9)

    set_answer(problem, 'd', 1, 9)
    set_answer(problem, 'd', 2, 3)
    set_answer(problem, 'd', 3, 6)
    set_answer(problem, 'd', 8, 5)

    set_answer(problem, 'e', 5, 3)

    set_answer(problem, 'f', 2, 5)
    set_answer(problem, 'f', 7, 7)
    set_answer(problem, 'f', 8, 1)
    set_answer(problem, 'f', 9, 3)

    set_answer(problem, 'g', 6, 8)
    set_answer(problem, 'g', 7, 4)
    set_answer(problem, 'g', 8, 6)

    set_answer(problem, 'h', 4, 4)
    set_answer(problem, 'h', 6, 7)

    set_answer(problem, 'i', 1, 7)
    set_answer(problem, 'i', 5, 9)
    set_answer(problem, 'i', 6, 6)
    set_answer(problem, 'i', 7, 8)

    print_first_solution(problem)

if __name__ == "__main__":
    main()
