# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Downloads\firgelli-l-12-100mm-actuator-1.snapshot.1\Firgelli L-12 100mm\Firgelli L12 100mm Assembly.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'pls_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Firgelli L12 100mm as-2')
body_1.SetPos(chrono.ChVectorD(0.0382955816516225,0.146436082509708,-0.0179743523617899))
body_1.SetRot(chrono.ChQuaternionD(0.707106781186548,9.81307786677361e-16,0,0.707106781186547))
body_1.SetMass(0.00727336703832292)
body_1.SetInertiaXX(chrono.ChVectorD(7.36946465159071e-08,7.9923120453682e-06,7.99124420346242e-06))
body_1.SetInertiaXY(chrono.ChVectorD(1.63055824362194e-22,1.10281010653753e-20,-3.9282977754743e-15))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(5.12883602945224e-19,0.0572037347627958,-8.8770970574344e-20),chrono.ChQuaternionD(1,0,0,0)))

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
body_2.SetName('Firgelli L12 100mm body-1')
body_2.SetPos(chrono.ChVectorD(0.0652955816516226,0.138936082509708,-0.0104743523617896))
body_2.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_2.SetMass(0.0231761154287022)
body_2.SetInertiaXX(chrono.ChVectorD(7.68856704249423e-07,3.64085472290743e-05,3.63326127300815e-05))
body_2.SetInertiaXY(chrono.ChVectorD(-2.66784800924916e-11,4.29155984982522e-07,-4.33740956438715e-14))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.0542952019414717,0.00749999598125523,-0.00797263745817144),chrono.ChQuaternionD(1,0,0,0)))
body_2.SetBodyFixed(True)

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
body_2.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_2)




# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Firgelli L12 100mm body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Firgelli L12 100mm as-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.0517044183483775,0.146436082509708,-0.0179743523617898)
dA = chrono.ChVectorD(-1,0,1.38777878078145e-15)
cB = chrono.ChVectorD(-0.0787044183483775,0.146436082509708,-0.0179743523617897)
dB = chrono.ChVectorD(1,0,-1.38777878078145e-15)
link_1.SetFlipped(True)
link_1.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_1.SetName("Concentric2")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.0517044183483775,0.146436082509708,-0.0179743523617898)
cB = chrono.ChVectorD(-0.0787044183483775,0.146436082509708,-0.0179743523617897)
dA = chrono.ChVectorD(-1,0,1.38777878078145e-15)
dB = chrono.ChVectorD(1,0,-1.38777878078145e-15)
link_2.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_2.SetName("Concentric2")
exported_items.append(link_2)


# Mate constraint: Parallel1 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Firgelli L12 100mm body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Firgelli L12 100mm as-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0662955816516226,0.150436082509708,-0.0304743523617896)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(-0.0727044183483775,0.149436082509708,-0.0224743523617897)
dB = chrono.ChVectorD(1.92592994438724e-30,1,1.38777878078145e-15)
link_3.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_3.SetName("Parallel1")
exported_items.append(link_3)


# Mate constraint: LimitDistance1 [MateLimitDistanceDim] type:5 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Firgelli L12 100mm body-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Firgelli L12 100mm as-2 ,  SW ref.type:2 (2)

