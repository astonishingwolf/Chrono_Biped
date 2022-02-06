# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\Chrono_Biped\BIped_V8\Assem1.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'bm_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Leg-2')
body_1.SetPos(chrono.ChVectorD(-0.01,-0.022,0.015))
body_1.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,-0.5))
body_1.SetMass(11.0)
body_1.SetInertiaXX(chrono.ChVectorD(1.34525745095411e-06,2.07315501130413e-05,2.07051345548124e-05))
body_1.SetInertiaXY(chrono.ChVectorD(-7.92028685429607e-22,2.46273496553236e-21,-6.20795015996827e-23))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-7.92013953888448e-18,2.98463826913282e-18,0.075),chrono.ChQuaternionD(1,0,0,0)))
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
body_1.SetBodyFixed(False)
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
body_2.SetName('Leg-3')
body_2.SetPos(chrono.ChVectorD(-0.01,-0.152,0.035))
body_2.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,-0.5))
body_2.SetMass(11.0)
body_2.SetInertiaXX(chrono.ChVectorD(1.34525745095411e-06,2.07315501130413e-05,2.07051345548124e-05))
body_2.SetInertiaXY(chrono.ChVectorD(-1.19726585505692e-21,2.27038592924694e-21,-6.79449337904933e-23))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-7.92013953888448e-18,2.98463826913282e-18,0.075),chrono.ChQuaternionD(1,0,0,0)))
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
body_2.SetBodyFixed(False)
body_2.SetCollide(False)

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
body_3.SetPos(chrono.ChVectorD(-0.01,-0.01,0))
body_3.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_3.SetMass(50.0)
body_3.SetInertiaXX(chrono.ChVectorD(0.00035377985747202,0.000247107383432273,0.000112392779593172))
body_3.SetInertiaXY(chrono.ChVectorD(2.51362904614565e-21,-7.92769899070822e-21,-3.21590869796614e-21))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.60761986495112e-19,0.0151370547889903,0.1),chrono.ChQuaternionD(1,0,0,0)))
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
body_3.SetBodyFixed(False)
body_3.SetCollide(False)


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
body_4.SetName('hinge-2')
body_4.SetPos(chrono.ChVectorD(-0.022,-0.01,0.185))
body_4.SetRot(chrono.ChQuaternionD(0.707106781186548,-1.2266347333467e-16,0.707106781186547,0))
body_4.SetMass(5.0)
body_4.SetInertiaXX(chrono.ChVectorD(1.41039569856009e-06,1.16788839933545e-06,1.10258717378839e-06))
body_4.SetInertiaXY(chrono.ChVectorD(1.83281325836241e-22,-4.57638357211045e-23,8.40259268341968e-23))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.64511644975648e-18,-0.0138096716915232,0.012),chrono.ChQuaternionD(1,0,0,0)))
mesh_4 = chrono.ChTriangleMeshConnected()
mesh_4.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_4_1.obj'))
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
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_4.GetAssets().push_back(body_4_1_level) 

exported_items.append(body_4)



