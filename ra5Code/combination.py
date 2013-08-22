#! /usr/bin/python
### #! /bin/env python
import sys, commands, math, ROOT, helper, copy, tables
from numpy import matrix
from collections import defaultdict
from myround import myround

args = sys.argv
print args

group1 = 'UCSx'
group2 = 'UFL'
group3 = 'ETH/Oviedo'

specialRegions = ['SR00', 'SR10', 'SR20', 'SR30', 'SR31', 'SR34', 'SR35']

includeSyst = 1

do3rdVeto = 0

def error():
	print 'something went wrong, please check the dictionaries..'
	print 'exiting...'
	sys.exit(1)

def quadSum(a,b):
	return math.sqrt(a*a + b*b)

def blue2(d1, d2):
	##
	if d1['f'] == 0.:
		return d2['f'], d2['fstat']
	if d2['f'] == 0.:
		return d1['f'], d1['fstat']
	## make the matrix
	M = matrix([ [     d1['fstat']*d1['fstat'] , r12*d1['fstat']*d2['fstat'] ] ,
	             [ r12*d2['fstat']*d1['fstat'] ,     d2['fstat']*d2['fstat'] ] ])
	Minv = M.I ## inverse of the matrix
	global m 
	m = Minv
	norm = Minv.sum() ## normalization value
	c  = [ Minv[0].sum()/norm, Minv[1].sum()/norm ]## normalization coefficients
	sigmSq  = 0 ## squared sigma
	central = c[0]*d1['f'] + c[1]*d2['f']
	print '-------------------------'
	print 'c_0: %.2f c_1: %.2f' %(c[0], c[1])
	print 'central values: %.2f %.2f' %(d1['f'], d2['f'])
	print 'error   values: %.2f %.2f' %(d1['fstat'], d2['fstat'])
	err0sq = d1['fstat']*d1['fstat']
	err1sq = d2['fstat']*d2['fstat']
	print 'foobar 1: %.2f 2: %.2f' %(1/((err0sq  *(1./err0sq+1./err1sq) )),1/((err1sq  *(1./err0sq+1./err1sq) )) )
	## calculate the squared sigma
	for i in range(len(Minv)):
		for j in range(len(Minv)):
			##sigmSq += Minv[i,j]*c[i]*c[j] ## are we sure this is correct?
			sigmSq += M[i,j]*c[i]*c[j] ## are we sure this is correct?
	if not sigmSq: error()
	print 'error %.2f and from blue: %.2f' %(1/math.sqrt(1./err0sq+1./err1sq) , math.sqrt(sigmSq))
	return central, math.sqrt(sigmSq)

