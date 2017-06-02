import copy
import math
import constants as c
from environments import ENVIRONMENTS
from population import POPULATION

envs = ENVIRONMENTS(c.numEnvs)


parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp = False, pb = True)
parents.Print()
# print
#
for g in range(0,c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs,pp = False, pb = True)
    children.Print()
    parents = children
best = 0
for i in children.p:
    current = i
    if children.p[current].fitness > children.p[best].fitness:
        best = current
for env in range(0,4):
    children.p[best].Start_Evaluation(envs.envs[env], pp = True, pb = False)


#     children = copy.deepcopy(parents)
#     children.Mutate()
#     children.Evaluate()
#     parents.ReplaceWith(children)
#     print g,
#     parents.Print()
#     print
#
# for i in range (0,10):
#     parents.p[i].Start_Evaluation(False)

# import matplotlib.pyplot as plt
# import random
# from individual import INDIVIDUAL
# from robot import ROBOT
# from pyrosim import PYROSIM
# import copy
# import pickle
#
#
# parent = INDIVIDUAL()
# parent.Evaluate(True)
#
# for i in range(0,10):
#     child = copy.deepcopy( parent )
#     child.Mutate()
#     child.Evaluate(True)
#     print "[g:",i,"]" "[pw:", parent.genome, "]""[p:", parent.fitness, "]","[c:",child.fitness,"]"
#     if (child.fitness > parent.fitness):
#         child.Evaluate(True)
#         parent = child
#         f = open('robot.p', 'w')
#         pickle.dump(parent, f)
#         f.close()


    # sim = PYROSIM(playPaused = False, evalTime=200)
    #robot = ROBOT(sim, self.genome)
    #sim.Start()
    #sim.Wait_To_Finish()
#x = sim.Get_Sensor_Data(sensorID = 4, s = 0)
#y = sim.Get_Sensor_Data(sensorID = 4, s = 1)
#z = sim.Get_Sensor_Data(sensorID = 4, s = 2)

#f = plt.figure()
#pn = f.add_subplot(111)
#plt.plot(sensorData)
#plt.show()
#pn.set_ylim(-1,+11)




