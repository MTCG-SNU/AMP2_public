import os, sys

# Location of POTCARs
pot = '/usr/local/vasp4us/pot/'

if not os.path.isdir(pot) :
	print 'Directory for POTCAR is wrong!. Fix make_INPUT.py first.'
	sys.exit(-1)

dir = os.popen('python ./src/cif2vasp.pyc '+pot).readlines()
for i in range(len(dir)) :
	dir[i] = dir[i].split()[0]
for target in dir :
	os.popen('mv '+target+' ./Cont')

