import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

class Environment():

    def __init__(self, height, width):
        '''
            height: grid height
            width: grid width
            env: environment state
            start_pos: starting position of agent
            end_pos: destination of agent
            done: flag raised when agent moves out of grid or crashes into pillar
        '''
        self.height = height
        self.width = width
        self.env = np.ones((self.height, self.width)) * 10
        self.start_pos = np.random.randint(0, high=(self.height))
        self.end_pos = np.random.randint(0, high=(self.height))
        self.agent_pos = [0,0]
        self.done = 0
        self.generate()

    def generate(self):
        '''
            10: walkable tiles
            20: pillar
            40: starting tile
            200: goal tile
            40: agent tile
        '''
        pillar_length = np.random.randint(1, high=(self.height//2)+1)
        for i in range(1,self.width,2):
            pillar_start = np.random.randint(1, high=(self.height//2)+1)
            for j in range(pillar_length):
                self.env[pillar_start+j][i] = 20
        
        self.env[self.start_pos][0] = 40
        self.agent_pos = [self.start_pos, 0]
        self.env[self.end_pos][self.width-1] = 200

    def step(self, action):
        '''
            action_space: [0:'UP',1:'DOWN',2:'RIGHT',3:'LEFT'] denotes the possible movements of agent
        '''
        if action not in range(4):
            return "Error: action out of action_space"
        
        elif action == 0:
            if self.agent_pos[0]-1 >= 0 and self.env[self.agent_pos[0]-1][self.agent_pos[1]] != 20:
                self.env[self.agent_pos[0]][self.agent_pos[1]] = 10
                self.agent_pos[0] -= 1
                if self.env[self.agent_pos[0]][self.agent_pos[1]] == 200:
                    reward = 1
                    self.done = 1
                    self.reset()
                    return self.env, reward, self.done
                reward =  0
                self.env[self.agent_pos[0]][self.agent_pos[1]] = 40
                return self.env, reward, self.done
            else:
                self.done = 1
                reward = -1
                self.reset()
                return self.env, reward, self.done
        
        elif action == 1:
            if self.agent_pos[0]+1 < self.height and self.env[self.agent_pos[0]+1][self.agent_pos[1]] != 20:
                self.env[self.agent_pos[0]][self.agent_pos[1]] = 10
                self.agent_pos[0] += 1
                if self.env[self.agent_pos[0]][self.agent_pos[1]] == 200:
                    reward = 1
                    self.done = 1
                    self.reset()
                    return self.env, reward, self.done
                reward =  0
                self.env[self.agent_pos[0]][self.agent_pos[1]] = 40
                return self.env, reward, self.done
            else:
                self.done = 1
                reward = -1
                self.reset()
                return self.env, reward, self.done

        elif action == 2:
            if self.agent_pos[1]+1 < self.width and self.env[self.agent_pos[0]][self.agent_pos[1]+1] != 20:
                self.env[self.agent_pos[0]][self.agent_pos[1]] = 10
                self.agent_pos[1] += 1
                if self.env[self.agent_pos[0]][self.agent_pos[1]] == 200:
                    reward = 1
                    self.done = 1
                    self.reset()
                    return self.env, reward, self.done
                reward =  0
                self.env[self.agent_pos[0]][self.agent_pos[1]] = 40
                return self.env, reward, self.done
            else:
                self.done = 1
                reward = -1
                self.reset()
                return self.env, reward, self.done

        elif action == 3:
            if self.agent_pos[1]-1 > 0 and self.env[self.agent_pos[0]][self.agent_pos[1]-1] != 20:
                self.env[self.agent_pos[0]][self.agent_pos[1]] = 10
                self.agent_pos[1] -= 1
                if self.env[self.agent_pos[0]][self.agent_pos[1]] == 200:
                    reward = 1
                    self.done = 1
                    self.reset()
                    return self.env, reward, self.done
                reward =  0
                self.env[self.agent_pos[0]][self.agent_pos[1]] = 40
                return self.env, reward, self.done
            else:
                self.done = 1
                reward = -1
                self.reset()
                return self.env, reward, self.done

    def reset(self):
        '''
            Resets the environment state at end of each episode
        '''
        self.agent_pos = [self.start_pos, 0]
        self.env[self.end_pos][self.width-1] = 200
        return
            

    def render(self):
        '''
            display the environment state
        '''
        # create discrete colormap
        cmap = colors.ListedColormap(['red','blue', 'yellow', 'yellow'])
        bounds = [10,20,40,100,200]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(self.env, cmap=cmap, norm=norm)

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, self.width, 1));
        ax.set_yticks(np.arange(-.5, self.height, 1));
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        plt.show()

env = Environment(6,9)
print(env.env)
while True:
    action = np.random.randint(0, high=4)
    obs, reward, done = env.step(action)
    print(action)
    print(env.env)
    env.render()
    if done:
        env.render()
        print(env.env)
        break