# Rigid body part
body_5= chrono.ChBodyAuxRef()
body_5.SetName('foot1-1')
body_5.SetPos(chrono.ChVectorD(-0.00999999999999999,-0.292,0.00499999999999999))
body_5.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_5.SetMass(6.0)
body_5.SetInertiaXX(chrono.ChVectorD(2.43703717003532e-05,4.33262746998229e-05,2.33784397310327e-05))
body_5.SetInertiaXY(chrono.ChVectorD(1.58581308825401e-22,1.13563087027456e-21,2.19260683720243e-22))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.029798870148641,-5.5016379469576e-19,0.03),chrono.ChQuaternionD(1,0,0,0)))
mesh_5 = chrono.ChTriangleMeshConnected()
mesh_5.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_5_1.obj'))
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
body_5.SetCollide(True)

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_5.GetAssets().push_back(body_5_1_level) 

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('Leg-1')
body_6.SetPos(chrono.ChVectorD(-0.01,-0.022,0.185))
body_6.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,-0.5))
body_6.SetMass(11.0)
body_6.SetInertiaXX(chrono.ChVectorD(1.34525745095411e-06,2.07315501130413e-05,2.07051345548124e-05))
body_6.SetInertiaXY(chrono.ChVectorD(1.38662462545107e-21,2.28840322208664e-21,-6.20795015996825e-23))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-7.92013953888448e-18,2.98463826913282e-18,0.075),chrono.ChQuaternionD(1,0,0,0)))
mesh_6 = chrono.ChTriangleMeshConnected()
mesh_6.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh_6.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_6 = chrono.ChMaterialSurfaceSMC()
body_6.GetCollisionModel().ClearModel()
body_6.GetCollisionModel().AddTriangleMesh(material_6,                # contact material
                                            mesh_6,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_6.GetCollisionModel().BuildModel()
body_6.SetBodyFixed(False)
body_6.SetCollide(False)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_6.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('Leg-4')
body_7.SetPos(chrono.ChVectorD(-0.00999999999999997,-0.152,0.165))
body_7.SetRot(chrono.ChQuaternionD(0.5,0.5,0.5,-0.5))
body_7.SetMass(11.0)
body_7.SetInertiaXX(chrono.ChVectorD(1.34525745095411e-06,2.07315501130413e-05,2.07051345548124e-05))
body_7.SetInertiaXY(chrono.ChVectorD(1.3865206651717e-21,2.28798361809534e-21,-6.20795015996825e-23))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-7.92013953888448e-18,2.98463826913282e-18,0.075),chrono.ChQuaternionD(1,0,0,0)))
mesh_7 = chrono.ChTriangleMeshConnected()
mesh_7.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh_7.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_7 = chrono.ChMaterialSurfaceSMC()
body_7.GetCollisionModel().ClearModel()
body_7.GetCollisionModel().AddTriangleMesh(material_7,                # contact material
                                            mesh_7,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_7.GetCollisionModel().BuildModel()
body_7.SetBodyFixed(False)
body_7.SetCollide(False)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_7.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_7)



