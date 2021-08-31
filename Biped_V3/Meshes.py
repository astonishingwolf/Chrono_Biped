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
body_1.SetName('leg2-1')
body_1.SetPos(chrono.ChVectorD(0.011735108078163,-0.065284037531251,0.0595449589836269))
body_1.SetRot(chrono.ChQuaternionD(0.57202285083082,0.820229326216699,-0.00303714532884826,-0.00211808633740107))
body_1.SetMass(0.0259472989030997)
body_1.SetInertiaXX(chrono.ChVectorD(2.31048504208172e-05,3.76584109073273e-06,2.04658269870986e-05))
body_1.SetInertiaXY(chrono.ChVectorD(-4.85050072064922e-11,-1.31714693887027e-10,7.11476816153068e-06))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.11979313670952e-18,-9.10055644846633e-19,0.0551561260622386),chrono.ChQuaternionD(1,0,0,0)))

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
body_2.SetPos(chrono.ChVectorD(0.0657119344540866,-0.0649796819567419,0.059903725995649))
body_2.SetRot(chrono.ChQuaternionD(0.571654315594126,0.820414719973791,-0.00939179167709608,-0.00654407839433264))
body_2.SetMass(0.0259472989030997)
body_2.SetInertiaXX(chrono.ChVectorD(2.31048415272292e-05,3.77747490823422e-06,2.04542020631852e-05))
body_2.SetInertiaXY(chrono.ChVectorD(-1.50238208443926e-10,-4.06944604425335e-10,7.12840084732315e-06))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.11979313670952e-18,-9.10055644846633e-19,0.0551561260622386),chrono.ChQuaternionD(1,0,0,0)))

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
body_3.SetName('torso_backet-2')
body_3.SetPos(chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766))
body_3.SetRot(chrono.ChQuaternionD(0.99993448249726,0,0,-0.0114468647645172))
body_3.SetMass(0.00408359922377617)
body_3.SetInertiaXX(chrono.ChVectorD(8.26304827168631e-07,7.8999107371446e-07,6.4299906896382e-07))
body_3.SetInertiaXY(chrono.ChVectorD(8.31956909905342e-10,6.77954123409238e-23,-1.42792093364732e-23))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.74739059678835e-18,-0.00991694834037615,-0.015),chrono.ChQuaternionD(1,0,0,0)))

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
body_4.SetName('knee-2')
body_4.SetPos(chrono.ChVectorD(0.0120919230397415,-0.0171029248233427,0.0111441007075707))
body_4.SetRot(chrono.ChQuaternionD(0.64147033728209,0.301434482845269,-0.30367508267708,0.636737389431527))
body_4.SetMass(0.0243190444078461)
body_4.SetInertiaXX(chrono.ChVectorD(4.80805505850175e-06,9.41479740231775e-06,6.31829833043837e-06))
body_4.SetInertiaXY(chrono.ChVectorD(-4.11627082083899e-11,-3.76793083026502e-06,5.02304992584686e-11))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.14836121412183e-18,-8.5046702510221e-20,0.0344503698921024),chrono.ChQuaternionD(1,0,0,0)))

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
body_5.SetName('knee-1')
body_5.SetPos(chrono.ChVectorD(0.0668074928950852,-0.0171350046556099,0.0111000211243938))
body_5.SetRot(chrono.ChQuaternionD(0.647471168670199,0.296814974021193,-0.303689315807076,0.632814946411884))
body_5.SetMass(0.0243190444078461)
body_5.SetInertiaXX(chrono.ChVectorD(4.86197334929779e-06,9.4147932874727e-06,6.26438415448738e-06))
body_5.SetInertiaXY(chrono.ChVectorD(-1.28320132739353e-10,-3.77833802390492e-06,1.54325607789338e-10))
body_5.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(1.14836121412183e-18,-8.5046702510221e-20,0.0344503698921024),chrono.ChQuaternionD(1,0,0,0)))

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
body_6.SetName('torso_backet-1')
body_6.SetPos(chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766))
body_6.SetRot(chrono.ChQuaternionD(0.999993144705762,0,0,-0.00370277483534016))
body_6.SetMass(0.00408359922377617)
body_6.SetInertiaXX(chrono.ChVectorD(8.26321883922498e-07,7.89974016960593e-07,6.4299906896382e-07))
body_6.SetInertiaXY(chrono.ChVectorD(2.69196234088221e-10,6.75661234710399e-23,-1.53275148946885e-23))
body_6.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.74739059678835e-18,-0.00991694834037615,-0.015),chrono.ChQuaternionD(1,0,0,0)))

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
body_7.SetName('torso-1')
body_7.SetPos(chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.00121479985497664))
body_7.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_7.SetMass(0.0259057709259329)
body_7.SetInertiaXX(chrono.ChVectorD(2.31020545817808e-06,1.23480659694851e-05,1.09419926703796e-05))
body_7.SetInertiaXY(chrono.ChVectorD(2.3027887993619e-12,4.39490384025259e-22,5.68926500197623e-23))
body_7.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(3.0653146371181e-18,2.39477706024852e-20,0.0150000024746274),chrono.ChQuaternionD(1,0,0,0)))
body_7.SetBodyFixed(True)

