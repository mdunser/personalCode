#! /bin/env python
import sys, commands, math, ROOT, helper, copy, tables
from numpy import matrix

args = sys.argv

group1 = 'UCSx'
group2 = 'UFL'
group3 = 'ETH/Oviedo'

def error():
	print 'something went wrong, please check the dictionaries..'
	print 'exiting...'
	sys.exit(1)

def quadSum(a,b):
	return math.sqrt(a*a + b*b)

def blue2(d1, d2):
	## make the matrix
	M = matrix([ [     d1['ferro']*d1['ferro'] , r12*d1['ferro']*d2['ferro'] ] ,
	             [ r12*d2['ferro']*d1['ferro'] ,     d2['ferro']*d2['ferro'] ] ])
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
	print 'error   values: %.2f %.2f' %(d1['ferro'], d2['ferro'])
	err0sq = d1['ferro']*d1['ferro']
	err1sq = d2['ferro']*d2['ferro']
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
	M = matrix([ [     d1['ferro']*d1['ferro'] , r12*d1['ferro']*d2['ferro'] , r13*d1['ferro']*d3['ferro'] ] ,
	             [ r21*d2['ferro']*d1['ferro'] ,     d2['ferro']*d2['ferro'] , r23*d2['ferro']*d3['ferro'] ] ,
	             [ r31*d3['ferro']*d1['ferro'] , r32*d3['ferro']*d2['ferro'] ,     d3['ferro']*d3['ferro'] ] ])
	Minv = M.I ## inverse of the matrix
	global m 
	m = Minv
	norm = Minv.sum() ## normalization value
	c  = [ Minv[0].sum()/norm, Minv[1].sum()/norm, Minv[2].sum()/norm ]## normalization coefficients
	sigmSq  = 0 ## squared sigma
	central = c[0]*d1['f'] + c[1]*d2['f'] + c[2]*d3['f']
	## print '-------------------------'
	print 'central values: %.2f %.2f %.2f' % (d1['f'], d2['f'], d3['f'])
	print 'error   values: %.2f %.2f %.2f' % (d1['ferro'], d2['ferro'], d3['ferro'])
	print 'c_0 c_1 c_2   : %.2f %.2f %.2f' % (c[0], c[1], c[2])
	err0sq = d1['ferro']*d1['ferro']
	err1sq = d2['ferro']*d2['ferro']
	err2sq = d3['ferro']*d3['ferro']
	## print 'foobar 1: %.2f 2: %.2f 3: %.2f' %(1/((err0sq  *(1./err0sq+1./err1sq+1./err2sq) )),1/((err1sq  *(1./err0sq+1./err1sq+1./err2sq) )), 1/((err2sq  *(1./err0sq+1./err1sq+1./err2sq) )) )
	## calculate the squared sigma
	for i in range(len(Minv)):
		for j in range(len(Minv)):
			##sigmSq += Minv[i,j]*c[i]*c[j] ## are we sure this is correct?
			sigmSq += M[i,j]*c[i]*c[j] ## are we sure this is correct?
	if not sigmSq: error()
	print 'error %.2f and from blue: %.2f' %(1/math.sqrt(1./err0sq+1./err1sq+1./err2sq) , math.sqrt(sigmSq))
	return central, math.sqrt(sigmSq)#*central

def weightedMean(d1, d2, d3):
	res = {}
	rel1, rel2, rel3 = d1['ferro']/d1['f'], d2['ferro']/d2['f'], d3['ferro']/d3['f']
	central = (rel1*d1['f'] + rel2*d2['f'] + rel3*d3['f'])/(rel1 + rel2 + rel3)
	error = central*(rel1 + rel2 + rel3)/3
	return central, error

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetLabelSize(0.045, 'X')

ROOT.gROOT.SetBatch()

