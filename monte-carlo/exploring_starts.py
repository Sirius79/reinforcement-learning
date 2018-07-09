import gym
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import defaultdict

class Agent():

    def __init__(self):

        self.policy = defaultdict(lambda: np.random.random(size=2))
        self.Q = defaultdict(lambda: np.random.randint(26,size=2))
        self.returns_hit = defaultdict(list)
        self.returns_stick = defaultdict(list) 

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
            
            action = np.argmax(self.policy[state])
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
            
            for step in range(len(states)):

                G += rewards[step]

                if states[step] not in states[0:step]:
                    action_taken = actions[step]
                    if action_taken == 0:
                        current_state = self.returns_hit[states[step]]
                        current_state.append(G)
                        self.Q[states[step][action_taken]] = sum(current_state)/len(current_state)
                    else:
                        current_state = self.returns_stick[states[step]]
                        current_state.append(G)
                        self.Q[states[step][action_taken]] = sum(current_state)/len(current_state)
                        
                    self.policy[states[step][np.argmax(self.Q[states[step]][action_taken])]] = 1

        return self.policy
        
episode_num = 1000


env = gym.make('Blackjack-v0')
agent = Agent()
v_pi = agent.play()
