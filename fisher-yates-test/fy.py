def shuffle_imperative(unshuffledlist):
    from random import randint
    #print range(len(unshuffledlist)-1,-1,-1)
    for i in range(len(unshuffledlist)-1,-1,-1):
        shuffleindex = randint(0, i)
        #print shuffleindex
        unshuffledlist[shuffleindex],unshuffledlist[i] \
                    = unshuffledlist[i],unshuffledlist[shuffleindex]
    return unshuffledlist # now shuffled ofcourse

def swap_tuple(l, s1, s2):
    if s1 == s2:
        return l
    elif s1 > s2:
        s2,s1 = s1,s2
    ln = l[0:s1]+l[s2:s2+1]+l[s1+1:s2]+l[s1:s1+1]+l[s2+1:]
    return ln

def swap_list(l, s1, s2):
    l = list(l)
    l[s1], l[s2] = l[s2], l[s1]
    return l

def shuffle_declarative_tuple(l):
    from random import randint
    r = len(l)
    return reduce(lambda a,x: swap_tuple(a, x, randint(0,x)), range(r-1,-1,-1), l)

def shuffle_declarative_list(l):
    from random import randint
    r = len(l)
    return reduce(lambda a,x: swap_list(a, x, randint(0,x)), range(r-1,-1,-1), l)

def pick_place(remainingdeck,accumulationgdeck):
    # from random import random
    from random import randint
    if not remainingdeck:
        return accumulationgdeck

    # print accumulationgdeck
    position = randint(0,len(accumulationgdeck))
    accumulationgdeck = accumulationgdeck[0:position] \
                            +remainingdeck[0:1] \
                            +accumulationgdeck[position:]
    # print position, accumulationgdeck
    return pick_place(remainingdeck[1:],accumulationgdeck)
    # if random() >= 0.5:
    #     return pick_place(remainingdeck[1:],remainingdeck[0:1]+accumulationgdeck)
    # else:
    #     return pick_place(remainingdeck[1:],accumulationgdeck+remainingdeck[0:1])

def shuffle_deck(deck):
    return pick_place(deck,[])
