from tmrl import get_environment
from time import sleep
import numpy as np
import random

""""
This document was meant for testing purposes, to test if the library work and play around with it.
"""


# actions: [Gas, Brake, Steer] MinVal: -1, MaxVal: 1
# Current actions for testing not optimal
def Get_Action():
    steer = random.uniform(-1, 1)
    gas = 1
    brake = 0
    return np.array([gas, brake, steer])


env = get_environment()

sleep(1.0)

# Test Runs:
episodes = 5
for episode in range(episodes + 1):
    obs, info = env.reset()
    terminated = False
    score = 0

    while not terminated:
        action = Get_Action()
        obs, rew, terminated, truncated, info = env.step(action)
        score += rew
    print('Episode: {}, Score: {}'.format(episode, score))
    sleep(1.0)
