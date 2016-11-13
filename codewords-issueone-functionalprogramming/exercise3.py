from timeit import timeit
##################################################
# Fisher-Yates Shuffle

#### Imperative
# print timeit("""
def shuffleImperative(unshuffledlist):
    from random import randint
    for i in range(len(unshuffledlist)-1,-1,-1):
        shuffleindex = randint(0, i)
        t = unshuffledlist[shuffleindex]
        unshuffledlist[shuffleindex] = unshuffledlist[i]
        unshuffledlist[i] = t
    return unshuffledlist
a = shuffleImperative(range(50))
# """)
# print a
#### Declerative
# print timeit("""
def swap(l, s1, s2):
    if s1 == s2:
        return l
    elif s1 > s2:
        s2,s1 = s1,s2
    ln = l[0:s1]+l[s2:s2+1]+l[s1+1:s2]+l[s1:s1+1]+l[s2+1:]
    # l = list(l)
    # l[s1], l[s2] = l[s2], l[s1]
    # print ln, s1, s2
    return ln
# def swap(l, s1, s2):
#     l = list(l)
#     l[s1], l[s2] = l[s2], l[s1]
#     return tuple(l)

def shuffleDeclerative(l):
    from random import randint
    r = len(l)
    # print l
    return reduce(lambda a,x: swap(a, x, randint(0,x)), range(r-1,-1,-1), l)

a = shuffleDeclerative(tuple(range(50)))
# """)

# print swap(tuple(range(5)), 3, 2)
# print a
