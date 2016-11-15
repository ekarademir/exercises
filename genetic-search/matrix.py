import numpy as np

import json
import codecs
import string
import re

from random import randint, choice, random

def test_device(devicematrix):
    """Tests a given device matrix. If it is None then tests a random device.
    Returns a dict containing device, and results."""

    target = np.array([
    [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],
    [0,0,0,0,0, 1,0,1,1,0, 1,0,1,1,0, 0,0,1,1,1],
    [1,1,0,1,1, 1,0,1,1,0, 1,0,1,0,1, 1,1,1,1,1],
    [1,1,0,1,1, 1,0,0,0,0, 1,0,1,1,0, 0,1,1,1,1],
    [1,1,0,1,1, 1,0,1,1,0, 1,0,1,1,1, 1,0,1,1,1],
    [1,1,0,1,1, 1,0,1,1,0, 1,0,1,0,0, 0,1,1,1,1],
    [1,0,1,1,0, 0,0,1,1,1, 1,0,0,1,1, 1,1,1,1,1],
    [1,0,1,0,1, 1,1,1,1,1, 0,1,1,0,1, 1,1,1,1,1],
    [1,0,1,1,0, 0,1,1,1,1, 0,0,0,0,1, 1,1,1,1,1],
    [1,0,1,1,1, 1,0,1,1,1, 0,1,1,0,1, 1,1,1,1,1],
    [1,0,1,0,0, 0,1,1,1,1, 0,1,1,0,1, 1,1,1,1,1],
    [0,0,0,0,0, 1,0,0,0,0, 1,0,0,0,1, 0,0,0,0,1],
    [1,1,0,1,1, 1,0,1,1,1, 0,1,1,1,1, 1,1,0,1,1],
    [1,1,0,1,1, 1,0,0,0,1, 1,0,0,1,1, 1,1,0,1,1],
    [1,1,0,1,1, 1,0,1,1,1, 1,1,1,0,1, 1,1,0,1,1],
    [1,1,0,1,1, 1,0,0,0,0, 0,0,0,1,1, 1,1,0,1,1],
    [1,1,1,1,1, 0,0,0,0,1, 1,1,1,1,1, 1,1,1,1,1],
    [0,0,0,0,0, 1,1,1,1,0, 1,1,1,1,1, 0,0,0,0,1],
    [1,1,1,1,1, 1,1,1,1,1, 0,0,0,0,0, 1,1,1,1,1],
    [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],
    ])

    score = 0
    for i in range(20):
        for j in range(20):
            if target[i,j] == devicematrix[i,j]:
                score = score + 1

    normscore = float(score)/(20.*20.)
    results = [
                "Genetic Dry run\n",
                "TM Input: 1.0 TE: 0.0 TM: {0} R: 0.0\n".format(normscore),
                "TE Input: 1.0 TE: {0} TM: 0.0 R: 0.0\n".format(normscore)
              ]

    # Handle monitor results
    # First line is TM input
    tminputpower = float(re.findall('Input: \d+?\.{1}\d+', results[1])[0] \
                            .strip('Input: '))

    tmreflectedpower = float(re.findall('R: \d+?\.{1}\d+', results[1])[0] \
                            .strip('R: '))

    tmtepower = float(re.findall('TE: \d+?\.{1}\d+', results[1])[0] \
                            .strip('TE: '))

    tmtmpower = float(re.findall('TM: \d+?\.{1}\d+', results[1])[0] \
                            .strip('TM: '))

    teinputpower = float(re.findall('Input: \d+?\.{1}\d+', results[2])[0] \
                            .strip('Input: '))

    tereflectedpower = float(re.findall('R: \d+?\.{1}\d+', results[2])[0] \
                            .strip('R: '))

    tetepower = float(re.findall('TE: \d+?\.{1}\d+', results[2])[0] \
                            .strip('TE: '))

    tetmpower = float(re.findall('TM: \d+?\.{1}\d+', results[2])[0] \
                            .strip('TM: '))

    results = {
            'device': devicematrix,
            'monitors': {
                'tminputpower': tminputpower,
                'teinputpower': teinputpower,
                'tmreflectedpower': tmreflectedpower,
                'tereflectedpower': tereflectedpower,
                'tminputtmpower': tmtmpower,
                'tminputtepower': tmtepower,
                'teinputtmpower': tetmpower,
                'teinputtepower': tetepower
            }
        }

    return results


def random_device(row=20, col=20):
    """Generates a random matrix with 1s and 0s given row and col and
    returns the flattened string to be used in Lumerical script."""
    dev = np.random.rand(row, col)
    for i in range(row):
        for j in range(col):
            dev[i, j] = int(dev[i, j] >= 0.5)

    return dev

