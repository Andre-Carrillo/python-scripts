# import itertools
import pandas as pd
import numpy as np
import neat

def test_eval(genomes, config):
    for id, genome in genomes:
        genome.fitness=5
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        #3*a+2*b**2
        a = np.random.randint(100)
        b = np.random.randint(100)
        result = 3*a+2*b**2
        genome.fitness-=abs(net.activate([a, b])[0]-result)


config_path='./config.txt'
config = neat.config.Config(neat.DefaultGenome,
                            neat.DefaultReproduction,
                            neat.DefaultSpeciesSet,
                            neat.DefaultStagnation,
                            config_path)

pop = neat.Population(config)
pop.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter().best_genomes(5)
pop.add_reporter(stats)
# pop.add_reporter(neat.best_gnome(5))
winner = pop.run(test_eval,50)


# prof_df = pd.read_csv('prof.csv')
# class_df = pd.read_csv('class.csv')

# print(prof_df.head())
