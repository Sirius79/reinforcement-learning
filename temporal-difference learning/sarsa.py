import gym
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

class Sarsa():

    def __init__(self, alpha, epsilon, gamma):
        '''
            alpha: step size (0,1]
            epsilon: greedy probability small>0
            gamma: discount factor
        '''
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.Q = defaultdict(lambda: np.zeros(2))

    def greedy_policy(self, state):
        '''
            returns action from state using epsilon greedy policy
            derived from Q
        '''
        prob = np.random.random()
        if prob <= self.epsilon:
            return np.random.randint(2)
        else:
            return np.argmax(self.Q[state])

    def play(self):
        score = 0
        for episode in range(1000):
            
            state = env.reset()
            action = self.greedy_policy(tuple(state))
            
            for step in itertools.count():
                
                observation, reward, done, info = env.step(action)
                next_action = self.greedy_policy(tuple(observation))
                self.Q[tuple(state)][action] += self.alpha * (reward + (self.gamma * self.Q[tuple(observation)][action]) - self.Q[tuple(state)][action])

                if step > score:
                    score = step
                state = observation
                action = next_action

                if done:
                    break
        return self.Q,score

alpha = 0.5
epsilon = 0.1
gamma = 0.8

env = gym.make('CartPole-v0')
agent = Sarsa(alpha, epsilon, gamma)
Q,score = agent.play()
print(score)
i = 1
for k,v in dict(Q).items():
    if i==10:
        break
    print(k,v)
    i += 1
