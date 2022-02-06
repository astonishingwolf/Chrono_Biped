"""
Created on Tue Sep 28 03:07:56 2021

@author: dasgu
"""



def main():
    pass

if __name__ == '__main__':
    main()


import os
import math
import time
import sys, getopt
import pychrono as chrono
import pychrono.postprocess as postprocess
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh
import math as m

class ChFunction_myf1 (chrono.ChFunction):
    def __init__(self):
         chrono.ChFunction.__init__(self)
    def Get_y(self,x):
            return -chrono.CH_C_PI * (-1.27657110e-10*pow(x,10)+2.65351677e-08*pow(x,9)-2.35692901e-06*pow(x,8)+1.16839755e-04*pow(x,7)-3.54346845e-03*pow(x,6)+6.78029658e-02*pow(x,5)-8.14717219e-01*pow(x,4)+5.93038925e+00*pow(x,3)-2.42777622e+01*pow(x,2)+4.87549530e+01*pow(x,1) ) / 2.0
class ChFunction_myf2 (chrono.ChFunction):
    def __init__(self):
         chrono.ChFunction.__init__(self)
    def Get_y(self,x):
            return -chrono.CH_C_PI * (2.33933236e-10*pow(x,10)-4.86253314e-08*pow(x,9)+4.32362493e-06*pow(x,8)-2.14816127e-04*pow(x,7)+6.53703984e-03*pow(x,6)-1.25632196e-01*pow(x,5)+1.51737363e+00*pow(x,4)-1.11096508e+01*pow(x,3)+4.57803195e+01*pow(x,2)-9.33340628e+01*pow(x,1)) / 2.0

# ---------------------------------------------------------------------
#
# Parse command-line parameters
chrono.SetChronoDataPath(r"C:\Users\dasgu\Documents\Chrono_Biped\Biped_V8\bp_shapes")
m_filename = "bm.py"
m_timestep = 0.01
m_length = 1.0
m_visualization = "irrlicht"
m_datapath = ""



###Soil Parameters
var_params = True

class MySoilParams (veh.SoilParametersCallback):
    def __init__(self):
        veh.SoilParametersCallback.__init__(self)
    def Set(self, x, y):
        if y > 0 :
            self.m_Bekker_Kphi = 0.2e6
            self.m_Bekker_Kc = 0
            self.m_Bekker_n = 1.1
            self.m_Mohr_cohesion = 0
            self.m_Mohr_friction = 30
            self.m_Janosi_shear = 0.01
            self.m_elastic_K = 4e7
            self.m_damping_R = 3e4
        else:
            self.m_Bekker_Kphi = 5301e3
            self.m_Bekker_Kc = 102e3
            self.m_Bekker_n = 0.793
            self.m_Mohr_cohesion = 1.3e3
            self.m_Mohr_friction = 31.1
            self.m_Janosi_shear = 1.2e-2
            self.m_elastic_K = 4e8
            self.m_damping_R = 3e4

# Global parameters for tire
tire_rad = 0.8
tire_vel_z0 = -3
tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
tire_w0 = tire_vel_z0 / tire_rad

# ----------------------------
# Create the mechanical system
# ----------------------------

mysystem = chrono.ChSystemSMC()
it = []
# Create the ground
ground = chrono.ChBody()
#it.append(ground)
ground.SetBodyFixed(True)
mysystem.Add(ground)# Remove the trailing .py and add / in case of file without ./
m_absfilename = os.path.abspath(m_filename)
m_modulename = os.path.splitext(m_absfilename)[0]
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.05)
exported_items = chrono.ImportSolidWorksSystem(m_modulename)

# Add items to the physical system
mysystem = chrono.ChSystemSMC()

j=0
it = []
it1 = []
for my_item1 in exported_items:
    it.append(my_item1)
    

#printing Component names

# Print exported items
#for my_item in exported_items:
	#print (my_item.GetName())
for my_item in exported_items:
	mysystem.Add(my_item)


#printing Component names

# Print exported items
for my_item in exported_items:
	print (my_item.GetName())



       
