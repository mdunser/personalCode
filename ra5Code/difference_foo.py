#! /usr/bin/python
import commands, sys, math

class event():
	pass


def fillSet(f):
	tmpFile = open(f,'r')
	tmpSet = set()
	for line in tmpFile.readlines():
		## tmp = event()
		run = line.split(':')[0]
		ls  = line.split(':')[1]
		evn = line.split(':')[2]
		all = run+':'+ls+':'+evn
		##tmp = math.log(abs(float(line.split()[2])))*math.log(abs(float(line.split()[4])))*math.log(abs(float(line.split()[6])))
		tmp = all
		## if float(line.split()[9]) < 20.:
		## 	continue
		## if float(line.split()[11]) < 20.:
		## 	continue
		## if float(line.split()[-2]) < 250.:
		## 	continue
		tmpSet.add(tmp)
	return tmpSet
	

def getCorrelations2(s1, s2):
	n1, n2 = len(s1), len(s2)
	inboth = s1.intersection(s2)
	print '--------------------------'
	print 'I have two sets here with lengths:', n1, '(set 1), and', n2, '(set 2)'
	print 'there are %d events in both sets' %( len(inboth) )
	ins1 = s1.difference(s2)
	ins2 = s2.difference(s1)
	## print 'in highpt but not lowpt:', ins1
	## print 'in lowpt but not hight:', ins2


set1  = fillSet('list3lb.txt')
set2  = fillSet('SR00_withveto.list')

getCorrelations2(set1, set2)
