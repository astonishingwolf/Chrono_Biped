# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\Biped_Cad\biped_with_plane.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'vb_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('torso_backet-1')
body_1.SetPos(chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766))
body_1.SetRot(chrono.ChQuaternionD(0.99909088936835,0,0,-0.04263091344506))
body_1.SetMass(0.00408359922377617)
body_1.SetInertiaXX(chrono.ChVectorD(8.26060095099226e-07,7.90235805783865e-07,6.4299906896382e-07))
body_1.SetInertiaXY(chrono.ChVectorD(3.08535225620012e-09,6.84157046834059e-23,1.05573659366834e-23))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.89931183719868e-18,-0.00991694834037615,-0.015),chrono.ChQuaternionD(1,0,0,0)))

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
body_2.SetName('knee-1')
body_2.SetPos(chrono.ChVectorD(0.0672275345305963,-0.0159166547136234,0.0131137181930944))
body_2.SetRot(chrono.ChQuaternionD(0.588989645014078,0.391268703151926,-0.391268703151926,0.588989645014078))
body_2.SetMass(0.0243190444078461)
body_2.SetInertiaXX(chrono.ChVectorD(2.87518661420606e-06,9.41479788325931e-06,8.25116629379249e-06))
body_2.SetInertiaXY(chrono.ChVectorD(7.74406088028674e-22,-2.74631028832329e-06,2.5729643977896e-22))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.11063988801742e-18,5.10080862685935e-20,0.0344503698921024),chrono.ChQuaternionD(1,0,0,0)))

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
body_3.SetName('knee-2')
body_3.SetPos(chrono.ChVectorD(0.0106879853408424,-0.0167986189560814,0.0114508053249753))
body_3.SetRot(chrono.ChQuaternionD(0.657915426122776,0.304156033273752,-0.331269451199618,0.604067008033684))
body_3.SetMass(0.0243190444078461)
body_3.SetInertiaXX(chrono.ChVectorD(4.44584710811114e-06,9.41473424725012e-06,6.6805694358966e-06))
body_3.SetInertiaXY(chrono.ChVectorD(-4.43244265364949e-10,-3.67685438286151e-06,5.97956786877366e-10))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.11063988801742e-18,5.10080862685935e-20,0.0344503698921024),chrono.ChQuaternionD(1,0,0,0)))

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
body_4.SetName('leg2-1')
body_4.SetPos(chrono.ChVectorD(0.00632477948808483,-0.0678332084270038,0.0588172252038629))
body_4.SetRot(chrono.ChQuaternionD(0.46791777375935,0.882743202873256,-0.037666391993322,-0.0199659133366251))
body_4.SetMass(0.0259472989030997)
body_4.SetInertiaXX(chrono.ChVectorD(2.31047139211078e-05,8.058431793496e-06,1.61733727840448e-05))
body_4.SetInertiaXY(chrono.ChVectorD(-9.02998661817333e-10,-1.33140230089473e-09,1.01921900895855e-05))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.2417842196311e-18,-8.49264657435101e-19,0.0551561260622386),chrono.ChQuaternionD(1,0,0,0)))

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
body_5.SetName('leg2-2')
body_5.SetPos(chrono.ChVectorD(0.0672275345305963,-0.0752793049019215,0.0448821678902378))
body_5.SetRot(chrono.ChQuaternionD(0.508753701448136,0.860912115876424,0,0))
body_5.SetMass(0.0259472989030997)
body_5.SetInertiaXX(chrono.ChVectorD(2.31048514602965e-05,6.25016771259813e-06,1.7981499325754e-05))
body_5.SetInertiaXY(chrono.ChVectorD(3.27930911233374e-23,-6.63942104043962e-23,9.27018130725739e-06))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.2417842196311e-18,-8.49264657435101e-19,0.0551561260622386),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_5.GetAssets().push_back(body_4_1_level) 

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('torso-1')
body_6.SetPos(chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.00121479985497664))
body_6.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_6.SetMass(0.0259057709259329)
body_6.SetInertiaXX(chrono.ChVectorD(2.31020545817808e-06,1.23480659694851e-05,1.09419926703796e-05))
body_6.SetInertiaXY(chrono.ChVectorD(2.30278879936775e-12,4.37874813267077e-22,6.33549980435918e-23))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(3.32075752354461e-18,1.59651804016568e-20,0.0150000024746274),chrono.ChQuaternionD(1,0,0,0)))
body_6.SetBodyFixed(True)

