import os, sys

nproc = sys.argv[1]
vasprun = sys.argv[2]
npar = sys.argv[3]
kpar = sys.argv[4]
pot = sys.argv[5]
gp = sys.argv[6]
cutoff = sys.argv[7]
relax = sys.argv[8]
band = sys.argv[9]
hse = sys.argv[10]
diel = sys.argv[11]
effm = sys.argv[12]

dir = os.popen('python ./src/cif2vasp.pyc '+pot).readlines()
for i in range(len(dir)) :
	dir[i] = dir[i].split()[0]
for target in dir :
	print target
	# k-point test
	notice = os.popen('python ./src/kpoint.pyc '+' '.join([nproc,vasprun,npar,kpar,target,gp])).readline()
	if not 'Success' in notice :
		print target+' >> '+notice
		os.popen('mv '+target+' ./ERROR/')
		continue
        # Energy cut-off test
	if int(cutoff) == 1 :
		notice = os.popen('python ./src/cutoff.pyc '+' '.join([nproc,vasprun,npar,kpar,target,gp])).readline()
		if not 'Success' in notice :
			print target+' >> '+notice
			os.popen('mv '+target+' ./ERROR/')
			continue
	# relaxation (GGA)
	notice = os.popen('python ./src/relax.pyc '+' '.join([nproc,vasprun,npar,kpar,target,relax,'GGA'])).readline()
	if not 'Success' in notice :
		print notice
		os.popen('mv '+target+' ./ERROR/')
		continue
	# band calculation
	if int(band) == 1 :
		notice = os.popen('python ./src/band.pyc '+' '.join([nproc,vasprun,npar,kpar,gp,target,'GGA'])).readline()
		if not 'Success' in notice :
			print notice
			os.popen('mv '+target+' ./ERROR/')
			continue
	# HSE band_gap
	if int(hse) != 0 :
		notice = os.popen('python ./src/hse_gap.pyc '+' '.join([nproc,vasprun,npar,kpar,target,hse])).readline()
		if not 'Success' in notice :
			print notice
			os.popen('mv '+target+' ./ERROR/')
			continue
	# Dielectic calculation
	if int(diel) == 1 :
		# Relaxation (LDA)
		notice = os.popen('python ./src/relax.pyc '+' '.join([nproc,vasprun,npar,kpar,target,relax,'LDA'])).readline()
		
		# Optical Calculation
		notice = os.popen('python ./src/dielec.pyc '+' '.join([nproc,vasprun,npar,kpar,target])).readline()
		if not 'Success' in notice :
			print notice
			os.popen('mv '+target+' ./ERROR/')
			continue
	# Effective mass calculation
	if int(effm) == 1 :
		notice = os.popen('python ./src/effm.py '+' '.join([nproc,vasprun,npar,kpar,target,effm,'GGA'])).readline()
		if not 'Success' in notice :
			print notice
			os.popen('mv '+target+' ./ERROR/')
			continue
	os.popen('mv '+target+' ./Done')