def blue(d1, d2, d3):
	## make the matrix
	if not includeSyst:
		M = matrix([ [     d1['fstat']*d1['fstat'] , r12*d1['fstat']*d2['fstat'] , r13*d1['fstat']*d3['fstat'] ] ,
		             [ r21*d2['fstat']*d1['fstat'] ,     d2['fstat']*d2['fstat'] , r23*d2['fstat']*d3['fstat'] ] ,
		             [ r31*d3['fstat']*d1['fstat'] , r32*d3['fstat']*d2['fstat'] ,     d3['fstat']*d3['fstat'] ] ])
	else:
		
		d1['ftot'] = math.sqrt(d1['fstat']*d1['fstat'] + 0.25*d1['f']*d1['f'])
		d2['ftot'] = math.sqrt(d2['fstat']*d2['fstat'] + 0.25*d2['f']*d2['f'])
		d3['ftot'] = math.sqrt(d3['fstat']*d3['fstat'] + 0.25*d3['f']*d3['f'])

		## 100% correlated systematics:
		m11 =     d1['fstat']*d1['fstat'] +    0.25*d1['f']*d1['f']
		m22 =     d2['fstat']*d2['fstat'] +    0.25*d2['f']*d2['f']
		m33 =     d3['fstat']*d3['fstat'] +    0.25*d3['f']*d3['f']
		m12 = r12*d1['fstat']*d2['fstat'] +0.5*0.25*d1['f']*d2['f']
		m13 = r13*d1['fstat']*d3['fstat'] +0.5*0.25*d1['f']*d3['f']
		m23 = r23*d2['fstat']*d3['fstat'] +0.5*0.25*d2['f']*d3['f']
		m21 = m12
		m31 = m13
		m32 = m23
		
		## ## use the correlation factors for stat+syst
		## m11 =     d1['ftot']*d1['ftot']
		## m22 =     d2['ftot']*d2['ftot']
		## m33 =     d3['ftot']*d3['ftot']
		## m12 = r12*d1['ftot']*d2['ftot']
		## m13 = r13*d1['ftot']*d3['ftot']
		## m23 = r23*d2['ftot']*d3['ftot']
		## m21 = m12
		## m31 = m13
		## m32 = m23

		## ## whatever lesya says
		## m11 =     d1['fstat']*d1['fstat'] +    0.25*d1['f']*d1['f']
		## m22 =     d2['fstat']*d2['fstat'] +    0.25*d2['f']*d2['f']
		## m33 =     d3['fstat']*d3['fstat'] +    0.25*d3['f']*d3['f']
		## m12 = r12*d1['ftot']*d2['ftot']
		## m13 = r13*d1['ftot']*d3['ftot']
		## m23 = r23*d2['ftot']*d3['ftot']
		## m21 = m12
		## m31 = m13
		## m32 = m23
		
		M = matrix([ [  m11, m12, m13] ,
		             [  m21, m22, m23] ,
		             [  m31, m32, m33] ])
	Minv = M.I ## inverse of the matrix
	global m 
	m = Minv
	norm = Minv.sum() ## normalization value
	c  = [ Minv[0].sum()/norm, Minv[1].sum()/norm, Minv[2].sum()/norm ]## normalization coefficients
	sigmSq  = 0 ## squared sigma
	central = c[0]*d1['f'] + c[1]*d2['f'] + c[2]*d3['f']
	## print '-------------------------'
	if not includeSyst:
		print 'central values: %.2f %.2f %.2f' % (d1['f'], d2['f'], d3['f'])
		print 'error   values: %.2f %.2f %.2f' % (d1['fstat'], d2['fstat'], d3['fstat'])
		print 'c_0 c_1 c_2   : %.2f %.2f %.2f' % (c[0], c[1], c[2])
		err0sq = d1['fstat']*d1['fstat']
		err1sq = d2['fstat']*d2['fstat']
		err2sq = d3['fstat']*d3['fstat']
	else:
		print 'central values: %.2f %.2f %.2f' % (d1['f'], d2['f'], d3['f'])
		print 'error   values: %.2f %.2f %.2f' % (d1['ftot'], d2['ftot'], d3['ftot'])
		print 'c_0 c_1 c_2   : %.2f %.2f %.2f' % (c[0], c[1], c[2])
		err0sq = d1['ftot']*d1['ftot']
		err1sq = d2['ftot']*d2['ftot']
		err2sq = d3['ftot']*d3['ftot']
	## print 'foobar 1: %.2f 2: %.2f 3: %.2f' %(1/((err0sq  *(1./err0sq+1./err1sq+1./err2sq) )),1/((err1sq  *(1./err0sq+1./err1sq+1./err2sq) )), 1/((err2sq  *(1./err0sq+1./err1sq+1./err2sq) )) )
	## calculate the squared sigma
	for i in range(len(Minv)):
		for j in range(len(Minv)):
			##sigmSq += Minv[i,j]*c[i]*c[j] ## are we sure this is correct?
			sigmSq += M[i,j]*c[i]*c[j]
	if not sigmSq: error()
	print 'error %.2f and from blue: %.2f' %(1/math.sqrt(1./err0sq+1./err1sq+1./err2sq) , math.sqrt(sigmSq))
	return central, math.sqrt(sigmSq)#*central

def weightedMean(d1, d2, d3):
	res = {}
	rel1, rel2, rel3 = d1['fstat']/d1['f'], d2['fstat']/d2['f'], d3['fstat']/d3['f']
	central = (rel1*d1['f'] + rel2*d2['f'] + rel3*d3['f'])/(rel1 + rel2 + rel3)
	error = central*(rel1 + rel2 + rel3)/3
	return central, error

def weightedMean2(d1, d2):
	##
	if d1['f'] == 0.:
		return d2['f'], d2['fstat']
	if d2['f'] == 0.:
		return d1['f'], d1['fstat']
	##
	res = {}
	rel1, rel2 = d1['fstat']/d1['f'], d2['fstat']/d2['f']
	central = (rel1*d1['f'] + rel2*d2['f'])/(rel1 + rel2)
	error = central*(rel1 + rel2)/2
	return central, error

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetLabelSize(0.045, 'X')

ROOT.gROOT.SetBatch()