# Rigid body part
body_8= chrono.ChBodyAuxRef()
body_8.SetName('hinge-1')
body_8.SetPos(chrono.ChVectorD(0.00199999999999999,-0.01,0.015))
body_8.SetRot(chrono.ChQuaternionD(0.707106781186548,6.2975033361764e-17,-0.707106781186547,6.2975033361764e-17))
body_8.SetMass(5.0)
body_8.SetInertiaXX(chrono.ChVectorD(1.41039569856009e-06,1.16788839933545e-06,1.10258717378839e-06))
body_8.SetInertiaXY(chrono.ChVectorD(-1.4121301533017e-22,-8.39153753563626e-24,-8.43294433353497e-23))
body_8.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.64511644975648e-18,-0.0138096716915232,0.012),chrono.ChQuaternionD(1,0,0,0)))
mesh_8 = chrono.ChTriangleMeshConnected()
mesh_8.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_4_1.obj'))
mesh_8.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_8 = chrono.ChMaterialSurfaceSMC()
body_8.GetCollisionModel().ClearModel()
body_8.GetCollisionModel().AddTriangleMesh(material_8,                # contact material
                                            mesh_8,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_8.GetCollisionModel().BuildModel()
body_8.SetBodyFixed(False)
body_8.SetCollide(False)

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_8.GetAssets().push_back(body_4_1_level) 

exported_items.append(body_8)



# Rigid body part
body_9= chrono.ChBodyAuxRef()
body_9.SetName('foot1-2')
body_9.SetPos(chrono.ChVectorD(-0.00999999999999995,-0.292,0.135))
body_9.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_9.SetMass(6.0)
body_9.SetInertiaXX(chrono.ChVectorD(2.43703717003532e-05,4.33262746998229e-05,2.33784397310327e-05))
body_9.SetInertiaXY(chrono.ChVectorD(1.58581308825401e-22,1.13563087027456e-21,2.19260683720243e-22))
body_9.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.029798870148641,-5.5016379469576e-19,0.03),chrono.ChQuaternionD(1,0,0,0)))
mesh_9 = chrono.ChTriangleMeshConnected()
mesh_9.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_5_1.obj'))
mesh_9.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_9 = chrono.ChMaterialSurfaceSMC()
body_9.GetCollisionModel().ClearModel()
body_9.GetCollisionModel().AddTriangleMesh(material_9,                # contact material
                                            mesh_9,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_9.GetCollisionModel().BuildModel()
body_9.SetBodyFixed(False)
body_9.SetCollide(True)

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_9.GetAssets().push_back(body_5_1_level) 

exported_items.append(body_9)




# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hinge-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.037,-0.00999999999999999,0.185)
dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
cB = chrono.ChVectorD(-6.93889390390723e-18,-0.01,0.185)
dB = chrono.ChVectorD(1,1.73472347597681e-16,1.22464679914735e-16)
link_1.SetFlipped(True)
link_1.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_1.SetName("Concentric2")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.037,-0.00999999999999999,0.185)
cB = chrono.ChVectorD(-6.93889390390723e-18,-0.01,0.185)
dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
dB = chrono.ChVectorD(1,1.73472347597681e-16,1.22464679914735e-16)
link_2.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_2.SetName("Concentric2")
exported_items.append(link_2)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hinge-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.02,-1.73472347597681e-18,0.2)
cB = chrono.ChVectorD(-0.02,-0.01,0.185)
dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
dB = chrono.ChVectorD(1,1.73472347597681e-16,1.22464679914735e-16)
link_3.Initialize(body_3,body_4,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident2")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.02,-1.73472347597681e-18,0.2)
dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
cB = chrono.ChVectorD(-0.02,-0.01,0.185)
dB = chrono.ChVectorD(1,1.73472347597681e-16,1.22464679914735e-16)
link_4.SetFlipped(True)
link_4.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_4.SetName("Coincident2")
exported_items.append(link_4)


# # Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
# #   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_8 , SW name: hinge-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.037,-0.00999999999999999,0.015)
dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
cB = chrono.ChVectorD(-9.54097911787244e-18,-0.01,0.015)
dB = chrono.ChVectorD(1,1.7812029254221e-16,1.0505695901855e-18)
link_5.SetFlipped(True)
link_5.Initialize(body_3,body_8,False,cA,cB,dA,dB)
link_5.SetName("Concentric3")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.037,-0.00999999999999999,0.015)
cB = chrono.ChVectorD(-9.54097911787244e-18,-0.01,0.015)
dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
dB = chrono.ChVectorD(1,1.7812029254221e-16,1.0505695901855e-18)
link_6.Initialize(body_3,body_8,False,cA,cB,dA,dB)
link_6.SetName("Concentric3")
exported_items.append(link_6)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_8 , SW name: hinge-1 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.02,-1.73472347597681e-18,0.2)
cB = chrono.ChVectorD(-0.02,-0.01,0.015)
dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
dB = chrono.ChVectorD(1,1.7812029254221e-16,1.0505695901855e-18)
link_7.Initialize(body_3,body_8,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident3")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.02,-1.73472347597681e-18,0.2)
dA = chrono.ChVectorD(-1,-1.73472347597681e-16,0)
cB = chrono.ChVectorD(-0.02,-0.01,0.015)
dB = chrono.ChVectorD(1,1.7812029254221e-16,1.0505695901855e-18)
link_8.SetFlipped(True)
link_8.Initialize(body_3,body_8,False,cA,cB,dA,dB)
link_8.SetName("Coincident3")
exported_items.append(link_8)


# # Mate constraint: Concentric4 [MateConcentric] type:1 align:1 flip:False
# #   Entity 0: C::E name: body_6 , SW name: Leg-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_4 , SW name: hinge-2 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.01,-0.032,0.325)
dA = chrono.ChVectorD(1.22409076701743e-16,-8.67384308198038e-17,-1)
cB = chrono.ChVectorD(-0.01,-0.032,0.152)
dB = chrono.ChVectorD(-1.22464679914735e-16,8.67361737988403e-17,1)
link_9.SetFlipped(True)
link_9.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_9.SetName("Concentric4")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.01,-0.032,0.325)
cB = chrono.ChVectorD(-0.01,-0.032,0.152)
dA = chrono.ChVectorD(1.22409076701743e-16,-8.67384308198038e-17,-1)
dB = chrono.ChVectorD(-1.22464679914735e-16,8.67361737988403e-17,1)
link_10.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_10.SetName("Concentric4")
exported_items.append(link_10)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: Leg-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: hinge-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.02,-0.172,0.195)
cB = chrono.ChVectorD(-0.01,-0.01,0.195)
dA = chrono.ChVectorD(-1.22409076701743e-16,8.67384308198038e-17,1)
dB = chrono.ChVectorD(1.22464679914735e-16,-8.67361737988404e-17,-1)
link_11.Initialize(body_6,body_4,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident4")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.02,-0.172,0.195)
dA = chrono.ChVectorD(-1.22409076701743e-16,8.67384308198038e-17,1)
cB = chrono.ChVectorD(-0.01,-0.01,0.195)
dB = chrono.ChVectorD(1.22464679914735e-16,-8.67361737988404e-17,-1)
link_12.SetFlipped(True)
link_12.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_12.SetName("Coincident4")
exported_items.append(link_12)


# # Mate constraint: Concentric5 [MateConcentric] type:1 align:0 flip:False
# #   Entity 0: C::E name: body_8 , SW name: hinge-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_1 , SW name: Leg-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.01,-0.032,0.048)
dA = chrono.ChVectorD(1.05056959018551e-18,-8.67361737988404e-17,-1)
cB = chrono.ChVectorD(-0.01,-0.032,0.155)
dB = chrono.ChVectorD(7.83378952765899e-18,-9.53408989478223e-17,-1)
link_13.Initialize(body_8,body_1,False,cA,cB,dA,dB)
link_13.SetName("Concentric5")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.01,-0.032,0.048)
cB = chrono.ChVectorD(-0.01,-0.032,0.155)
dA = chrono.ChVectorD(1.05056959018551e-18,-8.67361737988404e-17,-1)
dB = chrono.ChVectorD(7.83378952765899e-18,-9.53408989478223e-17,-1)
link_14.Initialize(body_8,body_1,False,cA,cB,dA,dB)
link_14.SetName("Concentric5")
exported_items.append(link_14)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_8 , SW name: hinge-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Leg-2 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.01,-0.01,0.005)
cB = chrono.ChVectorD(-0.02,-0.172,0.005)
dA = chrono.ChVectorD(-1.05056959018551e-18,8.67361737988404e-17,1)
dB = chrono.ChVectorD(7.83378952765899e-18,-9.53408989478223e-17,-1)
link_15.Initialize(body_8,body_1,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident5")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.01,-0.01,0.005)
dA = chrono.ChVectorD(-1.05056959018551e-18,8.67361737988404e-17,1)
cB = chrono.ChVectorD(-0.02,-0.172,0.005)
dB = chrono.ChVectorD(7.83378952765899e-18,-9.53408989478223e-17,-1)
link_16.SetFlipped(True)
link_16.Initialize(body_8,body_1,False,cA,cB,dA,dB)
link_16.SetName("Coincident5")
exported_items.append(link_16)


# # Mate constraint: Concentric6 [MateConcentric] type:1 align:0 flip:False
# #   Entity 0: C::E name: body_1 , SW name: Leg-2 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_2 , SW name: Leg-3 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00999999999999998,-0.162,0.155)
dA = chrono.ChVectorD(7.83378952765899e-18,-9.53408989478223e-17,-1)
cB = chrono.ChVectorD(-0.00999999999999999,-0.162,0.175)
dB = chrono.ChVectorD(-1.08753281892024e-17,-8.58077796207783e-17,-1)
link_17.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_17.SetName("Concentric6")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00999999999999998,-0.162,0.155)
cB = chrono.ChVectorD(-0.00999999999999999,-0.162,0.175)
dA = chrono.ChVectorD(7.83378952765899e-18,-9.53408989478223e-17,-1)
dB = chrono.ChVectorD(-1.08753281892024e-17,-8.58077796207783e-17,-1)
link_18.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_18.SetName("Concentric6")
exported_items.append(link_18)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Leg-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Leg-3 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.02,-0.172,0.025)
cB = chrono.ChVectorD(-0.02,-0.302,0.025)
dA = chrono.ChVectorD(-7.83378952765899e-18,9.53408989478223e-17,1)
dB = chrono.ChVectorD(-1.08753281892024e-17,-8.58077796207783e-17,-1)
link_19.Initialize(body_1,body_2,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident8")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.02,-0.172,0.025)
dA = chrono.ChVectorD(-7.83378952765899e-18,9.53408989478223e-17,1)
cB = chrono.ChVectorD(-0.02,-0.302,0.025)
dB = chrono.ChVectorD(-1.08753281892024e-17,-8.58077796207783e-17,-1)
link_20.SetFlipped(True)
link_20.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_20.SetName("Coincident8")
exported_items.append(link_20)


# # Mate constraint: Concentric7 [MateConcentric] type:1 align:0 flip:False
# #   Entity 0: C::E name: body_6 , SW name: Leg-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_7 , SW name: Leg-4 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.01,-0.162,0.325)
dA = chrono.ChVectorD(1.22409076701743e-16,-8.67384308198038e-17,-1)
cB = chrono.ChVectorD(-0.00999999999999999,-0.162,0.305)
dB = chrono.ChVectorD(1.2240371413546e-16,-8.67167569223382e-17,-1)
link_21.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_21.SetName("Concentric7")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateGeneric()
link_22.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.01,-0.162,0.325)
cB = chrono.ChVectorD(-0.00999999999999999,-0.162,0.305)
dA = chrono.ChVectorD(1.22409076701743e-16,-8.67384308198038e-17,-1)
dB = chrono.ChVectorD(1.2240371413546e-16,-8.67167569223382e-17,-1)
link_22.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_22.SetName("Concentric7")
exported_items.append(link_22)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: Leg-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: Leg-4 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.02,-0.172,0.175)
cB = chrono.ChVectorD(-0.0199999999999999,-0.302,0.175)
dA = chrono.ChVectorD(1.22409076701743e-16,-8.67384308198038e-17,-1)
dB = chrono.ChVectorD(-1.2240371413546e-16,8.67167569223382e-17,1)
link_23.Initialize(body_6,body_7,False,cA,cB,dB)
link_23.SetDistance(0)
link_23.SetName("Coincident9")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.02,-0.172,0.175)
dA = chrono.ChVectorD(1.22409076701743e-16,-8.67384308198038e-17,-1)
cB = chrono.ChVectorD(-0.0199999999999999,-0.302,0.175)
dB = chrono.ChVectorD(-1.2240371413546e-16,8.67167569223382e-17,1)
link_24.SetFlipped(True)
link_24.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_24.SetName("Coincident9")
exported_items.append(link_24)


