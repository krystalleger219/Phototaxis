from individual import INDIVIDUAL
import copy
import random
class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize


    def Print(self):
        for i in self.p:
            if ( i in self.p):
                self.p[i].Print()


    def Evaluate(self, envs, pp, pb):
        for i in self.p:
            self.p[i].fitness = 0
        for e in range(0,envs.numEnvs):
            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e], pp,pb)
            for i in self.p:
                self.p[i].Compute_Fitness()
        for i in self.p:
            self.p[i].fitness = self.p[i].fitness/envs.numEnvs

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if (self.p[i].fitness < other.p[i].fitness):
                self.p[i] = other.p[i]

    def Initialize(self):
        for i in range (0, self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Fill_From(self, other):
        self.Copy_Best_From(other)
        print
        self.Collect_Children_From(other)

    def Copy_Best_From(self,other):
        best = 0
        for i in other.p:
            current = i
            if other.p[current].fitness > other.p[best].fitness:
                best = current
        self.p[0] = copy.deepcopy(other.p[best])

    def Collect_Children_From(self,other):
        for i in range (1, self.popSize):
            winner = other.Winner_of_Tournament_Selection()
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()

    def Winner_of_Tournament_Selection(self):
        p1 = random.randint(0,self.popSize-1)
        p2 = random.randint(0, self.popSize-1)
        while p1 == p2:
            p2 = random.randint(0, self.popSize-1)
        if self.p[p1].fitness > self.p[p2].fitness:
            return self.p[p1]
        elif self.p[p1].fitness < self.p[p2].fitness:
            return self.p[p2]





