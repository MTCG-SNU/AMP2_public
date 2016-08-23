[Automated Ab intio Modeling of Materials Property Package]
AMP2 band structure v0.96b (2016-06-27)
	- Developed by Kanghoon Yim & Kyuhuyn Lee
	- Contact: amp2.mtcg@gmail.com

<Requirements>

1) Message Passing Interface (MPI)
    Portable Batch System (PBS) [optional]
2) VASP parallel run file - 5.x version is recommended.
3) PYTHON - 2.6 or higher (http://www.python.org/)
4) Gnuplot (http://www.gnuplot.info/)


### How to run AMP^2 ###

1. Modify 'run.sh' file.
  (1) If you use PBS such as TORQUE, modify the setting for your own system.
      Otherwise, set only the NPROC - Number of processors that you will use.
  (2) VASRUN - location of VASP run file.
      ex) VASPRUN=/home/user/vasp
  (3) Set parallel option for VASP INCAR file.
       NPAR: band parallelization
       KPAR: k-point parallelization
  * Below settings are optional.
  (4) POT: pseudo-potentail type ('GGA' or 'LDA')
  (5) RELAX: Setting '1' means full-structural relaxation for equilibrium structure.
	     If you don't want relax the initial structure, set '0' this option.
  (6) BAND: If you want calculate band structure and find band gap(GGA), set '1' this option.
            Set '0' to turn off.
  (7) HSE: If you want calculate hybrid band gap(HSE06), set number of ionic steps.
           Set '1' one-shot calcuation or give a number large than 1 for more relaxation using HSE06.
	   Set '0' to turn off.
  (8) DIEL: If you want calculate static dielectric tensor, set '1' this option.
	    set '0' to turn off.
  (9) gnuplot - location of gnuplot run file

2. Put structure files in [Submit] directory.
   - Supported structure file:
    (1) *.cif files from ICSD(Inorganic Crystal Structure Database, http://icsd.fiz-karlsruhe.de/)
	  *File name is used as the directory name in [Result]
    (2) POSCAR file - Modify the filename in below format.
	Format: POSCAR_{space group nubmer}_{Title}
	    	Ex) POSCAR_225_NaCl

3. run 'run.sh' file.
   ex) qsub run.sh


### How to check AMP^2 simulation result ###

After the simulation is done, You can find the simulation results in the below location.
 - Done/[Title]/kpoint: k-point convergence test result (KPOINTS_converged)
 - Done/[Title]/relax_XXX: Ground-state relaxed structure (CONTCAR) using funtional XXX
 - Done/[Title]/band_XXX: Band structure plots[*] ([Title].png, [Title].eps)
                          GGA Band gap (Band_gap.log)
 - Done/[Title]/HSE: HSE Band gap (Band_gap.log)
 - Done/[Title]/dielectric: Static dielectric tensor (dielectrics.log)

[*]Symmetric k-points in the 1st BZ are refered from below article.
   "High-throughput electronic band structure calculations: Challenges and tools"
   W. Setyawan et al. Comp. Mater. Sci. 49, 299-312 (2010)
