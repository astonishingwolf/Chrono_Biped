# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\Chrono_Biped\BIped_V8\bp.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'bp_shapes/' 

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
body_1.SetPos(chrono.ChVectorD(0.01,0.01,0))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(0.0597809724509617)
body_1.SetInertiaXX(chrono.ChVectorD(0.000140625912538313,4.84277733151519e-05,9.58767412289814e-05))
body_1.SetInertiaXY(chrono.ChVectorD(4.83878358182806e-22,-3.52930394689291e-22,-1.00230259135432e-20))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(3.38915551194847e-19,0.0248306855503033,0.06),chrono.ChQuaternionD(1,0,0,0)))
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
body_2.SetName('Leg-4')
body_2.SetPos(chrono.ChVectorD(0.01,-0.26,-0.03))
body_2.SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5))
body_2.SetMass(0.011085840734641)
body_2.SetInertiaXX(chrono.ChVectorD(1.34525745095411e-06,2.07315501130413e-05,2.07051345548124e-05))
body_2.SetInertiaXY(chrono.ChVectorD(9.83202385717014e-22,6.09157861233718e-22,6.20795015996829e-23))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-9.43872349021925e-18,4.83272628537986e-18,0.075),chrono.ChQuaternionD(1,0,0,0)))
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
body_2.SetBodyFixed(False)
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
body_3.SetName('Leg-3')
body_3.SetPos(chrono.ChVectorD(0.01,-0.26,0.15))
body_3.SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5))
body_3.SetMass(0.011085840734641)
body_3.SetInertiaXX(chrono.ChVectorD(1.34525745095411e-06,2.07315501130413e-05,2.07051345548124e-05))
body_3.SetInertiaXY(chrono.ChVectorD(9.83202385717014e-22,6.09157861233718e-22,6.28126806235343e-23))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-9.43872349021925e-18,4.83272628537986e-18,0.075),chrono.ChQuaternionD(1,0,0,0)))
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
body_3.SetBodyFixed(False)
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
body_4.SetName('Leg-2')
body_4.SetPos(chrono.ChVectorD(0.01,-0.13,-0.01))
body_4.SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5))
body_4.SetMass(0.011085840734641)
body_4.SetInertiaXX(chrono.ChVectorD(1.34525745095411e-06,2.07315501130413e-05,2.07051345548124e-05))
body_4.SetInertiaXY(chrono.ChVectorD(9.83202385717014e-22,6.09157861233718e-22,6.28126806235339e-23))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-9.43872349021925e-18,4.83272628537986e-18,0.075),chrono.ChQuaternionD(1,0,0,0)))
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
body_5.SetName('Leg-1')
body_5.SetPos(chrono.ChVectorD(0.01,-0.13,0.13))
body_5.SetRot(chrono.ChQuaternionD(0.5,-0.5,-0.5,-0.5))
body_5.SetMass(0.011085840734641)
body_5.SetInertiaXX(chrono.ChVectorD(1.34525745095411e-06,2.07315501130413e-05,2.07051345548124e-05))
body_5.SetInertiaXY(chrono.ChVectorD(9.83202385717014e-22,6.09157861233718e-22,6.20795015996829e-23))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-9.43872349021925e-18,4.83272628537986e-18,0.075),chrono.ChQuaternionD(1,0,0,0)))
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


