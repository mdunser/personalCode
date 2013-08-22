#! /usr/bin/python
import commands, sys, math

args = sys.argv

list1 = args[1]
list2 = args[2]

verbose = False
if args[-1] in ['-v', 'verbose']:
	verbose=True

def fillSet(f):
	tmpFile = open(f,'r')
	tmpSet = set()
	for line in tmpFile.readlines():
		run = line.split(':')[0]
		ls  = line.split(':')[1]
		evn = line.split(':')[2]
		all = run+':'+ls+':'+evn
		tmp = all
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
	print 'There are', len(ins1),'events in list 1 and not in list 2'
	if verbose:
		print 'It\'s these events:'
		print '==================='
		print ins1
	print 'There are', len(ins2),'events in list 2 and not in list 1'
	if verbose:
		print 'It\'s these events:'
		print '==================='
		print ins2
	if verbose:
		print 'These events are in both sets:'
		print '==================='
		print inboth
	


set1  = fillSet(list1)
set2  = fillSet(list2)

getCorrelations2(set1, set2)