def makeSomePlots(blue, weighted, average, dirlist, hilo='highpt'):
	srs = dirlist[0].keys()
	srs.sort()
	histos = {}
	ngroups = len(dirlist)
	nbins = ngroups+4
	for sr in srs:
		if sr is 'name': continue
		if sr in ['SR00', 'SR10', 'SR20', 'SR30', 'SR31', 'SR34', 'SR35']: continue
		histo = ROOT.TH1D('results'+sr, 'results'+sr, nbins , 0, nbins)
		for dir in dirlist:
			i = dirlist.index(dir)
			histo.SetBinContent (i+1, dir[sr]['f'])
			histo.SetBinError   (i+1, dir[sr]['fstat'])
			histo.GetXaxis().SetBinLabel(i+1, dir['name'])
		histo.SetBinContent (ngroups+1, 0.) ## empty bin in the middle
		histo.GetXaxis().SetBinLabel(ngroups+1, '')
		histo.SetBinContent (ngroups+2, average[sr]['f'])
		histo.SetBinError   (ngroups+2, average[sr]['fstat'])
		histo.GetXaxis().SetBinLabel(ngroups+2, 'average')
		histo.SetBinContent (ngroups+3, weighted[sr]['f'])
		histo.SetBinError   (ngroups+3, weighted[sr]['fstat'])
		histo.GetXaxis().SetBinLabel(ngroups+3, 'weighted')
		histo.SetBinContent (ngroups+4, blue[sr]['f'])
		histo.SetBinError   (ngroups+4, blue[sr]['fstat'])
		histo.GetXaxis().SetBinLabel(ngroups+4, 'BLUE')
		histo.Draw('hist e')
		histo.GetYaxis().SetRangeUser(0., 1.3*max(dirlist[0][sr]['f']+dirlist[0][sr]['fstat'], dirlist[1][sr]['f']+dirlist[1][sr]['fstat']))
		histo.GetYaxis().SetTitle('prediction')
		histo.SetTitle(sr)
		histos[sr] = copy.deepcopy(histo)
	for i in ['0', '1', '2']:
		canv = ROOT.TCanvas('foobar0', 'foobar0', 600, 900)
		canv.Divide(2,4)
		for sr, histo in histos.items():
			if not sr[2] is i: continue
			canv.cd(int(sr[3]))
			histo.Draw('hist e')
		if do3rdVeto:
			plotdir = 'plots_3rdVeto'
		else:
			plotdir = 'plots'
		canv.SaveAs(plotdir+'/'+'SR'+i+'_fakeComparison_'+hilo+'.pdf')
	
def makeComparison(dirlist, combres, bkg ='r', hilo = 'high'):
	srs = dirlist[0].keys()
	##canv = ROOT.TCanvas('foobar', 'foobar', 550, 500)
	if bkg is 'r': typ='rare'
	if bkg is 'c': typ='flip'
	if bkg is 'f': typ='fakes'
	if bkg is 'total': typ='total'
	histos = {}
	ngroups = len(dirlist)
	nbins   = ngroups+2
	for sr in srs:
		if sr in ['SR00', 'SR10', 'SR20', 'SR30', 'SR31', 'SR34', 'SR35']: continue
		if sr is 'name': continue
		avg = sum(i[sr][bkg] for i in dirlist)/len(dirlist)
		histo = ROOT.TH1D('results'+sr, 'results'+sr, nbins, 0, nbins)
		for i in range(ngroups):
			histo.SetBinContent (i+1, dirlist[i][sr][bkg])
			histo.SetBinError   (i+1, dirlist[i][sr][bkg+'erro'])
			histo.GetXaxis().SetBinLabel(i+1, dirlist[i]['name'])
		histo.SetBinContent (ngroups+1, 0.) ## empty bin in the middle
		histo.SetBinContent (ngroups+2, combres[sr][bkg])
		histo.SetBinError   (ngroups+2, combres[sr][bkg+'erro'])
		histo.Draw('hist e')
		## histo.DrawCopy('0 E2 same')
		histo.GetXaxis().SetBinLabel(ngroups+1, '')
		histo.GetXaxis().SetBinLabel(ngroups+2, 'combined')
		histo.GetYaxis().SetRangeUser(0., 1.5*max(dirlist[0][sr][bkg]+ dirlist[0][sr][bkg+'erro'], dirlist[1][sr][bkg]))
		histo.SetTitle(sr)
		histo.GetYaxis().SetTitle(typ)
		histo.GetYaxis().SetTitle(typ)
		histos[sr] = copy.deepcopy(histo)
	for i in ['0', '1', '2']:
		canv = ROOT.TCanvas('foobar0', 'foobar0', 600, 900)
		canv.Divide(2,4)
		for sr, histo in histos.items():
			if not sr[2] is i: continue
			canv.cd(int(sr[3]))
			histo.Draw('hist e')
		if do3rdVeto:
			plotdir = 'plots_3rdVeto'
		else:
			plotdir = 'plots'
		canv.SaveAs(plotdir+'/'+'SR'+i+'_'+hilo+'_'+typ+'Comparison.pdf')
	