# Optionally set some solver parameters.
#Motors Variables
#st = chrono.ChVectorD(0.0122275345305963,0.00120884241999014,0.0332147998549766)
#sc = chrono.ChVectorD(0.245,0.0,0.0)
#Between Torso_backet-2 and torso
my_motor = chrono.ChLinkMotorRotationAngle()
my_motor.Initialize(it[1],   # the first connected body
                    it[5],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.01,0.01,0.12))) # where to create the motor in abs.space
my_angularspeed = ChFunction_myf1() # ang.speed: 180°/s
#my_angularspeed = chrono.ChFunction_Sine() # ang.speed: 180°/s
my_motor.SetAngleFunction(my_angularspeed)
#mysystem.Add(my_motor)

my_motor1 = chrono.ChLinkMotorRotationAngle()
my_motor1.Initialize(it[5],   # the first connected body
                    it[3],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.01,-0.12,-0.00999999999999998),chrono.Q_ROTATE_X_TO_Y)) # where to create the motor in abs.space
#my_angularspeed1 = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
#my_angularspeed1 = chrono.ChFunction_Const(chrono.CH_C_PI) 
my_angularspeed1 = ChFunction_myf2() # ang.speed: 180°/s
my_motor1.SetAngleFunction(my_angularspeed1)
#mysystem.Add(my_motor1)

my_motor2 = chrono.ChLinkMotorRotationSpeed()
my_motor2.Initialize(it[4],   # the first connected body
                    it[2],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.01,-0.12,-0.00999999999999998),chrono.Q_ROTATE_X_TO_Y)) # where to create the motor in abs.space
#my_angularspeed2 = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
my_angularspeed2 = chrono.ChFunction_Const(chrono.CH_C_PI*0) # ang.speed: 180°/s
my_motor2.SetMotorFunction(my_angularspeed2)
#mysystem.Add(my_motor2)

my_motor3 = chrono.ChLinkMotorRotationSpeed()
my_motor3.Initialize(it[5],   # the first connected body
                    it[3],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.01,-0.12,-0.00999999999999998),chrono.Q_ROTATE_X_TO_Y)) # where to create the motor in abs.space
#my_angularspeed3 = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
my_angularspeed3 = chrono.ChFunction_Const(chrono.CH_C_PI*0) # ang.speed: 180°/s
my_motor3.SetMotorFunction(my_angularspeed3)
#mysystem.Add(my_motor3)

# =============================================================================
# my_motor4 = chrono.ChLinkMotorRotationSpeed()
# my_motor4.Initialize(it[3],   # the first connected body
#                     it[9],   # the second connected body
#                     chrono.ChFrameD(chrono.ChVectorD(0.01,-0.25,0.01),chrono.Q_ROTATE_X_TO_Y)) # where to create the motor in abs.space
# #my_angularspeed3 = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
# my_angularspeed4 = chrono.ChFunction_Sine() # ang.speed: 180°/s
# my_motor4.SetMotorFunction(my_angularspeed4)
# #mysystem.Add(my_motor4)
# 
# my_motor5 = chrono.ChLinkMotorRotationSpeed()
# my_motor5.Initialize(it[2],   # the first connected body
#                     it[7],   # the second connected body
#                     chrono.ChFrameD(chrono.ChVectorD(0.01,-0.25,-0.17),chrono.Q_ROTATE_X_TO_Y)) # where to create the motor in abs.space
# #my_angularspeed3 = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
# my_angularspeed5 = chrono.ChFunction_Sine() # ang.speed: 180°/s
# my_motor3.SetMotorFunction(my_angularspeed5)
# #mysystem.Add(my_motor5)
# 
# my_motor6 = chrono.ChLinkMotorRotationSpeed()
# my_motor6.Initialize(it[9],   # the first connected body
#                     it[6],   # the second connected body
#                     chrono.ChFrameD(chrono.ChVectorD(0.01,-0.25,0.16),chrono.Q_ROTATE_X_TO_Y)) # where to create the motor in abs.space
# #my_angularspeed3 = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
# my_angularspeed6 = chrono.ChFunction_Sine() # ang.speed: 180°/s
# my_motor6.SetMotorFunction(my_angularspeed6)
# #mysystem.Add(my_motor6)
# 
# my_motor7 = chrono.ChLinkMotorRotationSpeed()
# my_motor7.Initialize(it[7],   # the first connected body
#                     it[8],   # the second connected body
#                     chrono.ChFrameD(chrono.ChVectorD(0.081512258846341,-0.25,-0.04),chrono.Q_ROTATE_X_TO_Y)) # where to create the motor in abs.space
# #my_angularspeed3 = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
# my_angularspeed7 = chrono.ChFunction_Sine() # ang.speed: 180°/s
# my_motor7.SetMotorFunction(my_angularspeed7)
# #mysystem.Add(my_motor7)
# =============================================================================

