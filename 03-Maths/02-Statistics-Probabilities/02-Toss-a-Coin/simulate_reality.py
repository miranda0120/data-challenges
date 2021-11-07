# pylint: disable=missing-docstring

import random


def play_one_game(n_toss):
    '''TO DO: return the number of heads'''


    count_heads = 0
    for i in range(n_toss):
        coin = random.randint(0, 1)
        if coin == 1:
            count_heads += 1
    return count_heads


def play_n_game(n_games, n_toss):
    '''TO DO: return a dictionary.
    The keys will be the possible head counts of each game
    The values will correspond to the probability of a game ending with that
     number of heads.
    '''
    count_dict = {k: 0 for k in range(n_toss + 1)}
    for _ in range(n_games):
        n_heads = play_one_game(n_toss)
        count_dict[n_heads] += 1
    # convert count to ratios
    result = {k: v / n_games for k, v in count_dict.items()}
    return result