def makeSomePlots(blue, weighted, average, d1, d2, d3):
	srs = d1.keys()
	srs.sort()
	histos = {}
	for sr in srs:
		if sr is 'name': continue
		## if sr[2] == '0': canv0.cd(); canv0.cd(int(sr[-1]))
		## if sr[2] == '1': canv0.cd(); canv1.cd(int(sr[-1]))
		## if sr[2] == '2': canv0.cd(); canv2.cd(int(sr[-1]))
		histo = ROOT.TH1D('results'+sr, 'results'+sr, 7 , 0, 7)
		histo.SetBinContent (1, d1[sr]['f'])
		histo.SetBinError   (1, d1[sr]['ferro'])
		histo.SetBinContent (2, d2[sr]['f'])
		histo.SetBinError   (2, d2[sr]['ferro'])
		histo.SetBinContent (3, d3[sr]['f'])
		histo.SetBinError   (3, d3[sr]['ferro'])
		histo.SetBinContent (4, 0.) ## empty bin in the middle
		histo.SetBinContent (5, average[sr]['f'])
		histo.SetBinError   (5, average[sr]['ferro'])
		histo.SetBinContent (6, weighted[sr]['f'])
		histo.SetBinError   (6, weighted[sr]['ferro'])
		histo.SetBinContent (7, blue[sr]['f'])
		histo.SetBinError   (7, blue[sr]['ferro'])
		histo.Draw('hist e')
		## histo.DrawCopy('0 E2 same')
		histo.GetXaxis().SetBinLabel(1, group1)
		histo.GetXaxis().SetBinLabel(2, group2)
		histo.GetXaxis().SetBinLabel(3, group3)
		histo.GetXaxis().SetBinLabel(4, '')
		histo.GetXaxis().SetBinLabel(5, 'average')
		histo.GetXaxis().SetBinLabel(6, 'weighted')
		histo.GetXaxis().SetBinLabel(7, 'BLUE')
		histo.GetYaxis().SetRangeUser(0., 1.2*max(d1[sr]['f']+d1[sr]['ferro'], max(d2[sr]['f']+d2[sr]['ferro'], d3[sr]['f']+d3[sr]['ferro'])))
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
		canv.SaveAs('plots/'+'SR'+i+'_fakeComparison.pdf')
		
def makeFlipComparison(d1, d2, d3, hilo = 'high'):
	srs = d1.keys()
	histos = {}
	##canv = ROOT.TCanvas('foobar', 'foobar', 550, 500)
	ngroups = 3
	if (hilo == 'low'): ngroups = 2
	for sr in srs:
		if sr is 'name': continue
		avg = ( d1[sr]['c'] + d2[sr]['c'] + d3[sr]['c'] ) / ngroups
		if (hilo == 'low'): 
			avg = ( d1[sr]['c'] + d2[sr]['c']) / ngroups
		histo = ROOT.TH1D('results'+sr, 'results'+sr, ngroups+2 , 0, ngroups+2)
		histo.SetBinContent (1, d1[sr]['c'])
		histo.SetBinError   (1, d1[sr]['cerro'])
		histo.SetBinContent (2, d2[sr]['c'])
		histo.SetBinError   (2, d2[sr]['cerro'])
		if ngroups == 3:
			histo.SetBinContent (3, d3[sr]['c'])
			histo.SetBinError   (3, d3[sr]['cerro'])
		histo.SetBinContent (ngroups+1, 0.) ## empty bin in the middle
		histo.SetBinContent (ngroups+2, avg)
		histo.SetBinError   (ngroups+2, 0.5*avg)
		histo.Draw('hist e')
		## histo.DrawCopy('0 E2 same')
		histo.GetXaxis().SetBinLabel(1, group1)
		histo.GetXaxis().SetBinLabel(2, group2)
		if ngroups == 3: histo.GetXaxis().SetBinLabel(3, group3)
		histo.GetXaxis().SetBinLabel(ngroups+1, '')
		histo.GetXaxis().SetBinLabel(ngroups+2, 'average')
		histo.GetYaxis().SetRangeUser(0., 1.2*max(d1[sr]['c']+d1[sr]['cerro'], d2[sr]['c']+d2[sr]['cerro']))
		histo.GetYaxis().SetTitle('flips')
		histo.SetTitle(sr)
		histos[sr] = copy.deepcopy(histo)
		## canv.SaveAs('plots/'+sr+'_flips.pdf')
	