# Visualization shape 
body_6_1_shape = chrono.ChObjShapeFile() 
body_6_1_shape.SetFilename(shapes_dir +'body_6_1.obj') 
body_6_1_level = chrono.ChAssetLevel() 
body_6_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_6_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_6_1_level.GetAssets().push_back(body_6_1_shape) 
body_6.GetAssets().push_back(body_6_1_level) 

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('torso_backet-2')
body_7.SetPos(chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766))
body_7.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_7.SetMass(0.00408359922377617)
body_7.SetInertiaXX(chrono.ChVectorD(8.2632387750958e-07,7.89972023373511e-07,6.4299906896382e-07))
body_7.SetInertiaXY(chrono.ChVectorD(-4.47218037017444e-22,6.906634997391e-23,4.69104723163494e-24))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.89931183719868e-18,-0.00991694834037615,-0.015),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_7.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_7)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: torso-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999014,0.0332147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,-1)
link_1.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999014,0.0332147998549766)
cB = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_2.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: torso-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_3.Initialize(body_1,body_6,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,1)
link_4.SetFlipped(True)
link_4.Initialize(body_1,body_6,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: torso-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0332147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0672275345305963,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,-1)
link_5.Initialize(body_7,body_6,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0332147998549766)
cB = chrono.ChVectorD(0.0672275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_6.Initialize(body_7,body_6,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: torso-1 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_7.Initialize(body_7,body_6,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,1)
link_8.SetFlipped(True)
link_8.Initialize(body_7,body_6,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: knee-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0147896043960484,-0.0232911575800099,0.0162147998549766)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.137227534530596,-0.0232911575800097,0.0162147998549763)
dB = chrono.ChVectorD(-1,0,0)
link_9.SetFlipped(True)
link_9.Initialize(body_7,body_2,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0147896043960484,-0.0232911575800099,0.0162147998549766)
cB = chrono.ChVectorD(0.137227534530596,-0.0232911575800097,0.0162147998549763)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,0,0)
link_10.Initialize(body_7,body_2,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: knee-1 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0772275345305962,-0.0332911575800099,-0.000785200145023358)
cB = chrono.ChVectorD(0.0772275345305962,-0.0935380354548387,0.0349064062289306)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_11.Initialize(body_7,body_2,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident3")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0772275345305962,-0.0332911575800099,-0.000785200145023358)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0.0772275345305962,-0.0935380354548387,0.0349064062289306)
dB = chrono.ChVectorD(1,0,0)
link_12.SetFlipped(True)
link_12.Initialize(body_7,body_2,False,cA,cB,dA,dB)
link_12.SetName("Coincident3")
exported_items.append(link_12)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: knee-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0421068104670209,-0.0187352161056869,0.0162147998549766)
dA = chrono.ChVectorD(0.99636521043768,-0.0851843144568204,0)
cB = chrono.ChVectorD(0.0798860835570418,-0.0291650072477104,0.0162147998549766)
dB = chrono.ChVectorD(-0.99636521043768,0.0851843144568203,-2.77237946172026e-16)
link_13.SetFlipped(True)
link_13.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_13.SetName("Concentric5")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0421068104670209,-0.0187352161056869,0.0162147998549766)
cB = chrono.ChVectorD(0.0798860835570418,-0.0291650072477104,0.0162147998549766)
dA = chrono.ChVectorD(0.99636521043768,-0.0851843144568204,0)
dB = chrono.ChVectorD(-0.99636521043768,0.0851843144568203,-2.77237946172026e-16)
link_14.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_14.SetName("Concentric5")
exported_items.append(link_14)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: knee-2 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.000674976422540831,-0.0323139141955416,-0.000785200145023354)
cB = chrono.ChVectorD(-0.00525760391805892,-0.0859149866235404,0.0510571924821376)
dA = chrono.ChVectorD(0.99636521043768,-0.0851843144568204,0)
dB = chrono.ChVectorD(-0.99636521043768,0.0851843144568203,-2.77237946172026e-16)
link_15.Initialize(body_1,body_3,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident4")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.000674976422540831,-0.0323139141955416,-0.000785200145023354)
dA = chrono.ChVectorD(0.99636521043768,-0.0851843144568204,0)
cB = chrono.ChVectorD(-0.00525760391805892,-0.0859149866235404,0.0510571924821376)
dB = chrono.ChVectorD(-0.99636521043768,0.0851843144568203,-2.77237946172026e-16)
link_16.SetFlipped(True)
link_16.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_16.SetName("Coincident4")
exported_items.append(link_16)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0147724654694038,-0.0822871805111,0.0410234531500316)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.134227534530596,-0.0822871805111003,0.0410234531500327)
dB = chrono.ChVectorD(-1,0,0)
link_17.SetFlipped(True)
link_17.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_17.SetName("Concentric6")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0147724654694038,-0.0822871805111,0.0410234531500316)
cB = chrono.ChVectorD(0.134227534530596,-0.0822871805111003,0.0410234531500327)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,0,0)
link_18.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_18.SetName("Concentric6")
exported_items.append(link_18)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0752275345305962,-0.0691926998507648,0.0463652296556621)
cB = chrono.ChVectorD(0.0752275345305963,-0.154639113020715,-0.00794794525887696)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_19.Initialize(body_2,body_5,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident5")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0752275345305962,-0.0691926998507648,0.0463652296556621)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0.0752275345305963,-0.154639113020715,-0.00794794525887696)
dB = chrono.ChVectorD(1,0,0)
link_20.SetFlipped(True)
link_20.Initialize(body_2,body_5,False,cA,cB,dA,dB)
link_20.SetName("Coincident5")
exported_items.append(link_20)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00101852981941216,-0.0598108150922161,0.0564053210753357)
cB = chrono.ChVectorD(-0.00796103889187117,-0.141014432883288,-0.00112794791536177)
dA = chrono.ChVectorD(0.99636521043768,-0.0851843144568203,2.77237946172026e-16)
dB = chrono.ChVectorD(-0.99636521043768,0.0851843144568207,9.72999903419265e-17)
link_21.Initialize(body_3,body_4,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Coincident6")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00101852981941216,-0.0598108150922161,0.0564053210753357)
dA = chrono.ChVectorD(0.99636521043768,-0.0851843144568203,2.77237946172026e-16)
cB = chrono.ChVectorD(-0.00796103889187117,-0.141014432883288,-0.00112794791536177)
dB = chrono.ChVectorD(-0.99636521043768,0.0851843144568207,9.72999903419265e-17)
link_22.SetFlipped(True)
link_22.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_22.SetName("Coincident6")
exported_items.append(link_22)


# Mate constraint: Concentric7 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0759411605449909,-0.0674448816874868,0.0543267560949868)
dA = chrono.ChVectorD(0.99636521043768,-0.0851843144568203,2.77237946172026e-16)
cB = chrono.ChVectorD(0.0725172558102234,-0.0801373445415534,0.0543267560949872)
dB = chrono.ChVectorD(-0.99636521043768,0.0851843144568207,9.72999903419265e-17)
link_23.SetFlipped(True)
link_23.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_23.SetName("Concentric7")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateGeneric()
link_24.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0759411605449909,-0.0674448816874868,0.0543267560949868)
cB = chrono.ChVectorD(0.0725172558102234,-0.0801373445415534,0.0543267560949872)
dA = chrono.ChVectorD(0.99636521043768,-0.0851843144568203,2.77237946172026e-16)
dB = chrono.ChVectorD(-0.99636521043768,0.0851843144568207,9.72999903419265e-17)
link_24.Initialize(body_3,body_4,False,cA,cB,dA,dB)
link_24.SetName("Concentric7")
exported_items.append(link_24)

