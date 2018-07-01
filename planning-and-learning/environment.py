import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

class Environment():

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.env = np.ones((self.height, self.width)) * 10
        self.generate()

    def generate(self):
        pillar_length = np.random.randint(1, high=(self.height//2)+1)
        for i in range(1,self.width,2):
            pillar_start = np.random.randint(1, high=(self.height//2)+1)
            for j in range(pillar_length):
                self.env[pillar_start+j][i] = 20
        return self.env

    def render(self):
        # create discrete colormap
        cmap = colors.ListedColormap(['red', 'blue'])
        bounds = [0,10,20]
        #norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(self.env, cmap=cmap)

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, self.width, 1));
        ax.set_yticks(np.arange(-.5, self.height, 1));
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        plt.show()

env = Environment(6,9)
env.render()
