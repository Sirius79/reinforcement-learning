import gym
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

class Agent():

    def __init__(self):
        '''
            First-visit Monte-Carlo preidction for estimating optimal value function
        '''
        
        self.V = defaultdict(float)
        self.returns = defaultdict(list)

    def policy(self, state):
        return 0 if state[0]<21 else 1

    def generate(self):
        '''
            Generate an episode following the policy
        '''
        state = env.reset()
        states = []
        rewards = []

        states.append(state)
        for step in itertools.count():
            
            action = self.policy(state)
            observation,reward,done,_ = env.step(action)
            states.append(observation)
            rewards.append(reward)

            if done:
                break
                
        states.pop()
        
        return states, rewards
            

    def play(self):
        
        for episode in range(episode_num):

            states, rewards = self.generate()
            G = 0.0
            
            for step in range(len(states)):
           
                G += rewards[step]

                if states[step] not in states[0:step]:
                    current_state = self.returns[states[step]]
                    current_state.append(G)
                    self.V[states[step]] = sum(current_state)/len(current_state)

        return self.V
        
episode_num = 1000


env = gym.make('Blackjack-v0')
agent = Agent()
v_pi = agent.play()

print(dict(v_pi))