## def combine(d1, d2, d3, method='avg', n=3):
def combine(dirlist, method='avg'):
	n = len(dirlist)
	res = {}
	## res = defaultdict(float)
	for dir in dirlist:
		addTotalError(dir)
		srs = dir.keys()
	refdir = dirlist[0]
	srs.sort()
	for sr in srs:
		if sr is 'name': continue
		## should work now... if sr in ['SR00', 'SR10', 'SR20', 'SR30', 'SR31', 'SR34', 'SR35']: continue
		## now move on to do the single errors
		res[sr] = {}
		## observed number of events
		res[sr]['o'] = refdir[sr]['o']
		## do the rare calculation
		res[sr]['r']     = refdir[sr]['r']    
		res[sr]['rstat'] = refdir[sr]['rstat']
		res[sr]['rsyst'] = refdir[sr]['rsyst']
		res[sr]['rerro'] = quadSum(refdir[sr]['rstat'], refdir[sr]['rsyst'])
		## do the charge flips
		res[sr]['c']     = sum(i[sr]['c'] for i in dirlist)/len(dirlist)
		res[sr]['cstat'] = max(i[sr]['cstat'] for i in dirlist)
		res[sr]['csyst'] = 0.3*res[sr]['c']
		res[sr]['cerro'] = quadSum(res[sr]['cstat'], res[sr]['csyst'])
		## do the fakes
		if method == 'blue':
			print '----- ', sr,' -----'
			if n==3 and sr in specialRegions:
				blueres = blue2(dirlist[0][sr], dirlist[2][sr])
			else:
				if (n==3): blueres = blue (dirlist[0][sr], dirlist[1][sr], dirlist[2][sr])
				if (n==2): blueres = blue2(dirlist[0][sr], dirlist[1][sr])
			res[sr]['f']     = blueres[0]
			res[sr]['fstat'] = blueres[1]
			res[sr]['fsyst'] = 0.5*res[sr]['f']
			if not includeSyst:
				res[sr]['ferro'] = quadSum(blueres[1], 0.5*res[sr]['f'])
			else:
				res[sr]['ferro'] = blueres[1]
		elif method =='avg':
			if n==3 and sr in specialRegions:
				res[sr]['f'] = (dirlist[0][sr]['f']+dirlist[2][sr]['f'])/2.
			else:
				res[sr]['f']     = sum(i[sr]['f'] for i in dirlist)/len(dirlist)
			res[sr]['fstat'] = max(i[sr]['fstat'] for i in dirlist)
			res[sr]['fsyst'] = 0.5*res[sr]['f']
			res[sr]['ferro'] = quadSum(res[sr]['fstat'], res[sr]['fsyst'])
		elif method == 'weight':
			if n==3 and sr in specialRegions:
				weightres = weightedMean2(dirlist[0][sr], dirlist[2][sr])
			else:
				if (n==3): weightres = weightedMean (dirlist[0][sr], dirlist[1][sr], dirlist[2][sr])
				if (n==2): weightres = weightedMean2(dirlist[0][sr], dirlist[1][sr])
			res[sr]['f'] = weightres[0]
			res[sr]['fstat'] = weightres[1]
			res[sr]['fsyst'] = 0.5*res[sr]['f']
			res[sr]['ferro'] = quadSum(res[sr]['fstat'], res[sr]['fsyst'])
	return res

def addTotalError(dir, isBlue = False):
	srs = dir.keys()
	for sr in srs:
		if sr is 'name': continue
		## if sr in ['o2x', 'f2x', 'r2x', 'c2x']: continue
		totbkg = dir[sr]['f']+dir[sr]['r']+dir[sr]['c']
		if isBlue and includeSyst:
			fakerr = dir[sr]['ferro']
		else:
			fakerr = quadSum(dir[sr]['fsyst'], dir[sr]['fstat'])
		rarerr = quadSum(dir[sr]['rsyst'], dir[sr]['rstat'])
		## chaerr = quadSum(dir[sr]['csyst'], dir[sr]['cstat'])
		chaerr = quadSum(0.3*dir[sr]['c'], dir[sr]['cstat']) ## temporary
		toterr = math.sqrt(fakerr*fakerr + rarerr*rarerr + chaerr*chaerr)
		dir[sr]['ferro'] = fakerr
		dir[sr]['rerro'] = rarerr
		dir[sr]['cerro'] = chaerr
		dir[sr]['total'] = totbkg
		dir[sr]['totalerro'] = toterr
		dir[sr]['t']  = myround(totbkg, toterr)[0]
		dir[sr]['te'] = myround(totbkg, toterr)[1]
		dir[sr]['fn'] = myround(dir[sr]['f'],fakerr)[0]
		dir[sr]['fe'] = myround(dir[sr]['f'],fakerr)[1]
		dir[sr]['cn'] = myround(dir[sr]['c'],chaerr)[0]
		dir[sr]['ce'] = myround(dir[sr]['c'],chaerr)[1]
		dir[sr]['rn'] = myround(dir[sr]['r'],rarerr)[0]
		dir[sr]['re'] = myround(dir[sr]['r'],rarerr)[1]
		## dir[sr]['t']  = str(round(totbkg,2))
		## dir[sr]['te'] = str(round(toterr,2))
		## dir[sr]['fn'] = str(round(dir[sr]['f'],2))
		## dir[sr]['cn'] = str(round(dir[sr]['c'],2))
		## dir[sr]['rn'] = str(round(dir[sr]['r'],2))
		## dir[sr]['fe'] = str(round(fakerr,2))
		## dir[sr]['ce'] = str(round(chaerr,2))
		## dir[sr]['re'] = str(round(rarerr,2))