# Visualization shape 
body_7_1_shape = chrono.ChObjShapeFile() 
body_7_1_shape.SetFilename(shapes_dir +'body_7_1.obj') 
body_7_1_level = chrono.ChAssetLevel() 
body_7_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_7_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_7_1_level.GetAssets().push_back(body_7_1_shape) 
body_7.GetAssets().push_back(body_7_1_level) 

exported_items.append(body_7)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_6 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: torso-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0332147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,-1)
link_1.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0332147998549766)
cB = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_2.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: torso-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_3.Initialize(body_6,body_7,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0122275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,1)
link_4.SetFlipped(True)
link_4.Initialize(body_6,body_7,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: torso-1 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0332147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0672275345305963,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,-1)
link_5.Initialize(body_3,body_7,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0332147998549766)
cB = chrono.ChVectorD(0.0672275345305963,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_6.Initialize(body_3,body_7,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_7 , SW name: torso-1 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_7.Initialize(body_3,body_7,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0672275345305962,0.00120884241999013,0.0312147998549766)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0397275345305962,0.00120884241999013,0.0312147998549766)
dB = chrono.ChVectorD(0,0,1)
link_8.SetFlipped(True)
link_8.Initialize(body_3,body_7,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
exported_items.append(link_8)


# Mate constraint: Concentric3 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: knee-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0142424867298577,-0.0220843159392615,0.0162147998549766)
dA = chrono.ChVectorD(0.999737938574126,-0.0228922295890472,0)
cB = chrono.ChVectorD(0.136648330605853,-0.0248871931463093,0.0162147998549767)
dB = chrono.ChVectorD(-0.999737938574126,0.0228922295890469,-7.4915862001921e-17)
link_9.SetFlipped(True)
link_9.Initialize(body_3,body_5,False,cA,cB,dA,dB)
link_9.SetName("Concentric3")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateGeneric()
link_10.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0142424867298577,-0.0220843159392615,0.0162147998549766)
cB = chrono.ChVectorD(0.136648330605853,-0.0248871931463093,0.0162147998549767)
dA = chrono.ChVectorD(0.999737938574126,-0.0228922295890472,0)
dB = chrono.ChVectorD(-0.999737938574126,0.0228922295890469,-7.4915862001921e-17)
link_10.Initialize(body_3,body_5,False,cA,cB,dA,dB)
link_10.SetName("Concentric3")
exported_items.append(link_10)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: torso_backet-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_5 , SW name: knee-1 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0764351319955154,-0.0335110387567077,-0.000785200145023358)
cB = chrono.ChVectorD(0.0752503315253722,-0.0852530490766312,0.0545586278682679)
dA = chrono.ChVectorD(-0.999737938574126,0.0228922295890472,0)
dB = chrono.ChVectorD(0.999737938574126,-0.0228922295890469,7.4915862001921e-17)
link_11.Initialize(body_3,body_5,False,cA,cB,dB)
link_11.SetDistance(0)
link_11.SetName("Coincident3")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0764351319955154,-0.0335110387567077,-0.000785200145023358)
dA = chrono.ChVectorD(-0.999737938574126,0.0228922295890472,0)
cB = chrono.ChVectorD(0.0752503315253722,-0.0852530490766312,0.0545586278682679)
dB = chrono.ChVectorD(0.999737938574126,-0.0228922295890469,7.4915862001921e-17)
link_12.SetFlipped(True)
link_12.Initialize(body_3,body_5,False,cA,cB,dA,dB)
link_12.SetName("Coincident3")
exported_items.append(link_12)


