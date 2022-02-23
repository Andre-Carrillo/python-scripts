# import itertools
import pandas as pd
import numpy as np
import neat


def test_eval(genomes, config):
    for id, genome in genomes:
        genome.fitness=5
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        print(net.activate([2,1]))


        

config_path='./config.txt'
config = neat.config.Config(neat.DefaultGenome,
                            neat.DefaultReproduction,
                            neat.DefaultSpeciesSet,
                            neat.DefaultStagnation,
                            config_path)

pop = neat.Population(config)
pop.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
pop.add_reporter(stats)
winner = pop.run(test_eval,50)


# prof_df = pd.read_csv('prof.csv')
# class_df = pd.read_csv('class.csv')

# print(prof_df.head())