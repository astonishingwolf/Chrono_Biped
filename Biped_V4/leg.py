# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:25:27 2021

@author: astonishing_wolf
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


print('Basic Leg Simulation with deformable terrain')
chrono.SetChronoDataPath(r"C:\Users\dasgu\Documents\Chrono_Biped\Biped_V4\biped_shapes")

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
rod_length = 1.5
crank_center = chrono.ChVectorD(-1,0.5,0)
crank_rad    = 0.4


mysystem = chrono.ChSystemSMC()
ground = chrono.ChBody()
#it.append(ground)
ground.SetBodyFixed(True)
mysystem.Add(ground)

mrod8a = 0.03
mrod8b = 0.3
mrod8c = 0.33

# Bracket to join thigs with torso
mrod = chrono.ChBody()
mysystem.Add(mrod)
#mrod.SetMass(50)
#mrod.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
mrod.SetPos(chrono.ChVectorD(mrod8a-0.06, mrod8b, mrod8c))
#mrod.SetRot(chrono.Q_ROTATE_Y_TO_Z)
#it.append(my_item)
#my_item.SetMass(10)
# Load mesh
mrod.SetMass(6)
#my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
#my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
mesh = chrono.ChTriangleMeshConnected()
mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
vis_shape = chrono.ChTriangleMeshShape()
vis_shape.SetMesh(mesh)
mrod.AddAsset(vis_shape)
mrod.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material = chrono.ChMaterialSurfaceSMC()

mrod.GetCollisionModel().ClearModel()
mrod.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                         mesh,                    # the mesh 
                                         False,                   # is it static?
                                         False,                   # is it convex?
                                         chrono.ChVectorD(0,0,0), # position on body
                                         chrono.ChMatrix33D(1),   # orientation on body 
                                         0.01)                    # "thickness" for increased robustness
mrod.GetCollisionModel().BuildModel()
mrod.SetBodyFixed(True)
mrod.SetCollide(True)

# LEft side bracket to connect torso with thigh
mrod8 = chrono.ChBody()
mysystem.Add(mrod8)
#mrod.SetMass(50)
#mrod.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
mrod8.SetPos(chrono.ChVectorD(mrod8a,mrod8b,mrod8c))
#mrod8.SetRot(chrono.Q_ROTATE_Y_TO_Z)
#it.append(my_item)
#my_item.SetMass(10)
# Load mesh
mrod8.SetMass(6)
#my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
#my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
mesh8 = chrono.ChTriangleMeshConnected()
mesh8.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh8.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
vis_shape8 = chrono.ChTriangleMeshShape()
vis_shape8.SetMesh(mesh8)
mrod8.AddAsset(vis_shape8)
mrod8.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material8 = chrono.ChMaterialSurfaceSMC()

mrod8.GetCollisionModel().ClearModel()
mrod8.GetCollisionModel().AddTriangleMesh(material8,                # contact material
                                         mesh8,                    # the mesh 
                                         False,                   # is it static?
                                         False,                   # is it convex?
                                         chrono.ChVectorD(0,0,0), # position on body
                                         chrono.ChMatrix33D(1),   # orientation on body 
                                         0.01)                    # "thickness" for increased robustness
mrod8.GetCollisionModel().BuildModel()
mrod8.SetBodyFixed(True)
mrod8.SetCollide(True)



#mysystem.Add(mrod)
# Torso
mrod2 = chrono.ChBody()
#mrod.SetMass(50)
#mrod.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
mrod2.SetPos(chrono.ChVectorD(0,0.3,0.3))
#mrod1.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
#it.append(my_item)
#my_item.SetMass(10)
# Load mesh
mrod2.SetMass(3)
#my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
#my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
mesh2 = chrono.ChTriangleMeshConnected()
mesh2.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_3_1.obj'))
mesh2.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
vis_shape2 = chrono.ChTriangleMeshShape()
vis_shape2.SetMesh(mesh2)
mrod2.AddAsset(vis_shape2)
mrod2.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material2 = chrono.ChMaterialSurfaceSMC()

