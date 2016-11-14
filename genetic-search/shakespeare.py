import string
from random import randint, choice

def fitness(individual, target):
    score = 0
    shorter = target if len(target) < len(individual) else individual
    longer = target if len(target) >= len(individual) else individual
    for i in range(len(shorter)):
        if shorter[i] == longer[i]:
            score = score + 1
    return score

def generate_random_individual(length):
    return ''.join(choice(string.ascii_lowercase + ' ') for i in range(length))

def mutation(gene):
    gene = list(gene)
    mutationtimes = int(randint(0,len(gene)-1)*0.2)
    for i in range(mutationtimes):
        mutationposition = randint(0,len(gene)-1)
        gene[mutationposition] = choice(string.ascii_lowercase + ' ')

    return ''.join(gene)

def genetic_search():
    """Implements a Genetic search"""

    target = "to be or not to be that is the question"

    generationsize = 18*4
    nchromosom = len(target)

    # create the first generation
    generation = [generate_random_individual(nchromosom) for x in range(generationsize)]

    # evaluate the fitness
    generation = sorted([(x, fitness(x, target)) for x in generation],
                    key=lambda individual: individual[1])

    for k in range(50000):
        # choose best two
        best1 = generation[-1]
        best2 = generation[-2]

        if best1[1] == nchromosom:
            print("Solution found! in generation", k)
            return best1

        print(best1[0], best1[1])
        # print(best2[0], best2[1])
        #cross and generate the next generation
        newgeneration = []
        for i in range(generationsize):
            offspring = ''
            for j in range(nchromosom):
                offspring = offspring + choice([best1[0][j], best2[0][j]])

            #mutation
            offspring = mutation(offspring)

            newgeneration.append(offspring)

        generation = sorted([(x, fitness(x, target)) for x in newgeneration],
                        key=lambda individual: individual[1])

    return generation

def genetic_search_diverse():
    """Implements a Genetic search"""

    target = "to be or not to be that is the question"

    generationsize = 18*4
    nchromosom = len(target)

    # create the first generation
    generation1 = [generate_random_individual(nchromosom) for x in range(generationsize)]
    generation2 = [generate_random_individual(nchromosom) for x in range(generationsize)]

    # evaluate the fitness
    generation1 = sorted([(x, fitness(x, target)) for x in generation1],
                    key=lambda individual: individual[1])
    generation2 = sorted([(x, fitness(x, target)) for x in generation2],
                    key=lambda individual: individual[1])

    for k in range(50000):
        # choose best two
        best1 = generation1[-1]
        best2 = generation2[-1]
        best12 = generation1[-2]
        best22 = generation2[-2]

        if best1[1] == nchromosom:
            print("Solution found! in generation 1,", k)
            return best1
        elif best2[1] == nchromosom:
            print("Solution found! in generation 2,", k)
            return best2

        print(best1[0], best1[1], best2[0], best2[1])
        # print(best2[0], best2[1])
        #cross and generate the next generation
        newgeneration1 = []
        newgeneration2 = []
        for i in range(generationsize):
            offspring1 = ''
            offspring2 = ''
            for j in range(nchromosom):
                offspring1 = offspring1 + choice([best1[0][j], best2[0][j]])
                offspring2 = offspring2 + choice([best12[0][j], best22[0][j]])

            #mutation
            offspring1 = mutation(offspring1)
            offspring2 = mutation(offspring2)

            newgeneration1.append(offspring1)
            newgeneration2.append(offspring2)

        generation1 = sorted([(x, fitness(x, target)) for x in newgeneration1],
                        key=lambda individual: individual[1])
        generation2 = sorted([(x, fitness(x, target)) for x in newgeneration2],
                        key=lambda individual: individual[1])

    return generation1+generation2



if __name__ == '__main__':

    print(genetic_search_diverse())
