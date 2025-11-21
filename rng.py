import random

def set_seed(seed_value):
    random.seed(seed_value)

def roulette_like_trial(p_win=0.49):
    """
    Returns True if the bettor wins (probability p_win),
    otherwise returns False.
    """
    return random.random() < p_win

