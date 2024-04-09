"""
Algorithm:
1. Initialize Variables:
    - numofelems: number of elements in the item list.
    - items: a list of distinct random numbers from 1 to 15 with numofelems elements.
    - target_sum: a random integer in the range [1, sum(items)].
    - population_size: the size of the population.
    - mutation_probability: the probability of mutation.
    - generations: the number of generations to run.

2. Define Functions:
    - generate_population(size): 
        - Generate a population of size chromosomes.
        - Each chromosome is a list of random binary values (0 or 1) representing item selection.

    - calculate_fitness(chromosome): 
        - Calculate the fitness value of a chromosome.
        - Fitness value is 1 if the subset sum equals the target sum, 0 if it exceeds the target sum, 
          or the ratio of subset sum to target sum otherwise.

    - select_chromosomes(population):
        - Select two parent chromosomes based on their fitness values.
        - Parent selection is based on fitness proportionate selection (roulette wheel selection).

    - crossover(parent1, parent2):
        - Perform crossover between two parent chromosomes.
        - Select a random crossover point and exchange the tails of the chromosomes to create two children.

    - mutate(chromosome):
        - Mutate a chromosome with a certain probability.
        - Select a random gene (bit) and flip its value.

    - get_best(population):
        - Get the chromosome with the highest fitness value in the population.

3. Main Loop:
    - Generate an initial population.
    - Iterate for a specified number of generations:
        - Select two parent chromosomes.
        - Perform crossover to produce two children.
        - Optionally mutate the children with a certain probability.
        - Replace the two least fit chromosomes in the population with the children.

4. Print Results:
    - Print the items matrix, target sum, elements that give the target sum, and their sum.

"""
import random
numofelems =   15

items = random.sample(range(1,16),numofelems)


target_sum = random.randint(1, sum(items))

def generate_population(size):
    population = []
    for _ in range(size):
        chromosome = [random.choice([0,   1]) for _ in range(len(items))]
        population.append(chromosome)
    return population

def calculate_fitness(chromosome):
    subset_sum = sum(item * bit for item, bit in zip(items, chromosome))
    if subset_sum == target_sum:
        return  1  
    elif subset_sum > target_sum:
        return  0  
    else:
        return subset_sum / target_sum  


def select_chromosomes(population):
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    fitness_values = [float(i)/sum(fitness_values) for i in fitness_values]
    parent1 = random.choices(population, weights=fitness_values, k=1)[0]
    parent2 = random.choices(population, weights=fitness_values, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(items)-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, len(items)-1)
    chromosome[mutation_point] =   1 - chromosome[mutation_point]
    return chromosome

def get_best(population):
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    max_value = max(fitness_values)
    max_index = fitness_values.index(max_value)
    return population[max_index]

population_size =   10
mutation_probability =   0.2
generations =  200000

population = generate_population(population_size)
for _ in range(generations):
    parent1, parent2 = select_chromosomes(population)
    child1, child2 = crossover(parent1, parent2)
    if random.uniform(0,  1) < mutation_probability:
        child1 = mutate(child1)
    if random.uniform(0,  1) < mutation_probability:
        child2 = mutate(child2)
    
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    min_fitness_indexes = sorted(range(len(fitness_values)), key=lambda x: fitness_values[x])[:2]
    population[min_fitness_indexes[0]] = child1
    population[min_fitness_indexes[1]] = child2


best = get_best(population)

subset_sum = sum(item * bit for item, bit in zip(items, best))

print("Items matrix:", items)
print("Target sum:", target_sum)
print("Elements that give the target sum:", [item for item, bit in zip(items, best) if bit ==  1])
print("Sum = ",sum([item for item, bit in zip(items, best) if bit ==  1]))