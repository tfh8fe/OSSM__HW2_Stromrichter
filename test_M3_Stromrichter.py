# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:14:35 2024

@author: free1
"""

import  M3_Stromrichter
import numpy as np

U_NRMS = 400 # V
alpha_max = 160 # °

# Maximum Power Point (MPP)

I_P = 20 # A
U_P = 150 # V

p = 3
alpha_max = 160
factor = 3 * np.sqrt(3) / (2*np.pi)
ue = 1.67
I_NRMS = 30

def test_calc_norm_u_dc():
    assert M3_Stromrichter.calc_norm_u_dc(3) == 3 * np.sqrt(3) / (2*np.pi)
    assert M3_Stromrichter.calc_norm_u_dc(2) == 2 / np.pi
    
def test_calc_ue():
    assert M3_Stromrichter.calc_ue(400, factor, alpha_max) == 1.758
    assert M3_Stromrichter.calc_ue(120, factor, alpha_max) == 0.528

def test_calc_alpha():
    assert M3_Stromrichter.calc_alpha(400, factor, 1.758, 150) == 124.32
    assert M3_Stromrichter.calc_alpha(400, factor, 1.758, 180) == 132.577

def test_calc_I_NRMS():
    assert M3_Stromrichter.calc_I_NRMS(20, U_P, U_NRMS, I_NRMS) == 9.287
    assert M3_Stromrichter.calc_I_NRMS(40, U_P, U_NRMS, I_NRMS) == 18.573

def test_calc_lambda():
    assert M3_Stromrichter.calc_lambda(I_P, U_P, U_NRMS, 10) == 0.433
    assert M3_Stromrichter.calc_lambda(I_P, U_P, U_NRMS, 19) == 0.228
    