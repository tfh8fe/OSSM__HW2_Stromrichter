# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:29:17 2024

@author: tfh8fe

Auslegung eines M3 Wechselrichters für eine Solarenergie Netzeinspeisung
mit Auslegung eines Dy Trafos (dafür gesucht Übersetzungsverhältnis) und 
Auslegung des Steuerwinkel alpha für die Zündung der Thyristoren im Betriebs-
punkt der PV-Anlage
Außerdem Bewertung des Stromrichters mittels totalem Leistungsfaktor wofür 
Netzstrom-Effektivwert berechnet wird

ToDo: 
    - Bild von Schaltung aus Skript einfügen (S. 23)
"""
import numpy as np


U_NRMS = 400  # V
alpha_max = 160  # °

# Maximum Power Point (MPP)
I_P = 20  # A
U_P = 150  # V

def calc_norm_u_dc(p):
    factor = p / np.pi * np.sin(np.pi / p)
    return round(factor, 3)


def calc_ue(U_NRMS, factor, alpha_max):
    U_N = 0.8 * U_NRMS  # worst case Netzspg: -20%
    U_P = 200  # V im Leerlauf 
    ue = - U_N / U_P * np.sqrt(2) * factor * np.cos(np.deg2rad(alpha_max))
    return round(ue, 3)


def calc_alpha(U_NRMS, factor, ue, U_P):
    U_amp_j0 = U_NRMS * np.sqrt(2) / ue
    U_d0 = factor * U_amp_j0
    alpha = np.rad2deg(np.arccos(- U_P / U_d0))
    return round(alpha, 3)


def calc_I_NRMS(I_P, ue):
    I_NRMS = I_P / ue 
    * np.sqrt(2/3) # Tastverhältnis 2/3 wegen Dreieck auf Primärseite
    return round(I_NRMS, 3)


def calc_lambda(I_P, U_P, U_NRMS, I_NRMS):
    LF = (I_P * U_P) / (3 * U_NRMS / np.sqrt(3) * I_NRMS)
    return round(LF, 3)


p = 3
factor = calc_norm_u_dc(p)
ue = calc_ue(U_NRMS, factor, alpha_max)
alpha = calc_alpha(U_NRMS, factor, ue, U_P)
I_NRMS = calc_I_NRMS(I_P, ue)
LF = calc_lambda(I_P, U_P, U_NRMS, I_NRMS)

print("ue: ", ue)
print("alpha: ", alpha)
print("I_NRMS: ", I_NRMS)
print("LF: ", LF)