mrod2.GetCollisionModel().ClearModel()
mrod2.GetCollisionModel().AddTriangleMesh(material2,                # contact material
                                          mesh2,                    # the mesh 
                                          False,                    # is it static?
                                          False,                    # is it convex?
                                          chrono.ChVectorD(0,0,0),  # position on body
                                          chrono.ChMatrix33D(1),    # orientation on body 
                                          0.01)                     # "thickness" for increased robustness
mrod2.GetCollisionModel().BuildModel()
mrod2.SetBodyFixed(True)
mrod2.SetCollide(True)
mysystem.Add(mrod2)


#mysystem.Add(mrod)
# Create a stylized rod
mrod3 = chrono.ChBody()
#mrod.SetMass(50)
#mrod.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
mrod3.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
mrod3.SetPos(chrono.ChVectorD(0.03,0.2,0.32))
#mrod1.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
#it.append(my_item)
#my_item.SetMass(10)
# Load mesh
mrod3.SetMass(6)
#my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
#my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
mesh3 = chrono.ChTriangleMeshConnected()
mesh3.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_4_1.obj'))
mesh3.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
vis_shape3 = chrono.ChTriangleMeshShape()
vis_shape3.SetMesh(mesh3)
mrod3.AddAsset(vis_shape3)
mrod3.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material3 = chrono.ChMaterialSurfaceSMC()

mrod3.GetCollisionModel().ClearModel()
mrod3.GetCollisionModel().AddTriangleMesh(material3,                # contact material
                                          mesh3,                    # the mesh 
                                          False,                   # is it static?
                                          False,                   # is it convex?
                                          chrono.ChVectorD(0,0,0), # position on body
                                          chrono.ChMatrix33D(1),   # orientation on body 
                                          0.01)                    # "thickness" for increased robustness
mrod3.GetCollisionModel().BuildModel()
mrod3.SetBodyFixed(True)
mrod3.SetCollide(True)
mysystem.Add(mrod3)


#mysystem.Add(mrod)
# Create a stylized rod
mrod4 = chrono.ChBody()
#mrod.SetMass(50)
#mrod.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
mrod4.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
mrod4.SetPos(chrono.ChVectorD(-0.03,0.2,0.32))
#mrod1.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
#it.append(my_item)
#my_item.SetMass(10)
# Load mesh
mrod4.SetMass(6)
#my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
#my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
mesh4 = chrono.ChTriangleMeshConnected()
mesh4.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_4_1.obj'))
mesh4.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
vis_shape4 = chrono.ChTriangleMeshShape()
vis_shape4.SetMesh(mesh4)
mrod4.AddAsset(vis_shape4)
mrod4.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material4 = chrono.ChMaterialSurfaceSMC()

mrod4.GetCollisionModel().ClearModel()
mrod4.GetCollisionModel().AddTriangleMesh(material4,                # contact material
                                          mesh4,                    # the mesh 
                                          False,                   # is it static?
                                          False,                   # is it convex?
                                          chrono.ChVectorD(0,0,0), # position on body
                                          chrono.ChMatrix33D(1),   # orientation on body 
                                          0.01)                    # "thickness" for increased robustness
mrod4.GetCollisionModel().BuildModel()
mrod4.SetBodyFixed(True)
mrod4.SetCollide(True)
mysystem.Add(mrod4)

#mysystem.Add(mrod)
# Create a stylized rod
mrod5 = chrono.ChBody()
#mrod.SetMass(50)
#mrod.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#mrod5.SetPos(chrono.ChVectorD(mrod8a,mrod8b-0.02,mrod8c-0.01))
mrod5.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
mrod5.SetPos(chrono.ChVectorD(mrod8a,mrod8b-0.02,mrod8c-0.01))
#it.append(my_item)
#my_item.SetMass(10)
# Load mesh
mrod5.SetMass(6)
#my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
#my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
mesh5 = chrono.ChTriangleMeshConnected()
mesh5.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_5_1.obj'))
mesh5.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
vis_shape5 = chrono.ChTriangleMeshShape()
vis_shape5.SetMesh(mesh5)
mrod5.AddAsset(vis_shape5)
mrod5.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material5 = chrono.ChMaterialSurfaceSMC()