# Mate constraint: Concentric5 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: knee-2 ,  SW ref.type:2 (2)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0403903924222537,-0.0229021567293663,0.0162147998549766)
dA = chrono.ChVectorD(0.999972578917038,-0.00740549890345833,0)
cB = chrono.ChVectorD(0.0820441803316543,-0.0238088706867194,0.0162147998549766)
dB = chrono.ChVectorD(-0.999972578917038,0.00740549890345856,-6.72252034481568e-17)
link_13.SetFlipped(True)
link_13.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_13.SetName("Concentric5")
exported_items.append(link_13)

link_14 = chrono.ChLinkMateGeneric()
link_14.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0403903924222537,-0.0229021567293663,0.0162147998549766)
cB = chrono.ChVectorD(0.0820441803316543,-0.0238088706867194,0.0162147998549766)
dA = chrono.ChVectorD(0.999972578917038,-0.00740549890345833,0)
dB = chrono.ChVectorD(-0.999972578917038,0.00740549890345856,-6.72252034481568e-17)
link_14.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_14.SetName("Concentric5")
exported_items.append(link_14)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_6 , SW name: torso_backet-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: knee-2 ,  SW ref.type:2 (2)

link_15 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.00197231902925657,-0.0332161565636131,-0.000785200145023354)
cB = chrono.ChVectorD(0.00158702610655224,-0.0852426793648344,0.054116428913619)
dA = chrono.ChVectorD(0.999972578917038,-0.00740549890345833,0)
dB = chrono.ChVectorD(-0.999972578917038,0.00740549890345856,-6.72252034481568e-17)
link_15.Initialize(body_6,body_4,False,cA,cB,dB)
link_15.SetDistance(0)
link_15.SetName("Coincident4")
exported_items.append(link_15)

link_16 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00197231902925657,-0.0332161565636131,-0.000785200145023354)
dA = chrono.ChVectorD(0.999972578917038,-0.00740549890345833,0)
cB = chrono.ChVectorD(0.00158702610655224,-0.0852426793648344,0.054116428913619)
dB = chrono.ChVectorD(-0.999972578917038,0.00740549890345856,-6.72252034481568e-17)
link_16.SetFlipped(True)
link_16.Initialize(body_6,body_4,False,cA,cB,dA,dB)
link_16.SetName("Coincident4")
exported_items.append(link_16)


# Mate constraint: Concentric6 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0164383799727796,-0.0706054336045032,0.0571330296996396)
dA = chrono.ChVectorD(0.999737938574126,-0.0228922295890469,7.4915862001921e-17)
cB = chrono.ChVectorD(0.132522572874765,-0.0740163758132715,0.0571330296996397)
dB = chrono.ChVectorD(-0.999737938574126,0.022892229589047,-2.86870375050352e-17)
link_17.SetFlipped(True)
link_17.Initialize(body_5,body_2,False,cA,cB,dA,dB)
link_17.SetName("Concentric6")
exported_items.append(link_17)

