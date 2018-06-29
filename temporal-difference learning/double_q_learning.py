import gym
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

class DoubleQLearning():

    def __init__(self, alpha, epsilon, gamma):
        '''
            alpha: step size (0,1]
            epsilon: greedy probability small>0
            gamma: discount factor
        '''
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.Q1 = defaultdict(lambda: np.random.randint(10,size=2))
        self.Q2 = defaultdict(lambda: np.random.randint(5,size=2))

    def greedy_policy(self, state):
        '''
            returns action from state using epsilon greedy policy
            derived from Q
        '''
        prob = np.random.random()
        if prob <= self.epsilon:
            action = np.random.randint(2)
            return action
        else:
            #print(np.argmax(self.Q[state]), self.Q[state])
            if np.amax(self.Q1[state]) >= np.amax(self.Q2[state]):
                action = np.argmax(self.Q1[state])
                return action
            else:
                action = np.argmax(self.Q2[state])
                return action

    def play(self):
        score = np.zeros(episode_num)
        for episode in range(episode_num):
            
            state = env.reset()
            
            for step in itertools.count():
                prob = np.random.random()
                action = self.greedy_policy(tuple(state))
                observation, reward, done, info = env.step(action)
                if prob <= 0.5:
                    next_action = np.argmax(self.Q1[tuple(observation)])
                    self.Q1[tuple(state)][action] += self.alpha * (reward + (self.gamma * self.Q2[tuple(state)][next_action]) - self.Q1[tuple(state)][action])
                else:
                    next_action = np.argmax(self.Q2[tuple(observation)])
                    self.Q2[tuple(state)][action] += self.alpha * (reward + (self.gamma * self.Q1[tuple(state)][next_action]) - self.Q2[tuple(state)][action])

                state = observation

                if done:
                    score[episode] = step
                    break
        return score

alpha = 0.1
epsilon = 0.12
gamma = 0.94
episode_num = 2000

env = gym.make('CartPole-v0')
agent = DoubleQLearning(alpha, epsilon, gamma)
score = agent.play()
print(np.amax(score))

plt.plot(score)
plt.xlabel("Episodes")
plt.ylabel("Time steps")
plt.xlim([1,episode_num])
plt.show()