mrod5.GetCollisionModel().ClearModel()
mrod5.GetCollisionModel().AddTriangleMesh(material5,                # contact material
                                          mesh5,                    # the mesh 
                                          False,                   # is it static?
                                          False,                   # is it convex?
                                          chrono.ChVectorD(0,0,0), # position on body
                                          chrono.ChMatrix33D(1),   # orientation on body 
                                          0.01)                    # "thickness" for increased robustness
mrod5.GetCollisionModel().BuildModel()
mrod5.SetBodyFixed(True)
mrod5.SetCollide(True)
mysystem.Add(mrod5)

#mysystem.Add(mrod)
# Create a stylized rod
mrod6 = chrono.ChBody()
#mrod.SetMass(50)
#mrod.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
mrod6.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
mrod6.SetPos(chrono.ChVectorD(mrod8a-0.06,mrod8b-0.02,mrod8c-0.01))
#mrod1.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
#it.append(my_item)
#my_item.SetMass(10)
# Load mesh
mrod6.SetMass(6)
#my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
#my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
mesh6 = chrono.ChTriangleMeshConnected()
mesh6.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_5_1.obj'))
mesh6.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
vis_shape6 = chrono.ChTriangleMeshShape()
vis_shape6.SetMesh(mesh6)
mrod6.AddAsset(vis_shape6)
mrod6.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material6 = chrono.ChMaterialSurfaceSMC()

mrod6.GetCollisionModel().ClearModel()
mrod6.GetCollisionModel().AddTriangleMesh(material6,                # contact material
                                          mesh6,                    # the mesh 
                                          False,                   # is it static?
                                          False,                   # is it convex?
                                          chrono.ChVectorD(0,0,0), # position on body
                                          chrono.ChMatrix33D(1),   # orientation on body 
                                          0.01)                    # "thickness" for increased robustness
mrod6.GetCollisionModel().BuildModel()
mrod6.SetBodyFixed(True)
mrod6.SetCollide(True)
mysystem.Add(mrod6)


####JOINTS
#between right bracket and torso
mjointB = chrono.ChLinkLockRevolute()
mjointB.Initialize(mrod,
                   mrod2, 
                   chrono.ChCoordsysD(chrono.ChVectorD(mrod8a-0.06, mrod8b, mrod8c)))
mysystem.Add(mjointB)

#between left bracket and torso
mjointC = chrono.ChLinkLockRevolute()
mjointC.Initialize(mrod8,
                   mrod2, 
                   chrono.ChCoordsysD(chrono.ChVectorD(mrod8a,mrod8b,mrod8c),chrono.Q_ROTATE_X_TO_Y))
mysystem.Add(mjointC)

##BETWEEN BRACKTS AND THIGHS
mjointD = chrono.ChLinkLockRevolute()
mjointD.Initialize(mrod6,
                   mrod, 
                   chrono.ChCoordsysD(chrono.ChVectorD(mrod8a-0.06,mrod8b-0.02,mrod8c-0.01),chrono.Q_from_AngX(math.pi/2)))
mysystem.Add(mjointD)

mjointE = chrono.ChLinkLockRevolute()
mjointE.Initialize(mrod6,
                   mrod2, 
                   chrono.ChCoordsysD(chrono.ChVectorD(mrod8a,mrod8b,mrod8c)))
#mysystem.Add(mjointE)

terrain = veh.SCMDeformableTerrain(mysystem)
terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0,-0.15,0), chrono.Q_from_AngX(-math.pi/2)))
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
mysystem.SetSolver(my_solver)
my_solver.SetMaxIterations(600)
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

    
    while(myapplication.GetDevice().run()):
        myapplication.BeginScene()
        myapplication.DrawAll()
        myapplication.DoStep()
        myapplication.EndScene()
        
