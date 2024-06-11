# random_straws.py
# write a program to perform one million runs of an experiment that places a varying number of straws end-to-end on each run
# in each run, start with a single straw of random length between 0 and 1 (inclusive)
# then enter a loop that keeps adding additional straws of random length until the total length > 1
# what is the mean number of straws added before the total length > 1 across all million runs of the experiment

import numpy as np
#run a trial
def run_trial():
    #initialize length to zero and number of straws to zero
    total_length = 0.0
    num_straws = 0
    #add straws until total length is greater than 1
    while total_length <= 1.0:
        total_length += 1 - np.random.rand()
        num_straws += 1
    #exit the loop once total length exceeds 1: return the number of straws it took 
    return num_straws


def main():
    # 1 million trials, 0 straws initially
    trials = 1_000_000
    straws = 0
    # anonymous placeholder (trial number doesn't matter because it isn't used anywhere else)
    for _ in range(trials):
        #run a million trials
        straws += run_trial()
    #find the average straws per trial
    print(straws / trials)
    print(np.e)


main()
