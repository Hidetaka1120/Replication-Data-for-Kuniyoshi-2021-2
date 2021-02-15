# Replication-Data-for-Kuniyoshi-2021
Resistive magnetohydrodynamics (MHD) simulation of reconnection in a twisted magnetic flux tube used in the paper 'Magnetic Reconnection in a Sheared Magnetic Flux Tube: Slippage versus Tearing'.

## Contact information
Hidetaka Kuniyoshi \
Department of Earth and Planetary Science, The University of Tokyo, Tokyo, Japan. \
E-mail: hidetaka@eps.s.u-tokyo.ac.jp \
ORCID ID of author: https://orcid.org/0000-0003-1134-2770 

## Data file description
This data set contains files of binary data describing the output of the resistive MHD simulation of reconnection in a twisted magnetic flux tube. It thus contains magnetic fields, fluid velocities, densities, pressures and resistivities in the simulation domain. The documentation of the variables and arrays are given below. The .dat files are made using the open source language Fortran. They are named asp\*eta\*-0200.dat, for which the \* has the usual meaning in a linux environment. The name "asp" refers to the aspect ratio of the flux tube <img src="https://render.githubusercontent.com/render/math?math=(b/a)^2"> and "eta" refers to the peak magnitude of the resistivity <img src="https://render.githubusercontent.com/render/math?math=\eta_A">, which are described in more detail in manuscript. The number 0200 refers to the time in units of the Alfven crossing time along the flux tube. The variables are structured identically in each file.

Because the dat files contain binary data, they can not be viewed in a text editor. Instead, the variables and arrays can be read into Python, an open source programming language. The file readData.py is the code for reading the asp\*eta\*-0200.dat files into Python. readData.py can be opened in any text editor.

## Documentation of variables and arrays
The usual MHD normalization is being applied.
The units are thoroughly explained in the paper 'Magnetic Reconnection in a Sheared Magnetic Flux Tube: Slippage versus Tearing'.

time: Current timestep \
nx, ny, nz: nx, ny and nz denote the number of grid cells in the x, y and z direction, respectively. \
x: Grid layot in the X direction \
y: Grid layot in the Y direction \
z: Grid layot in the Z direction \
gamma: Ratio of specific heats \
ro: Mass density \
vx: Fluid velocity in the X direction \
vy: Fluid velocity in the Y direction \
vz: Fluid velocity in the Z direction \
bx: Magnetic field in the X direction \
by: Magnetic field in the Y direction \
bz: Magnetic field in the Z direction \
pr: Gas pressure \
eta: Resistivity 

## Usage of the Python file
For example, when reading asp10eta79-0200.dat [<img src="https://render.githubusercontent.com/render/math?math=(b/a)^2=0.10, \eta_A=79">], where "asp10" refers to the <img src="https://render.githubusercontent.com/render/math?math=(b/a)^2=0.10">, and "eta79" refers to the <img src="https://render.githubusercontent.com/render/math?math=\eta_A=79">. write these commands in Python,

```python
import numpy as np
import readData as rd

filename='data/asp10eta79-0200.dat'
data=rd.readFile(filename) 
bx=data['bx']
```

Then you can get the array of bx which size is <img src="https://render.githubusercontent.com/render/math?math=nx \times ny \times nz">.
