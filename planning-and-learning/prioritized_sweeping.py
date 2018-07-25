import gym
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict
import heapq

class Agent():

    def __init__(self, gamma, alpha, theta, epsilon):
        '''
            gamma: discount factor
            epsilon: greedy
            theta: threshold value
            alpha: step
            Q: prob per action, s->a
            model: s,a-> r,s'
        '''
        self.gamma = gamma
        self.alpha = alpha
        self.theta = theta
        self.epsilon = epsilon
        self.Q = defaultdict(lambda: np.random.rand(2))
        self.model = defaultdict(lambda: np.random.rand(5))
        self.PQueue = []

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
        
        for episode in range(episode_num):

            state = env.reset()
            action = self.greedy_policy(tuple(state))
            observation, reward, done, info = env.step(action)
            self.model[(*state,action)] = np.asarray((reward, *observation))
            P = abs(reward + (self.gamma * self.Q[tuple(observation)][np.argmax(self.Q[tuple(observation)])] - self.Q[tuple(state)][action]))
            print(P)
                    
            
            
        
episode_num = 2


env = gym.make('CartPole-v0')
agent = Agent(0.1,0.1,0.95,0.1)
agent.play()
