from individual import INDIVIDUAL
import copy
import random
from environment import ENVIRONMENT
class ENVIRONMENTS:
    def __init__(self, numEnvs):
        self.envs = {}
        self.numEnvs = numEnvs
        for i in range (0, self.numEnvs):
            self.envs[i] = ENVIRONMENT(i)