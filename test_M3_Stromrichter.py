# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:14:35 2024

@author: free1
"""

import M3_Stromrichter
import numpy as np

U_NRMS = 400  # V
alpha_max = 160  # °

# Maximum Power Point (MPP)

I_P = 20  # A
U_P = 150  # V

p = 3
alpha_max = 160
factor = 3 * np.sqrt(3) / (2 * np.pi)
ue = 1.758
I_NRMS = 30


def test_calc_norm_u_dc():
    assert M3_Stromrichter.calc_norm_u_dc(3) == round(3 * np.sqrt(3) / (2 * np.pi), 3)
    assert M3_Stromrichter.calc_norm_u_dc(2) == round(2 / np.pi, 3)


def test_calc_ue():
    assert M3_Stromrichter.calc_ue(400, factor, alpha_max) == 1.758
    assert M3_Stromrichter.calc_ue(120, factor, alpha_max) == 0.528


def test_calc_alpha():
    assert M3_Stromrichter.calc_alpha(400, factor, 1.758, 150) == 124.311
    assert M3_Stromrichter.calc_alpha(400, factor, 1.758, 180) == 132.564


def test_calc_I_NRMS():
    assert M3_Stromrichter.calc_I_NRMS(20, ue) == 9.289
    assert M3_Stromrichter.calc_I_NRMS(40, ue) == 18.578


def test_calc_lambda():
    assert M3_Stromrichter.calc_lambda(I_P, U_P, U_NRMS, 10) == 0.433
    assert M3_Stromrichter.calc_lambda(I_P, U_P, U_NRMS, 19) == 0.228
