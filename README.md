# OSSM__HW2_Stromrichter

[![license](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/danielhuppmann/lecture-spring-2024/blob/main/LICENSE)

M3_Stromrichter.py is providing functions to calculate the most important 
design elements of an M3 inverter for a solar energy grid feed-in. It includes
calculating the design of a Dy transformer.

### function calc_norm_u_dc
This function calculates the standardized DC voltage. It is a factor for how big 
the DC voltage on the output is compared to the grid voltage amplitude. The factor is 
calculated based on the pulse number. 

### function calc_ue
This function calculates the transformer ratio which is required to properly run 
the system in worst case scenario which is lowest grid voltage and highest output
voltage of PV system (in idle mode). 

### function calc_alpha
For the inverter system the control angle alpha for firing the thyristors at the operating 
point of the PV system is calculated in this function. 

### function calc_I_NRMS
This function calculates the effective value of the grid current which is caused by the 
PV system feed-in. 

### function calc_lambda
The system is evaluated by calculating the total power factor. 

![alt text](https://github.com/tfh8fe/OSSM__HW2_Stromrichter/blob/7443c63583ef879beb39d04b7d50c3bd3d07de22/Stromrichter.png)