def makeComparison(d1, d2, d3, bkg ='r', hilo = 'high'):
	srs = d1.keys()
	##canv = ROOT.TCanvas('foobar', 'foobar', 550, 500)
	if bkg is 'r': typ='rare'
	if bkg is 'c': typ='flip'
	histos = {}
	ngroups = 3
	if (hilo == 'low'): ngroups = 2
	for sr in srs:
		if sr is 'name': continue
		avg = ( d1[sr][bkg] + d2[sr][bkg] + d3[sr][bkg] ) / ngroups
		if (hilo == 'low'): 
			avg = ( d1[sr][bkg] + d2[sr][bkg]) / ngroups
		histo = ROOT.TH1D('results'+sr, 'results'+sr, ngroups+2 , 0, ngroups+2)
		histo.SetBinContent (1, d1[sr][bkg])
		histo.SetBinError   (1, d1[sr][bkg+'erro'])
		histo.SetBinContent (2, d2[sr][bkg])
		histo.SetBinError   (2, d2[sr][bkg+'erro'])
		if ngroups == 3:
			histo.SetBinContent (3, d3[sr][bkg])
			histo.SetBinError   (3, d3[sr][bkg+'erro'])
		histo.SetBinContent (ngroups+1, 0.) ## empty bin in the middle
		histo.SetBinContent (ngroups+2, avg)
		histo.SetBinError   (ngroups+2, 0.5*avg)
		histo.Draw('hist e')
		## histo.DrawCopy('0 E2 same')
		histo.GetXaxis().SetBinLabel(1, group1)
		histo.GetXaxis().SetBinLabel(2, group2)
		if ngroups == 3: histo.GetXaxis().SetBinLabel(3, group3)
		histo.GetXaxis().SetBinLabel(ngroups+1, '')
		histo.GetXaxis().SetBinLabel(ngroups+2, 'average')
		histo.GetYaxis().SetRangeUser(0., 1.5*max(d1[sr][bkg]+ d1[sr][bkg+'erro'], d2[sr][bkg]))
		histo.SetTitle(sr)
		if bkg == 'r': histo.GetYaxis().SetTitle('rares')
		if bkg == 'c': histo.GetYaxis().SetTitle('flips')
		histos[sr] = copy.deepcopy(histo)
	for i in ['0', '1', '2']:
		canv = ROOT.TCanvas('foobar0', 'foobar0', 600, 900)
		canv.Divide(2,4)
		for sr, histo in histos.items():
			if not sr[2] is i: continue
			canv.cd(int(sr[3]))
			histo.Draw('hist e')
		canv.SaveAs('plots/'+'SR'+i+'_'+hilo+'_'+typ+'Comparison.pdf')
	