def make2x(dir):
	fakes2x = 0.
	faerr2x = 0.
	rares2x = 0.
	raerr2x = 0.
	flips2x = 0.
	flerr2x = 0.
	obs2x = 0
	for sr in ['SR21', 'SR22', 'SR23', 'SR24', 'SR25', 'SR26', 'SR27', 'SR28']:
		obs2x   += dir[sr]['o']
		fakes2x += dir[sr]['f']
		rares2x += dir[sr]['r']
		flips2x += dir[sr]['c']
		faerr2x += dir[sr]['fstat']
		raerr2x += dir[sr]['rstat']
		flerr2x += dir[sr]['cstat']
	dir['o2x'] = obs2x
	dir['f2x'] = fakes2x
	dir['r2x'] = rares2x
	dir['c2x'] = flips2x
	dir['fe2x'] = quadSum(0.5*fakes2x, faerr2x)
	dir['re2x'] = quadSum(0.5*rares2x, raerr2x)
	dir['ce2x'] = quadSum(0.3*flips2x, flerr2x)
	dir['to2x'] = fakes2x+rares2x+flips2x
	dir['te2x'] = math.sqrt(dir['fe2x']*dir['fe2x'] + dir['re2x']*dir['re2x'] + dir['ce2x']*dir['ce2x'])

		
def makeInput(res, hilo='highpt'):
	if do3rdVeto:
		plotdir = 'plots_3rdVeto'
	else:
		plotdir = 'plots'
	f = open(plotdir+'/predictionsYields_'+hilo+'.txt', 'w')
	srs = res.keys()
	srs.sort()
	for sr in srs:
		if sr is 'name': continue
		f.writelines('%s\t\t%d\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\n' 
			%(sr.lstrip('SR'), 
			res[sr]['o'], 
			res[sr]['total'], res[sr]['totalerro'],
			res[sr]['f'], res[sr]['ferro'], 
			res[sr]['r'], res[sr]['rerro'], 
			res[sr]['c'], res[sr]['cerro'] ) )
	f.close()



