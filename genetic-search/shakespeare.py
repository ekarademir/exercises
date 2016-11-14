# For python v3.5

import string
from random import randint, choice

def fitness(individual, target):
    """Fitness metric to measure the quality of offspring.
    Just compares two strings character by character. Best score
    is two strings being equal.

    Arguments
    individual - offspring to be tested.
    target     - target string."""

    score = 0
    # This part is for future, if/when we don't keep
    # offspring length constant. Score is calculated through
    # shorter one.
    shorter = target if len(target) < len(individual) else individual
    longer = target if len(target) >= len(individual) else individual
    for i in range(len(shorter)):
        if shorter[i] == longer[i]:
            score = score + 1
    return score

def generate_random_individual(length):
    """Generates a random string of given length."""
    return ''.join(choice(string.ascii_lowercase + ' ') for i in range(length))

def mutation(gene):
    """Mutates the gene. Introduces diversity. Iz gud."""

    # Convert string to list, because strings are immutable.
    gene = list(gene)

    # How many times we should mutate a gene.
    # Each mutation has 20% probability
    mutationtimes = int(randint(0,len(gene)-1)*0.2)

    # Execute mutations.
    for i in range(mutationtimes):
        # Choose a random point in gene to mutate.
        mutationposition = randint(0,len(gene)-1)
        gene[mutationposition] = choice(string.ascii_lowercase + ' ')

    return ''.join(gene)

def genetic_search():
    """Implements a Genetic search without diversity. Which means
    it uses inbreeding. Iz bad."""

    target = "to be or not to be that is the question"

    # Choose a generation size.
    # Number of chromosomes is the length of the string because, why not?
    generationsize = 18*4
    nchromosom = len(target)

    # Create the first generation
    generation = [generate_random_individual(nchromosom) for x in range(generationsize)]

    # Evaluate the fitness and pair the fitness value with offspring
    # via tuples. Then sort them according to fitness metric.
    generation = sorted([(x, fitness(x, target)) for x in generation],
                    key=lambda individual: individual[1])

    # Generations are created limited times.
    # Just in case something goes horribly wrong.
    for k in range(50000):
        # Choose best two
        best1 = generation[-1]
        best2 = generation[-2]

        # If the correct solution is found, then stop searching.
        if best1[1] == nchromosom:
            print("Solution found! in generation", k)
            return best1

        print(best1[0], best1[1])

        # Cross and generate the next generation
        newgeneration = []
        for i in range(generationsize):
            offspring = ''
            for j in range(nchromosom):
                offspring = offspring + choice([best1[0][j], best2[0][j]])

            # Mutation
            offspring = mutation(offspring)

            newgeneration.append(offspring)

        # Sort the new generation and repeat the whole process again.
        generation = sorted([(x, fitness(x, target)) for x in newgeneration],
                        key=lambda individual: individual[1])

    return generation

def genetic_search_diverse():
    """Implements a Genetic search with diversity. Which means
    parents are from different families. Iz gud."""

    target = "to be or not to be that is the question"

    # Choose a generation size.
    # Number of chromosomes is the length of the string because, why not?
    generationsize = 18*4
    nchromosom = len(target)

    # Create the first generation
    generation1 = [generate_random_individual(nchromosom) for x in range(generationsize)]
    generation2 = [generate_random_individual(nchromosom) for x in range(generationsize)]

    # Evaluate the fitness and pair the fitness value with offspring
    # via tuples. Then sort them according to fitness metric.
    generation1 = sorted([(x, fitness(x, target)) for x in generation1],
                    key=lambda individual: individual[1])
    generation2 = sorted([(x, fitness(x, target)) for x in generation2],
                    key=lambda individual: individual[1])

    # Generations are created limited times.
    # Just in case something goes horribly wrong.
    for k in range(50000):
        # Choose best two from each family.
        best1 = generation1[-1]
        best2 = generation2[-1]
        best12 = generation1[-2]
        best22 = generation2[-2]

        # If the correct solution is found, then stop searching.
        if best1[1] == nchromosom:
            print("Solution found! in generation 1,", k)
            return best1
        elif best2[1] == nchromosom:
            print("Solution found! in generation 2,", k)
            return best2

        print(best1[0], best1[1], best2[0], best2[1])

        # Cross and generate the next generation. Crossing is
        # between highest performing individuals of two families.
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

        # Sort the new generation and repeat the whole process again.
        generation1 = sorted([(x, fitness(x, target)) for x in newgeneration1],
                        key=lambda individual: individual[1])
        generation2 = sorted([(x, fitness(x, target)) for x in newgeneration2],
                        key=lambda individual: individual[1])

    return generation1+generation2



if __name__ == '__main__':

    print(genetic_search_diverse())