# =============================================================================
# 
# # Rigid body part
# body_6= chrono.ChBodyAuxRef()
# body_6.SetName('foot2-2')
# body_6.SetPos(chrono.ChVectorD(0.0815122588463411,-0.25,0.13))
# body_6.SetRot(chrono.ChQuaternionD(1,0,0,0))
# body_6.SetMass(0.0363806034038677)
# body_6.SetInertiaXX(chrono.ChVectorD(7.03687599506156e-06,1.52472732066469e-05,1.0668495695318e-05))
# body_6.SetInertiaXY(chrono.ChVectorD(1.80888883561503e-22,1.9064639122864e-22,2.80235531152582e-22))
# body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.0289190202186129,-2.2400744469877e-19,0.02),chrono.ChQuaternionD(1,0,0,0)))
# mesh_6 = chrono.ChTriangleMeshConnected()
# mesh_6.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_6_1.obj'))
# mesh_6.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# material_6 = chrono.ChMaterialSurfaceSMC()
# body_6.GetCollisionModel().ClearModel()
# body_6.GetCollisionModel().AddTriangleMesh(material_6,                # contact material
#                                             mesh_6,                    # the mesh 
#                                             False,                   # is it static?
#                                             False,                   # is it convex?
#                                             chrono.ChVectorD(0,0,0), # position on body
#                                             chrono.ChMatrix33D(1),   # orientation on body 
#                                             0.01)                    # "thickness" for increased robustness
# body_6.GetCollisionModel().BuildModel()
# body_6.SetBodyFixed(False)
# body_6.SetCollide(True)
# 
# # Visualization shape 
# body_6_1_shape = chrono.ChObjShapeFile() 
# body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
# body_6_1_level = chrono.ChAssetLevel() 
# body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
# body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
# body_6_1_level.GetAssets().push_back(body_6_1_shape) 
# body_6.GetAssets().push_back(body_6_1_level) 
# 
# exported_items.append(body_6)
# 
# 
# 
# # Rigid body part
# body_7= chrono.ChBodyAuxRef()
# body_7.SetName('foot1-2')
# body_7.SetPos(chrono.ChVectorD(0.01,-0.25,-0.05))
# body_7.SetRot(chrono.ChQuaternionD(1,0,0,0))
# body_7.SetMass(0.0451513997306626)
# body_7.SetInertiaXX(chrono.ChVectorD(7.63795821191866e-06,2.56155980781203e-05,2.1053183028529e-05))
# body_7.SetInertiaXY(chrono.ChVectorD(-9.54247213948555e-22,-6.20385459414771e-22,1.02744646208717e-22))
# body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.0360530173074554,6.62673811516263e-19,0.02),chrono.ChQuaternionD(1,0,0,0)))
# mesh_7 = chrono.ChTriangleMeshConnected()
# mesh_7.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_7_1.obj'))
# mesh_7.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# material_7 = chrono.ChMaterialSurfaceSMC()
# body_7.GetCollisionModel().ClearModel()
# body_7.GetCollisionModel().AddTriangleMesh(material_7,                # contact material
#                                             mesh_7,                    # the mesh 
#                                             False,                   # is it static?
#                                             False,                   # is it convex?
#                                             chrono.ChVectorD(0,0,0), # position on body
#                                             chrono.ChMatrix33D(1),   # orientation on body 
#                                             0.01)                    # "thickness" for increased robustness
# body_7.GetCollisionModel().BuildModel()
# body_7.SetBodyFixed(False)
# body_7.SetCollide(True)
# 
# # Visualization shape 
# body_7_1_shape = chrono.ChObjShapeFile() 
# body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
# body_7_1_level = chrono.ChAssetLevel() 
# body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
# body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
# body_7_1_level.GetAssets().push_back(body_7_1_shape) 
# body_7.GetAssets().push_back(body_7_1_level) 
# 
# exported_items.append(body_7)
# 
# 
# 
# # Rigid body part
# body_8= chrono.ChBodyAuxRef()
# body_8.SetName('foot2-3')
# body_8.SetPos(chrono.ChVectorD(0.081512258846341,-0.25,-0.05))
# body_8.SetRot(chrono.ChQuaternionD(1,0,0,0))
# body_8.SetMass(0.0363806034038677)
# body_8.SetInertiaXX(chrono.ChVectorD(7.03687599506156e-06,1.52472732066469e-05,1.0668495695318e-05))
# body_8.SetInertiaXY(chrono.ChVectorD(1.80888883561503e-22,1.9064639122864e-22,2.80235531152582e-22))
# body_8.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.0289190202186129,-2.2400744469877e-19,0.02),chrono.ChQuaternionD(1,0,0,0)))
# mesh_8 = chrono.ChTriangleMeshConnected()
# mesh_8.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_6_1.obj'))
# mesh_8.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# material_8 = chrono.ChMaterialSurfaceSMC()
# body_8.GetCollisionModel().ClearModel()
# body_8.GetCollisionModel().AddTriangleMesh(material_8,                # contact material
#                                             mesh_8,                    # the mesh 
#                                             False,                   # is it static?
#                                             False,                   # is it convex?
#                                             chrono.ChVectorD(0,0,0), # position on body
#                                             chrono.ChMatrix33D(1),   # orientation on body 
#                                             0.01)                    # "thickness" for increased robustness
# body_8.GetCollisionModel().BuildModel()
# body_8.SetBodyFixed(False)
# body_8.SetCollide(True)
# 
# # Visualization shape 
# body_6_1_shape = chrono.ChObjShapeFile() 
# body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
# body_6_1_level = chrono.ChAssetLevel() 
# body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
# body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
# body_6_1_level.GetAssets().push_back(body_6_1_shape) 
# body_8.GetAssets().push_back(body_6_1_level) 
# 
# exported_items.append(body_8)
# 
# 
# 
# # Rigid body part
# body_9= chrono.ChBodyAuxRef()
# body_9.SetName('foot1-1')
# body_9.SetPos(chrono.ChVectorD(0.01,-0.25,0.13))
# body_9.SetRot(chrono.ChQuaternionD(1,0,0,0))
# body_9.SetMass(0.0451513997306626)
# body_9.SetInertiaXX(chrono.ChVectorD(7.63795821191866e-06,2.56155980781203e-05,2.1053183028529e-05))
# body_9.SetInertiaXY(chrono.ChVectorD(-9.54247213948555e-22,-6.20385459414771e-22,1.02744646208717e-22))
# body_9.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.0360530173074554,6.62673811516263e-19,0.02),chrono.ChQuaternionD(1,0,0,0)))
# mesh_9 = chrono.ChTriangleMeshConnected()
# mesh_9.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_7_1.obj'))
# mesh_9.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# material_9 = chrono.ChMaterialSurfaceSMC()
# body_9.GetCollisionModel().ClearModel()
# body_8.GetCollisionModel().AddTriangleMesh(material_9,                # contact material
#                                             mesh_9,                    # the mesh 
#                                             False,                   # is it static?
#                                             False,                   # is it convex?
#                                             chrono.ChVectorD(0,0,0), # position on body
#                                             chrono.ChMatrix33D(1),   # orientation on body 
#                                             0.01)                    # "thickness" for increased robustness
# body_9.GetCollisionModel().BuildModel()
# body_9.SetBodyFixed(False)
# body_9.SetCollide(True)
# 
# #body 9 Right Feet 1
# #body 8 Left  Feet 2
# #body 7 Left  Feet 1
# #body 6 Right Feet 2
# #body 5 Right Thigh
# #body 4 Left Thigh 
# #body 3 Right Leg
# #body 2 Left leg
# #body 1 Torso
# # Visualization shape 
# body_7_1_shape = chrono.ChObjShapeFile() 
# body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
# body_7_1_level = chrono.ChAssetLevel() 
# body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
# body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
# body_7_1_level.GetAssets().push_back(body_7_1_shape) 
# body_9.GetAssets().push_back(body_7_1_level) 
# 
# exported_items.append(body_9)
# 
# =============================================================================



# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: Leg-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.01,0.01,0.12)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.00999999999999999,0.00999999999999998,-0.00999999999999998)
dB = chrono.ChVectorD(0,0,1)
link_1.SetFlipped(True)
link_1.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.01,0.01,0.12)
cB = chrono.ChVectorD(0.00999999999999999,0.00999999999999998,-0.00999999999999998)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_2.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# =============================================================================
# # Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_5 , SW name: Leg-1 ,  SW ref.type:2 (2)
# 
# link_3 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(0.01,0.01,0.12)
# cB = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.12)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,-1)
# link_3.Initialize(body_1,body_5,False,cA,cB,dB)
# link_3.SetDistance(0)
# link_3.SetName("Coincident1")
# exported_items.append(link_3)
# 
# link_4 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,0.01,0.12)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.12)
# dB = chrono.ChVectorD(0,0,-1)
# link_4.SetFlipped(True)
# link_4.Initialize(body_1,body_5,False,cA,cB,dA,dB)
# link_4.SetName("Coincident1")
# exported_items.append(link_4)
# 
# 
# # Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
# #   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_4 , SW name: Leg-2 ,  SW ref.type:2 (2)
# 
# link_5 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,0.01,0.12)
# dA = chrono.ChVectorD(0,0,-1)
# cB = chrono.ChVectorD(0.01,0.01,-0.15)
# dB = chrono.ChVectorD(0,0,1)
# link_5.SetFlipped(True)
# link_5.Initialize(body_1,body_4,False,cA,cB,dA,dB)
# link_5.SetName("Concentric2")
# exported_items.append(link_5)
# 
# link_6 = chrono.ChLinkMateGeneric()
# link_6.SetConstrainedCoords(False, True, True, False, False, False)
# cA = chrono.ChVectorD(0.01,0.01,0.12)
# cB = chrono.ChVectorD(0.01,0.01,-0.15)
# dA = chrono.ChVectorD(0,0,-1)
# dB = chrono.ChVectorD(0,0,1)
# link_6.Initialize(body_1,body_4,False,cA,cB,dA,dB)
# link_6.SetName("Concentric2")
# exported_items.append(link_6)
# 
# 
# # Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_4 , SW name: Leg-2 ,  SW ref.type:2 (2)
# 
# link_7 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(0.01,0.01,0)
# cB = chrono.ChVectorD(1.04083408558608e-17,0.02,-3.46944695195361e-18)
# dA = chrono.ChVectorD(0,0,-1)
# dB = chrono.ChVectorD(0,0,1)
# link_7.Initialize(body_1,body_4,False,cA,cB,dB)
# link_7.SetDistance(0)
# link_7.SetName("Coincident2")
# exported_items.append(link_7)
# 
# link_8 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,0.01,0)
# dA = chrono.ChVectorD(0,0,-1)
# cB = chrono.ChVectorD(1.04083408558608e-17,0.02,-3.46944695195361e-18)
# dB = chrono.ChVectorD(0,0,1)
# link_8.SetFlipped(True)
# link_8.Initialize(body_1,body_4,False,cA,cB,dA,dB)
# link_8.SetName("Coincident2")
# exported_items.append(link_8)
# 
# 
# # Mate constraint: Concentric5 [MateConcentric] type:1 align:0 flip:False
# #   Entity 0: C::E name: body_5 , SW name: Leg-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_3 , SW name: Leg-3 ,  SW ref.type:2 (2)
# 
# link_9 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,-0.12,-0.00999999999999998)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.01,-0.12,0.01)
# dB = chrono.ChVectorD(0,0,1)
# link_9.Initialize(body_5,body_3,False,cA,cB,dA,dB)
# link_9.SetName("Concentric5")
# exported_items.append(link_9)
# 
# link_10 = chrono.ChLinkMateGeneric()
# link_10.SetConstrainedCoords(False, True, True, False, False, False)
# cA = chrono.ChVectorD(0.01,-0.12,-0.00999999999999998)
# cB = chrono.ChVectorD(0.01,-0.12,0.01)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,1)
# link_10.Initialize(body_5,body_3,False,cA,cB,dA,dB)
# link_10.SetName("Concentric5")
# exported_items.append(link_10)
# #
# 
# # Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_5 , SW name: Leg-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_3 , SW name: Leg-3 ,  SW ref.type:2 (2)
# 
# link_11 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.14)
# cB = chrono.ChVectorD(1.04083408558608e-17,-0.11,0.14)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,-1)
# link_11.Initialize(body_5,body_3,False,cA,cB,dB)
# link_11.SetDistance(0)
# link_11.SetName("Coincident5")
# exported_items.append(link_11)
# 
# link_12 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.14)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(1.04083408558608e-17,-0.11,0.14)
# dB = chrono.ChVectorD(0,0,-1)
# link_12.SetFlipped(True)
# link_12.Initialize(body_5,body_3,False,cA,cB,dA,dB)
# link_12.SetName("Coincident5")
# exported_items.append(link_12)
# 
# 
# # Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
# #   Entity 0: C::E name: body_4 , SW name: Leg-2 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_2 , SW name: Leg-4 ,  SW ref.type:2 (2)
# 
# link_13 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,-0.12,-0.15)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.01,-0.12,-0.17)
# dB = chrono.ChVectorD(0,0,1)
# link_13.Initialize(body_4,body_2,False,cA,cB,dA,dB)
# link_13.SetName("Concentric6")
# exported_items.append(link_13)
# 
# link_14 = chrono.ChLinkMateGeneric()
# link_14.SetConstrainedCoords(False, True, True, False, False, False)
# cA = chrono.ChVectorD(0.01,-0.12,-0.15)
# cB = chrono.ChVectorD(0.01,-0.12,-0.17)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,1)
# link_14.Initialize(body_4,body_2,False,cA,cB,dA,dB)
# link_14.SetName("Concentric6")
# exported_items.append(link_14)
# 
# 
# # Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_4 , SW name: Leg-2 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_2 , SW name: Leg-4 ,  SW ref.type:2 (2)
# 
# link_15 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(1.04083408558608e-17,0.02,-0.02)
# cB = chrono.ChVectorD(-6.93889390390723e-18,-0.11,-0.02)
# dA = chrono.ChVectorD(0,0,-1)
# dB = chrono.ChVectorD(0,0,1)
# link_15.Initialize(body_4,body_2,False,cA,cB,dB)
# link_15.SetDistance(0)
# link_15.SetName("Coincident6")
# exported_items.append(link_15)
# 
# link_16 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(1.04083408558608e-17,0.02,-0.02)
# dA = chrono.ChVectorD(0,0,-1)
# cB = chrono.ChVectorD(-6.93889390390723e-18,-0.11,-0.02)
# dB = chrono.ChVectorD(0,0,1)
# link_16.SetFlipped(True)
# link_16.Initialize(body_4,body_2,False,cA,cB,dA,dB)
# link_16.SetName("Coincident6")
# exported_items.append(link_16)
# =============================================================================