#Between Torso_backet-2 and torso
#my_motor1 = chrono.ChLinkMotorRotationSpeed()
#my_motor1.Initialize(it[2],   # the first connected body
  #                   chrono.ChFrameD(chrono.ChVectorD(0.141018628033538,-0.090598704515718,0.0952556529655919))) # where to create the motor in abs.space
#my_angularspeed = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
#my_motor1.SetMotorFunction(my_angularspeed)
#mysystem.Add(my_motor1)
#




terrain = veh.SCMDeformableTerrain(mysystem)
terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0,-0.25,0), chrono.Q_from_AngX(-math.pi/2)))
terrain.Initialize(4.0, 14.0, 0.004)#gives us the dimension of the plane

my_params = MySoilParams()
if var_params:
    # Location-dependent soil properties
    terrain.RegisterSoilParametersCallback(my_params)
else :
    # Constant soil properties
    terrain.SetSoilParameters(0.2e6,  # Bekker Kphi
                               0,      # Bekker Kc
                               1.1,    # Bekker n exponent
                               0,      # Mohr cohesive limit (Pa)
                               30,     # Mohr friction limit (degrees)
                               0.01,   # Janosi shear coefficient (m)
                               4e7,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                               3e4     # Damping (Pa s/m), proportional to negative vertical speed (optional)
    )

# Set terrain visualization mode
terrain.SetPlotType(veh.SCMDeformableTerrain.PLOT_PRESSURE, 0, 30000.2)


#my_system.SetMaxPenetrationRecoverySpeed(1.00)
my_solver = chrono.ChSolverBB()
mysystem.SetSolver(my_solver)
my_solver.SetMaxIterations(9000)
my_solver.EnableWarmStart(True);
mysystem.Set_G_acc(chrono.ChVectorD(0,-9.8,0))
    
if m_visualization == "irrlicht":

    # ---------------------------------------------------------------------
    #
    #  Create an Irrlicht application to visualize the system
    #

    myapplication = chronoirr.ChIrrApp(mysystem, 'Deformable soil', chronoirr.dimension2du(1280,720), False, True)
    myapplication.AddTypicalSky()
    #myapplication.AddTypicalLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
    myapplication.AddTypicalCamera(chronoirr.vector3df(2.0,1.4,0.0), chronoirr.vector3df(0,tire_rad,0))
    myapplication.AddTypicalLights()
    myapplication.AddLightWithShadow(chronoirr.vector3df(1.5,5.5,-2.5),    # point
                                 chronoirr.vector3df(0,0,0),           # aim point
                                 3,                                    # radius (power)
                                 2.2, 7.2,                             # near, far
                                 40,                                   # angle of FOV
                                 512,                                  # resoluition
                                 chronoirr.SColorf(0.8,0.8,1))         # light color
    myapplication.AssetBindAll()
    myapplication.AssetUpdateAll()
    myapplication.AddShadowAll()
    myapplication.SetTimestep(0.00001)

    
    while(myapplication.GetDevice().run()):
        myapplication.BeginScene()
        myapplication.DrawAll()
        myapplication.DoStep()
        myapplication.EndScene()
        