# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\Biped_Cad\biped_with_plane.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'Meshes_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('torso_backet-2')
body_1.SetPos(chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766))
body_1.SetRot(chrono.ChQuaternionD(0.999999664045456,0,0,-0.000819700540144573))
body_1.SetMass(0.00408359922377617)
body_1.SetInertiaXX(chrono.ChVectorD(8.26323779809098e-07,7.89972121073993e-07,6.4299906896382e-07))
body_1.SetInertiaXY(chrono.ChVectorD(5.95951688342873e-11,6.7866934845368e-23,-7.43199776545551e-24))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.26630666882227e-18,-0.00991694834037615,-0.015),chrono.ChQuaternionD(1,0,0,0)))

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
body_2.SetName('leg2-2')
body_2.SetPos(chrono.ChVectorD(0.0671180033713246,-0.0656027817738135,0.0611998759226639))
body_2.SetRot(chrono.ChQuaternionD(0.496241612698117,0.868184076056338,-0.000711651195170847,-0.00040676965462703))
body_2.SetMass(0.0259472989030997)
body_2.SetInertiaXX(chrono.ChVectorD(2.31048514093543e-05,6.79632385098439e-06,1.74353432383099e-05))
body_2.SetInertiaXY(chrono.ChVectorD(-1.57694890763888e-11,-2.67748448640787e-11,9.594014488302e-06))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.12977097059401e-18,-7.46715562846943e-19,0.0551561260622386),chrono.ChQuaternionD(1,0,0,0)))

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
body_3.SetName('knee-1')
body_3.SetPos(chrono.ChVectorD(0.0671974525521571,-0.0171405099637163,0.0110991535392462))
body_3.SetRot(chrono.ChQuaternionD(0.640730737938272,0.299980471932769,-0.300472663857862,0.63968118324227))
body_3.SetMass(0.0243190444078461)
body_3.SetInertiaXX(chrono.ChVectorD(4.86303736310096e-06,9.41479785968963e-06,6.26331556846728e-06))
body_3.SetInertiaXY(chrono.ChVectorD(-9.19345345495616e-12,-3.77853343323184e-06,1.10534353629162e-11))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.25853171525096e-18,-2.42360052035725e-19,0.0344503698921024),chrono.ChQuaternionD(1,0,0,0)))

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
body_4.SetName('torso-1')
body_4.SetPos(chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.00121479985497664))
body_4.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_4.SetMass(0.0259057709259329)
body_4.SetInertiaXX(chrono.ChVectorD(2.31020545817808e-06,1.23480659694851e-05,1.09419926703796e-05))
body_4.SetInertiaXY(chrono.ChVectorD(2.30278879937442e-12,4.16064370583816e-22,7.39509807929662e-23))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(3.0653146371181e-18,6.38607216066271e-20,0.0150000024746274),chrono.ChQuaternionD(1,0,0,0)))
body_4.SetBodyFixed(True)

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
body_5.SetName('torso_backet-1')
body_5.SetPos(chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766))
body_5.SetRot(chrono.ChQuaternionD(0.999999599749934,0,0,-0.000894706639973221))
body_5.SetMass(0.00408359922377617)
body_5.SetInertiaXX(chrono.ChVectorD(8.26323761111041e-07,7.8997213977205e-07,6.4299906896382e-07))
body_5.SetInertiaXY(chrono.ChVectorD(6.50483603630767e-11,6.78680489724786e-23,-7.42181680994708e-24))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.26630666882227e-18,-0.00991694834037615,-0.015),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_5.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_5)



# Rigid body part
body_6= chrono.ChBodyAuxRef()
body_6.SetName('knee-2')
body_6.SetPos(chrono.ChVectorD(0.0121954739058518,-0.0167079723299176,0.0116692471231617))
body_6.SetRot(chrono.ChQuaternionD(0.626697741675863,0.32826560496241,-0.328853534054661,0.625577322412502))
body_6.SetMass(0.0243190444078461)
body_6.SetInertiaXX(chrono.ChVectorD(4.20161201306026e-06,9.41479785517883e-06,6.92474092301877e-06))
body_6.SetInertiaXY(chrono.ChVectorD(-8.91641288642003e-12,-3.59355700127716e-06,1.29133123033944e-11))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.25853171525096e-18,-2.42360052035725e-19,0.0344503698921024),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_3_1_shape = chrono.ChObjShapeFile() 
body_3_1_shape.SetFilename(shapes_dir +'body_3_1.obj') 
body_3_1_level = chrono.ChAssetLevel() 
body_3_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_3_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_3_1_level.GetAssets().push_back(body_3_1_shape) 
body_6.GetAssets().push_back(body_3_1_level) 

