import timeit

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print names


#################

# t = timeit.timeit("hashednames = map(hash, ['Mary', 'Isla', 'Sam'])")
# print t
hashednames = map(hash, names)

print hashednames
