import math
import random
import numpy
import random
import constants as c
from robot import ROBOT
from pyrosim import PYROSIM

class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = numpy.random.random((5,8)) * 2 - 1

        self.fitness = 0

    def Start_Evaluation(self, env, pp, pb):

        self.sim = PYROSIM(playPaused = pp, playBlind = pb, evalTime=c.evaluationTime )
        robot = ROBOT(self.sim, self.genome)
        env.Send_To(self.sim)
        self.sim.Start()

    def Compute_Fitness(self):
        self.sim.Wait_To_Finish()
        y = self.sim.Get_Sensor_Data(sensorID = 4)
        self.fitness = self.fitness + y[-1]
        del self.sim


    def Mutate(self):
        geneToMutateX = random.randint(0,4)
        geneToMutateY = random.randint(0,7)
        self.genome[geneToMutateX, geneToMutateY] = random.gauss(self.genome[geneToMutateX, geneToMutateY], math.fabs(self.genome[geneToMutateX, geneToMutateY]))

    def Print(self):
         print '[',
         print self.ID,
         print self.fitness,
         print ']',
         print "",