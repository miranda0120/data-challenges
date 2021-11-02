import math
import statistics


def my_mean(samples):
    '''returns the mean of the observations'''
    return sum(samples)/ (len(samples))



def my_standard_deviation(samples):
    '''returns the standard deviation of the observations'''
    result = 0
    for i in range(len(samples)):
        subtotal = (my_mean(samples) - samples[i]) ** 2
        result += subtotal
    return (result/((len(samples)-1))) ** 0.5

def my_mode(samples):
    '''returns the mode of the observations'''
    return statistics.mode(samples)


def my_multimodes(samples):
    '''returns the modes of the observations as a sorted list'''
    return statistics.multimode(samples)


def my_median(samples):
    '''returns the median of the observations'''
    return statistics.median(samples)