def makeNicePlots(res, dirlist, nb, hilo='high'):
	regions0 = ['SR01', 'SR02', 'SR03', 'SR04', 'SR05', 'SR06','SR07', 'SR08']
	regions1 = ['SR11', 'SR12', 'SR13', 'SR14', 'SR15', 'SR16','SR17', 'SR18']
	regions2 = ['SR21', 'SR22', 'SR23', 'SR24', 'SR25', 'SR26','SR27', 'SR28']
	if nb == 0: regions = regions0
	if nb == 1: regions = regions1
	if nb == 2: regions = regions2
	global canv
	fourThree = True
	if fourThree:
		ROOT.gStyle.SetPadRightMargin(0.03)
		##ROOT.gStyle.SetPadTopMargin(0.02)
		##ROOT.gStyle.SetPadBottomMargin(0.18)
		##ROOT.gStyle.SetPadLeftMargin(0.14)
		##ROOT.gStyle.SetPadRightMargin(0.05)
		canv = ROOT.TCanvas('foobar', 'foobar', 900, 675)
	else: 
		canv = ROOT.TCanvas('foobar', 'foobar', 900, 500)
	global r_h, f_h, c_h, t_h, a_s, o_h
	r_h = ROOT.TH1D('r', 'r', 8, 0, 8)
	c_h = ROOT.TH1D('c', 'c', 8, 0, 8)
	f_h = ROOT.TH1D('f', 'f', 8, 0, 8)
	o_h = ROOT.TH1D('o', 'o', 8, 0, 8)
	t_h = ROOT.TH1D('t', 't', 8, 0, 8)
	if (nb == 0): nstr = '0'
	if (nb == 1): nstr = '1'
	if (nb == 2): nstr = '#geq 2'
	if (hilo=='high'): a_s = ROOT.THStack('a', 'high-p_{T} signal regions with '+nstr+' b-tags')
	if (hilo=='low' ): a_s = ROOT.THStack('a', 'low-p_{T} signal regions with '+nstr+' b-tags')
	## some cosmetics. this should really be somewhere else...
	## fakecolor = 50
	## flipcolor = 42
	## rarecolor = 31
	mycolor1 = ROOT.TColor()
	mycolor2 = ROOT.TColor()
	mycolor3 = ROOT.TColor()
	colorText = 'blueRedYellow'
	fakecolor = mycolor2.GetColor(51, 102, 153)
	flipcolor = mycolor1.GetColor(102, 0, 0)
	rarecolor = mycolor3.GetColor(255, 204, 0)
	o_h.SetMarkerColor(ROOT.kBlack)
	o_h.SetMarkerStyle(20)
	o_h.SetMarkerSize(1.2)
	o_h.SetLineWidth(2)
	o_h.SetLineColor(ROOT.kBlack)
	o_h.SetFillColor(ROOT.kBlack)
	f_h.SetLineWidth(1)
	f_h.SetLineColor(ROOT.kBlack)
	f_h.SetFillColor(fakecolor)
	c_h.SetLineWidth(1)
	c_h.SetLineColor(ROOT.kBlack)
	c_h.SetFillColor(flipcolor)
	r_h.SetLineWidth(1)
	r_h.SetLineColor(ROOT.kBlack)
	r_h.SetFillColor(rarecolor)
	t_h.SetLineWidth(1)
	t_h.SetFillColor(12)
	t_h.SetFillStyle(3005)
	## t_h.SetFillStyle(3005)
	## end cosmetics
	for reg in regions:
		r,c,f,o  = res[reg]['r'], res[reg]['c'], res[reg]['f'], res[reg]['o']
		print r,c,f,o
		toterr = res[reg]['totalerro'] ##math.sqrt(quadSum(res[reg]['ferro'], 0.5*f)**2 + quadSum(res[reg]['rerro'], 0.5*r)**2 + quadSum(res[reg]['cerro'], 0.3*c)**2 )
		r_h.SetBinContent(regions.index(reg)+1, r)
		c_h.SetBinContent(regions.index(reg)+1, c)
		f_h.SetBinContent(regions.index(reg)+1, f)
		o_h.SetBinContent(regions.index(reg)+1, o)
		o_h.SetBinError  (regions.index(reg)+1, math.sqrt(o))
		t_h.SetBinContent(regions.index(reg)+1, r+c+f)
		t_h.SetBinError  (regions.index(reg)+1, toterr)
		r_h.GetXaxis().SetBinLabel  (regions.index(reg)+1, reg)
	o_e = helper.getErrorHist(o_h)
	o_e.SetMarkerColor(ROOT.kBlack)
	o_e.SetMarkerStyle(20)
	o_e.SetMarkerSize(1.2)
	
	a_s.Add(f_h)
	a_s.Add(c_h)
	a_s.Add(r_h)
	a_s.Draw('goff')
	mx = 0.
	for i in range(1,8):
		mx = max(mx, max(t_h.GetBinContent(i)+t_h.GetBinError(i), o_h.GetBinContent(i)+o_h.GetBinError(i)))
	if fourThree: ymaxfactor = 1.15
	else:         ymaxfactor = 1.1
	if hilo == 'high': ymaxfactor = 1.05
	##a_s.SetMaximum(ymaxfactor*mx)
	if nb ==0: 
		a_s.SetMaximum(73.)
	if nb ==1: 
		a_s.SetMaximum(53.)
	if nb ==2: 
		a_s.SetMaximum(18.)
	##else:  a_s.SetMaximum(15.)
	for reg in regions:
		a_s.GetXaxis().SetBinLabel  (regions.index(reg)+1, reg)
	if fourThree: xlabelsize = 0.07
	else:         xlabelsize = 0.08
	a_s.GetXaxis().SetLabelSize(xlabelsize)
	a_s.GetXaxis().SetTitleSize(0.08)

	if fourThree: ytitleoffset = 0.65
	else:         ytitleoffset = 0.55
	a_s.GetYaxis().SetTitleOffset(ytitleoffset)
	a_s.GetYaxis().SetTitleSize(0.07)
	a_s.GetYaxis().SetLabelSize(0.06)
	a_s.GetYaxis().SetTitle('Events / bin')
	ROOT.gStyle.SetOptTitle(0)
	a_s.Draw('hist')
	nmulti = 'b-tags'
	if nstr == '1':
		nmulti = 'b-tag'
	if fourThree: x1cap, y1cap, sizecap, fontcap =  0.350, 0.85, 0.05, 62
	else:         x1cap, y1cap, sizecap, fontcap =  0.455, 0.82, 0.05, 62
	if (hilo=='high'): 
		helper.drawLatex('High-p_{T} signal regions with '+nstr+' '+nmulti, x1cap, y1cap, sizecap, fontcap)
	if (hilo=='low' ):
		helper.drawLatex('Low-p_{T} signal regions with '+nstr+' '+nmulti, x1cap, y1cap, sizecap, fontcap)
	## ## here's the color text
	## helper.drawLatex(colorText, 0.25, 0.75)
	t_h.SetMarkerColor(rarecolor)
	t_h.DrawCopy('0 E2 same')
	t_h.SetFillColor(12)
	t_h.SetLineColor(12)
	if fourThree: o_e.SetLineWidth(2)
	if fourThree: o_e.SetMarkerSize(1.5)
	o_e.Draw('P same')
	if fourThree: x1leg, y1leg, x2leg,y2leg = 0.54, 0.50, 0.75, 0.80
	else:         x1leg, y1leg, x2leg,y2leg = 0.56, 0.45, 0.75, 0.75
	leg = helper.makeLegend(x1leg, y1leg, x2leg,y2leg)
	leg.SetBorderSize(0)
	leg.SetTextSize(0.05)
	leg.SetTextFont(42)
	leg.AddEntry(o_e, 'Data' , 'pe')
	leg.AddEntry(r_h, 'Rare SM processes', 'f')
	leg.AddEntry(c_h, 'Charge misID', 'f')
	leg.AddEntry(f_h, 'Non-prompt #font[12]{e/#mu}', 'f')
	leg.AddEntry(t_h, 'Total bkg uncertainty', 'f')
	leg.Draw('same')
	helper.drawTopLine(19500., 'fb', 1)
	if do3rdVeto:
		plotdir = 'plots_3rdVeto'
	else:
		plotdir = 'plots'
	if (hilo == 'high'): canv.SaveAs(plotdir+'/highptsummary_regions'+str(nb)+'.pdf')
	if (hilo == 'low' ): canv.SaveAs(plotdir+'/lowptsummary_regions'+str(nb)+'.pdf')