# Mate constraint: Concentric8 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Leg-3 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: foot1-1 ,  SW ref.type:2 (2)
# =============================================================================
# 
# link_17 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,-0.25,0.01)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.01,-0.25,0.13)
# dB = chrono.ChVectorD(0,0,1)
# link_17.Initialize(body_3,body_9,False,cA,cB,dA,dB)
# link_17.SetName("Concentric8")
# #exported_items.append(link_17)
# 
# link_18 = chrono.ChLinkMateGeneric()
# link_18.SetConstrainedCoords(False, True, True, False, False, False)
# cA = chrono.ChVectorD(0.01,-0.25,0.01)
# cB = chrono.ChVectorD(0.01,-0.25,0.13)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,1)
# link_18.Initialize(body_3,body_9,False,cA,cB,dA,dB)
# link_18.SetName("Concentric8")
# #exported_items.append(link_18)
# 
# 
# # Mate constraint: Coincident8 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_3 , SW name: Leg-3 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_9 , SW name: foot1-1 ,  SW ref.type:2 (2)
# 
# link_19 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(1.04083408558608e-17,-0.11,0.16)
# cB = chrono.ChVectorD(0.03,-0.235527608818748,0.16)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,1.19864330244476e-16,-1)
# link_19.Initialize(body_3,body_9,False,cA,cB,dB)
# link_19.SetDistance(0)
# link_19.SetName("Coincident8")
# #exported_items.append(link_19)
# 
# link_20 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(1.04083408558608e-17,-0.11,0.16)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.03,-0.235527608818748,0.16)
# dB = chrono.ChVectorD(0,1.19864330244476e-16,-1)
# link_20.SetFlipped(True)
# link_20.Initialize(body_3,body_9,False,cA,cB,dA,dB)
# link_20.SetName("Coincident8")
# #exported_items.append(link_20)
# 
# 
# # Mate constraint: Concentric9 [MateConcentric] type:1 align:0 flip:False
# #   Entity 0: C::E name: body_2 , SW name: Leg-4 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_7 , SW name: foot1-2 ,  SW ref.type:2 (2)
# 
# link_21 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,-0.25,-0.17)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.01,-0.25,-0.05)
# dB = chrono.ChVectorD(0,0,1)
# link_21.Initialize(body_2,body_7,False,cA,cB,dA,dB)
# link_21.SetName("Concentric9")
# #exported_items.append(link_21)
# 
# link_22 = chrono.ChLinkMateGeneric()
# link_22.SetConstrainedCoords(False, True, True, False, False, False)
# cA = chrono.ChVectorD(0.01,-0.25,-0.17)
# cB = chrono.ChVectorD(0.01,-0.25,-0.05)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,1)
# link_22.Initialize(body_2,body_7,False,cA,cB,dA,dB)
# link_22.SetName("Concentric9")
# #exported_items.append(link_22)
# 
# 
# # Mate constraint: Coincident9 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_2 , SW name: Leg-4 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_7 , SW name: foot1-2 ,  SW ref.type:2 (2)
# 
# link_23 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(-6.93889390390723e-18,-0.11,-0.02)
# cB = chrono.ChVectorD(0.03,-0.235527608818748,-0.02)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,1.19864330244476e-16,-1)
# link_23.Initialize(body_2,body_7,False,cA,cB,dB)
# link_23.SetDistance(0)
# link_23.SetName("Coincident9")
# #exported_items.append(link_23)
# 
# link_24 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(-6.93889390390723e-18,-0.11,-0.02)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.03,-0.235527608818748,-0.02)
# dB = chrono.ChVectorD(0,1.19864330244476e-16,-1)
# link_24.SetFlipped(True)
# link_24.Initialize(body_2,body_7,False,cA,cB,dA,dB)
# link_24.SetName("Coincident9")
# #exported_items.append(link_24)
# 
# 
# # Mate constraint: Concentric10 [MateConcentric] type:1 align:0 flip:False
# #   Entity 0: C::E name: body_9 , SW name: foot1-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_6 , SW name: foot2-2 ,  SW ref.type:2 (2)
# 
# link_25 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.081512258846341,-0.25,0.14)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.0815122588463411,-0.25,0.13)
# dB = chrono.ChVectorD(0,0,1)
# link_25.Initialize(body_9,body_6,False,cA,cB,dA,dB)
# link_25.SetName("Concentric10")
# #exported_items.append(link_25)
# 
# link_26 = chrono.ChLinkMateGeneric()
# link_26.SetConstrainedCoords(False, True, True, False, False, False)
# cA = chrono.ChVectorD(0.081512258846341,-0.25,0.14)
# cB = chrono.ChVectorD(0.0815122588463411,-0.25,0.13)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,1)
# link_26.Initialize(body_9,body_6,False,cA,cB,dA,dB)
# link_26.SetName("Concentric10")
# #exported_items.append(link_26)
# 
# 
# # Mate constraint: Coincident10 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_9 , SW name: foot1-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_6 , SW name: foot2-2 ,  SW ref.type:2 (2)
# 
# link_27 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(0.01,-0.25,0.16)
# cB = chrono.ChVectorD(0.101512258846341,-0.235527608818748,0.16)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,1.19864330244476e-16,-1)
# link_27.Initialize(body_9,body_6,False,cA,cB,dB)
# link_27.SetDistance(0)
# link_27.SetName("Coincident10")
# #exported_items.append(link_27)
# 
# link_28 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,-0.25,0.16)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.101512258846341,-0.235527608818748,0.16)
# dB = chrono.ChVectorD(0,1.19864330244476e-16,-1)
# link_28.SetFlipped(True)
# link_28.Initialize(body_9,body_6,False,cA,cB,dA,dB)
# link_28.SetName("Coincident10")
# #exported_items.append(link_28)
# 
# 
# # Mate constraint: Concentric11 [MateConcentric] type:1 align:0 flip:False
# #   Entity 0: C::E name: body_7 , SW name: foot1-2 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_8 , SW name: foot2-3 ,  SW ref.type:2 (2)
# 
# link_29 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.081512258846341,-0.25,-0.04)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.081512258846341,-0.25,-0.05)
# dB = chrono.ChVectorD(0,0,1)
# link_29.Initialize(body_7,body_8,False,cA,cB,dA,dB)
# link_29.SetName("Concentric11")
# #exported_items.append(link_29)
# 
# link_30 = chrono.ChLinkMateGeneric()
# link_30.SetConstrainedCoords(False, True, True, False, False, False)
# cA = chrono.ChVectorD(0.081512258846341,-0.25,-0.04)
# cB = chrono.ChVectorD(0.081512258846341,-0.25,-0.05)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,1)
# link_30.Initialize(body_7,body_8,False,cA,cB,dA,dB)
# link_30.SetName("Concentric11")
# #exported_items.append(link_30)
# 
# 
# # Mate constraint: Coincident11 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_7 , SW name: foot1-2 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_8 , SW name: foot2-3 ,  SW ref.type:2 (2)
# 
# link_31 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(0.01,-0.25,-0.02)
# cB = chrono.ChVectorD(0.101512258846341,-0.235527608818748,-0.02)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,1.19864330244476e-16,-1)
# link_31.Initialize(body_7,body_8,False,cA,cB,dB)
# link_31.SetDistance(0)
# link_31.SetName("Coincident11")
# #exported_items.append(link_31)
# 
# link_32 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.01,-0.25,-0.02)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0.101512258846341,-0.235527608818748,-0.02)
# dB = chrono.ChVectorD(0,1.19864330244476e-16,-1)
# link_32.SetFlipped(True)
# link_32.Initialize(body_7,body_8,False,cA,cB,dA,dB)
# link_32.SetName("Coincident11")
# #exported_items.append(link_32)
# 
# =============================================================================

