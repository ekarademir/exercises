from random import randint, randrange

sum = reduce(lambda a, x: a+x, [0,1,2,3,4])

# print sum


people = [{'name': 'Mary', 'height': 160},
    {'name': 'Isla', 'height': 80},
    {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    # print average_height
    # => 120

############
hlist = map(lambda x: x['height'],
    filter(lambda x: 'height' in x, people)
    )
tot = len(hlist)
# print reduce(lambda a,x: a+x, hlist)/tot
