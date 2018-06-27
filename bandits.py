'''
    k Bandit problem
'''
import numpy as np
import matplotlib.pyplot as plt

class Bandit():

    def __init__(self, k):
        self.k = k # number of bandits
        self.true_val = np.random.normal(0,1,self.k) # q*(a)

    def reward(self, t):
        return np.random.normal(self.true_val[t],1,1) #R_t


class Agent():

    def __init__(self, bandit, epsilon):
        self.epsilon = epsilon
        self.Q = np.zeros(bandit.k) # Q(a)
        self.N = np.zeros(bandit.k, dtype=int) # N(a)

    def select_action(self, bandit):
        prob = np.random.random()
        if prob <= self.epsilon:
            return np.random.randint(bandit.k) # choose random action
        else:
            return np.argmax(self.Q) # argmax Q(a)

    def update(self, action, reward):
        self.N[action] += 1
        self.Q[action] += (1/self.N[action]) * (reward - self.Q[action])

    def play(self):
        rewards = []
        for t_step in range(1000):
            action = self.select_action(bandit)
            reward = bandit.reward(action)
            self.update(action, reward)
            rewards.append(reward)
        return np.array(rewards)

k = 10
epsilon = 0.01

bandit = Bandit(k)
agent = Agent(bandit, epsilon)
rewards = agent.play()

plt.plot(rewards)
plt.xlabel("Steps")
plt.ylabel("Rewards")
plt.xlim([1,1000])
plt.show()
