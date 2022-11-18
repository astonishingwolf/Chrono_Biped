# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:09:08 2022

@author: dasgu
"""
import pychrono as chrono
from pychrono import irrlicht as chronoirr
import numpy as np
import sys, getopt
import pychrono as chrono
import pychrono.postprocess as postprocess
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh
import math 
import numpy as np
import os
chrono.SetChronoDataPath(r"C:\Users\dasgu\Documents\Chrono_Biped\Biped_V12\em_shapes")


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
                      
class Model(object):
   def __init__(self, render):
      self.render = render
      self.observation_space= np.empty([4,1])
      self.action_space= np.empty([1,1])
      self.info =  {}
      self.timestep = 0.01

      var_params = True
      self.m_filename = "em.py"
      self.tire_rad = 0.8
      self.tire_vel_z0 = -3
      self.tire_center = chrono.ChVectorD(0, 0.02 + self.tire_rad, -1.5)
      self.tire_w0 = self.tire_vel_z0 / self.tire_rad
      self.mysystem = chrono.ChSystemSMC()
      self.it = []
      self.ground = chrono.ChBody()
      self.ground.SetBodyFixed(True)
      self.mysystem.Add(self.ground)# Remove the trailing .py and add / in case of file without ./
      self.m_absfilename = os.path.abspath(self.m_filename)
      self.m_modulename = os.path.splitext(self.m_absfilename)[0]
      chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
      chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.05)
      self.exported_items = chrono.ImportSolidWorksSystem(self.m_modulename)
      self.mysystem = chrono.ChSystemSMC()
      self.j=0
      self.it = []
      self.it1 = []
      
      for self.my_item1 in self.exported_items:
          self.it.append(self.my_item1)
          
      for self.my_item in self.exported_items:
          self.mystem.Add(self.my_item)
          
      for self.my_item in self.exported_items:
          print(self.my_item.GetName())
                    
      self.my_motor = chrono.ChLinkMotorRotationSpeed()
      self.my_motor.Initialize(self.it[4],   # the first connected body
                               self.it[6],   # the second connected body
                               chrono.ChFrameD(chrono.ChVectorD(-6.93889390390723e-18,-0.01,0.185),chrono.Q_ROTATE_X_TO_Z)) # where to create the motor in abs.space
      self.my_angularspeed = chrono.ChFunction_Const(0) # ang.speed: 180°/s
      self.my_motor.SetMotorFunction(self.my_angularspeed)
      self.mysystem.Add(self.my_motor)
      self.my_motor1 = chrono.ChLinkMotorRotationSpeed()
      self.my_motor1.Initialize(self.it[4],   # the first connected body
                                self.it[5],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-9.54097911787244e-18,-0.01,0.015),chrono.Q_ROTATE_X_TO_Z)) # where to create the motor in abs.space
      self.my_angularspeed1 = chrono.ChFunction_Sine() # ang.speed: 180°/s
      self.my_angularspeed1 = chrono.ChFunction_Const(0) # ang.speed: 180°/s
      self.my_motor1.SetMotorFunction(self.my_angularspeed1)
      self.mysystem.Add(self.my_motor1)
      self.my_motor2 = chrono.ChLinkMotorRotationSpeed()
      self.my_motor2.Initialize(self.it[6],   # the first connected body
                                self.it[8],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-0.01,-0.032,0.152))) # where to create the motor in abs.space
      self.my_angularspeed2 = chrono.ChFunction_Sine()
      self.my_motor2.SetMotorFunction(self.my_angularspeed2)
      self.mysystem.Add(self.my_motor2)
      self.my_motor3 = chrono.ChLinkMotorRotationSpeed()
      self.my_motor3.Initialize(self.it[5],   # the first connected body
                                self.it[2],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-0.01,-0.032,0.155))) # where to create the motor in abs.space
      self.my_angularspeed3 = chrono.ChFunction_Sine() # ang.speed: 180°/s
      self.my_motor3.SetMotorFunction(self.my_angularspeed3)
      self.mysystem.Add(self.my_motor3)
      self.my_motor4 = chrono.ChLinkMotorRotationSpeed()
      self.my_motor4.Initialize(self.it[2],   # the first connected body
                                self.it[1],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-0.00999999999999999,-0.162,0.175))) # where to create the motor in abs.space
      self.my_angularspeed4 = chrono.ChFunction_Sine() # ang.speed: 180°/s
      self.my_motor4.SetMotorFunction(self.my_angularspeed4)
      self.mysystem.Add(self.my_motor4)
      self.my_motor5 = chrono.ChLinkMotorRotationSpeed()
      self.my_motor5.Initialize(self.it[8],   # the first connected body
                                self.it[3],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-0.00999999999999999,-0.162,0.305))) # where to create the motor in abs.space
      self.my_angularspeed5 = chrono.ChFunction_Sine() # ang.speed: 180°/s
      self.my_motor5.SetMotorFunction(self.my_angularspeed5)
      self.mysystem.Add(self.my_motor5)
      self.my_motor6 = chrono.ChLinkMotorRotationSpeed()
      self.my_motor6.Initialize(self.it[1],   # the first connected body
                                self.it[7],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-0.01,-0.292,0.175))) # where to create the motor in abs.space
      self.my_angularspeed6 = chrono.ChFunction_Sine() # ang.speed: 180°/s
      self.my_motor6.SetMotorFunction(self.my_angularspeed6)
      
      self.my_motor7 = chrono.ChLinkMotorRotationSpeed()
      self.my_motor7.Initialize(self.it[3],   # the first connected body
                                self.it[9],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-0.00999999999999995,-0.292,0.0750000000000001))) # where to create the motor in abs.space
      self.my_angularspeed7 = chrono.ChFunction_Sine() # ang.speed: 180°/s
      self.my_motor7.SetMotorFunction(self.my_angularspeed7)
                
      self.my_motor8 = chrono.ChLinkMotorRotationSpeed()
      self.my_motor8.Initialize(self.it[4],   # the first connected body
                                self.it[10],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-0.01,0.013,0.0126259017947352))) # where to create the motor in abs.space
      self.my_angularspeed8 = chrono.ChFunction_Const(0) # ang.speed: 180°/s
      self.my_motor8.SetMotorFunction(self.my_angularspeed8)
      self.mysystem.Add(self.my_motor8)
      
      self.motorl = chrono.ChLinkMotorLinearSpeed()
      self.msp = chrono.ChFunction_Const(10)  # amplitude
      
      self.rc2 = chrono.ChForce()
      self.frc2.SetF_x(self.msp)
      self.it[4].AddForce(self.frc2)
      self.a = self.it[2].SetFrame_COG_to_REF
      self.terrain = veh.SCMDeformableTerrain(self.mysystem)
      self.terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(-0.1,-0.26,-0.1), chrono.Q_from_AngX(-math.pi/2)))
      self.terrain.Initialize(0.60, 0.40, 0.004)#gives us the dimension of the plane
      
      self.terrain1 = veh.SCMDeformableTerrain(self.mysystem)
      self.terrain1.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(-0.1,-0.26,0.3), chrono.Q_from_AngX(-math.pi/2)))
      self.terrain1.Initialize(0.60, 0.40, 0.004)#gives us the dimension of the plane
      
      self.terrain2 = veh.SCMDeformableTerrain(self.mysystem)
      self.terrain2.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0.5,-0.26,-0.1), chrono.Q_from_AngX(-math.pi/2)))
      self.terrain2.Initialize(1.0, 0.40, 0.004)#gives us the dimension of the plane
      
      self.terrain3 = veh.SCMDeformableTerrain(self.mysystem)
      self.terrain3.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0.5,-0.26,0.3), chrono.Q_from_AngX(-math.pi/2)))
      self.terrain3.Initialize(1.0, 0.40, 0.004)#gives us the dimension of the plane
                
      self.my_params = MySoilParams()
      
      if self.var_params:
          # Location-dependent soil properties
          self.terrain.RegisterSoilParametersCallback(self.my_params)
          self.terrain1.RegisterSoilParametersCallback(self.my_params)
          self.terrain2.RegisterSoilParametersCallback(self.my_params)
          self.terrain3.RegisterSoilParametersCallback(self.my_params)
      else :
          self.terrain.SetSoilParameters(0.2e6,  # Bekker Kphi
                                         0,      # Bekker Kc
                                         1.1,    # Bekker n exponent
                                         0,      # Mohr cohesive limit (Pa)
                                         30,     # Mohr friction limit (degrees)
                                         0.01,   # Janosi shear coefficient (m)
                                         4e7,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                                         3e4     # Damping (Pa s/m), proportional to negative vertical speed (optional)
                                         )   
          
          # Set terrain visualization mode
          self.terrain.SetPlotType(veh.SCMDeformableTerrain.PRESSURE, 0, 30000.2)
          
          
          #my_system.SetMaxPenetrationRecoverySpeed(1.00)
          self.my_solver = chrono.ChSolverBB()
          self.mysystem.SetSolver(self.my_solver)
          self.my_solver.SetMaxIterations(9000)
          self.my_solver.EnableWarmStart(True);
          self.mysystem.Set_G_acc(chrono.ChVectorD(0,0,0))
          
          if self.m_visualization == "irrlicht":
              
              # ---------------------------------------frc2------------------------------
              #
              #  Create an Irrlicht application to visualize the system
              #
              
              self.myapplication = chronoirr.ChIrrApp(self.mysystem, 'Deformable soil', chronoirr.dimension2du(1280,720), False, True)
              self.myapplication.AddTypicalSky()
              #myapplication.AddTypicalLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
              self.myapplication.AddTypicalCamera(chronoirr.vector3df(2.5,0.0,0), chronoirr.vector3df(0.3,0,0))
              self.myapplication.AddTypicalLights()
              self.myapplication.AddLightWithShadow(chronoirr.vector3df(1.5,5.5,-2.5),    # point
                                                    chronoirr.vector3df(0,0,0),           # aim point
                                                    3,                                    # radius (power)
                                                    2.2, 7.2,                             # near, far
                                                    40,                                   # angle of FOV
                                                    512,                                  # resoluition
                                                    chronoirr.SColorf(0.8,0.8,1))         # light color
              self.myapplication.AssetBindAll()
              self.myapplication.AssetUpdateAll()
              self.myapplication.AddShadowAll()
              self.myapplication.SetTimestep(0.01)
              
              
              while(self.myapplication.GetDevice().run()):
                  self.myapplication.BeginScene()
                  self.myapplication.DrawAll()
                  self.myapplication.DoStep()
                  self.myapplication.EndScene()
                                
   def reset(self):
      
       self.observation_space= np.empty([4,1])
       self.action_space= np.empty([1,1])
       self.info =  {}
       self.timestep = 0.01
       
       var_params = True
       
       self.tire_rad = 0.8
       self.tire_vel_z0 = -3
       self.tire_center = chrono.ChVectorD(0, 0.02 + self.tire_rad, -1.5)
       self.tire_w0 = self.tire_vel_z0 / self.tire_rad
       self.mysystem = chrono.ChSystemSMC()
       self.it = []
       self.ground = chrono.ChBody()
       self.ground.SetBodyFixed(True)
       self.mysystem.Add(self.ground)# Remove the trailing .py and add / in case of file without ./
       self.m_absfilename = os.path.abspath(self.m_filename)
       self.m_modulename = os.path.splitext(self.m_absfilename)[0]
       chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
       chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.05)
       self.exported_items = chrono.ImportSolidWorksSystem(self.m_modulename)
       self.mysystem = chrono.ChSystemSMC()
       self.j=0
       self.it = []
       self.it1 = []
       
       for self.my_item1 in self.exported_items:
           self.it.append(self.my_item1)
           
       for self.my_item in self.exported_items:
           self.mystem.Add(self.my_item)
               
       for self.my_item in self.exported_items:
           print(self.my_item.GetName())
                        
       self.my_motor = chrono.ChLinkMotorRotationSpeed()
       self.my_motor.Initialize(self.it[4],   # the first connected body
                                self.it[6],   # the second connected body
                                chrono.ChFrameD(chrono.ChVectorD(-6.93889390390723e-18,-0.01,0.185),chrono.Q_ROTATE_X_TO_Z)) # where to create the motor in abs.space
       self.my_angularspeed = chrono.ChFunction_Const(0) # ang.speed: 180°/s
       self.my_motor.SetMotorFunction(self.my_angularspeed)
       self.mysystem.Add(self.my_motor)
       self.my_motor1 = chrono.ChLinkMotorRotationSpeed()
       self.my_motor1.Initialize(self.it[4],   # the first connected body
                                 self.it[5],   # the second connected body
                                 chrono.ChFrameD(chrono.ChVectorD(-9.54097911787244e-18,-0.01,0.015),chrono.Q_ROTATE_X_TO_Z)) # where to create the motor in abs.space
       self.my_angularspeed1 = chrono.ChFunction_Sine() # ang.speed: 180°/s
       self.my_angularspeed1 = chrono.ChFunction_Const(0) # ang.speed: 180°/s
       self.my_motor1.SetMotorFunction(self.my_angularspeed1)
       self.mysystem.Add(self.my_motor1)
       self.my_motor2 = chrono.ChLinkMotorRotationSpeed()
       self.my_motor2.Initialize(self.it[6],   # the first connected body
                                 self.it[8],   # the second connected body
                                 chrono.ChFrameD(chrono.ChVectorD(-0.01,-0.032,0.152))) # where to create the motor in abs.space
       self.my_angularspeed2 = chrono.ChFunction_Sine()
       self.my_motor2.SetMotorFunction(self.my_angularspeed2)
       self.mysystem.Add(self.my_motor2)
       self.my_motor3 = chrono.ChLinkMotorRotationSpeed()
       self.my_motor3.Initialize(self.it[5],   # the first connected body
                                 self.it[2],   # the second connected body
                                 chrono.ChFrameD(chrono.ChVectorD(-0.01,-0.032,0.155))) # where to create the motor in abs.space
       self.my_angularspeed3 = chrono.ChFunction_Sine() # ang.speed: 180°/s
       self.my_motor3.SetMotorFunction(self.my_angularspeed3)
       self.mysystem.Add(self.my_motor3)
       self.my_motor4 = chrono.ChLinkMotorRotationSpeed()
       self.my_motor4.Initialize(self.it[2],   # the first connected body
                                 self.it[1],   # the second connected body
                                 chrono.ChFrameD(chrono.ChVectorD(-0.00999999999999999,-0.162,0.175))) # where to create the motor in abs.space
       self.my_angularspeed4 = chrono.ChFunction_Sine() # ang.speed: 180°/s
       self.my_motor4.SetMotorFunction(self.my_angularspeed4)
       self.mysystem.Add(self.my_motor4)
       self.my_motor5 = chrono.ChLinkMotorRotationSpeed()
       self.my_motor5.Initialize(self.it[8],   # the first connected body
                                 self.it[3],   # the second connected body
                                 chrono.ChFrameD(chrono.ChVectorD(-0.00999999999999999,-0.162,0.305))) # where to create the motor in abs.space
       self.my_angularspeed5 = chrono.ChFunction_Sine() # ang.speed: 180°/s
       self.my_motor5.SetMotorFunction(self.my_angularspeed5)
       self.mysystem.Add(self.my_motor5)
       self.my_motor6 = chrono.ChLinkMotorRotationSpeed()
       self.my_motor6.Initialize(self.it[1],   # the first connected body
                                 self.it[7],   # the second connected body
                                 chrono.ChFrameD(chrono.ChVectorD(-0.01,-0.292,0.175))) # where to create the motor in abs.space
       self.my_angularspeed6 = chrono.ChFunction_Sine() # ang.speed: 180°/s
       self.my_motor6.SetMotorFunction(self.my_angularspeed6)
       
       self.my_motor7 = chrono.ChLinkMotorRotationSpeed()
       self.my_motor7.Initialize(self.it[3],   # the first connected body
                                 self.it[9],   # the second connected body
                                 chrono.ChFrameD(chrono.ChVectorD(-0.00999999999999995,-0.292,0.0750000000000001))) # where to create the motor in abs.space
       self.my_angularspeed7 = chrono.ChFunction_Sine() # ang.speed: 180°/s
       self.my_motor7.SetMotorFunction(self.my_angularspeed7)
                    
       self.my_motor8 = chrono.ChLinkMotorRotationSpeed()
       self.my_motor8.Initialize(self.it[4],   # the first connected body
                                 self.it[10],   # the second connected body
                                 chrono.ChFrameD(chrono.ChVectorD(-0.01,0.013,0.0126259017947352))) # where to create the motor in abs.space
       self.my_angularspeed8 = chrono.ChFunction_Const(0) # ang.speed: 180°/s
       self.my_motor8.SetMotorFunction(self.my_angularspeed8)
       self.mysystem.Add(self.my_motor8)
       
       self.motorl = chrono.ChLinkMotorLinearSpeed()
       self.msp = chrono.ChFunction_Const(10)  # amplitude
       
       self.rc2 = chrono.ChForce()
       self.frc2.SetF_x(self.msp)
       self.it[4].AddForce(self.frc2)
       self.a = self.it[2].SetFrame_COG_to_REF
       self.terrain = veh.SCMDeformableTerrain(self.mysystem)
       self.terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(-0.1,-0.26,-0.1), chrono.Q_from_AngX(-math.pi/2)))
       self.terrain.Initialize(0.60, 0.40, 0.004)#gives us the dimension of the plane
       
       self.terrain1 = veh.SCMDeformableTerrain(self.mysystem)
       self.terrain1.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(-0.1,-0.26,0.3), chrono.Q_from_AngX(-math.pi/2)))
       self.terrain1.Initialize(0.60, 0.40, 0.004)#gives us the dimension of the plane
       
       self.terrain2 = veh.SCMDeformableTerrain(self.mysystem)
       self.terrain2.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0.5,-0.26,-0.1), chrono.Q_from_AngX(-math.pi/2)))
       self.terrain2.Initialize(1.0, 0.40, 0.004)#gives us the dimension of the plane
       
       self.terrain3 = veh.SCMDeformableTerrain(self.mysystem)
       self.terrain3.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0.5,-0.26,0.3), chrono.Q_from_AngX(-math.pi/2)))
       self.terrain3.Initialize(1.0, 0.40, 0.004)#gives us the dimension of the plane
                    
       self.my_params = MySoilParams()
       
       if self.var_params:
           # Location-dependent soil properties
           self.terrain.RegisterSoilParametersCallback(self.my_params)
           self.terrain1.RegisterSoilParametersCallback(self.my_params)
           self.terrain2.RegisterSoilParametersCallback(self.my_params)
           self.terrain3.RegisterSoilParametersCallback(self.my_params)
       else :
           self.terrain.SetSoilParameters(0.2e6,  # Bekker Kphi
                                          0,      # Bekker Kc
                                          1.1,    # Bekker n exponent
                                          0,      # Mohr cohesive limit (Pa)
                                          30,     # Mohr friction limit (degrees)
                                          0.01,   # Janosi shear coefficient (m)
                                          4e7,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                                          3e4     # Damping (Pa s/m), proportional to negative vertical speed (optional)
                                          )   
           
           # Set terrain visualization mode
           self.terrain.SetPlotType(veh.SCMDeformableTerrain.PRESSURE, 0, 30000.2)
           
           
           #my_system.SetMaxPenetrationRecoverySpeed(1.00)
           self.my_solver = chrono.ChSolverBB()
           self.mysystem.SetSolver(self.my_solver)
           self.my_solver.SetMaxIterations(9000)
           self.my_solver.EnableWarmStart(True);
           self.mysystem.Set_G_acc(chrono.ChVectorD(0,0,0))
           
   def  step(self, ac):
           
       self.myapplication = chronoirr.ChIrrApp(self.mysystem, 'Deformable soil', chronoirr.dimension2du(1280,720), False, True)
       self.myapplication.AddTypicalSky()
       #myapplication.AddTypicalLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
       self.myapplication.AddTypicalCamera(chronoirr.vector3df(2.5,0.0,0), chronoirr.vector3df(0.3,0,0))
       self.myapplication.AddTypicalLights()
       self.myapplication.AddLightWithShadow(chronoirr.vector3df(1.5,5.5,-2.5),    # point
                                             chronoirr.vector3df(0,0,0),           # aim point
                                             3,                                    # radius (power)
                                             2.2, 7.2,                             # near, far
                                             40,                                   # angle of FOV
                                             512,                                  # resoluition
                                             chronoirr.SColorf(0.8,0.8,1))         # light color
       self.myapplication.AssetBindAll()
       self.myapplication.AssetUpdateAll()
       self.myapplication.AddShadowAll()
       self.myapplication.SetTimestep(0.01)
       
       
       while(self.myapplication.GetDevice().run()):
           self.myapplication.BeginScene()
           self.myapplication.DrawAll()
           self.myapplication.DoStep()
           self.myapplication.EndScene()
       

              

   def get_ob(self):
          self.state = [self.link_slider.GetDist(), self.link_slider.GetDist_dt(), self.pin_joint.GetRelAngle(), self.omega]
          return np.asarray(self.state)

   def is_done(self):
          if abs(self.link_slider.GetDist()) > 2 or self.steps> 100000 or abs(self.pin_joint.GetRelAngle()) >  0.2  :
                 self.isdone = True
   
   def ScreenCapture(self, interval):
          try: 
              self.myapplication.SetVideoframeSave(True)
              self.myapplication.SetVideoframeSaveInterval(interval)
              
          except:
                 print('No ChIrrApp found. Cannot save video frames.')
                     
       
   def __del__(self):
        if self.render:
            self.myapplication.GetDevice().closeDevice()
            print('Destructor called, Device deleted.')
        else:
            print('Destructor called, No device to delete.')
        
