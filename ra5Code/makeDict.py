#! /usr/env/python
import sys

folder = '/shome/mdunser/workspace/CMSSW_5_2_5/src/DiLeptonAnalysis/NTupleProducer/macros/plots/Jan17_muPFIso0p10_elPFIso0p09_jet40_withZveto_oldAeff_oldZVeto_noTriggerElCut/IntPredictions/'

srs = ['SR01', 'SR02', 'SR03', 'SR04', 'SR05', 'SR06', 'SR07', 'SR08',
       'SR11', 'SR12', 'SR13', 'SR14', 'SR15', 'SR16', 'SR17', 'SR18',
       'SR21', 'SR22', 'SR23', 'SR24', 'SR25', 'SR26', 'SR27', 'SR28' ]

outfile = open('eth_highpt.txt', 'w')
outfile.write('{\n')

tmp = open(folder+'NoteTable.tex','r')
lines = tmp.readlines()

for sr in srs:	
	outfile.write('{\''+sr+':{\n')
	for line in lines:
		if sr in line:
			ind = lines.index(line)
	dfline = lines[ind+2]
	sfline = lines[ind+3]
	chline = lines[ind+4]
	raline = lines[ind+5]
	wzline = lines[ind+6]
	fakes = float(dfline.split()[1])+float(sfline.split()[1])
	fstat = math.sqrt( float(dfline.split()[3])**2+float(sfline.split()[3])**2 )
	fsyst = 0.5*fakes
	flips = float(dfline.split()[1])+float(sfline.split()[1])
	outfile.write('\'f\': '+str(fakes)+', ')
	outfile.write('\'fstat\': '+str(fstat)+', ')
	outfile.write('\'fsyst\': '+fsyst+', ')
	

outfile.close()
