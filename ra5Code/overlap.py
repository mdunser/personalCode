#! /usr/bin/python
import commands, sys, math

class event():
	pass


def fillSet(f):
	tmpFile = open(f,'r')
	tmpSet = set()
	for line in tmpFile.readlines():
		## tmp = event()
		run = line.split()[2]
		ls  = line.split()[4]
		evn = line.split()[6]
		all = run+ls+evn
		##tmp = math.log(abs(float(line.split()[2])))*math.log(abs(float(line.split()[4])))*math.log(abs(float(line.split()[6])))
		tmp = int(all)
		if line.split()[8] != '0' and float(line.split()[10]) > 200.: 
			tmpSet.add(tmp)
	return tmpSet
	

def getCorrelations2(s1, s2):
	n1, n2 = len(s1), len(s2)
	inboth = s1.intersection(s2)
	print '--------------------------'
	print 'I have two sets here with lengths:', n1, '(set 1), and', n2, '(set 2)'
	print 'there are %d events in both sets' %( len(inboth) )
	print 'the overlap in set 1 is: %.2f +- %.2f' %( len(inboth)/float(n1), math.sqrt(len(inboth))/float(n1) )
	print 'the overlap in set 2 is: %.2f +- %.2f' %( len(inboth)/float(n2), math.sqrt(len(inboth))/float(n2) )
	print '------> the correlation factor is then: %.3f' %(len(inboth)/math.sqrt(n1*n2))


def getCorrelations3(s1, s2, s3):
	n1, n2, n3 = len(s1), len(s2), len(s3)
	inall = s1.intersection(s2, s3)
	in12 = s1.intersection(s2)
	in13 = s1.intersection(s3)
	in23 = s2.intersection(s3)
	print '--------------------------'
	print 'I have three sets here with lengths: %d (set 1), %d (set 2) and %d (set 3)' %(n1, n2, n3)
	print 'there are %d events in all three sets' %( len(inall) )
	print 'the total overlap of set 1 is %.2f +- %.2f' %( len(inall)/float(n1), math.sqrt(len(inall))/float(n1) )
	print 'the total overlap of set 2 is %.2f +- %.2f' %( len(inall)/float(n2), math.sqrt(len(inall))/float(n2) )
	print 'the total overlap of set 3 is %.2f +- %.2f' %( len(inall)/float(n3), math.sqrt(len(inall))/float(n3) )
	print 'the overlap of set 1 and 2 is %.2f and %.2f respectively' %( len(in12)/float(n1), len(in12)/float(n2) )
	print 'the overlap of set 1 and 3 is %.2f and %.2f respectively' %( len(in13)/float(n1), len(in13)/float(n3) )
	print 'the overlap of set 2 and 3 is %.2f and %.2f respectively' %( len(in23)/float(n2), len(in23)/float(n3) )


uflSet_high  = fillSet('overlaps/UF_BaselineH1_tightD0_sorted.txt')
uflSet_highb = fillSet('overlaps/UF_BaselineH2_tightD0_sorted.txt')

uflSet_low   = fillSet('overlaps/UF_BaselineL1_tightD0_sorted.txt')
uflSet_lowb  = fillSet('overlaps/UF_BaselineL2_tightD0_sorted.txt')

ucsSet_high  = fillSet('overlaps/ucfnal_exclusive_highpt_sr0.txt')
ucsSet_highb = fillSet('overlaps/ucfnal_exclusive_highpt_sr20.txt')

ucsSet_low   = fillSet('overlaps/ucfnal_exclusive_lowpt_sr0.txt')
ucsSet_lowb  = fillSet('overlaps/ucfnal_exclusive_lowpt_sr20.txt')

ethSet_high  = fillSet('overlaps/eth_sidebands_nob.txt')
ethSet_highb = fillSet('overlaps/eth_sidebands_withb.txt')


## print 'doing overlap for high-pT no b-tag:'
## print '==================================='
## getCorrelations3(uflSet_high, ucsSet_high, ethSet_high)
## print '\n \n'
## 
## print 'doing overlap for high-pT with b-tag:'
## print '====================================='
## getCorrelations3(uflSet_highb, ucsSet_highb, ethSet_highb)
## print '\n \n'

print 'doing overlap for low-pT no b-tag:'
print '====================================='
getCorrelations2(uflSet_low, ucsSet_low)
print '\n \n'

print 'doing overlap for low-pT with b-tag:'
print '====================================='
getCorrelations2(uflSet_lowb, ucsSet_lowb)
print '\n \n'

print '====================================='
print '====================================='
print '====================================='
print '====================================='
print '====================================='
print '====================================='


print 'doing overlap for high-pT no b-tag:'
print '====================================='
getCorrelations2(uflSet_high, ucsSet_high)
print '\n'

print 'doing overlap for high-pT no b-tag:'
print '====================================='
getCorrelations2(uflSet_high, ethSet_high)
print '\n'

print 'doing overlap for high-pT no b-tag:'
print '====================================='
getCorrelations2(ethSet_high, ucsSet_high)
print '\n'

print '====================================='
print '====================================='

print 'doing overlap for high-pT with b-tag:'
print '====================================='
getCorrelations2(uflSet_highb, ucsSet_highb)
print '\n'

print 'doing overlap for high-pT with b-tag:'
print '====================================='
getCorrelations2(uflSet_highb, ethSet_highb)
print '\n'

print 'doing overlap for high-pT with b-tag:'
print '====================================='
getCorrelations2(ethSet_highb, ucsSet_highb)
print '\n'
