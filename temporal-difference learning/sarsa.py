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
            Q: estimated action value for state-action pair. It uses a defaultdict whose key is observation(state) 
               and columns are the possible actions with the cells indicating the estimated action value at each time step.
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
            return np.argmax(self.Q[state])

    def play(self):
        score = np.zeros(episode_num)
        for episode in range(episode_num):
            
            state = env.reset()
            action = self.greedy_policy(tuple(state))
            
            for step in itertools.count():
                
                observation, reward, done, info = env.step(action)
                next_action = self.greedy_policy(tuple(observation))
                self.Q[tuple(state)][action] += self.alpha * (reward + (self.gamma * self.Q[tuple(observation)][action]) - self.Q[tuple(state)][action])

                state = observation
                action = next_action

                if done:
                    score[episode] = step
                    break
        return self.Q,score

alpha = 0.3
epsilon = 0.25
gamma = 0.8
episode_num = 5000

env = gym.make('CartPole-v0')
agent = Sarsa(alpha, epsilon, gamma)
Q,score = agent.play()
print(np.amax(score)) # print maximum time steps pole is balanced

# plot time steps over episodes

plt.plot(score)
plt.xlabel("Episodes")
plt.ylabel("Time steps")
plt.xlim([1,episode_num])
plt.show()
