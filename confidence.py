import random
import numpy as np

pop = 10000
sample_size = 500
times = 200 
#Calculate random dsitribution of red balls
#Something wrong is here, idk why i have to make the rate to be more than a half
red = random.randint(5000, 10000)
red_rate = red / pop

#calculate random samples
times_correctly_predicted = 0
for i in range(times):
    sample = np.floor(np.random.random((1, sample_size))/red_rate)
    sample_rate = np.sum(sample)/sample_size
    sample_std = (sample_rate*(1-sample_rate)/sample_size)**.5
    sample_range = [sample_rate+2*sample_std, sample_rate-2*sample_std]
    real_rate_is_correctly_predicted = (red_rate > sample_range[1]) or (red_rate <sample_range[0])
    times_correctly_predicted += real_rate_is_correctly_predicted
    print(times_correctly_predicted/(i+1)*100)