def combine(d1, d2, d3, method='avg', n=3):
	srs = d1.keys()
	res = {}
	srs.sort()
	for sr in srs:
		if sr is 'name': continue
		if sr in ['SR00', 'SR10', 'SR20', 'SR30', 'SR31', 'SR34', 'SR35']: continue
		## print '-----------------------'
		## print 'at signal region', sr
		if (n==3):
			if(d1.has_key(sr)*d2.has_key(sr)*d3.has_key(sr) == 0): error()
		if (n==2):
			if(d1.has_key(sr)*d2.has_key(sr) == 0): error()
		## put the total errors in the dictionary
		## fakes
		d1[sr]['ferro'] = math.sqrt(d1[sr]['fstat']**2) ## + d1[sr]['fsyst']**2)
		d2[sr]['ferro'] = math.sqrt(d2[sr]['fstat']**2) ## + d2[sr]['fsyst']**2)
		if (n==3): d3[sr]['ferro'] = math.sqrt(d3[sr]['fstat']**2) ## + d3[sr]['fsyst']**2)
		## flips
		d1[sr]['cerro'] = math.sqrt(d1[sr]['cstat']**2) ## + d1[sr]['csyst']**2)
		d2[sr]['cerro'] = math.sqrt(d2[sr]['cstat']**2) ## + d2[sr]['csyst']**2)
		if (n==3): d3[sr]['cerro'] = math.sqrt(d3[sr]['cstat']**2) ## + d3[sr]['csyst']**2)
		## rare
		d1[sr]['rerro'] = math.sqrt(d1[sr]['rstat']**2)  ##+ d1[sr]['rsyst']**2)
		d2[sr]['rerro'] = math.sqrt(d2[sr]['rstat']**2)  ##+ d2[sr]['rsyst']**2)
		if (n==3): d3[sr]['rerro'] = math.sqrt(d3[sr]['rstat']**2)  ##+ d3[sr]['rsyst']**2)
		## now move on to do the single errors
		res[sr] = {}
		## observed number of events
		res[sr]['o'] = d1[sr]['o']
		## do the rare calculation
		res[sr]['r']     = (d1[sr]['r']) ##+d2[sr]['r']+d3[sr]['r'])/3.
		res[sr]['rstat'] = d1[sr]['rstat'] ## take just one value for now
		res[sr]['rsyst'] = d1[sr]['rsyst'] ## take just one value for now
		if (n==3): res[sr]['rerro'] = max([ d1[sr]['rerro'], d2[sr]['rerro'], d3[sr]['rerro'] ])
		if (n==2): res[sr]['rerro'] = max([ d1[sr]['rerro'], d2[sr]['rerro'] ])
		## do the charge flips
		if(n==3): res[sr]['c']     = (d1[sr]['c']+d2[sr]['c']+d3[sr]['c'])/3.
		if(n==2): res[sr]['c']     = (d1[sr]['c']+d2[sr]['c'])/2.
		res[sr]['cstat'] = d1[sr]['cstat'] ## take just one value for now
		res[sr]['csyst'] = d1[sr]['csyst'] ## take just one value for now
		if (n==3): res[sr]['cerro'] = max([ d1[sr]['cerro'], d2[sr]['cerro'], d3[sr]['cerro'] ])
		if (n==2): res[sr]['cerro'] = max([ d1[sr]['cerro'], d2[sr]['cerro'] ])
		## do the fakes
		if method =='avg':
			res[sr]['f']     = (d1[sr]['f']+d2[sr]['f']+d3[sr]['f'])/3.
			res[sr]['fstat'] = d1[sr]['fstat'] ## take just one value for now
			res[sr]['fsyst'] = d1[sr]['fsyst'] ## take just one value for now
			if (n==3): res[sr]['ferro'] = max([ d1[sr]['ferro'], d2[sr]['ferro'], d3[sr]['ferro'] ])
			if (n==2): res[sr]['ferro'] = max([ d1[sr]['ferro'], d2[sr]['ferro'] ])
		elif method == 'blue':
			print '----- ', sr,' -----'
			if (n==3): blueres = blue(d1[sr], d2[sr], d3[sr])
			if (n==2): blueres = blue2(d1[sr], d2[sr])
			res[sr]['f'] = blueres[0]
			res[sr]['fstat'] = d1[sr]['fstat'] ## dummy
			res[sr]['fsyst'] = d1[sr]['fsyst'] ## dummy
			res[sr]['ferro'] = blueres[1]
		elif method == 'weight':
			weightres = weightedMean(d1[sr], d2[sr], d3[sr])
			res[sr]['f'] = weightres[0]
			res[sr]['ferro'] = weightres[1]
			res[sr]['fstat'] = d1[sr]['fstat'] ## dummy
			res[sr]['fsyst'] = d1[sr]['fsyst'] ## dummy
	return res