# # Mate constraint: Concentric8 [MateConcentric] type:1 align:1 flip:False
# #   Entity 0: C::E name: body_5 , SW name: foot1-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_2 , SW name: Leg-3 ,  SW ref.type:2 (2)

link_25 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00999999999999999,-0.292,-0.055)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(-0.01,-0.292,0.175)
dB = chrono.ChVectorD(-1.08753281892024e-17,-8.58077796207783e-17,-1)
link_25.SetFlipped(True)
link_25.Initialize(body_5,body_2,False,cA,cB,dA,dB)
link_25.SetName("Concentric8")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateGeneric()
link_26.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00999999999999999,-0.292,-0.055)
cB = chrono.ChVectorD(-0.01,-0.292,0.175)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(-1.08753281892024e-17,-8.58077796207783e-17,-1)
link_26.Initialize(body_5,body_2,False,cA,cB,dA,dB)
link_26.SetName("Concentric8")
exported_items.append(link_26)


# Mate constraint: Coincident10 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: foot1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Leg-3 ,  SW ref.type:2 (2)

link_27 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.01,-0.277527608818748,0.025)
cB = chrono.ChVectorD(-0.02,-0.302,0.025)
dA = chrono.ChVectorD(0,-1.19864330244476e-16,1)
dB = chrono.ChVectorD(-1.08753281892024e-17,-8.58077796207783e-17,-1)
link_27.Initialize(body_5,body_2,False,cA,cB,dB)
link_27.SetDistance(0)
link_27.SetName("Coincident10")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.01,-0.277527608818748,0.025)
dA = chrono.ChVectorD(0,-1.19864330244476e-16,1)
cB = chrono.ChVectorD(-0.02,-0.302,0.025)
dB = chrono.ChVectorD(-1.08753281892024e-17,-8.58077796207783e-17,-1)
link_28.SetFlipped(True)
link_28.Initialize(body_5,body_2,False,cA,cB,dA,dB)
link_28.SetName("Coincident10")
exported_items.append(link_28)


