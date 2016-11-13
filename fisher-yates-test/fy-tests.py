import matplotlib.pyplot as plt
import numpy as np

from timeit import timeit

def time_tests(test = 'imperative', decksize = 5, number = 10000):
    teststrs = {
    'imperative': """from fy import shuffle_imperative
aimperative = shuffle_imperative(range({0}))""".format(decksize),
    'declarativetuple': """from fy import shuffle_declarative_tuple
adeclarativetuple = shuffle_declarative_tuple(range({0}))""".format(decksize),
    'declarativelist': """from fy import shuffle_declarative_list
adeclarativelist = shuffle_declarative_list(range({0}))""".format(decksize)
    }
    result = timeit(teststrs[test], number=number)
    print test, decksize, number, result
    return result

def profile_test(test = 'imperative', decksize = 5):
    import cProfile
    teststrs = {
    'imperative': """from fy import shuffle_imperative
aimperative = shuffle_imperative(range({0}))""".format(decksize),
    'declarativetuple': """from fy import shuffle_declarative_tuple
adeclarativetuple = shuffle_declarative_tuple(range({0}))""".format(decksize),
    'declarativelist': """from fy import shuffle_declarative_list
adeclarativelist = shuffle_declarative_list(range({0}))""".format(decksize)
    }
    result = cProfile.run(teststrs[test])
    # print test, decksize, number, result
    return result

def scale_test():
    scalefactor = np.linspace(5,500,20)
    timperative = [time_tests(test = 'imperative',decksize=int(x)) for x in scalefactor]
    tdeclarativetuple = [time_tests(test = 'declarativetuple',decksize=int(x)) for x in scalefactor]
    tdeclarativelist = [time_tests(test = 'declarativelist',decksize=int(x)) for x in scalefactor]
    # print scalefactor, time
    with plt.style.context('fivethirtyeight'):
        plt.plot(scalefactor, timperative, label=u"Imperative")
        plt.plot(scalefactor, tdeclarativetuple, label=u"Declarative Tuple")
        plt.plot(scalefactor, tdeclarativelist, label=u"Declarative List")
    ax = plt.gca()
    ax.legend(loc='upper center')
    plt.xlabel('Deck Size')
    plt.ylabel('Time (s)')
    plt.show()

def add_one(matrix, row, column):
    matrix[row, column] = matrix[row, column] + 1
    return matrix

def test_fairness(style):
    # Fairness matrix is a square matrix of dimensions n x n where n is the
    # size od the deck. Each row/column is the position of a certain number and
    # consequently each column/row is the particular number. We expect, with a
    # fair shuffle, each number has equal probability to be placed in any of
    # the positions. So if we repeat the shuffle enough times, then the matrix
    # should have equal numbers for each element.

    decksize = 5

    fairnessmatrix = np.zeros((decksize,decksize))
    deck = range(decksize)
    shuffle = 10000

    for i in range(shuffle):
        shuffleddeck = style(deck)
        # print shuffleddeck
        map(lambda x: add_one(fairnessmatrix, x, shuffleddeck[x]), deck)

    return fairnessmatrix



if __name__ == "__main__":
    # scale_test()

    ### Fairness test
    # from fy import shuffle_imperative, shuffle_declarative_list, shuffle_declarative_tuple
    # fm = test_fairness(shuffle_declarative_tuple)
    # occurancescol = [sum(fm[:,x]) for x in range(len(fm[0,:]))]
    # occurancesrow = [sum(fm[x,:]) for x in range(len(fm[:,0]))]
    # print fm/occurancescol[0]
    # print occurancescol
    # print occurancesrow
    # plt.imshow(fm/occurancescol[0], extent = [0,5,0,5], interpolation='none')
    # plt.colorbar()
    # plt.show()

    # print profile_test(test = 'declarativetuple')
