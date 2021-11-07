# pylint: disable=missing-docstring

import math


def count_possibilities(n_toss, n_heads):
    '''TO DO: '''
    possibilities = math.factorial(n_toss) / (math.factorial(n_heads) *
                                              math.factorial(n_toss - n_heads))
    return possibilities


def count_total_possibilities(n_toss):
    '''TO DO: '''
    return 2 ** n_toss


def probability(n_toss):
    '''TO DO: '''
    count_heads_dict = {}


    for n_heads in range(n_toss + 1):
        proba = count_possibilities(n_toss, n_heads)
        count_heads_dict[n_heads] = proba / count_total_possibilities(n_toss)
    return count_heads_dict