# # Mate constraint: Concentric9 [MateConcentric] type:1 align:1 flip:False
# #   Entity 0: C::E name: body_7 , SW name: Leg-4 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_9 , SW name: foot1-2 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00999999999999997,-0.292,0.305)
dA = chrono.ChVectorD(1.2240371413546e-16,-8.67167569223382e-17,-1)
cB = chrono.ChVectorD(-0.00999999999999995,-0.292,0.0750000000000001)
dB = chrono.ChVectorD(0,0,1)
link_29.SetFlipped(True)
link_29.Initialize(body_7,body_9,False,cA,cB,dA,dB)
link_29.SetName("Concentric9")
exported_items.append(link_29)

link_30 = chrono.ChLinkMateGeneric()
link_30.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00999999999999997,-0.292,0.305)
cB = chrono.ChVectorD(-0.00999999999999995,-0.292,0.0750000000000001)
dA = chrono.ChVectorD(1.2240371413546e-16,-8.67167569223382e-17,-1)
dB = chrono.ChVectorD(0,0,1)
link_30.Initialize(body_7,body_9,False,cA,cB,dA,dB)
link_30.SetName("Concentric9")
exported_items.append(link_30)


# Mate constraint: Coincident11 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: Leg-4 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_9 , SW name: foot1-2 ,  SW ref.type:2 (2)

