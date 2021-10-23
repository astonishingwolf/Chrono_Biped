# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\Chrono_Biped\Biped_V5\Assem1.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'BP2_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Main_leg-8')
body_1.SetPos(chrono.ChVectorD(0.247693295345429,-0.469969202030413,-0.0356312635354698))
body_1.SetRot(chrono.ChQuaternionD(-0.390128439029838,0.589745539245649,-0.390128439029838,-0.589745539245649))
body_1.SetMass(0.314182522957532)
body_1.SetInertiaXX(chrono.ChVectorD(0.000216025953973108,0.00338753472701888,0.00338433776964922))
body_1.SetInertiaXY(chrono.ChVectorD(-6.37209447763325e-20,3.78380039445936e-20,1.65864592225565e-06))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.53438639878404e-18,-7.55706440556755e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))

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
body_2.SetName('Main_leg-6')
body_2.SetPos(chrono.ChVectorD(0.0129737728010893,0.082214413931304,0.0643687364645302))
body_2.SetRot(chrono.ChQuaternionD(-0.390128439029838,0.589745539245649,-0.390128439029838,-0.589745539245649))
body_2.SetMass(0.314182522957532)
body_2.SetInertiaXX(chrono.ChVectorD(0.000216025953973108,0.00338753472701888,0.00338433776964922))
body_2.SetInertiaXY(chrono.ChVectorD(-6.37209447763325e-20,3.78380039445936e-20,1.65864592225565e-06))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.53438639878404e-18,-7.55706440556755e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))
body_2.SetBodyFixed(True)

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
body_3.SetName('Main_leg-5')
body_3.SetPos(chrono.ChVectorD(0.15409573739939,-0.328700988778952,-0.02))
body_3.SetRot(chrono.ChQuaternionD(-0.390128439029838,0.589745539245649,-0.390128439029838,-0.589745539245649))
body_3.SetMass(0.314182522957532)
body_3.SetInertiaXX(chrono.ChVectorD(0.000216025953973108,0.00338753472701888,0.00338433776964922))
body_3.SetInertiaXY(chrono.ChVectorD(-6.37209447763325e-20,3.78380039445936e-20,1.65864592225565e-06))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.53438639878404e-18,-7.55706440556755e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))

exported_items.append(body_3)



# Rigid body part
body_4= chrono.ChBodyAuxRef()
body_4.SetName('Main_leg-7')
body_4.SetPos(chrono.ChVectorD(0.130333534073259,-0.193877394049555,0.0143687364645302))
body_4.SetRot(chrono.ChQuaternionD(-0.390128439029838,0.589745539245649,-0.390128439029838,-0.589745539245649))
body_4.SetMass(0.314182522957532)
body_4.SetInertiaXX(chrono.ChVectorD(0.000216025953973108,0.00338753472701888,0.00338433776964922))
body_4.SetInertiaXY(chrono.ChVectorD(-6.37209447763325e-20,3.78380039445936e-20,1.65864592225565e-06))
body_4.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.53438639878404e-18,-7.55706440556755e-18,0.18),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_4.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_4)




# Mate constraint: Concentric8 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Main_leg-6 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Main_leg-7 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0012377966738723,0.10982359472939,0.33936873646453)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.00123779667387225,0.10982359472939,0.28936873646453)
dB = chrono.ChVectorD(0,0,-1)
link_1.Initialize(body_2,body_4,False,cA,cB,dA,dB)
link_1.SetName("Concentric8")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0012377966738723,0.10982359472939,0.33936873646453)
cB = chrono.ChVectorD(0.00123779667387225,0.10982359472939,0.28936873646453)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_2.Initialize(body_2,body_4,False,cA,cB,dA,dB)
link_2.SetName("Concentric8")
exported_items.append(link_2)


# Mate constraint: Concentric9 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_4 , SW name: Main_leg-7 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Main_leg-8 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.118597557946042,-0.166268213251469,0.28936873646453)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.118597557946042,-0.166268213251469,0.23936873646453)
dB = chrono.ChVectorD(0,0,-1)
link_3.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_3.SetName("Concentric9")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateGeneric()
link_4.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.118597557946042,-0.166268213251469,0.28936873646453)
cB = chrono.ChVectorD(0.118597557946042,-0.166268213251469,0.23936873646453)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,-1)
link_4.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_4.SetName("Concentric9")
exported_items.append(link_4)


# Mate constraint: Coincident15 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Main_leg-6 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_4 , SW name: Main_leg-7 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.104850290060443,0.423304563614349,0.0393687364645302)
cB = chrono.ChVectorD(0.0125094712117268,0.14721275563349,0.0393687364645302)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_5.Initialize(body_2,body_4,False,cA,cB,dB)
link_5.SetDistance(0)
link_5.SetName("Coincident15")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.104850290060443,0.423304563614349,0.0393687364645302)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.0125094712117268,0.14721275563349,0.0393687364645302)
dB = chrono.ChVectorD(0,0,1)
link_6.SetFlipped(True)
link_6.Initialize(body_2,body_4,False,cA,cB,dA,dB)
link_6.SetName("Coincident15")
exported_items.append(link_6)


# Mate constraint: Coincident16 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_4 , SW name: Main_leg-7 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Main_leg-8 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0125094712117268,0.14721275563349,-0.0106312635354698)
cB = chrono.ChVectorD(0.129869232483897,-0.128879052347369,-0.0106312635354698)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_7.Initialize(body_4,body_1,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident16")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0125094712117268,0.14721275563349,-0.0106312635354698)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.129869232483897,-0.128879052347369,-0.0106312635354698)
dB = chrono.ChVectorD(0,0,1)
link_8.SetFlipped(True)
link_8.Initialize(body_4,body_1,False,cA,cB,dA,dB)
link_8.SetName("Coincident16")
exported_items.append(link_8)

