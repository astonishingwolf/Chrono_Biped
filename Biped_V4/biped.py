# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\Biped_Cad\biped_with_plane.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'biped_shapes/' 

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
body_1.SetPos(chrono.ChVectorD(-0.065,-0.007,0.03))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(0.00408359922377617)
body_1.SetInertiaXX(chrono.ChVectorD(8.2632387750958e-07,7.89972023373511e-07,6.4299906896382e-07))
body_1.SetInertiaXY(chrono.ChVectorD(-4.35162206000101e-22,6.82585564069637e-23,1.16375258252681e-23))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.24098646208722e-18,-0.00991694834037615,-0.015),chrono.ChQuaternionD(1,0,0,0)))

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
body_2.SetName('torso_backet-2')
body_2.SetPos(chrono.ChVectorD(-0.00999999999999999,-0.007,0.03))
body_2.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_2.SetMass(0.00408359922377617)
body_2.SetInertiaXX(chrono.ChVectorD(8.2632387750958e-07,7.89972023373511e-07,6.4299906896382e-07))
body_2.SetInertiaXY(chrono.ChVectorD(-4.35162206000101e-22,6.82585564069637e-23,1.16375258252681e-23))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.24098646208722e-18,-0.00991694834037615,-0.015),chrono.ChQuaternionD(1,0,0,0)))

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
body_3.SetName('torso-1')
body_3.SetPos(chrono.ChVectorD(-0.0375,-0.007,0))
body_3.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_3.SetMass(0.0259057709259329)
body_3.SetInertiaXX(chrono.ChVectorD(2.31020545817808e-06,1.23480659694851e-05,1.09419926703796e-05))
body_3.SetInertiaXY(chrono.ChVectorD(2.30278879935503e-12,4.03089204837415e-22,6.46234935435607e-23))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(3.35268788434792e-18,1.27721443213254e-19,0.0150000024746274),chrono.ChQuaternionD(1,0,0,0)))

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
body_4.SetName('leg2-2')
body_4.SetPos(chrono.ChVectorD(-0.00999999999999999,-0.0875,0.015))
body_4.SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,-9.06043357168898e-17,-9.59557881788002e-17))
body_4.SetMass(0.0259472989030997)
body_4.SetInertiaXX(chrono.ChVectorD(2.31048514602965e-05,1.14576985373264e-06,2.30858971846195e-05))
body_4.SetInertiaXY(chrono.ChVectorD(2.17477956089045e-22,-4.73437155235067e-23,-1.21198687993976e-21))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.17802570544879e-18,-8.49264657435101e-19,0.0551561260622386),chrono.ChQuaternionD(1,0,0,0)))

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
body_5.SetName('knee-2')
body_5.SetPos(chrono.ChVectorD(-0.065,-0.0235,0.015))
body_5.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
body_5.SetMass(0.0243190444078461)
body_5.SetInertiaXX(chrono.ChVectorD(1.72032470320509e-06,9.41479788325932e-06,9.40602820479346e-06))
body_5.SetInertiaXY(chrono.ChVectorD(5.94919129634391e-22,-2.77199466467084e-21,-4.15400287881099e-23))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.7129547097722e-18,-1.70193081208137e-20,0.0344503698921024),chrono.ChQuaternionD(1,0,0,0)))

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
body_6.SetName('leg2-1')
body_6.SetPos(chrono.ChVectorD(-0.065,-0.0875,0.015))
body_6.SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,-2.04922098720443e-16,-2.35582203634753e-16))
body_6.SetMass(0.0259472989030997)
body_6.SetInertiaXX(chrono.ChVectorD(2.31048514602965e-05,1.14576985373264e-06,2.30858971846194e-05))
body_6.SetInertiaXY(chrono.ChVectorD(1.00343388147534e-21,-5.41507892119005e-23,3.10415277932626e-22))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.17802570544879e-18,-8.49264657435101e-19,0.0551561260622386),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_4_1_shape = chrono.ChObjShapeFile() 
body_4_1_shape.SetFilename(shapes_dir +'body_4_1.obj') 
body_4_1_level = chrono.ChAssetLevel() 
body_4_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_4_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_4_1_level.GetAssets().push_back(body_4_1_shape) 
body_6.GetAssets().push_back(body_4_1_level) 

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('knee-1')
body_7.SetPos(chrono.ChVectorD(-0.00999999999999999,-0.0235,0.015))
body_7.SetRot(chrono.ChQuaternionD(0.5,0.5,-0.5,0.5))
body_7.SetMass(0.0243190444078461)
body_7.SetInertiaXX(chrono.ChVectorD(1.72032470320509e-06,9.41479788325932e-06,9.40602820479346e-06))
body_7.SetInertiaXY(chrono.ChVectorD(8.63049218561548e-22,-2.74812036347922e-21,-6.16018876585617e-23))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.7129547097722e-18,-1.70193081208137e-20,0.0344503698921024),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_5_1_shape = chrono.ChObjShapeFile() 
body_5_1_shape.SetFilename(shapes_dir +'body_5_1.obj') 
body_5_1_level = chrono.ChAssetLevel() 
body_5_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_5_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_5_1_level.GetAssets().push_back(body_5_1_shape) 
body_7.GetAssets().push_back(body_5_1_level) 