def combineAvgres(avgres):
	for reg in avgres.keys():
		avgres[reg]['total']  = avgres[reg]['f'] + avgres[reg]['r'] + avgres[reg]['c']
		avgres[reg]['fsyst']  = 0.5*avgres[reg]['f']
		avgres[reg]['rsyst']  = 0.5*avgres[reg]['r']
		avgres[reg]['csyst']  = 0.3*avgres[reg]['c']
		avgres[reg]['ferro']  = math.sqrt(avgres[reg]['fstat']*avgres[reg]['fstat'] + avgres[reg]['fsyst']*avgres[reg]['fsyst'])
		avgres[reg]['rerro']  = math.sqrt(avgres[reg]['rstat']*avgres[reg]['rstat'] + avgres[reg]['rsyst']*avgres[reg]['rsyst'])
		avgres[reg]['cerro']  = math.sqrt(avgres[reg]['cstat']*avgres[reg]['cstat'] + avgres[reg]['csyst']*avgres[reg]['csyst'])
		avgres[reg]['totalerro'] = math.sqrt(avgres[reg]['ferro']*avgres[reg]['ferro'] + avgres[reg]['rerro']*avgres[reg]['rerro'] + avgres[reg]['cerro']*avgres[reg]['cerro'])

def blueVsAvg(blueres, avgres):
	regions  = ['SR01', 'SR02', 'SR03', 'SR04', 'SR05', 'SR06','SR07', 'SR08',
	            'SR11', 'SR12', 'SR13', 'SR14', 'SR15', 'SR16','SR17', 'SR18',
	            'SR21', 'SR22', 'SR23', 'SR24', 'SR25', 'SR26','SR27', 'SR28']
	histo = ROOT.TH1F('blue/avg', 'blue/avg', 24, 0, 24)
	combineAvgres(avgres)
	totratio = 0.
	for reg in regions:
		ind = regions.index(reg)
		ratio = (avgres[reg]['f'] + avgres[reg]['r'] + avgres[reg]['c'])/blueres[reg]['total']
		histo.Fill(ind, ratio)
		histo.GetXaxis().SetBinLabel(ind+1, reg)
		totratio += ratio
	totratio /= len(regions)
	c = ROOT.TCanvas('foo', 'bar', 900, 675)
	histo.SetTitle('average / BLUE')
	histo.GetYaxis().SetRangeUser(0.9, 1.1)
	histo.Draw('')
	helper.drawLatex('total ratio: %.3f' %(ratio), 0.4, 0.85)
	c.SaveAs('avgDivBlue.pdf')
		
		
	


def makeComparison(dirlist, combres, bkg ='r', hilo = 'high'):
	srs = dirlist[0].keys()
	##canv = ROOT.TCanvas('foobar', 'foobar', 550, 500)
	if bkg is 'r': typ='rare'
	if bkg is 'c': typ='flip'
	if bkg is 'f': typ='fakes'
	if bkg is 'total': typ='total'
	histos = {}
	ngroups = len(dirlist)
	nbins   = ngroups+2
	for sr in srs:
		if sr in ['SR00', 'SR10', 'SR20', 'SR30', 'SR31', 'SR34', 'SR35']: continue
		if sr is 'name': continue
		avg = sum(i[sr][bkg] for i in dirlist)/len(dirlist)
		histo = ROOT.TH1D('results'+sr, 'results'+sr, nbins, 0, nbins)
		for i in range(ngroups):
			histo.SetBinContent (i+1, dirlist[i][sr][bkg])
			histo.SetBinError   (i+1, dirlist[i][sr][bkg+'erro'])
			histo.GetXaxis().SetBinLabel(i+1, dirlist[i]['name'])
		histo.SetBinContent (ngroups+1, 0.) ## empty bin in the middle
		histo.SetBinContent (ngroups+2, combres[sr][bkg])
		histo.SetBinError   (ngroups+2, combres[sr][bkg+'erro'])
		histo.Draw('hist e')
		## histo.DrawCopy('0 E2 same')
		histo.GetXaxis().SetBinLabel(ngroups+1, '')
		histo.GetXaxis().SetBinLabel(ngroups+2, 'combined')
		histo.GetYaxis().SetRangeUser(0., 1.5*max(dirlist[0][sr][bkg]+ dirlist[0][sr][bkg+'erro'], dirlist[1][sr][bkg]))
		histo.SetTitle(sr)
		histo.GetYaxis().SetTitle(typ)
		histo.GetYaxis().SetTitle(typ)
		histos[sr] = copy.deepcopy(histo)
	for i in ['0', '1', '2']:
		canv = ROOT.TCanvas('foobar0', 'foobar0', 600, 900)
		canv.Divide(2,4)
		for sr, histo in histos.items():
			if not sr[2] is i: continue
			canv.cd(int(sr[3]))
			histo.Draw('hist e')
		if do3rdVeto:
			plotdir = 'plots_3rdVeto'
		else:
			plotdir = 'plots'
		canv.SaveAs(plotdir+'/'+'SR'+i+'_'+hilo+'_'+typ+'Comparison.pdf')
	

		