# Mate constraint: Coincident12 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: bp ,  SW ref.type:4 (4)
# =============================================================================
# 
# link_33 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(0,0.02,0.12)
# cB = chrono.ChVectorD(0,0,0)
# dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
# dB = chrono.ChVectorD(1,0,0)
# link_33.Initialize(body_1,body_0,False,cA,cB,dB)
# link_33.SetDistance(0)
# link_33.SetName("Coincident12")
# #exported_items.append(link_33)
# 
# link_34 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0,0.02,0.12)
# dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
# cB = chrono.ChVectorD(0,0,0)
# dB = chrono.ChVectorD(1,0,0)
# link_34.SetFlipped(True)
# link_34.Initialize(body_1,body_0,False,cA,cB,dA,dB)
# link_34.SetName("Coincident12")
# #exported_items.append(link_34)
# 
# 
# # Mate constraint: Coincident13 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name:  , SW name: bp ,  SW ref.type:4 (4)
# 
# link_35 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(3.46944695195361e-18,1.73472347597681e-18,0.12)
# cB = chrono.ChVectorD(0,0,0)
# dA = chrono.ChVectorD(0,-1,0)
# dB = chrono.ChVectorD(0,1,0)
# link_35.Initialize(body_1,body_0,False,cA,cB,dB)
# link_35.SetDistance(0)
# link_35.SetName("Coincident13")
# #exported_items.append(link_35)
# 
# link_36 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(3.46944695195361e-18,1.73472347597681e-18,0.12)
# dA = chrono.ChVectorD(0,-1,0)
# cB = chrono.ChVectorD(0,0,0)
# dB = chrono.ChVectorD(0,1,0)
# link_36.SetFlipped(True)
# link_36.Initialize(body_1,body_0,False,cA,cB,dA,dB)
# link_36.SetName("Coincident13")
# #exported_items.append(link_36)
# #
# 
# # Mate constraint: Coincident14 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_4 , SW name: Leg-2 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name:  , SW name: bp ,  SW ref.type:4 (4)
# 
# link_37 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(1.04083408558608e-17,0.02,-3.46944695195361e-18)
# cB = chrono.ChVectorD(0,0,0)
# dA = chrono.ChVectorD(0,0,1)
# dB = chrono.ChVectorD(0,0,1)
# link_37.Initialize(body_4,body_0,False,cA,cB,dB)
# link_37.SetDistance(0)
# link_37.SetName("Coincident14")
# #exported_items.append(link_37)
# 
# link_38 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(1.04083408558608e-17,0.02,-3.46944695195361e-18)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(0,0,0)
# dB = chrono.ChVectorD(0,0,1)
# link_38.Initialize(body_4,body_0,False,cA,cB,dA,dB)
# link_38.SetName("Coincident14")
# #exported_items.append(link_38)
# 
# 
# # Mate constraint: Coincident15 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_5 , SW name: Leg-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_4 , SW name: Leg-2 ,  SW ref.type:2 (2)
# 
# link_39 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.12)
# cB = chrono.ChVectorD(1.04083408558608e-17,0.02,-0.02)
# dA = chrono.ChVectorD(-1,-1.66533453693773e-16,0)
# dB = chrono.ChVectorD(-1,-1.38777878078145e-16,0)
# link_39.Initialize(body_5,body_4,False,cA,cB,dB)
# link_39.SetDistance(0)
# link_39.SetName("Coincident15")
# #exported_items.append(link_39)
# 
# link_40 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.12)
# dA = chrono.ChVectorD(-1,-1.66533453693773e-16,0)
# cB = chrono.ChVectorD(1.04083408558608e-17,0.02,-0.02)
# dB = chrono.ChVectorD(-1,-1.38777878078145e-16,0)
# link_40.Initialize(body_5,body_4,False,cA,cB,dA,dB)
# link_40.SetName("Coincident15")
# #exported_items.append(link_40)
# 
# 
# # Mate constraint: Coincident16 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_3 , SW name: Leg-3 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_2 , SW name: Leg-4 ,  SW ref.type:2 (2)
# 
# link_41 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(1.04083408558608e-17,-0.11,0.14)
# cB = chrono.ChVectorD(-6.93889390390723e-18,-0.11,-0.04)
# dA = chrono.ChVectorD(-1,-1.38777878078145e-16,0)
# dB = chrono.ChVectorD(-1,-1.66533453693773e-16,0)
# link_41.Initialize(body_3,body_2,False,cA,cB,dB)
# link_41.SetDistance(0)
# link_41.SetName("Coincident16")
# #exported_items.append(link_41)
# 
# link_42 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(1.04083408558608e-17,-0.11,0.14)
# dA = chrono.ChVectorD(-1,-1.38777878078145e-16,0)
# cB = chrono.ChVectorD(-6.93889390390723e-18,-0.11,-0.04)
# dB = chrono.ChVectorD(-1,-1.66533453693773e-16,0)
# link_42.Initialize(body_3,body_2,False,cA,cB,dA,dB)
# link_42.SetName("Coincident16")
# #exported_items.append(link_42)
# 
# 
# # Mate constraint: Coincident17 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_2 , SW name: Leg-4 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_7 , SW name: foot1-2 ,  SW ref.type:2 (2)
# # =============================================================================
# # 
# # link_43 = chrono.ChLinkMateXdistance()
# # cA = chrono.ChVectorD(0.01,-0.26,-0.03)
# # cB = chrono.ChVectorD(0.01,-0.26,-0.01)
# # dA = chrono.ChVectorD(1.66533453693773e-16,-1,0)
# # dB = chrono.ChVectorD(0,-1,0)
# # link_43.Initialize(body_2,body_7,False,cA,cB,dB)
# # link_43.SetDistance(0)
# # link_43.SetName("Coincident17")
# # #exported_items.append(link_43)
# # 
# # link_44 = chrono.ChLinkMateParallel()
# # cA = chrono.ChVectorD(0.01,-0.26,-0.03)
# # dA = chrono.ChVectorD(1.66533453693773e-16,-1,0)
# # cB = chrono.ChVectorD(0.01,-0.26,-0.01)
# # dB = chrono.ChVectorD(0,-1,0)
# # link_44.Initialize(body_2,body_7,False,cA,cB,dA,dB)
# # link_44.SetName("Coincident17")
# # #exported_items.append(link_44)
# # 
# # 
# # # Mate constraint: Coincident18 [MateCoincident] type:0 align:0 flip:False
# # #   Entity 0: C::E name: body_7 , SW name: foot1-2 ,  SW ref.type:2 (2)
# # #   Entity 1: C::E name: body_9 , SW name: foot1-1 ,  SW ref.type:2 (2)
# # 
# # link_45 = chrono.ChLinkMateXdistance()
# # cA = chrono.ChVectorD(0.01,-0.26,-0.01)
# # cB = chrono.ChVectorD(0.01,-0.26,0.17)
# # dA = chrono.ChVectorD(0,-1,0)
# # dB = chrono.ChVectorD(0,-1,0)
# # link_45.Initialize(body_7,body_9,False,cA,cB,dB)
# # link_45.SetDistance(0)
# # link_45.SetName("Coincident18")
# # #exported_items.append(link_45)
# # 
# # link_46 = chrono.ChLinkMateParallel()
# # cA = chrono.ChVectorD(0.01,-0.26,-0.01)
# # dA = chrono.ChVectorD(0,-1,0)
# # cB = chrono.ChVectorD(0.01,-0.26,0.17)
# # dB = chrono.ChVectorD(0,-1,0)
# # link_46.Initialize(body_7,body_9,False,cA,cB,dA,dB)
# # link_46.SetName("Coincident18")
# # #exported_items.append(link_46)
# # 
# # 
# # # Mate constraint: Coincident19 [MateCoincident] type:0 align:0 flip:False
# # #   Entity 0: C::E name: body_6 , SW name: foot2-2 ,  SW ref.type:2 (2)
# # #   Entity 1: C::E name: body_8 , SW name: foot2-3 ,  SW ref.type:2 (2)
# # 
# # link_47 = chrono.ChLinkMateXdistance()
# # cA = chrono.ChVectorD(0.0815122588463411,-0.26,0.17)
# # cB = chrono.ChVectorD(0.081512258846341,-0.26,-0.01)
# # dA = chrono.ChVectorD(0,-1,0)
# # dB = chrono.ChVectorD(0,-1,0)
# # link_47.Initialize(body_6,body_8,False,cA,cB,dB)
# # link_47.SetDistance(0)
# # link_47.SetName("Coincident19")
# # #exported_items.append(link_47)
# # 
# # link_48 = chrono.ChLinkMateParallel()
# # cA = chrono.ChVectorD(0.0815122588463411,-0.26,0.17)
# # dA = chrono.ChVectorD(0,-1,0)
# # cB = chrono.ChVectorD(0.081512258846341,-0.26,-0.01)
# # dB = chrono.ChVectorD(0,-1,0)
# # link_48.Initialize(body_6,body_8,False,cA,cB,dA,dB)
# # link_48.SetName("Coincident19")
# # #exported_items.append(link_48)
# # 
# # 
# # # Mate constraint: Coincident20 [MateCoincident] type:0 align:0 flip:False
# # #   Entity 0: C::E name: body_9 , SW name: foot1-1 ,  SW ref.type:2 (2)
# # #   Entity 1: C::E name: body_6 , SW name: foot2-2 ,  SW ref.type:2 (2)
# # 
# # link_49 = chrono.ChLinkMateXdistance()
# # cA = chrono.ChVectorD(0.01,-0.26,0.17)
# # cB = chrono.ChVectorD(0.0815122588463411,-0.26,0.17)
# # dA = chrono.ChVectorD(0,-1,0)
# # dB = chrono.ChVectorD(0,-1,0)
# # link_49.Initialize(body_9,body_6,False,cA,cB,dB)
# # link_49.SetDistance(0)
# # link_49.SetName("Coincident20")
# # #exported_items.append(link_49)
# # 
# # link_50 = chrono.ChLinkMateParallel()
# # cA = chrono.ChVectorD(0.01,-0.26,0.17)
# # dA = chrono.ChVectorD(0,-1,0)
# # cB = chrono.ChVectorD(0.0815122588463411,-0.26,0.17)
# # dB = chrono.ChVectorD(0,-1,0)
# # link_50.Initialize(body_9,body_6,False,cA,cB,dA,dB)
# # link_50.SetName("Coincident20")
# # #exported_items.append(link_50)
# # 
# # =============================================================================
# 
# # Mate constraint: Coincident21 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_5 , SW name: Leg-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_3 , SW name: Leg-3 ,  SW ref.type:2 (2)
# 
# link_51 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.12)
# cB = chrono.ChVectorD(1.04083408558608e-17,-0.11,0.14)
# dA = chrono.ChVectorD(-1,-1.66533453693773e-16,0)
# dB = chrono.ChVectorD(-1,-1.38777878078145e-16,0)
# link_51.Initialize(body_5,body_3,False,cA,cB,dB)
# link_51.SetDistance(0)
# link_51.SetName("Coincident21")
# #exported_items.append(link_51)
# 
# link_52 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.12)
# dA = chrono.ChVectorD(-1,-1.66533453693773e-16,0)
# cB = chrono.ChVectorD(1.04083408558608e-17,-0.11,0.14)
# dB = chrono.ChVectorD(-1,-1.38777878078145e-16,0)
# link_52.Initialize(body_5,body_3,False,cA,cB,dA,dB)
# link_52.SetName("Coincident21")
# #exported_items.append(link_52)
# 
# 
# # Mate constraint: Coincident22 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_1 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_5 , SW name: Leg-1 ,  SW ref.type:2 (2)
# 
# link_53 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(0,0.02,0.12)
# cB = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.12)
# dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
# dB = chrono.ChVectorD(-1,-1.66533453693773e-16,0)
# link_53.Initialize(body_1,body_5,False,cA,cB,dB)
# link_53.SetDistance(0)
# link_53.SetName("Coincident22")
# #exported_items.append(link_53)
# 
# link_54 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0,0.02,0.12)
# dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
# cB = chrono.ChVectorD(-8.67361737988404e-18,0.02,0.12)
# dB = chrono.ChVectorD(-1,-1.66533453693773e-16,0)
# link_54.Initialize(body_1,body_5,False,cA,cB,dA,dB)
# link_54.SetName("Coincident22")
# #exported_items.append(link_54)
# 
# 
# =============================================================================
