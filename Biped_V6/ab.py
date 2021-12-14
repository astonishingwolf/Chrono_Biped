# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\Chrono_Biped\Biped_V5\Assem1.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'ab_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Torso-1')
body_1.SetPos(chrono.ChVectorD(0.025,-0.025,0.05))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(0.723285413235575)
body_1.SetInertiaXX(chrono.ChVectorD(0.00799207954939873,0.00799207954939873,0.00036119417290903))
body_1.SetInertiaXY(chrono.ChVectorD(4.02006102661444e-36,1.15648231731788e-20,-8.61597626531233e-36))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(5.59251337018444e-18,1.27149367289098e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))
mesh = chrono.ChTriangleMeshConnected()
mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material = chrono.ChMaterialSurfaceSMC()
body_1.GetCollisionModel().ClearModel()
body_1.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                            mesh,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_1.GetCollisionModel().BuildModel()
body_1.SetBodyFixed(True)
body_1.SetCollide(False)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Main_leg-1')
body_2.SetPos(chrono.ChVectorD(0.025,0.00499999999999999,0.435))
body_2.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
body_2.SetMass(0.314182522957532)
body_2.SetInertiaXX(chrono.ChVectorD(0.000216025953973108,0.00338823977615053,0.00338363272051758))
body_2.SetInertiaXY(chrono.ChVectorD(4.38405724653105e-20,5.97501259547907e-20,1.53730203414675e-20))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.53438639878404e-18,-7.55706440556755e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))
mesh_2 = chrono.ChTriangleMeshConnected()
mesh_2.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_2_1.obj'))
mesh_2.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_2 = chrono.ChMaterialSurfaceSMC()
body_2.GetCollisionModel().ClearModel()
body_2.GetCollisionModel().AddTriangleMesh(material_2,                # contact material
                                            mesh_2,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_2.GetCollisionModel().BuildModel()
body_2.SetBodyFixed(True)
body_2.SetCollide(False)
# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_2.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Main_leg-2')
body_3.SetPos(chrono.ChVectorD(0.025,-0.295,0.485))
body_3.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,-0.5))
body_3.SetMass(0.314182522957532)
body_3.SetInertiaXX(chrono.ChVectorD(0.000216025953973108,0.00338823977615053,0.00338363272051758))
body_3.SetInertiaXY(chrono.ChVectorD(4.38405724653105e-20,-5.97501259547907e-20,-1.5404988211714e-20))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.53438639878404e-18,-7.55706440556755e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))
mesh_3 = chrono.ChTriangleMeshConnected()
mesh_3.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_2_1.obj'))
mesh_3.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_3 = chrono.ChMaterialSurfaceSMC()
body_3.GetCollisionModel().ClearModel()
body_3.GetCollisionModel().AddTriangleMesh(material_3,                # contact material
                                            mesh_3,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_3.GetCollisionModel().BuildModel()
body_3.SetBodyFixed(True)
body_3.SetCollide(False)
# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_3.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Main_leg-3')
body_4.SetPos(chrono.ChVectorD(0.025,-0.655,-0.025))
body_4.SetRot(chrono.ChQuaternionD(0.5,-0.5,0.5,0.5))
body_4.SetMass(0.314182522957532)
body_4.SetInertiaXX(chrono.ChVectorD(0.000216025953973108,0.00338823977615052,0.00338363272051758))
body_4.SetInertiaXY(chrono.ChVectorD(-4.38405724653105e-20,5.97501259547907e-20,-1.5628763303439e-20))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.53438639878404e-18,-7.55706440556755e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))
mesh_4 = chrono.ChTriangleMeshConnected()
mesh_4.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_2_1.obj'))
mesh_4.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_4 = chrono.ChMaterialSurfaceSMC()
body_4.GetCollisionModel().ClearModel()
body_4.GetCollisionModel().AddTriangleMesh(material_4,                # contact material
                                            mesh_4,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_4.GetCollisionModel().BuildModel()
body_4.SetBodyFixed(False)
body_4.SetCollide(False)

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_4.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('Main_leg-4')
body_5.SetPos(chrono.ChVectorD(0.025,-0.355,0.025))
body_5.SetRot(chrono.ChQuaternionD(-0.5,0.5,0.5,0.5))
body_5.SetMass(0.314182522957532)
body_5.SetInertiaXX(chrono.ChVectorD(0.000216025953973108,0.00338823977615053,0.00338363272051758))
body_5.SetInertiaXY(chrono.ChVectorD(-4.38405724653105e-20,-5.97501259547907e-20,1.54689239522068e-20))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.53438639878404e-18,-7.55706440556755e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))
mesh_5 = chrono.ChTriangleMeshConnected()
mesh_5.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_2_1.obj'))
mesh_5.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_5 = chrono.ChMaterialSurfaceSMC()
body_5.GetCollisionModel().ClearModel()
body_5.GetCollisionModel().AddTriangleMesh(material_5,                # contact material
                                            mesh_5,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_5.GetCollisionModel().BuildModel()
body_5.SetBodyFixed(False)
body_5.SetCollide(False)
# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_5.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_5)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Main_leg-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.025,-0.025,0.41)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.025,-0.025,0.16)
dB = chrono.ChVectorD(0,0,1)
link_1.SetFlipped(True)
link_1.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
#exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.025,-0.025,0.41)
cB = chrono.ChVectorD(0.025,-0.025,0.16)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_2.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
#exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Main_leg-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.025,-0.025,0.41)
cB = chrono.ChVectorD(0.05,-0.355,0.41)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,-1)
link_3.Initialize(body_1,body_2,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
#exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.025,-0.025,0.41)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0.05,-0.355,0.41)
dB = chrono.ChVectorD(0,0,-1)
link_4.SetFlipped(True)
link_4.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
#exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Main_leg-4 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.025,-0.025,0.41)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.025,-0.025,-0.25)
dB = chrono.ChVectorD(0,0,1)
link_5.SetFlipped(True)
link_5.Initialize(body_1,body_5,False,cA,cB,dA,dB)
#link_5.AddAsset()
link_5.SetName("Concentric2")
#exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.025,-0.025,0.41)
cB = chrono.ChVectorD(0.025,-0.025,-0.25)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_6.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
#exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Main_leg-4 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.025,-0.025,0.05)
cB = chrono.ChVectorD(3.46944695195361e-17,0.00499999999999995,0.05)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_7.Initialize(body_1,body_5,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
#exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.025,-0.025,0.05)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(3.46944695195361e-17,0.00499999999999995,0.05)
dB = chrono.ChVectorD(0,0,1)
link_8.SetFlipped(True)
link_8.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
#exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: Main_leg-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Main_leg-4 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0250000000000001,-0.325,0.25)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.025,-0.325,-0.25)
dB = chrono.ChVectorD(0,0,1)
link_9.SetFlipped(True)
link_9.Initialize(body_4,body_5,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
#exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0250000000000001,-0.325,0.25)
cB = chrono.ChVectorD(0.025,-0.325,-0.25)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_10.Initialize(body_4,body_5,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
#exported_items.append(link_10)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: Main_leg-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Main_leg-4 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.05,-0.295,-2.42861286636753e-17)
cB = chrono.ChVectorD(3.46944695195361e-17,0.00499999999999995,-3.46944695195361e-18)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,-1)
link_11.Initialize(body_4,body_5,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident3")
#exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.05,-0.295,-2.42861286636753e-17)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(3.46944695195361e-17,0.00499999999999995,-3.46944695195361e-18)
dB = chrono.ChVectorD(0,0,-1)
link_12.SetFlipped(True)
link_12.Initialize(body_4,body_5,False,cA,cB,dA,dB)
link_12.SetName("Coincident3")
#exported_items.append(link_12)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Main_leg-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Main_leg-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0250000000000001,-0.325,0.16)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0.025,-0.325,0.76)
dB = chrono.ChVectorD(0,0,-1)
link_13.SetFlipped(True)
link_13.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_13.SetName("Concentric4")
#exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0250000000000001,-0.325,0.16)
cB = chrono.ChVectorD(0.025,-0.325,0.76)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,-1)
link_14.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_14.SetName("Concentric4")
#exported_items.append(link_14)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Main_leg-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Main_leg-2 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.05,-0.355,0.46)
cB = chrono.ChVectorD(4.5102810375397e-17,-0.655,0.46)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,-1)
link_15.Initialize(body_2,body_3,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident4")
#exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.05,-0.355,0.46)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(4.5102810375397e-17,-0.655,0.46)
dB = chrono.ChVectorD(0,0,-1)
link_16.SetFlipped(True)
link_16.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_16.SetName("Coincident4")
#exported_items.append(link_16)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Main_leg-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Main_leg-2 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.05,-0.355,0.41)
cB = chrono.ChVectorD(0.0500000000000001,-0.655,0.51)
dA = chrono.ChVectorD(1,6.93889390390723e-18,0)
dB = chrono.ChVectorD(1,0,0)
link_17.Initialize(body_2,body_3,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Coincident5")
#exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.05,-0.355,0.41)
dA = chrono.ChVectorD(1,6.93889390390723e-18,0)
cB = chrono.ChVectorD(0.0500000000000001,-0.655,0.51)
dB = chrono.ChVectorD(1,0,0)
link_18.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_18.SetName("Coincident5")
#exported_items.append(link_18)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_4 , SW name: Main_leg-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Main_leg-4 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.05,-0.295,-2.42861286636753e-17)
cB = chrono.ChVectorD(0.05,0.00499999999999995,-3.46944695195361e-18)
dA = chrono.ChVectorD(1,-4.85722573273506e-17,0)
dB = chrono.ChVectorD(1,-1.38777878078145e-17,0)
link_19.Initialize(body_4,body_5,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident6")
#exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.05,-0.295,-2.42861286636753e-17)
dA = chrono.ChVectorD(1,-4.85722573273506e-17,0)
cB = chrono.ChVectorD(0.05,0.00499999999999995,-3.46944695195361e-18)
dB = chrono.ChVectorD(1,-1.38777878078145e-17,0)
link_20.Initialize(body_4,body_5,False,cA,cB,dA,dB)
link_20.SetName("Coincident6")
#exported_items.append(link_20)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Main_leg-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.05,-0.025,0.41)
cB = chrono.ChVectorD(0.05,-0.355,0.41)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,6.93889390390723e-18,0)
link_21.Initialize(body_1,body_2,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Coincident7")
#exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.05,-0.025,0.41)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.05,-0.355,0.41)
dB = chrono.ChVectorD(1,6.93889390390723e-18,0)
link_22.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_22.SetName("Coincident7")
#exported_items.append(link_22)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Main_leg-4 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.05,-0.025,0.41)
cB = chrono.ChVectorD(0.05,0.00499999999999995,-3.46944695195361e-18)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,-1.38777878078145e-17,0)
link_23.Initialize(body_1,body_5,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Coincident8")
#exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.05,-0.025,0.41)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.05,0.00499999999999995,-3.46944695195361e-18)
dB = chrono.ChVectorD(1,-1.38777878078145e-17,0)
link_24.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_24.SetName("Coincident8")
#exported_items.append(link_24)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: Main_leg-4 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(3.46944695195361e-17,0.00499999999999995,-3.46944695195361e-18)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_25.Initialize(body_5,body_0,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Coincident9")
#exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(3.46944695195361e-17,0.00499999999999995,-3.46944695195361e-18)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_26.SetFlipped(True)
link_26.Initialize(body_5,body_0,False,cA,cB,dA,dB)
link_26.SetName("Coincident9")
#exported_items.append(link_26)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_27 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.025,0,0.41)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_27.Initialize(body_1,body_0,False,cA,cB,dB)
link_27.SetDistance(0)
link_27.SetName("Coincident10")
#exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.025,0,0.41)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,1,0)
link_28.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_28.SetName("Coincident10")
#exported_items.append(link_28)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_29 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-3.46944695195361e-18,-0.025,0.41)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_29.Initialize(body_1,body_0,False,cA,cB,dB)
link_29.SetDistance(0)
link_29.SetName("Coincident11")
#exported_items.append(link_29)

link_30 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-3.46944695195361e-18,-0.025,0.41)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_30.SetFlipped(True)
link_30.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_30.SetName("Coincident11")
#exported_items.append(link_30)

