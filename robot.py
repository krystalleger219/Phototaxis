import constants as c
class ROBOT:
    def __init__(self, sim, wts):
        self.Send_Objects(sim)
        self.Send_Joints(sim)
        self.Send_Sensors(sim)
        self.Send_Neurons(sim)
        self.Send_Synapses(sim,wts)

    def Send_Objects(self,sim):
        sim.Send_Box(objectID=0, x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=.5, g=.5, b=.5)
        sim.Send_Cylinder(objectID = 1, x=0, y=c.L, z = c.L + c.R, r1=0, r2=1, r3=0, length=c.L, radius =c.R, r=1, g=0, b=0)
        sim.Send_Cylinder(objectID = 2, x=c.L, y=0, z = c.L + c.R, r1=1, r2=0, r3=0, length=c.L, radius =c.R, r=0, g=1, b=0)
        sim.Send_Cylinder(objectID = 3, x=0, y=-c.L, z = c.L + c.R, r1=0, r2=1, r3=0, length=c.L, radius =c.R, r=0, g=0, b=1)
        sim.Send_Cylinder(objectID = 4, x=-c.L, y=0, z = c.L + c.R, r1=1, r2=0, r3=0, length=c.L, radius =c.R, r=.5, g=0, b=.5)
        sim.Send_Cylinder(objectID = 5, x=0, y=c.L*1.5, z = (c.L +c.R)/1.75, length=c.L, radius =c.R, r=1, g=0, b=0)
        sim.Send_Cylinder(objectID = 6, x=c.L*1.5, y=0, z = (c.L +c.R)/1.75,length=c.L, radius =c.R, r=0, g=1, b=0)
        sim.Send_Cylinder(objectID = 7, x=0, y=-c.L*1.5, z = (c.L +c.R)/1.75, length=c.L, radius =c.R, r=0, g=0, b=1)
        sim.Send_Cylinder(objectID = 8, x=-c.L*1.5, y=0, z = (c.L +c.R)/1.75, length=c.L, radius =c.R, r=.5, g=0, b=.5)






        #sim.Send_Cylinder(objectID=0,x =0, y=0, z=.6, length = 1.0, radius = 0.1,)
        #sim.Send_Cylinder(objectID=1 , x=0 , y=.5 , z=1.1, r1=0, r2=1, r3=0, r=1, g=0, b=0)

    def Send_Joints(self,sim):
        sim.Send_Joint(jointID = 0, firstObjectID = 0, secondObjectID =1, x =0, y =c.L*.5, z=c.L+c.R, n1=-1, n2=0, n3=0)
        sim.Send_Joint(jointID =1, firstObjectID=1, secondObjectID = 5, x = 0, y = c.L*1.5, z=c.L+c.R, n1 = -1, n2=0, n3=0)
        sim.Send_Joint(jointID =2, firstObjectID=0, secondObjectID = 2, x = c.L*.5, y = 0, z=c.L+c.R, n1 = 0, n2=-1, n3=0)
        sim.Send_Joint(jointID =3, firstObjectID=2, secondObjectID = 6, x = c.L*1.5, y = 0, z=c.L+c.R, n1 = 0, n2=-1, n3=0)
        sim.Send_Joint(jointID =4, firstObjectID=0, secondObjectID = 3, x = 0, y = -c.L*.5, z=c.L+c.R, n1 = -1, n2=0, n3=0)
        sim.Send_Joint(jointID =5, firstObjectID=3, secondObjectID = 7, x = 0, y = -c.L*1.5, z=c.L+c.R, n1 = -1, n2=0, n3=0)
        sim.Send_Joint(jointID =6, firstObjectID=0, secondObjectID = 4, x = -c.L*.5, y = 0, z=c.L+c.R, n1 = 0, n2=-1, n3=0)
        sim.Send_Joint(jointID =7, firstObjectID=4, secondObjectID = 8, x = -c.L*1.5, y = 0, z=c.L+c.R, n1 = 0, n2=-1, n3=0)


        #sim.Send_Joint( jointID =0,firstObjectID = 0, secondObjectID=1, x =0, y =0, z=1.1, n1 = 1, n2 =0, n3 =0, lo=-3.14159/2 , hi=3.14159/2)

    def Send_Sensors(self,sim):
        sim.Send_Touch_Sensor(sensorID=0, objectID=5)
        sim.Send_Touch_Sensor(sensorID=1, objectID=6)
        sim.Send_Touch_Sensor(sensorID=2, objectID=7)
        sim.Send_Touch_Sensor(sensorID=3, objectID=8)
        #sim.Send_Proprioceptive_Sensor(sensorID=2, jointID=0)
        #sim.Send_Ray_Sensor(sensorID = 3 , objectID = 1 , x = 0 , y = 1.1 , z = 1.1 , r1 = 0 , r2 = 1, r3 = 0)
        sim.Send_Light_Sensor(sensorID=4, objectID=0)

    def Send_Neurons(self, sim):
        for sn in range (0,5):
            sim.Send_Sensor_Neuron(neuronID = sn, sensorID =sn)

        for mn in range (0,8):
            sim.Send_Motor_Neuron(neuronID=mn+5 , jointID=mn, tau = .3 )

    def Send_Synapses(self, sim, wts):
        for j in range (0,5):
            for i in range (0,8):
                sim.Send_Synapse(sourceNeuronID = j , targetNeuronID = i+5 , weight = wts[j,i] )

        #sim.Send_Synapse(sourceNeuronID = 0 , targetNeuronID = 2 , weight = -1.0 )






