import pygad
import numpy as np

def fitness_func(ga_instance, x, solution_idx):
    a = 2
    b = -4
    c = 3
    return a * x**2 + b * x + c

# Define the genetic algorithm parameters
ga_instance = pygad.GA(num_generations=100,
                       num_parents_mating=5,
                       fitness_func=fitness_func,
                       sol_per_pop=50,
                       num_genes=1,
                       init_range_low=-10.0,
                       init_range_high=10.0,
                       mutation_percent_genes=10,
                       mutation_by_replacement=True,
                       crossover_type="single_point",
                       mutation_type="random",
                       crossover_probability=0.5,
                       mutation_probability=0.2,
                       parent_selection_type="sss",
                       keep_parents=1,
                       on_generation=None)

# Run the genetic algorithm
ga_instance.run()

# Get the best solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()

print("Best individual: ", solution)
print("Minimum value: ", solution_fitness)