link_18 = chrono.ChLinkMateGeneric()
link_18.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0164383799727796,-0.0706054336045032,0.0571330296996396)
cB = chrono.ChVectorD(0.132522572874765,-0.0740163758132715,0.0571330296996397)
dA = chrono.ChVectorD(0.999737938574126,-0.0228922295890469,7.4915862001921e-17)
dB = chrono.ChVectorD(-0.999737938574126,0.022892229589047,-2.86870375050352e-17)
link_18.Initialize(body_5,body_2,False,cA,cB,dA,dB)
link_18.SetName("Concentric6")
exported_items.append(link_18)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_5 , SW name: knee-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: leg2-2 ,  SW ref.type:2 (2)

link_19 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0738604178469148,-0.0585867708127151,0.0584287368483655)
cB = chrono.ChVectorD(0.0717330992459277,-0.151489958969571,0.0194968262666033)
dA = chrono.ChVectorD(-0.999737938574126,0.0228922295890469,-7.4915862001921e-17)
dB = chrono.ChVectorD(0.999737938574126,-0.022892229589047,2.86870375050352e-17)
link_19.Initialize(body_5,body_2,False,cA,cB,dB)
link_19.SetDistance(0)
link_19.SetName("Coincident5")
exported_items.append(link_19)

link_20 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0738604178469148,-0.0585867708127151,0.0584287368483655)
dA = chrono.ChVectorD(-0.999737938574126,0.0228922295890469,-7.4915862001921e-17)
cB = chrono.ChVectorD(0.0717330992459277,-0.151489958969571,0.0194968262666033)
dB = chrono.ChVectorD(0.999737938574126,-0.022892229589047,2.86870375050352e-17)
link_20.SetFlipped(True)
link_20.Initialize(body_5,body_2,False,cA,cB,dA,dB)
link_20.SetName("Coincident5")
exported_items.append(link_20)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_21 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.00378395117945581,-0.0586590779889784,0.0581766823679784)
cB = chrono.ChVectorD(0.00309562015576331,-0.151605165468497,0.0192085967272168)
dA = chrono.ChVectorD(0.999972578917038,-0.00740549890345856,6.72252034481568e-17)
dB = chrono.ChVectorD(-0.999972578917038,0.00740549890345875,-2.72944393897108e-17)
link_21.Initialize(body_4,body_1,False,cA,cB,dB)
link_21.SetDistance(0)
link_21.SetName("Coincident6")
exported_items.append(link_21)

link_22 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.00378395117945581,-0.0586590779889784,0.0581766823679784)
dA = chrono.ChVectorD(0.999972578917038,-0.00740549890345856,6.72252034481568e-17)
cB = chrono.ChVectorD(0.00309562015576331,-0.151605165468497,0.0192085967272168)
dB = chrono.ChVectorD(-0.999972578917038,0.00740549890345875,-2.72944393897108e-17)
link_22.SetFlipped(True)
link_22.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_22.SetName("Coincident6")
exported_items.append(link_22)


# Mate constraint: Concentric7 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: knee-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: leg2-1 ,  SW ref.type:2 (2)

link_23 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0703182375219747,-0.0721837223744708,0.0567803930342245)
dA = chrono.ChVectorD(0.999972578917038,-0.00740549890345856,6.72252034481568e-17)
cB = chrono.ChVectorD(0.0786776767366639,-0.0732871417110866,0.0567803930342245)
dB = chrono.ChVectorD(-0.999972578917038,0.00740549890345875,-2.72944393897108e-17)
link_23.SetFlipped(True)
link_23.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_23.SetName("Concentric7")
exported_items.append(link_23)

link_24 = chrono.ChLinkMateGeneric()
link_24.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0703182375219747,-0.0721837223744708,0.0567803930342245)
cB = chrono.ChVectorD(0.0786776767366639,-0.0732871417110866,0.0567803930342245)
dA = chrono.ChVectorD(0.999972578917038,-0.00740549890345856,6.72252034481568e-17)
dB = chrono.ChVectorD(-0.999972578917038,0.00740549890345875,-2.72944393897108e-17)
link_24.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_24.SetName("Concentric7")
exported_items.append(link_24)

