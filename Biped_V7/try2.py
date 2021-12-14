# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: 


import pychrono as chrono 
import builtins 

shapes_dir = 'try2_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('leg-1')
body_1.SetPos(chrono.ChVectorD(0.15,0.01,0.16))
body_1.SetRot(chrono.ChQuaternionD(0.707106781186547,0,-0.707106781186547,0))
body_1.SetMass(0.00569292036732052)
body_1.SetInertiaXX(chrono.ChVectorD(7.26057597221778e-07,1.0660158649151e-05,1.06741125565207e-05))
body_1.SetInertiaXY(chrono.ChVectorD(-2.0585724061437e-21,-1.68667296778391e-21,7.06016023606855e-23))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.64366357978219e-17,1.84821439837332e-17,0.075),chrono.ChQuaternionD(1,0,0,0)))
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
body_1.SetCollide(True)

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
body_2.SetName('leg-2')
body_2.SetPos(chrono.ChVectorD(0.28,0.01,0.18))
body_2.SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0))
body_2.SetMass(0.00569292036732052)
body_2.SetInertiaXX(chrono.ChVectorD(7.26057597221778e-07,1.0660158649151e-05,1.06741125565207e-05))
body_2.SetInertiaXY(chrono.ChVectorD(-2.0585724061437e-21,-1.68667296778391e-21,7.06016023606855e-23))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.64366357978219e-17,1.84821439837332e-17,0.075),chrono.ChQuaternionD(1,0,0,0)))
mesh_2 = chrono.ChTriangleMeshConnected()
mesh_2.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
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
body_2.SetCollide(True)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Torso-1')
body_3.SetPos(chrono.ChVectorD(0.01,0.01,0))
body_3.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_3.SetMass(0.0482190275490383)
body_3.SetInertiaXX(chrono.ChVectorD(9.23370455766283e-05,9.23370455766283e-05,3.85273784436298e-06))
body_3.SetInertiaXY(chrono.ChVectorD(-4.68268034450765e-39,-1.83670992315982e-38,0))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(2.90671085979368e-18,5.1383868916214e-19,0.075),chrono.ChQuaternionD(1,0,0,0)))
mesh_3 = chrono.ChTriangleMeshConnected()
mesh_3.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_3_1.obj'))
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
body_3.SetCollide(True)

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_3.GetAssets().push_back(body_3_1_level) 

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('leg-4')
body_4.SetPos(chrono.ChVectorD(0.28,0.00999999999999993,-0.03))
body_4.SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0))
body_4.SetMass(0.00569292036732052)
body_4.SetInertiaXX(chrono.ChVectorD(7.26057597221778e-07,1.0660158649151e-05,1.06741125565207e-05))
body_4.SetInertiaXY(chrono.ChVectorD(-2.0585724061437e-21,-1.68667296778391e-21,7.06016023606856e-23))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.64366357978219e-17,1.84821439837332e-17,0.075),chrono.ChQuaternionD(1,0,0,0)))
mesh_4 = chrono.ChTriangleMeshConnected()
mesh_4.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
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
body_4.SetBodyFixed(True)
body_4.SetCollide(True)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_4.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('leg-3')
body_5.SetPos(chrono.ChVectorD(0.15,0.00999999999999999,-0.01))
body_5.SetRot(chrono.ChQuaternionD(0.707106781186548,0,-0.707106781186547,0))
body_5.SetMass(0.00569292036732052)
body_5.SetInertiaXX(chrono.ChVectorD(7.26057597221778e-07,1.0660158649151e-05,1.06741125565207e-05))
body_5.SetInertiaXY(chrono.ChVectorD(-2.0585724061437e-21,-1.68667296778391e-21,7.06016023606856e-23))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.64366357978219e-17,1.84821439837332e-17,0.075),chrono.ChQuaternionD(1,0,0,0)))
mesh_5 = chrono.ChTriangleMeshConnected()
mesh_5.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
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
body_5.SetBodyFixed(True)
body_5.SetCollide(True)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_5.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_5)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: leg-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.01,0.00999999999999999,0.15)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.01,0.01,0.02)
dB = chrono.ChVectorD(0,0,1)
link_1.SetFlipped(True)
link_1.Initialize(body_3,body_1,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.01,0.00999999999999999,0.15)
cB = chrono.ChVectorD(0.01,0.01,0.02)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_2.Initialize(body_3,body_1,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: leg-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.01,0.01,0.15)
cB = chrono.ChVectorD(0,0,0.15)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,-1)
link_3.Initialize(body_3,body_1,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.01,0.01,0.15)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0,0,0.15)
dB = chrono.ChVectorD(0,0,-1)
link_4.SetFlipped(True)
link_4.Initialize(body_3,body_1,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: leg-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: leg-2 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.14,0.01,0.02)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0.14,0.01,0.0400000000000001)
dB = chrono.ChVectorD(0,0,1)
link_5.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_5.SetName("Concentric3")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.14,0.01,0.02)
cB = chrono.ChVectorD(0.14,0.01,0.0400000000000001)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,1)
link_6.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_6.SetName("Concentric3")
exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: leg-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: leg-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0.17)
cB = chrono.ChVectorD(0.13,2.42861286636753e-17,0.17)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,-1)
link_7.Initialize(body_1,body_2,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0.17)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0.13,2.42861286636753e-17,0.17)
dB = chrono.ChVectorD(0,0,-1)
link_8.SetFlipped(True)
link_8.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
exported_items.append(link_8)


# Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: leg-3 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.01,0.00999999999999999,0.15)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.00999999999999995,0.00999999999999999,-0.15)
dB = chrono.ChVectorD(0,0,1)
link_9.SetFlipped(True)
link_9.Initialize(body_3,body_5,False,cA,cB,dA,dB)
link_9.SetName("Concentric4")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.01,0.00999999999999999,0.15)
cB = chrono.ChVectorD(0.00999999999999995,0.00999999999999999,-0.15)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_10.Initialize(body_3,body_5,False,cA,cB,dA,dB)
link_10.SetName("Concentric4")
exported_items.append(link_10)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: leg-3 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.01,0.01,0)
cB = chrono.ChVectorD(-5.55111512312578e-17,-1.21430643318376e-17,6.93889390390723e-18)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_11.Initialize(body_3,body_5,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident3")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.01,0.01,0)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(-5.55111512312578e-17,-1.21430643318376e-17,6.93889390390723e-18)
dB = chrono.ChVectorD(0,0,1)
link_12.SetFlipped(True)
link_12.Initialize(body_3,body_5,False,cA,cB,dA,dB)
link_12.SetName("Coincident3")
exported_items.append(link_12)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: leg-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: leg-4 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.14,0.00999999999999999,-0.15)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0.14,0.00999999999999993,-0.17)
dB = chrono.ChVectorD(0,0,1)
link_13.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_13.SetName("Concentric5")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.14,0.00999999999999999,-0.15)
cB = chrono.ChVectorD(0.14,0.00999999999999993,-0.17)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,1)
link_14.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_14.SetName("Concentric5")
exported_items.append(link_14)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: leg-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: leg-4 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-5.55111512312578e-17,-1.21430643318376e-17,-0.02)
cB = chrono.ChVectorD(0.13,-7.63278329429795e-17,-0.02)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_15.Initialize(body_5,body_4,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident4")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-5.55111512312578e-17,-1.21430643318376e-17,-0.02)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.13,-7.63278329429795e-17,-0.02)
dB = chrono.ChVectorD(0,0,1)
link_16.SetFlipped(True)
link_16.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_16.SetName("Coincident4")
exported_items.append(link_16)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_17 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.01,0.01,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_17.Initialize(body_3,body_0,False,cA,cB,dB)
link_17.SetDistance(0)
link_17.SetName("Coincident5")
#exported_items.append(link_17)

link_18 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.01,0.01,0)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_18.SetFlipped(True)
link_18.Initialize(body_3,body_0,False,cA,cB,dA,dB)
link_18.SetName("Coincident5")
#exported_items.append(link_18)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,-5.20417042793042e-18,0.15)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_19.Initialize(body_3,body_0,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident6")
#exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,-5.20417042793042e-18,0.15)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_20.SetFlipped(True)
link_20.Initialize(body_3,body_0,False,cA,cB,dA,dB)
link_20.SetName("Coincident6")
#exported_items.append(link_20)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,-5.20417042793042e-18,0.15)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(0,1,0)
link_21.Initialize(body_3,body_0,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Coincident7")
#exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,-5.20417042793042e-18,0.15)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,1,0)
link_22.SetFlipped(True)
link_22.Initialize(body_3,body_0,False,cA,cB,dA,dB)
link_22.SetName("Coincident7")
#exported_items.append(link_22)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: leg-3 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0.02,0.15)
cB = chrono.ChVectorD(-5.55111512312578e-17,0.02,-0.02)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_23.Initialize(body_3,body_5,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Coincident8")
#exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0.02,0.15)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(-5.55111512312578e-17,0.02,-0.02)
dB = chrono.ChVectorD(0,1,0)
link_24.Initialize(body_3,body_5,False,cA,cB,dA,dB)
link_24.SetName("Coincident8")
#exported_items.append(link_24)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: leg-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: leg-4 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-5.55111512312578e-17,0.02,-0.02)
cB = chrono.ChVectorD(0.13,0.0199999999999999,-0.04)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_25.Initialize(body_5,body_4,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Coincident9")
#exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-5.55111512312578e-17,0.02,-0.02)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0.13,0.0199999999999999,-0.04)
dB = chrono.ChVectorD(0,1,0)
link_26.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_26.SetName("Coincident9")
#exported_items.append(link_26)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: leg-1 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0.02,0.15)
cB = chrono.ChVectorD(0,0.02,0.15)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_27.Initialize(body_3,body_1,False,cA,cB,dB)
link_27.SetDistance(0)
link_27.SetName("Coincident10")
#exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0.02,0.15)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0,0.02,0.15)
dB = chrono.ChVectorD(0,1,0)
link_28.Initialize(body_3,body_1,False,cA,cB,dA,dB)
link_28.SetName("Coincident10")
#exported_items.append(link_28)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: leg-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: leg-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0.02,0.15)
cB = chrono.ChVectorD(0.13,0.02,0.17)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_29.Initialize(body_1,body_2,False,cA,cB,dB)
link_29.SetDistance(0)
link_29.SetName("Coincident11")
#exported_items.append(link_29)

link_30 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0.02,0.15)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0.13,0.02,0.17)
dB = chrono.ChVectorD(0,1,0)
link_30.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_30.SetName("Coincident11")
#exported_items.append(link_30)