def addTotalError(res):
	srs = res.keys()
	for sr in srs:
		if sr is 'name': continue
		totbkg = res[sr]['f']+res[sr]['r']+res[sr]['c']
		toterr = quadSum(res[sr]['fsyst'], res[sr]['fstat']) + quadSum(res[sr]['rsyst'], res[sr]['rstat']) + quadSum(res[sr]['csyst'], res[sr]['cstat'])
		res[sr]['t']  = str(round(totbkg,2))
		res[sr]['te'] = str(round(toterr,2))
		res[sr]['fn'] = str(round(res[sr]['f'],2))
		res[sr]['cn'] = str(round(res[sr]['c'],2))
		res[sr]['rn'] = str(round(res[sr]['r'],2))
		res[sr]['fe'] = str(round(quadSum(res[sr]['fstat'], 0.5*res[sr]['f']),2))
		res[sr]['ce'] = str(round(quadSum(res[sr]['cstat'], 0.3*res[sr]['c']),2))
		res[sr]['re'] = str(round(quadSum(res[sr]['rstat'], 0.5*res[sr]['r']),2))

		
def makeInput(res):
	f = open('plots/predictionsYields.txt', 'w')
	srs = res.keys()
	for sr in srs:
		if sr is 'name': continue
		totbkg = res[sr]['f']+res[sr]['r']+res[sr]['c']
		toterr = quadSum(res[sr]['ferro'], 0.5*res[sr]['f']) + quadSum(res[sr]['rerro'], 0.5*res[sr]['r']) + quadSum(res[sr]['cerro'], 0.3*res[sr]['c'])
		f.writelines('%s\t\t%d\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\t\t%.3f\n' 
			%(sr.lstrip('SR'), 
			res[sr]['o'], 
			totbkg, toterr,
			res[sr]['f'], quadSum(res[sr]['ferro'], 0.5*res[sr]['f']), 
			res[sr]['r'], quadSum(res[sr]['rerro'], 0.5*res[sr]['r']), 
			res[sr]['c'], quadSum(res[sr]['cerro'], 0.3*res[sr]['c']) ) )
	f.close()



def makeNicePlots(res, d1, d2, d3, nb, hilo='high'):
	regions0 = ['SR01', 'SR02', 'SR03', 'SR04', 'SR05', 'SR06','SR07', 'SR08']
	regions1 = ['SR11', 'SR12', 'SR13', 'SR14', 'SR15', 'SR16','SR17', 'SR18']
	regions2 = ['SR21', 'SR22', 'SR23', 'SR24', 'SR25', 'SR26','SR27', 'SR28']
	if nb == 0: regions = regions0
	if nb == 1: regions = regions1
	if nb == 2: regions = regions2
	global canv
	canv = ROOT.TCanvas('foobar', 'foobar', 900, 500)
	global r_h, f_h, c_h, t_h, a_s, o_h
	r_h = ROOT.TH1D('r', 'r', 8, 0, 8)
	c_h = ROOT.TH1D('c', 'c', 8, 0, 8)
	f_h = ROOT.TH1D('f', 'f', 8, 0, 8)
	o_h = ROOT.TH1D('o', 'o', 8, 0, 8)
	t_h = ROOT.TH1D('t', 't', 8, 0, 8)
	if (nb == 0): nstr = '#geq 0'
	if (nb == 1): nstr = '= 1'
	if (nb == 2): nstr = '#geq 2'
	if (hilo=='high'): a_s = ROOT.THStack('a', 'high-p_{T} signal regions with '+nstr+' b-tags')
	if (hilo=='low' ): a_s = ROOT.THStack('a', 'low-p_{T} signal regions with '+nstr+' b-tags')
	## some cosmetics. this should really be somewhere else...
	o_h.SetMarkerColor(ROOT.kBlack)
	o_h.SetMarkerStyle(20)
	o_h.SetMarkerSize(1.2)
	o_h.SetLineWidth(2)
	o_h.SetLineColor(ROOT.kBlack)
	o_h.SetFillColor(ROOT.kBlack)
	f_h.SetLineWidth(1)
	f_h.SetLineColor(50)
	f_h.SetFillColor(50)
	##f_h.SetLineColor(ROOT.kRed+1)
	##f_h.SetFillColor(ROOT.kRed+1)
	c_h.SetLineWidth(1)
	c_h.SetLineColor(42)
	c_h.SetFillColor(42)
	##c_h.SetLineColor(ROOT.kOrange-2)
	##c_h.SetFillColor(ROOT.kOrange-2)
	r_h.SetLineWidth(1)
	r_h.SetLineColor(31)
	r_h.SetFillColor(31)
	##r_h.SetLineColor(ROOT.kBlue-7)
	##r_h.SetFillColor(ROOT.kBlue-7)
	t_h.SetLineWidth(1)
	t_h.SetFillColor(12)
	t_h.SetFillStyle(3005)
	## end cosmetics
	for reg in regions:
		r,c,f,o  = res[reg]['r'], res[reg]['c'], res[reg]['f'], res[reg]['o']
		print r,c,f,o
		toterr = math.sqrt(quadSum(res[reg]['ferro'], 0.5*f)**2 + quadSum(res[reg]['rerro'], 0.5*r)**2 + quadSum(res[reg]['cerro'], 0.3*c)**2 )
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
	leg = helper.makeLegend(0.45, 0.72, 0.55, 0.88)
	leg.AddEntry(f_h, 'fakes', 'f')
	leg.AddEntry(r_h, 'rares', 'f')
	leg.AddEntry(c_h, 'flips', 'f')
	leg.AddEntry(o_e, 'data' , 'pe')
	if not nb==2: a_s.SetMaximum(1.5*t_h.GetBinContent(1))
	else:  a_s.SetMaximum(15.)
	for reg in regions:
		a_s.GetXaxis().SetBinLabel  (regions.index(reg)+1, reg)
	a_s.Draw('hist')
	t_h.DrawCopy('0 E2 same')
	o_e.Draw('P same')
	leg.Draw('same')
	if (hilo == 'high'): canv.SaveAs('plots/highptsummary_regions'+str(nb)+'.pdf')
	if (hilo == 'low' ): canv.SaveAs('plots/lowptsummary_regions'+str(nb)+'.pdf')

		
