# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:01:21 2019

@author: SB
"""

import pychrono as chrono
import chtrain_biped

# Properly set path to Chrono data directory, taking into account the location of the chrono-tensorflow
# demos relative to the other PyChrono demos.
# If running from a different directory, you must change this path accordingly.
chrono.SetChronoDataPath('../../' + chrono.GetChronoDataPath())

def Init(env_name, render):
    return chtrain_biped.Model(render)

                            
       