lowpt = False
if 'low' in args:
	lowpt = True
		

if lowpt:
	## THIS SECTION FOR THE LOW-PT ANALYSES
	## ------------------------------------
	ucsdlow = eval(open('ucfnal_signal_lowpt.txt_may26').read())
	ufldlow = eval(open('uf_signal_lowpt.txt_may26').read())
	addTotalError(ucsdlow)
	addTotalError(ufldlow)
	ucsdlow['name'] = 'UC/FNAL'
	ufldlow['name'] = 'UFL'
	
	## correlation factors before tighter d0:
	## r12 = 0.275
	## r21 = 0.275
	
	## correlation factors after tighter d0:
	r12 = 0.276 ## 0.301 for 2b
	r21 = 0.276 ## 0.301 for 2b
	
	blueres = combine([ucsdlow, ufldlow], 'blue'  )
	avgres  = combine([ucsdlow, ufldlow], 'avg'   )
	weighres= combine([ucsdlow, ufldlow], 'weight')
	blueres['name'] = 'combined'
	addTotalError(blueres, 1)

	makeSomePlots(blueres, weighres, avgres, [ucsdlow, ufldlow], 'lowpt') ## needs adaption for low-pt
	makeComparison([ucsdlow, ufldlow], blueres, 'r'    )
	makeComparison([ucsdlow, ufldlow], blueres, 'c'    )
	makeComparison([ucsdlow, ufldlow], blueres, 'total')

	dummy=1
	makeInput(blueres, 'lowpt')
	makeNicePlots(blueres, [ucsdlow, ufldlow, dummy], 0, hilo='low')
	makeNicePlots(blueres, [ucsdlow, ufldlow, dummy], 1, hilo='low')
	makeNicePlots(blueres, [ucsdlow, ufldlow, dummy], 2, hilo='low')

	
	tables.makeTables2([ucsdlow, ufldlow, blueres], do3rdVeto)


else:
	## THIS SECTION FOR THE HIGH-PT ANALYSES
	## -------------------------------------
	if not do3rdVeto:
		## normal files: (i.e. without 3rd lepton veto)
		## ============================================
		ucsd = eval(open('ucfnal_signal_highpt.txt_may26').read())
		ufld = eval(open('uf_signal_highpt.txt_may26').read())
		ethd = eval(open('eth_signalRegions_highpt.txt_may26').read())
	else:
		## with 3rd lepton veto
		## ============================================
		ucsd = eval(open('ucfnal_highpt_3rdveto.txt').read())
		ufld = eval(open('ufl_highpt_3rdveto.txt').read())
		ethd = eval(open('eth_highpt_3rdveto.txt').read())
	addTotalError(ucsd)
	addTotalError(ufld)
	addTotalError(ethd)
	ucsd['name'] = 'UC/FNAL'
	ufld['name'] = 'UFL'
	ethd['name'] = 'ETH/Oviedo'
	
	## correlation factors before tighter d0:
	## r12 = 0.275
	## r21 = 0.275
	## r13 = 0.398
	## r31 = 0.398
	## r23 = 0.488
	## r32 = 0.488
	
	## correlation factors before tighter d0:
	r12 = 0.277 ## for b's 0.290
	r21 = 0.277 ## for b's 0.290
	r13 = 0.529 ## for b's 0.493
	r31 = 0.529 ## for b's 0.493
	r23 = 0.277 ## for b's 0.381
	r32 = 0.377 ## for b's 0.381
	
	blueres = combine([ucsd, ufld, ethd], 'blue')
	avgres  = combine([ucsd, ufld, ethd], 'avg' )
	weighres= combine([ucsd, ufld, ethd], 'weight')
	blueres['name'] = 'combined'
	addTotalError(blueres, 1)
	
	## makeSomePlots(blueres, weighres, avgres, [ucsd, ufld, ethd])
	## makeComparison([ucsd, ufld, ethd], blueres, 'r'    )
	## makeComparison([ucsd, ufld, ethd], blueres, 'c'    )
	## makeComparison([ucsd, ufld, ethd], blueres, 'total')
	
	makeInput(blueres)
	## tables.makeTables([ucsd, ufld, ethd, blueres], do3rdVeto)
	## tables.makeSpecialTables([ucsd, ufld, ethd, blueres], do3rdVeto)
	makeNicePlots(blueres, [ucsd, ufld, ethd], 0)
	makeNicePlots(blueres, [ucsd, ufld, ethd], 1)
	makeNicePlots(blueres, [ucsd, ufld, ethd], 2)

	## helper.calculateBVetoRegions(blueres)
	## helper.makeInputBVeto(blueres, 'highpt_bVeto')
	## make2x(blueres)
	
	## blueVsAvg(blueres, avgres)

