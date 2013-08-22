def myround(val, err):
	if err >= 0.355:
		retval = '%.1f' %(val)
		reterr = '%.1f' %(err)
		if err >= 3.55:
			retval = '%.0f' %(val)
			reterr = '%.0f' %(err)
	else:
		retval = '%.2f' %(val)
		reterr = '%.2f' %(err)
	return retval, reterr