exported_items.append(body_7)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: torso-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.065,-0.007,0.032)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(-0.065,-0.007,0.03)
dB = chrono.ChVectorD(0,0,-1)
link_1.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.065,-0.007,0.032)
cB = chrono.ChVectorD(-0.065,-0.007,0.03)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_2.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: torso-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.065,-0.007,0.03)
cB = chrono.ChVectorD(-0.0375,-0.007,0.03)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_3.Initialize(body_1,body_3,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.065,-0.007,0.03)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(-0.0375,-0.007,0.03)
dB = chrono.ChVectorD(0,0,1)
link_4.SetFlipped(True)
link_4.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: torso-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00999999999999999,-0.007,0.032)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(-0.01,-0.007,0.03)
dB = chrono.ChVectorD(0,0,-1)
link_5.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.00999999999999999,-0.007,0.032)
cB = chrono.ChVectorD(-0.01,-0.007,0.03)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_6.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: torso-1 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.00999999999999999,-0.007,0.03)
cB = chrono.ChVectorD(-0.0375,-0.007,0.03)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_7.Initialize(body_2,body_3,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00999999999999999,-0.007,0.03)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(-0.0375,-0.007,0.03)
dB = chrono.ChVectorD(0,0,1)
link_8.SetFlipped(True)
link_8.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: knee-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0624379301345478,-0.0315,0.015)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.06,-0.0315,0.015)
dB = chrono.ChVectorD(-1,1.42640828083732e-16,-6.17883390286422e-19)
link_9.SetFlipped(True)
link_9.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0624379301345478,-0.0315,0.015)
cB = chrono.ChVectorD(0.06,-0.0315,0.015)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,1.42640828083732e-16,-6.17883390286422e-19)
link_10.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: knee-1 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(6.93889390390723e-18,-0.0415,-0.002)
cB = chrono.ChVectorD(-5.20417042793042e-18,-0.1035,0.005)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,-1.42640828083732e-16,6.17883390286422e-19)
link_11.Initialize(body_2,body_7,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident3")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(6.93889390390723e-18,-0.0415,-0.002)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(-5.20417042793042e-18,-0.1035,0.005)
dB = chrono.ChVectorD(1,-1.42640828083732e-16,6.17883390286422e-19)
link_12.SetFlipped(True)
link_12.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_12.SetName("Coincident3")
exported_items.append(link_12)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: knee-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.117437930134548,-0.0315,0.015)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.00500000000000002,-0.0315,0.015)
dB = chrono.ChVectorD(-1,3.71222462650258e-16,3.38189521705227e-17)
link_13.SetFlipped(True)
link_13.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_13.SetName("Concentric5")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.117437930134548,-0.0315,0.015)
cB = chrono.ChVectorD(0.00500000000000002,-0.0315,0.015)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,3.71222462650258e-16,3.38189521705227e-17)
link_14.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_14.SetName("Concentric5")
exported_items.append(link_14)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: knee-2 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.075,-0.0415,-0.002)
cB = chrono.ChVectorD(-0.075,-0.1035,0.00500000000000001)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,3.71222462650258e-16,3.38189521705227e-17)
link_15.Initialize(body_1,body_5,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident4")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.075,-0.0415,-0.002)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(-0.075,-0.1035,0.00500000000000001)
dB = chrono.ChVectorD(-1,3.71222462650258e-16,3.38189521705227e-17)
link_16.SetFlipped(True)
link_16.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_16.SetName("Coincident4")
exported_items.append(link_16)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.092,-0.0955,0.015)
dA = chrono.ChVectorD(1,-1.42640828083732e-16,6.17883390286422e-19)
cB = chrono.ChVectorD(0.057,-0.0955,0.015)
dB = chrono.ChVectorD(-1,2.6383585741129e-16,7.56809665002857e-18)
link_17.SetFlipped(True)
link_17.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_17.SetName("Concentric6")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.092,-0.0955,0.015)
cB = chrono.ChVectorD(0.057,-0.0955,0.015)
dA = chrono.ChVectorD(1,-1.42640828083732e-16,6.17883390286422e-19)
dB = chrono.ChVectorD(-1,2.6383585741129e-16,7.56809665002857e-18)
link_18.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_18.SetName("Concentric6")
exported_items.append(link_18)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_7 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.002,-0.0855,0.025)
cB = chrono.ChVectorD(-0.00200000000000002,-0.1825,0.00699999999999999)
dA = chrono.ChVectorD(-1,1.42640828083732e-16,-6.17883390286422e-19)
dB = chrono.ChVectorD(1,-2.6383585741129e-16,-7.56809665002857e-18)
link_19.Initialize(body_7,body_4,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident5")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.002,-0.0855,0.025)
dA = chrono.ChVectorD(-1,1.42640828083732e-16,-6.17883390286422e-19)
cB = chrono.ChVectorD(-0.00200000000000002,-0.1825,0.00699999999999999)
dB = chrono.ChVectorD(1,-2.6383585741129e-16,-7.56809665002857e-18)
link_20.SetFlipped(True)
link_20.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_20.SetName("Coincident5")
exported_items.append(link_20)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.073,-0.0855,0.025)
cB = chrono.ChVectorD(-0.0730000000000001,-0.1825,0.007)
dA = chrono.ChVectorD(1,-3.71222462650258e-16,-3.38189521705227e-17)
dB = chrono.ChVectorD(-1,6.22967158674417e-16,4.33599361935986e-17)
link_21.Initialize(body_5,body_6,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Coincident6")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.073,-0.0855,0.025)
dA = chrono.ChVectorD(1,-3.71222462650258e-16,-3.38189521705227e-17)
cB = chrono.ChVectorD(-0.0730000000000001,-0.1825,0.007)
dB = chrono.ChVectorD(-1,6.22967158674417e-16,4.33599361935986e-17)
link_22.SetFlipped(True)
link_22.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_22.SetName("Coincident6")
exported_items.append(link_22)


# Mate constraint: Concentric7 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.147,-0.0955,0.015)
dA = chrono.ChVectorD(1,-3.71222462650258e-16,-3.38189521705227e-17)
cB = chrono.ChVectorD(0.00199999999999999,-0.0955,0.015)
dB = chrono.ChVectorD(-1,6.22967158674417e-16,4.33599361935986e-17)
link_23.SetFlipped(True)
link_23.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_23.SetName("Concentric7")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateGeneric()
link_24.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.147,-0.0955,0.015)
cB = chrono.ChVectorD(0.00199999999999999,-0.0955,0.015)
dA = chrono.ChVectorD(1,-3.71222462650258e-16,-3.38189521705227e-17)
dB = chrono.ChVectorD(-1,6.22967158674417e-16,4.33599361935986e-17)
link_24.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_24.SetName("Concentric7")
exported_items.append(link_24)


