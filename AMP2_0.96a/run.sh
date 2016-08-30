#!/bin/sh
#PBS -l nodes=2:ppn=8
#PBS -N AMP2_run
#PBS -l walltime=48:00:00

cd $PBS_O_WORKDIR
cat $PBS_NODEFILE > nodefile
NPROC=`wc -l < $PBS_NODEFILE`

### VASP binary and POTCAR location ###
VASPRUN=/home/usr/vasp
POT=/home/usr/vasp/pot/
### Calculation setting ###
NPAR=2		# Band parallelization
KPAR=2          # k-point parallelization; Number of node is recommended.
CUTOFF=1	# 1 - CUTOFF energy test / 0 - Use default ENCUT
RELAX=1		# 1 - Structural relaxation / 0 - Turn off
BAND=1		# 1 - Band- related calculation / 0 - Turn off
HSE=1		# > 1 - HSE calculation (# of max ionic steps) / 0 - Turn off
DIEL=1		# 1 - Calculate dielectric constant (LDA) / 0 - Turn off
EFFM=1		# 1 - Calculate effective mass / 0 - Turn off
### Gnuplot binary location ###
gnuplot=/usr/local/bin/gnuplot

python main.py $NPROC $VASPRUN $NPAR $KPAR $POT $gnuplot $CUTOFF $RELAX $BAND $HSE $DIEL $EFFM
