import gym
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

class QLearning():

    def __init__(self, alpha, epsilon, gamma):
        '''
            alpha: step size (0,1]
            epsilon: greedy probability small>0
            gamma: discount factor
        '''
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.Q = defaultdict(lambda: np.random.randint(10,size=2))

    def greedy_policy(self, state):
        '''
            returns action from state using epsilon greedy policy
            derived from Q
        '''
        prob = np.random.random()
        if prob <= self.epsilon:
            return np.random.randint(2)
        else:
            #print(np.argmax(self.Q[state]), self.Q[state])
            return np.argmax(self.Q[state])

    def play(self):
        score = np.zeros(episode_num)
        for episode in range(episode_num):
            
            state = env.reset()
            
            for step in itertools.count():
                action = self.greedy_policy(tuple(state))
                observation, reward, done, info = env.step(action)
                next_action = np.argmax(self.Q[tuple(observation)])
                self.Q[tuple(state)][action] += self.alpha * (reward + (self.gamma * self.Q[tuple(observation)][next_action]) - self.Q[tuple(state)][action])

                state = observation

                if done:
                    score[episode] = step
                    break
        return self.Q,score

alpha = 0.3
epsilon = 0.25
gamma = 0.8
episode_num = 5000

env = gym.make('CartPole-v0')
agent = QLearning(alpha, epsilon, gamma)
Q,score = agent.play()
print(np.amax(score))

plt.plot(score)
plt.xlabel("Episodes")
plt.ylabel("Time steps")
plt.xlim([1,episode_num])
plt.show()