link_31 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0199999999999999,-0.302,0.175)
cB = chrono.ChVectorD(0.01,-0.277527608818748,0.175)
dA = chrono.ChVectorD(-1.2240371413546e-16,8.67167569223382e-17,1)
dB = chrono.ChVectorD(0,4.79457320977904e-16,-1)
link_31.Initialize(body_7,body_9,False,cA,cB,dB)
link_31.SetDistance(0)
link_31.SetName("Coincident11")
exported_items.append(link_31)

link_32 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0199999999999999,-0.302,0.175)
dA = chrono.ChVectorD(-1.2240371413546e-16,8.67167569223382e-17,1)
cB = chrono.ChVectorD(0.01,-0.277527608818748,0.175)
dB = chrono.ChVectorD(0,4.79457320977904e-16,-1)
link_32.SetFlipped(True)
link_32.Initialize(body_7,body_9,False,cA,cB,dA,dB)
link_32.SetName("Coincident11")
exported_items.append(link_32)


# Mate constraint: Coincident12 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)
# =============================================================================
# 
# link_33 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(0,-1.73472347597681e-18,0.2)
# cB = chrono.ChVectorD(0,0,0)
# dA = chrono.ChVectorD(1,1.73472347597681e-16,0)
# dB = chrono.ChVectorD(1,0,0)
# link_33.Initialize(body_3,body_0,False,cA,cB,dB)
# link_33.SetDistance(0)
# link_33.SetName("Coincident12")
# exported_items.append(link_33)
# 
# link_34 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0,-1.73472347597681e-18,0.2)
# dA = chrono.ChVectorD(1,1.73472347597681e-16,0)
# cB = chrono.ChVectorD(0,0,0)
# dB = chrono.ChVectorD(1,0,0)
# link_34.Initialize(body_3,body_0,False,cA,cB,dA,dB)
# link_34.SetName("Coincident12")
# exported_items.append(link_34)
# 
# 
# # Mate constraint: Coincident13 [MateCoincident] type:0 align:1 flip:False
# #   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)
# 
# link_35 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(-0.01,-0.01,0)
# cB = chrono.ChVectorD(0,0,0)
# dA = chrono.ChVectorD(0,0,-1)
# dB = chrono.ChVectorD(0,0,1)
# link_35.Initialize(body_3,body_0,False,cA,cB,dB)
# link_35.SetDistance(0)
# link_35.SetName("Coincident13")
# exported_items.append(link_35)
# 
# link_36 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(-0.01,-0.01,0)
# dA = chrono.ChVectorD(0,0,-1)
# cB = chrono.ChVectorD(0,0,0)
# dB = chrono.ChVectorD(0,0,1)
# link_36.SetFlipped(True)
# link_36.Initialize(body_3,body_0,False,cA,cB,dA,dB)
# link_36.SetName("Coincident13")
# exported_items.append(link_36)
# 
# 
# # Mate constraint: Coincident14 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)
# 
# link_37 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(-0.02,-1.73472347597681e-18,0.2)
# cB = chrono.ChVectorD(0,0,0)
# dA = chrono.ChVectorD(0,1,0)
# dB = chrono.ChVectorD(0,1,0)
# link_37.Initialize(body_3,body_0,False,cA,cB,dB)
# link_37.SetDistance(0)
# link_37.SetName("Coincident14")
# exported_items.append(link_37)
# 
# link_38 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(-0.02,-1.73472347597681e-18,0.2)
# dA = chrono.ChVectorD(0,1,0)
# cB = chrono.ChVectorD(0,0,0)
# dB = chrono.ChVectorD(0,1,0)
# link_38.Initialize(body_3,body_0,False,cA,cB,dA,dB)
# link_38.SetName("Coincident14")
# exported_items.append(link_38)
# 
# 
# # Mate constraint: Parallel1 [MateParallel] type:3 align:0 flip:False
# #   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_4 , SW name: hinge-2 ,  SW ref.type:2 (2)
# 
# link_39 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(-0.01,-0.01,0.2)
# dA = chrono.ChVectorD(0,0,1)
# cB = chrono.ChVectorD(-6.93889390390723e-18,-0.01,0.1975)
# dB = chrono.ChVectorD(-1.22464679914735e-16,1.73472347597681e-16,1)
# link_39.Initialize(body_3,body_4,False,cA,cB,dA,dB)
# link_39.SetName("Parallel1")
# exported_items.append(link_39)
# 
# 
# # Mate constraint: Parallel2 [MateParallel] type:3 align:0 flip:False
# #   Entity 0: C::E name: body_3 , SW name: Torso-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_8 , SW name: hinge-1 ,  SW ref.type:2 (2)
# 
# link_40 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(-0.01,-0.01,0)
# dA = chrono.ChVectorD(0,0,-1)
# cB = chrono.ChVectorD(-9.54097911787244e-18,-0.01,0.0025)
# dB = chrono.ChVectorD(1.0505695901855e-18,0,-1)
# link_40.Initialize(body_3,body_8,False,cA,cB,dA,dB)
# link_40.SetName("Parallel2")
# exported_items.append(link_40)
# 
# 
# # Mate constraint: Parallel3 [MateParallel] type:3 align:0 flip:False
# #   Entity 0: C::E name: body_8 , SW name: hinge-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_1 , SW name: Leg-2 ,  SW ref.type:2 (2)
# 
# link_41 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.00199999999999999,-0.01,0.015)
# dA = chrono.ChVectorD(1,1.7812029254221e-16,1.0505695901855e-18)
# cB = chrono.ChVectorD(2.08166817117217e-17,-0.172,0.025)
# dB = chrono.ChVectorD(1,1.66533453693774e-16,-2.37859856229133e-17)
# link_41.Initialize(body_8,body_1,False,cA,cB,dA,dB)
# link_41.SetName("Parallel3")
# exported_items.append(link_41)
# 
# 
# # Mate constraint: Parallel4 [MateParallel] type:3 align:0 flip:False
# #   Entity 0: C::E name: body_6 , SW name: Leg-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_4 , SW name: hinge-2 ,  SW ref.type:2 (2)
# 
# link_42 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(1.21430643318376e-17,-0.172,0.195)
# dA = chrono.ChVectorD(1,1.66533453693774e-16,1.22409076701743e-16)
# cB = chrono.ChVectorD(0.00199999999999999,-0.01,0.185)
# dB = chrono.ChVectorD(1,1.73472347597681e-16,1.22464679914735e-16)
# link_42.Initialize(body_6,body_4,False,cA,cB,dA,dB)
# link_42.SetName("Parallel4")
# exported_items.append(link_42)
# 
# 
# # Mate constraint: Coincident19 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_6 , SW name: Leg-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_7 , SW name: Leg-4 ,  SW ref.type:2 (2)
# 
# link_43 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(1.21430643318376e-17,-0.172,0.195)
# cB = chrono.ChVectorD(4.68375338513738e-17,-0.302,0.175)
# dA = chrono.ChVectorD(1,1.66533453693774e-16,1.22409076701743e-16)
# dB = chrono.ChVectorD(1,1.66533453693774e-16,1.2240371413546e-16)
# link_43.Initialize(body_6,body_7,False,cA,cB,dB)
# link_43.SetDistance(0)
# link_43.SetName("Coincident19")
# exported_items.append(link_43)
# 
# link_44 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(1.21430643318376e-17,-0.172,0.195)
# dA = chrono.ChVectorD(1,1.66533453693774e-16,1.22409076701743e-16)
# cB = chrono.ChVectorD(4.68375338513738e-17,-0.302,0.175)
# dB = chrono.ChVectorD(1,1.66533453693774e-16,1.2240371413546e-16)
# link_44.Initialize(body_6,body_7,False,cA,cB,dA,dB)
# link_44.SetName("Coincident19")
# exported_items.append(link_44)
# 
# 
# # Mate constraint: Coincident20 [MateCoincident] type:0 align:0 flip:False
# #   Entity 0: C::E name: body_1 , SW name: Leg-2 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_2 , SW name: Leg-3 ,  SW ref.type:2 (2)
# 
# link_45 = chrono.ChLinkMateXdistance()
# cA = chrono.ChVectorD(2.08166817117217e-17,-0.172,0.025)
# cB = chrono.ChVectorD(-3.46944695195361e-18,-0.302,0.045)
# dA = chrono.ChVectorD(1,1.66533453693774e-16,-2.37859856229133e-17)
# dB = chrono.ChVectorD(1,-5.55111512312578e-17,-1.08753281892024e-17)
# link_45.Initialize(body_1,body_2,False,cA,cB,dB)
# link_45.SetDistance(0)
# link_45.SetName("Coincident20")
# exported_items.append(link_45)
# 
# link_46 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(2.08166817117217e-17,-0.172,0.025)
# dA = chrono.ChVectorD(1,1.66533453693774e-16,-2.37859856229133e-17)
# cB = chrono.ChVectorD(-3.46944695195361e-18,-0.302,0.045)
# dB = chrono.ChVectorD(1,-5.55111512312578e-17,-1.08753281892024e-17)
# link_46.Initialize(body_1,body_2,False,cA,cB,dA,dB)
# link_46.SetName("Coincident20")
# exported_items.append(link_46)
# 
# 
# # Mate constraint: Parallel5 [MateParallel] type:3 align:0 flip:False
# #   Entity 0: C::E name: body_5 , SW name: foot1-1 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_2 , SW name: Leg-3 ,  SW ref.type:2 (2)
# 
# link_47 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(0.048512258846341,-0.292,0.00499999999999999)
# dA = chrono.ChVectorD(1,0,0)
# cB = chrono.ChVectorD(-3.46944695195361e-18,-0.302,0.045)
# dB = chrono.ChVectorD(1,-5.55111512312578e-17,-1.08753281892024e-17)
# link_47.Initialize(body_5,body_2,False,cA,cB,dA,dB)
# link_47.SetName("Parallel5")
# exported_items.append(link_47)
# 
# 
# # Mate constraint: Parallel6 [MateParallel] type:3 align:0 flip:False
# #   Entity 0: C::E name: body_7 , SW name: Leg-4 ,  SW ref.type:2 (2)
# #   Entity 1: C::E name: body_9 , SW name: foot1-2 ,  SW ref.type:2 (2)
# 
# link_48 = chrono.ChLinkMateParallel()
# cA = chrono.ChVectorD(4.68375338513738e-17,-0.302,0.175)
# dA = chrono.ChVectorD(1,1.66533453693774e-16,1.2240371413546e-16)
# cB = chrono.ChVectorD(0.0485122588463411,-0.292,0.135)
# dB = chrono.ChVectorD(1,0,0)
# link_48.Initialize(body_7,body_9,False,cA,cB,dA,dB)
# link_48.SetName("Parallel6")
# exported_items.append(link_48)
# 
# 
# =============================================================================