def performance_metric(monitors):
    """Calculates the performance of the device."""

    # Polarization performance is awarded with correct polarization output
    # and punished with incorrect polarization output and reflection
    tmperformance = (monitors['tminputtmpower'] \
                        - monitors['tmreflectedpower'] \
                        - monitors['tminputtepower'])/monitors['tminputpower']

    teperformance = (monitors['teinputtepower'] \
                        - monitors['tereflectedpower'] \
                        - monitors['teinputtmpower'])/monitors['teinputpower']

    # Total performance is then sum of both. Ideal device has
    # performance of 2
    return tmperformance + teperformance

def shuffle_list(unshuffledlist):
    """Implements Fisher Yates Shuffle"""

    # Mark the unshuffled part of the list
    for mark in range(len(unshuffledlist)-1,-1,-1):
        # Choose a random item to shuffle
        shufflethis = randint(0,mark)

        # Swap
        unshuffledlist[mark], unshuffledlist[shufflethis] = \
        unshuffledlist[shufflethis], unshuffledlist[mark]

    return unshuffledlist # now shuffled of course

def mutate_device(devicematrix):
    """Introduces number of mutations in the given device matrix."""
    sh = np.shape(devicematrix)
    mutationtimes = int(randint(0,sh[0]*sh[1]-1)*0.005)
    for i in range(mutationtimes):
        mutationrow = randint(0,sh[0]-1)
        mutationcol = randint(0,sh[1]-1)
        devicematrix[mutationrow, mutationcol] = choice([0,1])

    return devicematrix

def xo_device(parents):
    """Cross over operation"""
    parent1, parent2 = parents
    sh = np.shape(parent1)

    offspring = np.zeros(sh)

    for i in range(sh[0]): # each row
        for j in range(sh[1]): # each col
            # choose a random gene from one parent
            # each gene is a matrix element
            pickparent1 = choice([True,False])
            offspring[i,j] = parent1[i,j] if pickparent1 else parent2[i,j]

    return mutate_device(offspring)

def choose_parents(evaluatedgenepool):
    poolsize = len(evaluatedgenepool)

    # starting from the best give each gene in the pool some chance.
    # 1st has 10 times
    # 2nd has 8 times
    # 3rd has 4 times
    # 4th has 2 times
    # the chance of selection compared to min
    times = [1 for x in evaluatedgenepool]
    times[-1] = 20
    times[-2] = 15
    times[-3] = 4
    times[-4] = 2

    # Throw each gene into a bag. Throw times amount of copy
    bag = []
    for i in range(poolsize):
        for j in range(times[i]):
            bag.append(i)

    # Choose two random genes from the bag
    parent1 = evaluatedgenepool[choice(bag)][0]['device']
    parent2 = evaluatedgenepool[choice(bag)][0]['device']

    return (parent1, parent2)

def printmatrix(devicematrix):
    print('Out:')
    for i in range(20):
        s = ''
        for j in range(20):
            a = 'x' if int(devicematrix[i,j]) == 1 else '.'
            s = s + a
        print(s)

def genetic_search(maxgeneration=1000000, targetscore=1.98):
    """Implements a Genetic search"""

    genepool = []
    genepoolsize = 6


    # create the first generation. List of matrices
    genepool = [random_device() for x in range(genepoolsize)]

    # test gene pool. list of result dictionaries
    testedgenepool = list(map(lambda x: test_device(x), genepool))

    # evaluate. list of tuples first element is result dictionary, second is score
    evaluatedgenepool = sorted([(x, performance_metric(x['monitors'])) for x in testedgenepool],
                            key=lambda gene: gene[1])

    for k in range(maxgeneration):
        # choose parents from evaluated list of matrices
        genepool = [xo_device(choose_parents(evaluatedgenepool))
                                for x in range(genepoolsize)]

        # check the performance of the best gene
        if evaluatedgenepool[-1][1] > targetscore:
            print('Found solution in generation {0}'.format(k+1))
            return [evaluatedgenepool[-1][0]['device']]

        # Report the best score in this generation
        print('Generation', k, evaluatedgenepool[-1][1])
        
        # test new gene pool. list of result dictionaries
        testedgenepool = list(map(lambda x: test_device(x), genepool))

        # evaluate. list of tuples first element is result dictionary, second is score
        evaluatedgenepool = sorted([(x, performance_metric(x['monitors'])) for x in testedgenepool],
                                key=lambda gene: gene[1])


    return [evaluatedgenepool[-1][0]['device']]



if __name__ == '__main__':
    for x in genetic_search(maxgeneration=10000, targetscore=1.989):
        printmatrix(x)