exported_items.append(body_6)



# Rigid body part
body_7= chrono.ChBodyAuxRef()
body_7.SetName('leg2-1')
body_7.SetPos(chrono.ChVectorD(0.0120991655231794,-0.0705291147713972,0.058456781752714))
body_7.SetRot(chrono.ChQuaternionD(0.364214759600132,0.931314559313579,-0.000833253653631439,-0.000325865494218135))
body_7.SetMass(0.0259472989030997)
body_7.SetInertiaXX(chrono.ChVectorD(2.3104851399605e-05,1.29885405328716e-05,1.1243126566172e-05))
body_7.SetInertiaXY(chrono.ChVectorD(-2.49186245880894e-11,-2.30091861059651e-11,1.09352951496923e-05))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.12977097059401e-18,-7.46715562846943e-19,0.0551561260622386),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_7.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_7)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_5 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: torso-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999014,0.0332147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,-1)
link_1.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999014,0.0332147998549766)
cB = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_2.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: torso-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_3.Initialize(body_5,body_4,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,1)
link_4.SetFlipped(True)
link_4.Initialize(body_5,body_4,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: torso-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0332147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0672275345305963,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,-1)
link_5.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0332147998549766)
cB = chrono.ChVectorD(0.0672275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_6.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: torso-1 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_7.Initialize(body_1,body_4,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,1)
link_8.SetFlipped(True)
link_8.Initialize(body_1,body_4,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: knee-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0147495095501069,-0.0232051578860403,0.0162147998549766)
dA = chrono.ChVectorD(0.999998656182049,-0.0016394005295249,0)
cB = chrono.ChVectorD(0.137187275150366,-0.0234058826935368,0.0162147998549767)
dB = chrono.ChVectorD(-0.999998656182049,0.00163940052952502,6.6608930751317e-18)
link_9.SetFlipped(True)
link_9.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0147495095501069,-0.0232051578860403,0.0162147998549766)
cB = chrono.ChVectorD(0.137187275150366,-0.0234058826935368,0.0162147998549767)
dA = chrono.ChVectorD(0.999998656182049,-0.0016394005295249,0)
dB = chrono.ChVectorD(-0.999998656182049,0.00163940052952502,6.6608930751317e-18)
link_10.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: knee-1 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0771709617741481,-0.0333075052235858,-0.000785200145023358)
cB = chrono.ChVectorD(0.0770861225270353,-0.0850576001980903,0.0545673379989616)
dA = chrono.ChVectorD(-0.999998656182049,0.0016394005295249,0)
dB = chrono.ChVectorD(0.999998656182049,-0.00163940052952502,-6.6608930751317e-18)
link_11.Initialize(body_1,body_3,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident3")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0771709617741481,-0.0333075052235858,-0.000785200145023358)
dA = chrono.ChVectorD(-0.999998656182049,0.0016394005295249,0)
cB = chrono.ChVectorD(0.0770861225270353,-0.0850576001980903,0.0545673379989616)
dB = chrono.ChVectorD(0.999998656182049,-0.00163940052952502,-6.6608930751317e-18)
link_12.SetFlipped(True)
link_12.Initialize(body_1,body_3,False,cA,cB,dA,dB)
link_12.SetName("Coincident3")
exported_items.append(link_12)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: knee-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0402541522586399,-0.0231972852645123,0.0162147998549766)
dA = chrono.ChVectorD(0.999998399000057,-0.00178941256373366,0)
cB = chrono.ChVectorD(0.0821835818527889,-0.0234163772349726,0.0162147998549764)
dB = chrono.ChVectorD(-0.999998399000057,0.00178941256373383,3.38722641571851e-16)
link_13.SetFlipped(True)
link_13.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_13.SetName("Concentric5")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0402541522586399,-0.0231972852645123,0.0162147998549766)
cB = chrono.ChVectorD(0.0821835818527889,-0.0234163772349726,0.0162147998549764)
dA = chrono.ChVectorD(0.999998399000057,-0.00178941256373366,0)
dB = chrono.ChVectorD(-0.999998399000057,0.00178941256373383,3.38722641571851e-16)
link_14.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_14.SetName("Concentric5")
exported_items.append(link_14)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_6 , SW name: knee-2 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.00216581580714688,-0.0332732082198745,-0.000785200145023361)
cB = chrono.ChVectorD(0.00206752274872348,-0.0882034702781987,0.0488958287347756)
dA = chrono.ChVectorD(0.999998399000057,-0.00178941256373366,0)
dB = chrono.ChVectorD(-0.999998399000057,0.00178941256373383,3.38722641571851e-16)
link_15.Initialize(body_5,body_6,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident4")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00216581580714688,-0.0332732082198745,-0.000785200145023361)
dA = chrono.ChVectorD(0.999998399000057,-0.00178941256373366,0)
cB = chrono.ChVectorD(0.00206752274872348,-0.0882034702781987,0.0488958287347756)
dB = chrono.ChVectorD(-0.999998399000057,0.00178941256373383,3.38722641571851e-16)
link_16.SetFlipped(True)
link_16.Initialize(body_5,body_6,False,cA,cB,dA,dB)
link_16.SetName("Coincident4")
exported_items.append(link_16)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0148931872655802,-0.0723616113550789,0.0571399703808202)
dA = chrono.ChVectorD(0.999998656182049,-0.00163940052952502,-6.6608930751317e-18)
cB = chrono.ChVectorD(0.134106612505545,-0.0726058820339783,0.0571399703808204)
dB = chrono.ChVectorD(-0.999998656182049,0.00163940052952513,-2.34545498758353e-19)
link_17.SetFlipped(True)
link_17.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_17.SetName("Concentric6")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0148931872655802,-0.0723616113550789,0.0571399703808202)
cB = chrono.ChVectorD(0.134106612505545,-0.0726058820339783,0.0571399703808204)
dA = chrono.ChVectorD(0.999998656182049,-0.00163940052952502,-6.6608930751317e-18)
dB = chrono.ChVectorD(-0.999998656182049,0.00163940052952513,-2.34545498758353e-19)
link_18.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_18.SetName("Concentric6")
exported_items.append(link_18)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0751297792005707,-0.0584263397352526,0.0584336911837463)
cB = chrono.ChVectorD(0.0749904510761034,-0.143413464435133,0.00609522792528596)
dA = chrono.ChVectorD(-0.999998656182049,0.00163940052952502,6.6608930751317e-18)
dB = chrono.ChVectorD(0.999998656182049,-0.00163940052952513,2.34545498758353e-19)
link_19.Initialize(body_3,body_2,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident5")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0751297792005707,-0.0584263397352526,0.0584336911837463)
dA = chrono.ChVectorD(-0.999998656182049,0.00163940052952502,6.6608930751317e-18)
cB = chrono.ChVectorD(0.0749904510761034,-0.143413464435133,0.00609522792528596)
dB = chrono.ChVectorD(0.999998656182049,-0.00163940052952513,2.34545498758353e-19)
link_20.SetFlipped(True)
link_20.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_20.SetName("Coincident5")
exported_items.append(link_20)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.00411435918154255,-0.0620311069097775,0.0551262265012599)
cB = chrono.ChVectorD(0.0039943720648899,-0.129084913830381,-0.0167664242382723)
dA = chrono.ChVectorD(0.999998399000057,-0.00178941256373383,-3.38722641571851e-16)
dB = chrono.ChVectorD(-0.999998399000057,0.00178941256373366,-8.56363574515432e-17)
link_21.Initialize(body_6,body_7,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Coincident6")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00411435918154255,-0.0620311069097775,0.0551262265012599)
dA = chrono.ChVectorD(0.999998399000057,-0.00178941256373383,-3.38722641571851e-16)
cB = chrono.ChVectorD(0.0039943720648899,-0.129084913830381,-0.0167664242382723)
dB = chrono.ChVectorD(-0.999998399000057,0.00178941256373366,-8.56363574515432e-17)
link_22.SetFlipped(True)
link_22.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_22.SetName("Coincident6")
exported_items.append(link_22)


# Mate constraint: Concentric12 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0699104146597545,-0.0758095547300348,0.0525792217094946)
dA = chrono.ChVectorD(0.999998399000057,-0.00178941256373383,-3.38722641571851e-16)
cB = chrono.ChVectorD(0.0790893467912506,-0.0760761772020295,0.0525792217094965)
dB = chrono.ChVectorD(-0.999998399000057,0.00178941256373366,-8.56363574515432e-17)
link_23.SetFlipped(True)
link_23.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_23.SetName("Concentric12")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateGeneric()
link_24.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0699104146597545,-0.0758095547300348,0.0525792217094946)
cB = chrono.ChVectorD(0.0790893467912506,-0.0760761772020295,0.0525792217094965)
dA = chrono.ChVectorD(0.999998399000057,-0.00178941256373383,-3.38722641571851e-16)
dB = chrono.ChVectorD(-0.999998399000057,0.00178941256373366,-8.56363574515432e-17)
link_24.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_24.SetName("Concentric12")
exported_items.append(link_24)