lowpt = False
if 'lowpt' in args:
	lowpt = True
		

if lowpt:
	## THIS SECTION FOR THE LOW-PT ANALYSES
	## ------------------------------------
	ucsdlow = eval(open('ucfnal_signal_lowpt.txt.1').read())
	ufldlow = eval(open('uf_signal_lowpt.txt.2').read())
	
	r12 = 0.275
	r21 = 0.275
	
	dummy = 1
	blueres = combine(ucsdlow, ufldlow, dummy, 'blue', 2)
	makeNicePlots(blueres, ucsdlow, ufldlow, dummy, 0, hilo='low')
	makeNicePlots(blueres, ucsdlow, ufldlow, dummy, 1, hilo='low')
	makeNicePlots(blueres, ucsdlow, ufldlow, dummy, 2, hilo='low')


else:
	## THIS SECTION FOR THE HIGH-PT ANALYSES
	## -------------------------------------
	ucsd = eval(open('ucfnal_signal_highpt.txt_apr12').read())
	ufld = eval(open('uf_signal_highpt.txt_apr12').read())
	ethd = eval(open('eth_signalRegions_highpt.txt_apr12').read())
	addTotalError(ucsd)
	addTotalError(ufld)
	addTotalError(ethd)
	ucsd['name'] = 'uc'
	ufld['name'] = 'uf'
	ethd['name'] = 'eo'
	
	r12 = 0.275
	r21 = 0.275
	r13 = 0.398
	r31 = 0.398
	r23 = 0.488
	r32 = 0.488
	
	blueres = combine(ucsd, ufld, ethd, 'blue')
	## avgres  = combine(ucsd, ufld, ethd, 'avg' )
	## weighres= combine(ucsd, ufld, ethd, 'weight')
	blueres['name'] = 'comb'
	addTotalError(blueres)
	
	## makeSomePlots(blueres, weighres, avgres, ucsd, ufld, ethd)
	## makeComparison(ucsd, ufld, ethd, 'r', 'high')
	## makeComparison(ucsd, ufld, ethd, 'c', 'high')
	
	makeInput(blueres)
	tables.makeTables([ucsd, ufld, ethd, blueres])
	makeNicePlots(blueres, ucsd, ufld, ethd, 0)
	makeNicePlots(blueres, ucsd, ufld, ethd, 1)
	makeNicePlots(blueres, ucsd, ufld, ethd, 2)