# Mate constraint: Coincident8 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: biped_with_plane ,  SW ref.type:4 (4)

link_25 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.0375,-0.007,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_25.Initialize(body_3,body_0,False,cA,cB,dB)
link_25.SetDistance(0)
link_25.SetName("Coincident8")
exported_items.append(link_25)

link_26 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0375,-0.007,0)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_26.SetFlipped(True)
link_26.Initialize(body_3,body_0,False,cA,cB,dA,dB)
link_26.SetName("Coincident8")
exported_items.append(link_26)


# Mate constraint: Coincident9 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: biped_with_plane ,  SW ref.type:4 (4)

link_27 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-5.20417042793042e-18,-0.1035,0.005)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(1,-1.42640828083732e-16,6.17883390286422e-19)
dB = chrono.ChVectorD(1,0,0)
link_27.Initialize(body_7,body_0,False,cA,cB,dB)
link_27.SetDistance(0)
link_27.SetName("Coincident9")
exported_items.append(link_27)

link_28 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-5.20417042793042e-18,-0.1035,0.005)
dA = chrono.ChVectorD(1,-1.42640828083732e-16,6.17883390286422e-19)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_28.Initialize(body_7,body_0,False,cA,cB,dA,dB)
link_28.SetName("Coincident9")
exported_items.append(link_28)


