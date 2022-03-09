import random
import numpy as np
def simulate(pop=10000, sample_size=500, times=1000, coeficient_of_std=2):
    #Calculate random dsitribution of red balls
    red = random.randint(sample_size, 10000)
    red_rate = red / pop
    
    #calculate random samples
    times_correctly_predicted = 0
    for i in range(times):

        sample = np.random.random((1, sample_size))
        comparison_value = np.full(sample.shape, red_rate)
        sample = np.greater_equal(comparison_value, sample)
        #This takes the ration of the ones
        sample_rate = np.sum(sample)/sample_size

        sample_std = (sample_rate*(1-sample_rate)/sample_size)**.5
        sample_range = [sample_rate+coeficient_of_std*sample_std, sample_rate-coeficient_of_std*sample_std]
        real_rate_is_correctly_predicted = (red_rate > sample_range[1]) and (red_rate < sample_range[0])
        times_correctly_predicted += real_rate_is_correctly_predicted
    return times_correctly_predicted/(i+1)*100

print(simulate(coeficient_of_std=2, times=10000))
print(simulate(coeficient_of_std=1.5, times=10000))

