from timeit import timeit
##################################################
# Fisher-Yates Shuffle

#### Imperative
print timeit("""
def shuffleImperative(unshuffledlist):
    from random import randint
    for i in range(len(unshuffledlist)-1,-1,-1):
        shuffleindex = randint(0, i)
        t = unshuffledlist[shuffleindex]
        unshuffledlist[shuffleindex] = unshuffledlist[i]
        unshuffledlist[i] = t
    return unshuffledlist
a = shuffleImperative(range(50))
""")
# print unshuffledlist

#### Declerative
print timeit("""
def swap(l, s1, s2):
    l = list(l)
    l[s1], l[s2] = l[s2], l[s1]
    return l

def shuffleDeclerative(l):
    from random import randint
    r = len(l)
    return reduce(lambda a,x: swap(a, x, randint(0,x)), range(r-1,-1,-1), l)

a = shuffleDeclerative(range(50))
""")

# print shuffle2(a)