# Mate constraint: Parallel1 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_29 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.055,-0.1035,0.025)
dA = chrono.ChVectorD(3.41542521246712e-17,2.77555756156289e-17,1)
cB = chrono.ChVectorD(-0.0730000000000001,-0.1825,0.023)
dB = chrono.ChVectorD(4.33599361935986e-17,-1.38777878078145e-17,1)
link_29.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_29.SetName("Parallel1")
exported_items.append(link_29)


# Mate constraint: Parallel2 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_7 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_30 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-5.20417042793042e-18,-0.1035,0.025)
dA = chrono.ChVectorD(-6.17883390286432e-19,2.77555756156289e-17,1)
cB = chrono.ChVectorD(-0.018,-0.1825,0.023)
dB = chrono.ChVectorD(7.56809665002859e-18,5.55111512312578e-17,1)
link_30.Initialize(body_7,body_4,False,cA,cB,dA,dB)
link_30.SetName("Parallel2")
exported_items.append(link_30)


# Mate constraint: Parallel3 [MateParallel] type:3 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: torso_backet-2 ,  SW ref.type:2 (2)

link_31 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.053,-0.007,0.032)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(-0.022,-0.007,0.032)
dB = chrono.ChVectorD(-1,0,0)
link_31.SetFlipped(True)
link_31.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_31.SetName("Parallel3")
exported_items.append(link_31)


# Mate constraint: Coincident13 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: torso-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: biped_with_plane ,  SW ref.type:4 (4)

link_32 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.075,0,0.03)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_32.Initialize(body_3,body_0,False,cA,cB,dB)
link_32.SetDistance(0)
link_32.SetName("Coincident13")
exported_items.append(link_32)

link_33 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.075,0,0.03)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,1,0)
link_33.Initialize(body_3,body_0,False,cA,cB,dA,dB)
link_33.SetName("Coincident13")
exported_items.append(link_33)


# Mate constraint: Parallel4 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: knee-1 ,  SW ref.type:2 (2)

link_34 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.00999999999999999,-0.007,-0.002)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(-5.20417042793042e-18,-0.1035,0.005)
dB = chrono.ChVectorD(6.17883390286432e-19,-2.77555756156289e-17,-1)
link_34.Initialize(body_2,body_7,False,cA,cB,dA,dB)
link_34.SetName("Parallel4")
exported_items.append(link_34)


# Mate constraint: Parallel5 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: knee-2 ,  SW ref.type:2 (2)

link_35 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.065,-0.007,-0.002)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(-0.055,-0.1035,0.00500000000000001)
dB = chrono.ChVectorD(-3.41542521246712e-17,-2.77555756156289e-17,-1)
link_35.Initialize(body_1,body_5,False,cA,cB,dA,dB)
link_35.SetName("Parallel5")
exported_items.append(link_35)

