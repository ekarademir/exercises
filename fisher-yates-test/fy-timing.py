from timeit import timeit
from fy import shuffle_declarative_list, \
               shuffle_declarative_tuple, \
               shuffle_imperative


def time_tests(test = 'imperative', decksize = 5, number = 10000):
    teststrs = {
    'imperative': """from fy import shuffle_imperative
aimperative = shuffle_imperative(range({0}))""".format(decksize),
    'declarativetuple': """from fy import shuffle_declarative_tuple
adeclerativetuple = shuffle_declerative_tuple(range({0}))""".format(decksize),
    'declarativelist': """from fy import shuffle_declarative_list
adeclarativelist = shuffle_declarative_list(range({0}))""".format(decksize)
    }

    return timeit(teststrs[test], number=number)

if __name__ == "__main__":
    print time_tests('declarativetuple')
