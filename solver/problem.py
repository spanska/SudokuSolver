#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sudoku import build_problem, set_answer, print_first_solution

PROBLEM = {
    'a3': 1,
    'a4': 7,
    'a5': 2,
    'a9': 9,
    'b4': 1,
    'b6': 3,
    'c2': 2,
    'c3': 7,
    'c4': 9,
    'd1': 9,
    'd2': 3,
    'd3': 6,
    'd8': 5,
    'e5': 3,
    'f2': 5,
    'f7': 7,
    'f8': 1,
    'f9': 3,
    'g6': 8,
    'g7': 4,
    'g8': 6,
    'h4': 4,
    'h6': 7,
    'i1': 7,
    'i5': 9,
    'i6': 6,
    'i7': 8
}


def main():

    problem = build_problem()

    for key, val in PROBLEM.items():
        set_answer(problem, key, val)

    print_first_solution(problem)

if __name__ == "__main__":
    main()
