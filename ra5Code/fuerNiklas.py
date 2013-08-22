def blue(d1, d2, d3):
	## make the matrix
	M = matrix([ [     d1['statErr']*d1['statErr'] , r12*d1['statErr']*d2['statErr'] , r13*d1['statErr']*d3['statErr'] ] ,
	             [ r21*d2['statErr']*d1['statErr'] ,     d2['statErr']*d2['statErr'] , r23*d2['statErr']*d3['statErr'] ] ,
	             [ r31*d3['statErr']*d1['statErr'] , r32*d3['statErr']*d2['statErr'] ,     d3['statErr']*d3['statErr'] ] ])
	Minv = M.I ## inverse of the matrix
	global m 
	m = Minv
	norm = Minv.sum() ## normalization value
	c  = [ Minv[0].sum()/norm, Minv[1].sum()/norm, Minv[2].sum()/norm ]## normalization coefficients
	sigmSq  = 0 ## squared sigma
	central = c[0]*d1['f'] + c[1]*d2['f'] + c[2]*d3['f']
	## print '-------------------------'
	print 'central values: %.2f %.2f %.2f' % (d1['f'], d2['f'], d3['f'])
	print 'error   values: %.2f %.2f %.2f' % (d1['statErr'], d2['statErr'], d3['statErr'])
	print 'c_0 c_1 c_2   : %.2f %.2f %.2f' % (c[0], c[1], c[2])
	err0sq = d1['statErr']*d1['statErr']
	err1sq = d2['statErr']*d2['statErr']
	err2sq = d3['statErr']*d3['statErr']
	## calculate the squared sigma
	for i in range(len(Minv)):
		for j in range(len(Minv)):
			sigmSq += M[i,j]*c[i]*c[j]
	if not sigmSq: error()
	print 'error %.2f and from blue: %.2f' %(1/math.sqrt(1./err0sq+1./err1sq+1./err2sq) , math.sqrt(sigmSq))
	return central, math.sqrt(sigmSq)

