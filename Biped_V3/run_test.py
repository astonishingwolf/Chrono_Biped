

def main():
    pass

if __name__ == '__main__':
    main()


import os
import math
#import time
#import sys, getopt
import pychrono as chrono
#import pychrono.postprocess as postprocess
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh



# ---------------------------------------------------------------------
#
# Parse command-line parameters

m_filename = "Meshes.py"
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
        
tire_rad = 0.8



# Remove the trailing .py and add / in case of file without ./
m_absfilename = os.path.abspath(m_filename)
m_modulename = os.path.splitext(m_absfilename)[0]

exported_items = chrono.ImportSolidWorksSystem(m_modulename)

# Add items to the physical system
my_system = chrono.ChSystemSMC()
it = []
add = 0
for my_item in exported_items:
    add+=1
print(add)
for i in range(add):
    my_system.Add(exported_items[i])
    it.append(my_item)

#printing Component names

# Print exported items
for my_item in exported_items:
	print (my_item.GetName())


ground = chrono.ChBody()
ground.SetBodyFixed(True)
my_system.Add(ground)        
# Optionally set some solver parameters.
#Motors Variables
st = chrono.ChVectorD(0.0122275345305963,0.00120884241999014,0.0332147998549766)
sc = chrono.ChVectorD(0.245,0.0,0.0)
#Between Torso_backet-2 and torso
my_motor = chrono.ChLinkMotorRotationSpeed()
my_motor.Initialize(it[4],   # the first connected body
                    it[5],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.0122275345305963,0.00120884241999014,0.0332147998549766))) # where to create the motor in abs.space
my_angularspeed = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
my_motor.SetMotorFunction(my_angularspeed)
#my_system.Add(my_motor)

#Between Torso_backet-1 and torso
my_motor1 = chrono.ChLinkMotorRotationSpeed()
my_motor1.Initialize(it[4],   # the first connected body
                    it[1],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0332147998549766))) # where to create the motor in abs.space
my_angularspeed = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
my_motor1.SetMotorFunction(my_angularspeed)
#my_system.Add(my_motor1)

#Between Torso_backet-1 and torso
my_motor1 = chrono.ChLinkMotorRotationSpeed()
my_motor1.Initialize(it[4],   # the first connected body
                    it[1],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0332147998549766))) # where to create the motor in abs.space
my_angularspeed = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
my_motor1.SetMotorFunction(my_angularspeed)
#my_system.Add(my_motor1)

#Between Torso_backet-1 and torso
my_motor2 = chrono.ChLinkMotorRotationSpeed()
my_motor2.Initialize(it[5],   # the first connected body
                    it[6],   # the second connected body
                    chrono.ChFrameD(st+sc)) # where to create the motor in abs.space
my_angularspeed = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
my_motor2.SetMotorFunction(my_angularspeed)
my_system.Add(my_motor2)



terrain = veh.SCMDeformableTerrain(my_system)
terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0,0.2,0), chrono.Q_from_AngX(-math.pi/2)))
terrain.Initialize(2.0, 6.0, 0.04)

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
my_system.SetSolver(my_solver)
my_solver.SetMaxIterations(600)
my_solver.EnableWarmStart(True);
my_system.Set_G_acc(chrono.ChVectorD(0,-9.8,0))
    
if m_visualization == "irrlicht":

    # ---------------------------------------------------------------------
    #
    #  Create an Irrlicht application to visualize the system
    #

    myapplication = chronoirr.ChIrrApp(my_system, 'Test', chronoirr.dimension2du(1280,720))

    myapplication.AddTypicalSky(chrono.GetChronoDataPath() + 'skybox/')
    myapplication.AddTypicalLogo(chrono.GetChronoDataPath() + 'logo_pychrono_alpha.png')
    myapplication.AddTypicalCamera(chronoirr.vector3df(1,1,1),chronoirr.vector3df(0.0,0.0,0.0))
    myapplication.AddTypicalLights()
    #myapplication.AddLightWithShadow(chronoirr.vector3df(10,20,10),chronoirr.vector3df(0,2.6,0), 10 ,10,40, 60, 512);

                # ==IMPORTANT!== Use this function for adding a ChIrrNodeAsset to all items
                # in the system. These ChIrrNodeAsset assets are 'proxies' to the Irrlicht meshes.
                # If you need a finer control on which item really needs a visualization proxy in
                # Irrlicht, just use application.AssetBind(myitem); on a per-item basis.

    myapplication.AssetBindAll();

                # ==IMPORTANT!== Use this function for 'converting' into Irrlicht meshes the assets
                # that you added to the bodies into 3D shapes, they can be visualized by Irrlicht!

    myapplication.AssetUpdateAll();

                # ==IMPORTANT!== Use this function for enabling cast soft shadows

    #myapplication.AddShadowAll();

    # ---------------------------------------------------------------------
    #
    #  Run the simulation forever until windows is closed
    #

    myapplication.SetTimestep(m_timestep);
    
    while(myapplication.GetDevice().run()):
        myapplication.BeginScene()
        myapplication.DrawAll()
        myapplication.DoStep()
        myapplication.EndScene()
        