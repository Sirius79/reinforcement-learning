import gym
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

class Agent():

    def __init__(self, gamma):

        self.gamma = gamma
        self.Q = defaultdict(lambda: np.random.randint(26,size=2))
        self.b = defaultdict(lambda: np.random.random(size=2))
        self.C = defaultdict(lambda: np.zeros(2))
        self.policy = defaultdict(int)

    def generate(self):
        '''
            Generate an episode following the policy
        '''
        state = env.reset()
        states = []
        actions = []
        rewards = []

        states.append(state)
        
        for step in itertools.count():
            
            action = np.argmax(self.b[state])
            actions.append(action)
            state,reward,done,_ = env.step(action)
            states.append(state)
            rewards.append(reward)

            if done:
                break

        states.pop()
        
        return states, actions, rewards
            

    def play(self):
        
        for episode in range(episode_num):

            states, actions, rewards = self.generate()
            G = 0.0
            W = 1.0
            
            for step in range(len(states)):

                current_state = states[step]
                current_action = actions[step]
                
                G = self.gamma * G + rewards[step]
                self.C[current_state][current_action] += W
                self.Q[current_state][current_action] += (W * (G - self.Q[current_state][current_action]) / self.C[current_state][current_action])
                self.policy[current_state] = np.argmax(self.Q[current_state])

                if self.policy[current_state] != current_action:
                    break

                W /= self.b[current_state][current_action] 
        return self.policy
        
episode_num = 1000


env = gym.make('Blackjack-v0')
agent = Agent(0.9)
v_pi = agent.play()
print(len(v_pi))
print(dict(v_pi))
