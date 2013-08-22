def makeTables(list, do3rdVeto = False):
	if do3rdVeto:
		tabdir = 'tables_3rdVeto'
	else:
		tabdir = 'tables'
	o = {}
	for d in list:
		if not d['name'] == 'combined': continue
		srs = d.keys()
		for sr in srs:
			if sr is 'name': continue
			o[sr] = int(d[sr]['o'])

	x = list[0] # make sure this is UC
	y = list[1] # make sure this is UF
	z = list[2] # make sure this is EO
	a = list[3] # make sure this is the combined
			
	for d in list:
		if d['name'] == 'UC/FNAL':
			filename = tabdir+'/UCTable_highpt.tex'
			caption = '\caption{Predicted and observed yields for the high-\pt analysis, UCSB/UCSD/FNAL.}'
			label   = '\label{tab:uctable_highpt}'
		if d['name'] == 'UFL':
			filename = tabdir+'/UFTable_highpt.tex'
			caption = '\caption{Predicted and observed yields for the high-\pt analysis, UFL.}'
			label   = '\label{tab:uftable_highpt}'
		if d['name'] == 'ETH/Oviedo':
			filename = tabdir+'/EOTable_highpt.tex'
			caption = '\caption{Predicted and observed yields for the high-\pt analysis, ETH/Oviedo.}'
			label   = '\label{tab:eotable_highpt}'
		if d['name'] == 'combined':
			filename = tabdir+'/combTable_highpt.tex'
			caption = '\caption{Predicted and observed yields for the high-\pt analysis after combining the three groups.}'
			label   = '\label{tab:combtable_highpt}'
		f= open(filename, 'w')
		f. write('''
\\begin{{table}}
\\begin{{center}}
{cap}
{lab}
\\begin{{tabular}}{{|c|c|c|c|c|l|c|}}
\\hline
NBjets                              & MET                            & NJets                             & HT      & SR & Predicted          & Observed \\\\ \\hline
\\multirow{{8}}{{*}}{{$=0$}}        & \\multirow{{4}}{{*}}{{50-120}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 1  & {sr01} $\pm$ {sr01e} & {sr01_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 2  & {sr02} $\pm$ {sr02e} & {sr02_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 3  & {sr03} $\pm$ {sr03e} & {sr03_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 4  & {sr04} $\pm$ {sr04e} & {sr04_o} \\\\ \\cline{{2-5}}
                                    & \\multirow{{4}}{{*}}{{$>120$}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 5  & {sr05} $\pm$ {sr05e} & {sr05_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 6  & {sr06} $\pm$ {sr06e} & {sr06_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 7  & {sr07} $\pm$ {sr07e} & {sr07_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 8  & {sr08} $\pm$ {sr08e} & {sr08_o} \\\\ \\hline
                                                                                                                                          
\\multirow{{8}}{{*}}{{$=1$}}        & \\multirow{{4}}{{*}}{{50-120}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 11 & {sr11} $\pm$ {sr11e} & {sr11_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 12 & {sr12} $\pm$ {sr12e} & {sr12_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 13 & {sr13} $\pm$ {sr13e} & {sr13_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 14 & {sr14} $\pm$ {sr14e} & {sr14_o} \\\\ \\cline{{2-5}}
                                    & \\multirow{{4}}{{*}}{{$>120$}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 15 & {sr15} $\pm$ {sr15e} & {sr15_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 16 & {sr16} $\pm$ {sr16e} & {sr16_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 17 & {sr17} $\pm$ {sr17e} & {sr17_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 18 & {sr18} $\pm$ {sr18e} & {sr18_o} \\\\ \\hline
                                                                                                                                          
\\multirow{{8}}{{*}}{{$\\geq 2$}}   & \\multirow{{4}}{{*}}{{50-120}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 21 & {sr21} $\pm$ {sr21e} & {sr21_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 22 & {sr22} $\pm$ {sr22e} & {sr22_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 23 & {sr23} $\pm$ {sr23e} & {sr23_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 24 & {sr24} $\pm$ {sr24e} & {sr24_o} \\\\ \\cline{{2-5}}
                                    & \\multirow{{4}}{{*}}{{$>120$}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 25 & {sr25} $\pm$ {sr25e} & {sr25_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 26 & {sr26} $\pm$ {sr26e} & {sr26_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 27 & {sr27} $\pm$ {sr27e} & {sr27_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 28 & {sr28} $\pm$ {sr28e} & {sr28_o} \\\\ \\hline

\\end{{tabular}}
\\end{{center}}
\\end{{table}}

'''.format( cap=caption, lab=label,
            sr01_o=o['SR01'],sr02_o=o['SR02'],sr03_o=o['SR03'],sr04_o=o['SR04'],sr05_o=o['SR05'],sr06_o=o['SR06'],sr07_o=o['SR07'],sr08_o=o['SR08'],  
            sr11_o=o['SR11'],sr12_o=o['SR12'],sr13_o=o['SR13'],sr14_o=o['SR14'],sr15_o=o['SR15'],sr16_o=o['SR16'],sr17_o=o['SR17'],sr18_o=o['SR18'],
            sr21_o=o['SR21'],sr22_o=o['SR22'],sr23_o=o['SR23'],sr24_o=o['SR24'],sr25_o=o['SR25'],sr26_o=o['SR26'],sr27_o=o['SR27'],sr28_o=o['SR28'],
## and the predicitons...
            sr01=d['SR01']['t'],sr02=d['SR02']['t'],sr03=d['SR03']['t'],sr04=d['SR04']['t'],sr05=d['SR05']['t'],sr06=d['SR06']['t'],sr07=d['SR07']['t'],sr08=d['SR08']['t'],  
            sr11=d['SR11']['t'],sr12=d['SR12']['t'],sr13=d['SR13']['t'],sr14=d['SR14']['t'],sr15=d['SR15']['t'],sr16=d['SR16']['t'],sr17=d['SR17']['t'],sr18=d['SR18']['t'],
            sr21=d['SR21']['t'],sr22=d['SR22']['t'],sr23=d['SR23']['t'],sr24=d['SR24']['t'],sr25=d['SR25']['t'],sr26=d['SR26']['t'],sr27=d['SR27']['t'],sr28=d['SR28']['t'],
## with the errors
            sr01e=d['SR01']['te'],sr02e=d['SR02']['te'],sr03e=d['SR03']['te'],sr04e=d['SR04']['te'],sr05e=d['SR05']['te'],sr06e=d['SR06']['te'],sr07e=d['SR07']['te'],sr08e=d['SR08']['te'],  
            sr11e=d['SR11']['te'],sr12e=d['SR12']['te'],sr13e=d['SR13']['te'],sr14e=d['SR14']['te'],sr15e=d['SR15']['te'],sr16e=d['SR16']['te'],sr17e=d['SR17']['te'],sr18e=d['SR18']['te'],
            sr21e=d['SR21']['te'],sr22e=d['SR22']['te'],sr23e=d['SR23']['te'],sr24e=d['SR24']['te'],sr25e=d['SR25']['te'],sr26e=d['SR26']['te'],sr27e=d['SR27']['te'],sr28e=d['SR28']['te']))

	f.close()
	## make a table that puts the has all three groups
	filename = tabdir+'/ComboTable_highpt.tex'
	caption = '\caption{Predicted and observed yields for the high-\pt analysis, all groups.}'
	label   = '\label{tab:combotable_highpt}'
	g = open(filename ,'w')
	g. write('''
\\begin{{table}}
\\begin{{center}}
{cap}
{lab}
\\begin{{tabular}}{{|c|rcl|rcl|rcl|c|}}
\\hline
SR & \\multicolumn{{3}}{{|c|}}{{UC/FNAL}}      & \\multicolumn{{3}}{{|c|}}{{UFL}}       & \\multicolumn{{3}}{{|c|}}{{ETH/Oviedo}}  & Observed \\\\ \\hline
1  & {ucsr01} & $\pm$ & {ucsr01e} & {ufsr01} & $\pm$ & {ufsr01e} & {eosr01} & $\pm$ & {eosr01e} & {sr01_o} \\\\ \\hline
2  & {ucsr02} & $\pm$ & {ucsr02e} & {ufsr02} & $\pm$ & {ufsr02e} & {eosr02} & $\pm$ & {eosr02e} & {sr02_o} \\\\ \\hline
3  & {ucsr03} & $\pm$ & {ucsr03e} & {ufsr03} & $\pm$ & {ufsr03e} & {eosr03} & $\pm$ & {eosr03e} & {sr03_o} \\\\ \\hline
4  & {ucsr04} & $\pm$ & {ucsr04e} & {ufsr04} & $\pm$ & {ufsr04e} & {eosr04} & $\pm$ & {eosr04e} & {sr04_o} \\\\ \\hline
5  & {ucsr05} & $\pm$ & {ucsr05e} & {ufsr05} & $\pm$ & {ufsr05e} & {eosr05} & $\pm$ & {eosr05e} & {sr05_o} \\\\ \\hline
6  & {ucsr06} & $\pm$ & {ucsr06e} & {ufsr06} & $\pm$ & {ufsr06e} & {eosr06} & $\pm$ & {eosr06e} & {sr06_o} \\\\ \\hline
7  & {ucsr07} & $\pm$ & {ucsr07e} & {ufsr07} & $\pm$ & {ufsr07e} & {eosr07} & $\pm$ & {eosr07e} & {sr07_o} \\\\ \\hline
8  & {ucsr08} & $\pm$ & {ucsr08e} & {ufsr08} & $\pm$ & {ufsr08e} & {eosr08} & $\pm$ & {eosr08e} & {sr08_o} \\\\ \\hline

11 & {ucsr11} & $\pm$ & {ucsr11e} & {ufsr11} & $\pm$ & {ufsr11e} & {eosr11} & $\pm$ & {eosr11e} & {sr11_o} \\\\ \\hline
12 & {ucsr12} & $\pm$ & {ucsr12e} & {ufsr12} & $\pm$ & {ufsr12e} & {eosr12} & $\pm$ & {eosr12e} & {sr12_o} \\\\ \\hline
13 & {ucsr13} & $\pm$ & {ucsr13e} & {ufsr13} & $\pm$ & {ufsr13e} & {eosr13} & $\pm$ & {eosr13e} & {sr13_o} \\\\ \\hline
14 & {ucsr14} & $\pm$ & {ucsr14e} & {ufsr14} & $\pm$ & {ufsr14e} & {eosr14} & $\pm$ & {eosr14e} & {sr14_o} \\\\ \\hline
15 & {ucsr15} & $\pm$ & {ucsr15e} & {ufsr15} & $\pm$ & {ufsr15e} & {eosr15} & $\pm$ & {eosr15e} & {sr15_o} \\\\ \\hline
16 & {ucsr16} & $\pm$ & {ucsr16e} & {ufsr16} & $\pm$ & {ufsr16e} & {eosr16} & $\pm$ & {eosr16e} & {sr16_o} \\\\ \\hline
17 & {ucsr17} & $\pm$ & {ucsr17e} & {ufsr17} & $\pm$ & {ufsr17e} & {eosr17} & $\pm$ & {eosr17e} & {sr17_o} \\\\ \\hline
18 & {ucsr18} & $\pm$ & {ucsr18e} & {ufsr18} & $\pm$ & {ufsr18e} & {eosr18} & $\pm$ & {eosr18e} & {sr18_o} \\\\ \\hline

21 & {ucsr21} & $\pm$ & {ucsr21e} & {ufsr21} & $\pm$ & {ufsr21e} & {eosr21} & $\pm$ & {eosr21e} & {sr21_o} \\\\ \\hline
22 & {ucsr22} & $\pm$ & {ucsr22e} & {ufsr22} & $\pm$ & {ufsr22e} & {eosr22} & $\pm$ & {eosr22e} & {sr22_o} \\\\ \\hline
23 & {ucsr23} & $\pm$ & {ucsr23e} & {ufsr23} & $\pm$ & {ufsr23e} & {eosr23} & $\pm$ & {eosr23e} & {sr23_o} \\\\ \\hline
24 & {ucsr24} & $\pm$ & {ucsr24e} & {ufsr24} & $\pm$ & {ufsr24e} & {eosr24} & $\pm$ & {eosr24e} & {sr24_o} \\\\ \\hline
25 & {ucsr25} & $\pm$ & {ucsr25e} & {ufsr25} & $\pm$ & {ufsr25e} & {eosr25} & $\pm$ & {eosr25e} & {sr25_o} \\\\ \\hline
26 & {ucsr26} & $\pm$ & {ucsr26e} & {ufsr26} & $\pm$ & {ufsr26e} & {eosr26} & $\pm$ & {eosr26e} & {sr26_o} \\\\ \\hline
27 & {ucsr27} & $\pm$ & {ucsr27e} & {ufsr27} & $\pm$ & {ufsr27e} & {eosr27} & $\pm$ & {eosr27e} & {sr27_o} \\\\ \\hline
28 & {ucsr28} & $\pm$ & {ucsr28e} & {ufsr28} & $\pm$ & {ufsr28e} & {eosr28} & $\pm$ & {eosr28e} & {sr28_o} \\\\ \\hline

\\end{{tabular}}
\\end{{center}}
\\end{{table}}

'''.format( cap=caption, lab=label,
            sr01_o=o['SR01'],sr02_o=o['SR02'],sr03_o=o['SR03'],sr04_o=o['SR04'],sr05_o=o['SR05'],sr06_o=o['SR06'],sr07_o=o['SR07'],sr08_o=o['SR08'],  
            sr11_o=o['SR11'],sr12_o=o['SR12'],sr13_o=o['SR13'],sr14_o=o['SR14'],sr15_o=o['SR15'],sr16_o=o['SR16'],sr17_o=o['SR17'],sr18_o=o['SR18'],
            sr21_o=o['SR21'],sr22_o=o['SR22'],sr23_o=o['SR23'],sr24_o=o['SR24'],sr25_o=o['SR25'],sr26_o=o['SR26'],sr27_o=o['SR27'],sr28_o=o['SR28'],
## UC/FNAL predicitons...
            ucsr01=x['SR01']['t'],ucsr02=x['SR02']['t'],ucsr03=x['SR03']['t'],ucsr04=x['SR04']['t'],ucsr05=x['SR05']['t'],ucsr06=x['SR06']['t'],ucsr07=x['SR07']['t'],ucsr08=x['SR08']['t'],  
            ucsr11=x['SR11']['t'],ucsr12=x['SR12']['t'],ucsr13=x['SR13']['t'],ucsr14=x['SR14']['t'],ucsr15=x['SR15']['t'],ucsr16=x['SR16']['t'],ucsr17=x['SR17']['t'],ucsr18=x['SR18']['t'],
            ucsr21=x['SR21']['t'],ucsr22=x['SR22']['t'],ucsr23=x['SR23']['t'],ucsr24=x['SR24']['t'],ucsr25=x['SR25']['t'],ucsr26=x['SR26']['t'],ucsr27=x['SR27']['t'],ucsr28=x['SR28']['t'],
## with the errors
            ucsr01e=x['SR01']['te'],ucsr02e=x['SR02']['te'],ucsr03e=x['SR03']['te'],ucsr04e=x['SR04']['te'],ucsr05e=x['SR05']['te'],ucsr06e=x['SR06']['te'],ucsr07e=x['SR07']['te'],ucsr08e=x['SR08']['te'],  
            ucsr11e=x['SR11']['te'],ucsr12e=x['SR12']['te'],ucsr13e=x['SR13']['te'],ucsr14e=x['SR14']['te'],ucsr15e=x['SR15']['te'],ucsr16e=x['SR16']['te'],ucsr17e=x['SR17']['te'],ucsr18e=x['SR18']['te'],
            ucsr21e=x['SR21']['te'],ucsr22e=x['SR22']['te'],ucsr23e=x['SR23']['te'],ucsr24e=x['SR24']['te'],ucsr25e=x['SR25']['te'],ucsr26e=x['SR26']['te'],ucsr27e=x['SR27']['te'],ucsr28e=x['SR28']['te'],
## UFL predictions
            ufsr01=y['SR01']['t'],ufsr02=y['SR02']['t'],ufsr03=y['SR03']['t'],ufsr04=y['SR04']['t'],ufsr05=y['SR05']['t'],ufsr06=y['SR06']['t'],ufsr07=y['SR07']['t'],ufsr08=y['SR08']['t'],  
            ufsr11=y['SR11']['t'],ufsr12=y['SR12']['t'],ufsr13=y['SR13']['t'],ufsr14=y['SR14']['t'],ufsr15=y['SR15']['t'],ufsr16=y['SR16']['t'],ufsr17=y['SR17']['t'],ufsr18=y['SR18']['t'],
            ufsr21=y['SR21']['t'],ufsr22=y['SR22']['t'],ufsr23=y['SR23']['t'],ufsr24=y['SR24']['t'],ufsr25=y['SR25']['t'],ufsr26=y['SR26']['t'],ufsr27=y['SR27']['t'],ufsr28=y['SR28']['t'],
## with the errors
            ufsr01e=y['SR01']['te'],ufsr02e=y['SR02']['te'],ufsr03e=y['SR03']['te'],ufsr04e=y['SR04']['te'],ufsr05e=y['SR05']['te'],ufsr06e=y['SR06']['te'],ufsr07e=y['SR07']['te'],ufsr08e=y['SR08']['te'],  
            ufsr11e=y['SR11']['te'],ufsr12e=y['SR12']['te'],ufsr13e=y['SR13']['te'],ufsr14e=y['SR14']['te'],ufsr15e=y['SR15']['te'],ufsr16e=y['SR16']['te'],ufsr17e=y['SR17']['te'],ufsr18e=y['SR18']['te'],
            ufsr21e=y['SR21']['te'],ufsr22e=y['SR22']['te'],ufsr23e=y['SR23']['te'],ufsr24e=y['SR24']['te'],ufsr25e=y['SR25']['te'],ufsr26e=y['SR26']['te'],ufsr27e=y['SR27']['te'],ufsr28e=y['SR28']['te'],
## ETH/Oviedo predicitons...
            eosr01=z['SR01']['t'],eosr02=z['SR02']['t'],eosr03=z['SR03']['t'],eosr04=z['SR04']['t'],eosr05=z['SR05']['t'],eosr06=z['SR06']['t'],eosr07=z['SR07']['t'],eosr08=z['SR08']['t'],  
            eosr11=z['SR11']['t'],eosr12=z['SR12']['t'],eosr13=z['SR13']['t'],eosr14=z['SR14']['t'],eosr15=z['SR15']['t'],eosr16=z['SR16']['t'],eosr17=z['SR17']['t'],eosr18=z['SR18']['t'],
            eosr21=z['SR21']['t'],eosr22=z['SR22']['t'],eosr23=z['SR23']['t'],eosr24=z['SR24']['t'],eosr25=z['SR25']['t'],eosr26=z['SR26']['t'],eosr27=z['SR27']['t'],eosr28=z['SR28']['t'],
## with the errors
            eosr01e=z['SR01']['te'],eosr02e=z['SR02']['te'],eosr03e=z['SR03']['te'],eosr04e=z['SR04']['te'],eosr05e=z['SR05']['te'],eosr06e=z['SR06']['te'],eosr07e=z['SR07']['te'],eosr08e=z['SR08']['te'],  
            eosr11e=z['SR11']['te'],eosr12e=z['SR12']['te'],eosr13e=z['SR13']['te'],eosr14e=z['SR14']['te'],eosr15e=z['SR15']['te'],eosr16e=z['SR16']['te'],eosr17e=z['SR17']['te'],eosr18e=z['SR18']['te'],
            eosr21e=z['SR21']['te'],eosr22e=z['SR22']['te'],eosr23e=z['SR23']['te'],eosr24e=z['SR24']['te'],eosr25e=z['SR25']['te'],eosr26e=z['SR26']['te'],eosr27e=z['SR27']['te'],eosr28e=z['SR28']['te']))

	g.close()
	## make a table that has the has all three backgrounds
	filename = tabdir+'/splitTable_highpt.tex'
	caption = '\caption{Predicted and observed yields for the high-\pt analysis, different background sources.}'
	label   = '\label{tab:splittable_highpt}'
	h = open(filename ,'w')
	h. write('''
\\begin{{table}}
\\begin{{center}}
{cap}
{lab}
\\begin{{tabular}}{{|c|rcl|rcl|rcl|rcl|c|}}
\\hline
SR & \\multicolumn{{3}}{{|c|}}{{Fakes}}   & \\multicolumn{{3}}{{|c|}}{{Flips}} & \\multicolumn{{3}}{{|c|}}{{Rares}}  & \\multicolumn{{3}}{{|c|}}{{Total}}  & Observed \\\\ \\hline
1  & {fsr01} & $\pm$ & {fsr01e} & {csr01} & $\pm$ & {csr01e} & {rsr01} & $\pm$ & {rsr01e} & {tsr01} & $\pm$ & {tsr01e} & {sr01_o} \\\\ \\hline
2  & {fsr02} & $\pm$ & {fsr02e} & {csr02} & $\pm$ & {csr02e} & {rsr02} & $\pm$ & {rsr02e} & {tsr02} & $\pm$ & {tsr02e} & {sr02_o} \\\\ \\hline
3  & {fsr03} & $\pm$ & {fsr03e} & {csr03} & $\pm$ & {csr03e} & {rsr03} & $\pm$ & {rsr03e} & {tsr03} & $\pm$ & {tsr03e} & {sr03_o} \\\\ \\hline
4  & {fsr04} & $\pm$ & {fsr04e} & {csr04} & $\pm$ & {csr04e} & {rsr04} & $\pm$ & {rsr04e} & {tsr04} & $\pm$ & {tsr04e} & {sr04_o} \\\\ \\hline
5  & {fsr05} & $\pm$ & {fsr05e} & {csr05} & $\pm$ & {csr05e} & {rsr05} & $\pm$ & {rsr05e} & {tsr05} & $\pm$ & {tsr05e} & {sr05_o} \\\\ \\hline
6  & {fsr06} & $\pm$ & {fsr06e} & {csr06} & $\pm$ & {csr06e} & {rsr06} & $\pm$ & {rsr06e} & {tsr06} & $\pm$ & {tsr06e} & {sr06_o} \\\\ \\hline
7  & {fsr07} & $\pm$ & {fsr07e} & {csr07} & $\pm$ & {csr07e} & {rsr07} & $\pm$ & {rsr07e} & {tsr07} & $\pm$ & {tsr07e} & {sr07_o} \\\\ \\hline
8  & {fsr08} & $\pm$ & {fsr08e} & {csr08} & $\pm$ & {csr08e} & {rsr08} & $\pm$ & {rsr08e} & {tsr08} & $\pm$ & {tsr08e} & {sr08_o} \\\\ \\hline
                                                                                         
11 & {fsr11} & $\pm$ & {fsr11e} & {csr11} & $\pm$ & {csr11e} & {rsr11} & $\pm$ & {rsr11e} & {tsr11} & $\pm$ & {tsr11e} & {sr11_o} \\\\ \\hline
12 & {fsr12} & $\pm$ & {fsr12e} & {csr12} & $\pm$ & {csr12e} & {rsr12} & $\pm$ & {rsr12e} & {tsr12} & $\pm$ & {tsr12e} & {sr12_o} \\\\ \\hline
13 & {fsr13} & $\pm$ & {fsr13e} & {csr13} & $\pm$ & {csr13e} & {rsr13} & $\pm$ & {rsr13e} & {tsr13} & $\pm$ & {tsr13e} & {sr13_o} \\\\ \\hline
14 & {fsr14} & $\pm$ & {fsr14e} & {csr14} & $\pm$ & {csr14e} & {rsr14} & $\pm$ & {rsr14e} & {tsr14} & $\pm$ & {tsr14e} & {sr14_o} \\\\ \\hline
15 & {fsr15} & $\pm$ & {fsr15e} & {csr15} & $\pm$ & {csr15e} & {rsr15} & $\pm$ & {rsr15e} & {tsr15} & $\pm$ & {tsr15e} & {sr15_o} \\\\ \\hline
16 & {fsr16} & $\pm$ & {fsr16e} & {csr16} & $\pm$ & {csr16e} & {rsr16} & $\pm$ & {rsr16e} & {tsr16} & $\pm$ & {tsr16e} & {sr16_o} \\\\ \\hline
17 & {fsr17} & $\pm$ & {fsr17e} & {csr17} & $\pm$ & {csr17e} & {rsr17} & $\pm$ & {rsr17e} & {tsr17} & $\pm$ & {tsr17e} & {sr17_o} \\\\ \\hline
18 & {fsr18} & $\pm$ & {fsr18e} & {csr18} & $\pm$ & {csr18e} & {rsr18} & $\pm$ & {rsr18e} & {tsr18} & $\pm$ & {tsr18e} & {sr18_o} \\\\ \\hline
                                                                                         
21 & {fsr21} & $\pm$ & {fsr21e} & {csr21} & $\pm$ & {csr21e} & {rsr21} & $\pm$ & {rsr21e} & {tsr21} & $\pm$ & {tsr21e} & {sr21_o} \\\\ \\hline
22 & {fsr22} & $\pm$ & {fsr22e} & {csr22} & $\pm$ & {csr22e} & {rsr22} & $\pm$ & {rsr22e} & {tsr22} & $\pm$ & {tsr22e} & {sr22_o} \\\\ \\hline
23 & {fsr23} & $\pm$ & {fsr23e} & {csr23} & $\pm$ & {csr23e} & {rsr23} & $\pm$ & {rsr23e} & {tsr23} & $\pm$ & {tsr23e} & {sr23_o} \\\\ \\hline
24 & {fsr24} & $\pm$ & {fsr24e} & {csr24} & $\pm$ & {csr24e} & {rsr24} & $\pm$ & {rsr24e} & {tsr24} & $\pm$ & {tsr24e} & {sr24_o} \\\\ \\hline
25 & {fsr25} & $\pm$ & {fsr25e} & {csr25} & $\pm$ & {csr25e} & {rsr25} & $\pm$ & {rsr25e} & {tsr25} & $\pm$ & {tsr25e} & {sr25_o} \\\\ \\hline
26 & {fsr26} & $\pm$ & {fsr26e} & {csr26} & $\pm$ & {csr26e} & {rsr26} & $\pm$ & {rsr26e} & {tsr26} & $\pm$ & {tsr26e} & {sr26_o} \\\\ \\hline
27 & {fsr27} & $\pm$ & {fsr27e} & {csr27} & $\pm$ & {csr27e} & {rsr27} & $\pm$ & {rsr27e} & {tsr27} & $\pm$ & {tsr27e} & {sr27_o} \\\\ \\hline
28 & {fsr28} & $\pm$ & {fsr28e} & {csr28} & $\pm$ & {csr28e} & {rsr28} & $\pm$ & {rsr28e} & {tsr28} & $\pm$ & {tsr28e} & {sr28_o} \\\\ \\hline

\\end{{tabular}}
\\end{{center}}
\\end{{table}}

'''.format( cap=caption, lab=label,
            sr01_o=o['SR01'],sr02_o=o['SR02'],sr03_o=o['SR03'],sr04_o=o['SR04'],sr05_o=o['SR05'],sr06_o=o['SR06'],sr07_o=o['SR07'],sr08_o=o['SR08'],  
            sr11_o=o['SR11'],sr12_o=o['SR12'],sr13_o=o['SR13'],sr14_o=o['SR14'],sr15_o=o['SR15'],sr16_o=o['SR16'],sr17_o=o['SR17'],sr18_o=o['SR18'],
            sr21_o=o['SR21'],sr22_o=o['SR22'],sr23_o=o['SR23'],sr24_o=o['SR24'],sr25_o=o['SR25'],sr26_o=o['SR26'],sr27_o=o['SR27'],sr28_o=o['SR28'],
## fake predicitons...
            fsr01=a['SR01']['fn'],fsr02=a['SR02']['fn'],fsr03=a['SR03']['fn'],fsr04=a['SR04']['fn'],fsr05=a['SR05']['fn'],fsr06=a['SR06']['fn'],fsr07=a['SR07']['fn'],fsr08=a['SR08']['fn'],  
            fsr11=a['SR11']['fn'],fsr12=a['SR12']['fn'],fsr13=a['SR13']['fn'],fsr14=a['SR14']['fn'],fsr15=a['SR15']['fn'],fsr16=a['SR16']['fn'],fsr17=a['SR17']['fn'],fsr18=a['SR18']['fn'],
            fsr21=a['SR21']['fn'],fsr22=a['SR22']['fn'],fsr23=a['SR23']['fn'],fsr24=a['SR24']['fn'],fsr25=a['SR25']['fn'],fsr26=a['SR26']['fn'],fsr27=a['SR27']['fn'],fsr28=a['SR28']['fn'],
## with the errors
            fsr01e=a['SR01']['fe'],fsr02e=a['SR02']['fe'],fsr03e=a['SR03']['fe'],fsr04e=a['SR04']['fe'],fsr05e=a['SR05']['fe'],fsr06e=a['SR06']['fe'],fsr07e=a['SR07']['fe'],fsr08e=a['SR08']['fe'],  
            fsr11e=a['SR11']['fe'],fsr12e=a['SR12']['fe'],fsr13e=a['SR13']['fe'],fsr14e=a['SR14']['fe'],fsr15e=a['SR15']['fe'],fsr16e=a['SR16']['fe'],fsr17e=a['SR17']['fe'],fsr18e=a['SR18']['fe'],
            fsr21e=a['SR21']['fe'],fsr22e=a['SR22']['fe'],fsr23e=a['SR23']['fe'],fsr24e=a['SR24']['fe'],fsr25e=a['SR25']['fe'],fsr26e=a['SR26']['fe'],fsr27e=a['SR27']['fe'],fsr28e=a['SR28']['fe'],
## flip predictions
            csr01=a['SR01']['cn'],csr02=a['SR02']['cn'],csr03=a['SR03']['cn'],csr04=a['SR04']['cn'],csr05=a['SR05']['cn'],csr06=a['SR06']['cn'],csr07=a['SR07']['cn'],csr08=a['SR08']['cn'],  
            csr11=a['SR11']['cn'],csr12=a['SR12']['cn'],csr13=a['SR13']['cn'],csr14=a['SR14']['cn'],csr15=a['SR15']['cn'],csr16=a['SR16']['cn'],csr17=a['SR17']['cn'],csr18=a['SR18']['cn'],
            csr21=a['SR21']['cn'],csr22=a['SR22']['cn'],csr23=a['SR23']['cn'],csr24=a['SR24']['cn'],csr25=a['SR25']['cn'],csr26=a['SR26']['cn'],csr27=a['SR27']['cn'],csr28=a['SR28']['cn'],
## with the errors
            csr01e=a['SR01']['ce'],csr02e=a['SR02']['ce'],csr03e=a['SR03']['ce'],csr04e=a['SR04']['ce'],csr05e=a['SR05']['ce'],csr06e=a['SR06']['ce'],csr07e=a['SR07']['ce'],csr08e=a['SR08']['ce'],  
            csr11e=a['SR11']['ce'],csr12e=a['SR12']['ce'],csr13e=a['SR13']['ce'],csr14e=a['SR14']['ce'],csr15e=a['SR15']['ce'],csr16e=a['SR16']['ce'],csr17e=a['SR17']['ce'],csr18e=a['SR18']['ce'],
            csr21e=a['SR21']['ce'],csr22e=a['SR22']['ce'],csr23e=a['SR23']['ce'],csr24e=a['SR24']['ce'],csr25e=a['SR25']['ce'],csr26e=a['SR26']['ce'],csr27e=a['SR27']['ce'],csr28e=a['SR28']['ce'],
## rare predicitons...
            rsr01=a['SR01']['rn'],rsr02=a['SR02']['rn'],rsr03=a['SR03']['rn'],rsr04=a['SR04']['rn'],rsr05=a['SR05']['rn'],rsr06=a['SR06']['rn'],rsr07=a['SR07']['rn'],rsr08=a['SR08']['rn'],  
            rsr11=a['SR11']['rn'],rsr12=a['SR12']['rn'],rsr13=a['SR13']['rn'],rsr14=a['SR14']['rn'],rsr15=a['SR15']['rn'],rsr16=a['SR16']['rn'],rsr17=a['SR17']['rn'],rsr18=a['SR18']['rn'],
            rsr21=a['SR21']['rn'],rsr22=a['SR22']['rn'],rsr23=a['SR23']['rn'],rsr24=a['SR24']['rn'],rsr25=a['SR25']['rn'],rsr26=a['SR26']['rn'],rsr27=a['SR27']['rn'],rsr28=a['SR28']['rn'],
## with the errors
            rsr01e=a['SR01']['re'],rsr02e=a['SR02']['re'],rsr03e=a['SR03']['re'],rsr04e=a['SR04']['re'],rsr05e=a['SR05']['re'],rsr06e=a['SR06']['re'],rsr07e=a['SR07']['re'],rsr08e=a['SR08']['re'],  
            rsr11e=a['SR11']['re'],rsr12e=a['SR12']['re'],rsr13e=a['SR13']['re'],rsr14e=a['SR14']['re'],rsr15e=a['SR15']['re'],rsr16e=a['SR16']['re'],rsr17e=a['SR17']['re'],rsr18e=a['SR18']['re'],
            rsr21e=a['SR21']['re'],rsr22e=a['SR22']['re'],rsr23e=a['SR23']['re'],rsr24e=a['SR24']['re'],rsr25e=a['SR25']['re'],rsr26e=a['SR26']['re'],rsr27e=a['SR27']['re'],rsr28e=a['SR28']['re'],
## total predicitons...
            tsr01=a['SR01']['t'],tsr02=a['SR02']['t'],tsr03=a['SR03']['t'],tsr04=a['SR04']['t'],tsr05=a['SR05']['t'],tsr06=a['SR06']['t'],tsr07=a['SR07']['t'],tsr08=a['SR08']['t'],  
            tsr11=a['SR11']['t'],tsr12=a['SR12']['t'],tsr13=a['SR13']['t'],tsr14=a['SR14']['t'],tsr15=a['SR15']['t'],tsr16=a['SR16']['t'],tsr17=a['SR17']['t'],tsr18=a['SR18']['t'],
            tsr21=a['SR21']['t'],tsr22=a['SR22']['t'],tsr23=a['SR23']['t'],tsr24=a['SR24']['t'],tsr25=a['SR25']['t'],tsr26=a['SR26']['t'],tsr27=a['SR27']['t'],tsr28=a['SR28']['t'],
## with the errors
            tsr01e=a['SR01']['te'],tsr02e=a['SR02']['te'],tsr03e=a['SR03']['te'],tsr04e=a['SR04']['te'],tsr05e=a['SR05']['te'],tsr06e=a['SR06']['te'],tsr07e=a['SR07']['te'],tsr08e=a['SR08']['te'],  
            tsr11e=a['SR11']['te'],tsr12e=a['SR12']['te'],tsr13e=a['SR13']['te'],tsr14e=a['SR14']['te'],tsr15e=a['SR15']['te'],tsr16e=a['SR16']['te'],tsr17e=a['SR17']['te'],tsr18e=a['SR18']['te'],
            tsr21e=a['SR21']['te'],tsr22e=a['SR22']['te'],tsr23e=a['SR23']['te'],tsr24e=a['SR24']['te'],tsr25e=a['SR25']['te'],tsr26e=a['SR26']['te'],tsr27e=a['SR27']['te'],tsr28e=a['SR28']['te']))

	h.close()


def makeTables2(list):
	if do3rdVeto:
		tabdir = 'tables_3rdVeto'
	else:
		tabdir = 'tables'
	o = {}
	for d in list:
		if not d['name'] == 'combined': continue
		srs = d.keys()
		for sr in srs:
			if sr is 'name': continue
			o[sr] = int(d[sr]['o'])

	x = list[0] # make sure this is UC
	y = list[1] # make sure this is UF
	a = list[2] # make sure this is the combined
			
	for d in list:
		if d['name'] == 'UC/FNAL':
			filename = tabdir+'/UCTable_lowpt.tex'
			caption = '\caption{Predicted and observed yields for the low-\pt analysis, UCSB/UCSD/FNAL.}'
			label   = '\label{tab:uctable_lowpt}'
		if d['name'] == 'UFL':
			filename = tabdir+'/UFTable_lowpt.tex'
			caption = '\caption{Predicted and observed yields for the low-\pt analysis, UFL.}'
			label   = '\label{tab:uftable_lowpt}'
		if d['name'] == 'combined':
			filename = tabdir+'/combTable_lowpt.tex'
			caption = '\caption{Predicted and observed yields for the low-\pt analysis after combining the two groups.}'
			label   = '\label{tab:combtable_lowpt}'
		f= open(filename, 'w')
		f. write('''
\\begin{{table}}
\\begin{{center}}
{cap}
{lab}
\\begin{{tabular}}{{|c|c|c|c|c|l|c|}}
\\hline
NBjets                              & MET                            & NJets                             & HT      & SR & Predicted          & Observed \\\\ \\hline
\\multirow{{8}}{{*}}{{$=0$}}        & \\multirow{{4}}{{*}}{{50-120}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 1  & {sr01} $\pm$ {sr01e} & {sr01_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 2  & {sr02} $\pm$ {sr02e} & {sr02_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 3  & {sr03} $\pm$ {sr03e} & {sr03_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 4  & {sr04} $\pm$ {sr04e} & {sr04_o} \\\\ \\cline{{2-5}}
                                    & \\multirow{{4}}{{*}}{{$>120$}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 5  & {sr05} $\pm$ {sr05e} & {sr05_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 6  & {sr06} $\pm$ {sr06e} & {sr06_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 7  & {sr07} $\pm$ {sr07e} & {sr07_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 8  & {sr08} $\pm$ {sr08e} & {sr08_o} \\\\ \\hline
                                                                                                                                          
\\multirow{{8}}{{*}}{{$=1$}}        & \\multirow{{4}}{{*}}{{50-120}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 11 & {sr11} $\pm$ {sr11e} & {sr11_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 12 & {sr12} $\pm$ {sr12e} & {sr12_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 13 & {sr13} $\pm$ {sr13e} & {sr13_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 14 & {sr14} $\pm$ {sr14e} & {sr14_o} \\\\ \\cline{{2-5}}
                                    & \\multirow{{4}}{{*}}{{$>120$}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 15 & {sr15} $\pm$ {sr15e} & {sr15_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 16 & {sr16} $\pm$ {sr16e} & {sr16_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 17 & {sr17} $\pm$ {sr17e} & {sr17_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 18 & {sr18} $\pm$ {sr18e} & {sr18_o} \\\\ \\hline
                                                                                                                                          
\\multirow{{8}}{{*}}{{$\\geq 2$}}   & \\multirow{{4}}{{*}}{{50-120}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 21 & {sr21} $\pm$ {sr21e} & {sr21_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 22 & {sr22} $\pm$ {sr22e} & {sr22_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 23 & {sr23} $\pm$ {sr23e} & {sr23_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 24 & {sr24} $\pm$ {sr24e} & {sr24_o} \\\\ \\cline{{2-5}}
                                    & \\multirow{{4}}{{*}}{{$>120$}} & \\multirow{{2}}{{*}}{{2-4}}       & 200-400 & 25 & {sr25} $\pm$ {sr25e} & {sr25_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 26 & {sr26} $\pm$ {sr26e} & {sr26_o} \\\\ \\cline{{3-5}}
                                    &                                & \\multirow{{2}}{{*}}{{$\\geq 4$}} & 200-400 & 27 & {sr27} $\pm$ {sr27e} & {sr27_o} \\\\ \\cline{{4-5}}
                                    &                                &                                   & $>400$  & 28 & {sr28} $\pm$ {sr28e} & {sr28_o} \\\\ \\hline

\\end{{tabular}}
\\end{{center}}
\\end{{table}}

'''.format( cap=caption, lab=label,
    sr01_o=o['SR01'],sr02_o=o['SR02'],sr03_o=o['SR03'],sr04_o=o['SR04'],sr05_o=o['SR05'],sr06_o=o['SR06'],sr07_o=o['SR07'],sr08_o=o['SR08'],  
    sr11_o=o['SR11'],sr12_o=o['SR12'],sr13_o=o['SR13'],sr14_o=o['SR14'],sr15_o=o['SR15'],sr16_o=o['SR16'],sr17_o=o['SR17'],sr18_o=o['SR18'],
    sr21_o=o['SR21'],sr22_o=o['SR22'],sr23_o=o['SR23'],sr24_o=o['SR24'],sr25_o=o['SR25'],sr26_o=o['SR26'],sr27_o=o['SR27'],sr28_o=o['SR28'],
## and the predicitons...
    sr01=d['SR01']['t'],sr02=d['SR02']['t'],sr03=d['SR03']['t'],sr04=d['SR04']['t'],sr05=d['SR05']['t'],sr06=d['SR06']['t'],sr07=d['SR07']['t'],sr08=d['SR08']['t'],  
    sr11=d['SR11']['t'],sr12=d['SR12']['t'],sr13=d['SR13']['t'],sr14=d['SR14']['t'],sr15=d['SR15']['t'],sr16=d['SR16']['t'],sr17=d['SR17']['t'],sr18=d['SR18']['t'],
    sr21=d['SR21']['t'],sr22=d['SR22']['t'],sr23=d['SR23']['t'],sr24=d['SR24']['t'],sr25=d['SR25']['t'],sr26=d['SR26']['t'],sr27=d['SR27']['t'],sr28=d['SR28']['t'],
## with errors
    sr01e=d['SR01']['te'],sr02e=d['SR02']['te'],sr03e=d['SR03']['te'],sr04e=d['SR04']['te'],sr05e=d['SR05']['te'],sr06e=d['SR06']['te'],sr07e=d['SR07']['te'],sr08e=d['SR08']['te'],  
    sr11e=d['SR11']['te'],sr12e=d['SR12']['te'],sr13e=d['SR13']['te'],sr14e=d['SR14']['te'],sr15e=d['SR15']['te'],sr16e=d['SR16']['te'],sr17e=d['SR17']['te'],sr18e=d['SR18']['te'],
    sr21e=d['SR21']['te'],sr22e=d['SR22']['te'],sr23e=d['SR23']['te'],sr24e=d['SR24']['te'],sr25e=d['SR25']['te'],sr26e=d['SR26']['te'],sr27e=d['SR27']['te'],sr28e=d['SR28']['te']))

	f.close()
	## make a table that puts the has all three groups
	filename = tabdir+'/ComboTable_lowpt.tex'
	caption = '\caption{Predicted and observed yields for the low-\pt analysis, UC/FNAL and UFL only.}'
	label   = '\label{tab:combotable_lowpt}'
	g = open(filename ,'w')
	g. write('''
\\begin{{table}}
\\begin{{center}}
{cap}
{lab}
\\begin{{tabular}}{{|c|rcl|rcl|c|}}
\\hline
SR & \\multicolumn{{3}}{{|c|}}{{UC/FNAL}}      & \\multicolumn{{3}}{{|c|}}{{UFL}}       & Observed \\\\ \\hline
1  & {ucsr01} & $\pm$ & {ucsr01e} & {ufsr01} & $\pm$ & {ufsr01e} &  {sr01_o} \\\\ \\hline
2  & {ucsr02} & $\pm$ & {ucsr02e} & {ufsr02} & $\pm$ & {ufsr02e} &  {sr02_o} \\\\ \\hline
3  & {ucsr03} & $\pm$ & {ucsr03e} & {ufsr03} & $\pm$ & {ufsr03e} &  {sr03_o} \\\\ \\hline
4  & {ucsr04} & $\pm$ & {ucsr04e} & {ufsr04} & $\pm$ & {ufsr04e} &  {sr04_o} \\\\ \\hline
5  & {ucsr05} & $\pm$ & {ucsr05e} & {ufsr05} & $\pm$ & {ufsr05e} &  {sr05_o} \\\\ \\hline
6  & {ucsr06} & $\pm$ & {ucsr06e} & {ufsr06} & $\pm$ & {ufsr06e} &  {sr06_o} \\\\ \\hline
7  & {ucsr07} & $\pm$ & {ucsr07e} & {ufsr07} & $\pm$ & {ufsr07e} &  {sr07_o} \\\\ \\hline
8  & {ucsr08} & $\pm$ & {ucsr08e} & {ufsr08} & $\pm$ & {ufsr08e} &  {sr08_o} \\\\ \\hline

11 & {ucsr11} & $\pm$ & {ucsr11e} & {ufsr11} & $\pm$ & {ufsr11e} &  {sr11_o} \\\\ \\hline
12 & {ucsr12} & $\pm$ & {ucsr12e} & {ufsr12} & $\pm$ & {ufsr12e} &  {sr12_o} \\\\ \\hline
13 & {ucsr13} & $\pm$ & {ucsr13e} & {ufsr13} & $\pm$ & {ufsr13e} &  {sr13_o} \\\\ \\hline
14 & {ucsr14} & $\pm$ & {ucsr14e} & {ufsr14} & $\pm$ & {ufsr14e} &  {sr14_o} \\\\ \\hline
15 & {ucsr15} & $\pm$ & {ucsr15e} & {ufsr15} & $\pm$ & {ufsr15e} &  {sr15_o} \\\\ \\hline
16 & {ucsr16} & $\pm$ & {ucsr16e} & {ufsr16} & $\pm$ & {ufsr16e} &  {sr16_o} \\\\ \\hline
17 & {ucsr17} & $\pm$ & {ucsr17e} & {ufsr17} & $\pm$ & {ufsr17e} &  {sr17_o} \\\\ \\hline
18 & {ucsr18} & $\pm$ & {ucsr18e} & {ufsr18} & $\pm$ & {ufsr18e} &  {sr18_o} \\\\ \\hline

21 & {ucsr21} & $\pm$ & {ucsr21e} & {ufsr21} & $\pm$ & {ufsr21e} &  {sr21_o} \\\\ \\hline
22 & {ucsr22} & $\pm$ & {ucsr22e} & {ufsr22} & $\pm$ & {ufsr22e} &  {sr22_o} \\\\ \\hline
23 & {ucsr23} & $\pm$ & {ucsr23e} & {ufsr23} & $\pm$ & {ufsr23e} &  {sr23_o} \\\\ \\hline
24 & {ucsr24} & $\pm$ & {ucsr24e} & {ufsr24} & $\pm$ & {ufsr24e} &  {sr24_o} \\\\ \\hline
25 & {ucsr25} & $\pm$ & {ucsr25e} & {ufsr25} & $\pm$ & {ufsr25e} &  {sr25_o} \\\\ \\hline
26 & {ucsr26} & $\pm$ & {ucsr26e} & {ufsr26} & $\pm$ & {ufsr26e} &  {sr26_o} \\\\ \\hline
27 & {ucsr27} & $\pm$ & {ucsr27e} & {ufsr27} & $\pm$ & {ufsr27e} &  {sr27_o} \\\\ \\hline
28 & {ucsr28} & $\pm$ & {ucsr28e} & {ufsr28} & $\pm$ & {ufsr28e} &  {sr28_o} \\\\ \\hline

\\end{{tabular}}
\\end{{center}}
\\end{{table}}

'''.format( cap=caption, lab=label,
## observed
    sr01_o=o['SR01'],sr02_o=o['SR02'],sr03_o=o['SR03'],sr04_o=o['SR04'],sr05_o=o['SR05'],sr06_o=o['SR06'],sr07_o=o['SR07'],sr08_o=o['SR08'],  
    sr11_o=o['SR11'],sr12_o=o['SR12'],sr13_o=o['SR13'],sr14_o=o['SR14'],sr15_o=o['SR15'],sr16_o=o['SR16'],sr17_o=o['SR17'],sr18_o=o['SR18'],
    sr21_o=o['SR21'],sr22_o=o['SR22'],sr23_o=o['SR23'],sr24_o=o['SR24'],sr25_o=o['SR25'],sr26_o=o['SR26'],sr27_o=o['SR27'],sr28_o=o['SR28'],
## Uredicitons...
    ucsr01=x['SR01']['t'],ucsr02=x['SR02']['t'],ucsr03=x['SR03']['t'],ucsr04=x['SR04']['t'],ucsr05=x['SR05']['t'],ucsr06=x['SR06']['t'],ucsr07=x['SR07']['t'],ucsr08=x['SR08']['t'],  
    ucsr11=x['SR11']['t'],ucsr12=x['SR12']['t'],ucsr13=x['SR13']['t'],ucsr14=x['SR14']['t'],ucsr15=x['SR15']['t'],ucsr16=x['SR16']['t'],ucsr17=x['SR17']['t'],ucsr18=x['SR18']['t'],
    ucsr21=x['SR21']['t'],ucsr22=x['SR22']['t'],ucsr23=x['SR23']['t'],ucsr24=x['SR24']['t'],ucsr25=x['SR25']['t'],ucsr26=x['SR26']['t'],ucsr27=x['SR27']['t'],ucsr28=x['SR28']['t'],
## werrors
    ucsr01e=x['SR01']['te'],ucsr02e=x['SR02']['te'],ucsr03e=x['SR03']['te'],ucsr04e=x['SR04']['te'],ucsr05e=x['SR05']['te'],ucsr06e=x['SR06']['te'],ucsr07e=x['SR07']['te'],ucsr08e=x['SR08']['te'],  
    ucsr11e=x['SR11']['te'],ucsr12e=x['SR12']['te'],ucsr13e=x['SR13']['te'],ucsr14e=x['SR14']['te'],ucsr15e=x['SR15']['te'],ucsr16e=x['SR16']['te'],ucsr17e=x['SR17']['te'],ucsr18e=x['SR18']['te'],
    ucsr21e=x['SR21']['te'],ucsr22e=x['SR22']['te'],ucsr23e=x['SR23']['te'],ucsr24e=x['SR24']['te'],ucsr25e=x['SR25']['te'],ucsr26e=x['SR26']['te'],ucsr27e=x['SR27']['te'],ucsr28e=x['SR28']['te'],
## Uctions
    ufsr01=y['SR01']['t'],ufsr02=y['SR02']['t'],ufsr03=y['SR03']['t'],ufsr04=y['SR04']['t'],ufsr05=y['SR05']['t'],ufsr06=y['SR06']['t'],ufsr07=y['SR07']['t'],ufsr08=y['SR08']['t'],  
    ufsr11=y['SR11']['t'],ufsr12=y['SR12']['t'],ufsr13=y['SR13']['t'],ufsr14=y['SR14']['t'],ufsr15=y['SR15']['t'],ufsr16=y['SR16']['t'],ufsr17=y['SR17']['t'],ufsr18=y['SR18']['t'],
    ufsr21=y['SR21']['t'],ufsr22=y['SR22']['t'],ufsr23=y['SR23']['t'],ufsr24=y['SR24']['t'],ufsr25=y['SR25']['t'],ufsr26=y['SR26']['t'],ufsr27=y['SR27']['t'],ufsr28=y['SR28']['t'],
## werrors
    ufsr01e=y['SR01']['te'],ufsr02e=y['SR02']['te'],ufsr03e=y['SR03']['te'],ufsr04e=y['SR04']['te'],ufsr05e=y['SR05']['te'],ufsr06e=y['SR06']['te'],ufsr07e=y['SR07']['te'],ufsr08e=y['SR08']['te'],  
    ufsr11e=y['SR11']['te'],ufsr12e=y['SR12']['te'],ufsr13e=y['SR13']['te'],ufsr14e=y['SR14']['te'],ufsr15e=y['SR15']['te'],ufsr16e=y['SR16']['te'],ufsr17e=y['SR17']['te'],ufsr18e=y['SR18']['te'],
    ufsr21e=y['SR21']['te'],ufsr22e=y['SR22']['te'],ufsr23e=y['SR23']['te'],ufsr24e=y['SR24']['te'],ufsr25e=y['SR25']['te'],ufsr26e=y['SR26']['te'],ufsr27e=y['SR27']['te'],ufsr28e=y['SR28']['te']))

	g.close()
	## make a table that has the has all three backgrounds
	filename = tabdir+'/splitTable_lowpt.tex'
	caption = '\caption{Predicted and observed yields for the low-\pt analysis, different background sources.}'
	label   = '\label{tab:splittable_lowpt}'
	h = open(filename ,'w')
	h. write('''
\\begin{{table}}
\\begin{{center}}
{cap}
{lab}
\\begin{{tabular}}{{|c|rcl|rcl|rcl|rcl|c|}}
\\hline
SR & \\multicolumn{{3}}{{|c|}}{{Fakes}}   & \\multicolumn{{3}}{{|c|}}{{Flips}} & \\multicolumn{{3}}{{|c|}}{{Rares}}  & \\multicolumn{{3}}{{|c|}}{{Total}}  & Observed \\\\ \\hline
1  & {fsr01} & $\pm$ & {fsr01e} & {csr01} & $\pm$ & {csr01e} & {rsr01} & $\pm$ & {rsr01e} & {tsr01} & $\pm$ & {tsr01e} & {sr01_o} \\\\ \\hline
2  & {fsr02} & $\pm$ & {fsr02e} & {csr02} & $\pm$ & {csr02e} & {rsr02} & $\pm$ & {rsr02e} & {tsr02} & $\pm$ & {tsr02e} & {sr02_o} \\\\ \\hline
3  & {fsr03} & $\pm$ & {fsr03e} & {csr03} & $\pm$ & {csr03e} & {rsr03} & $\pm$ & {rsr03e} & {tsr03} & $\pm$ & {tsr03e} & {sr03_o} \\\\ \\hline
4  & {fsr04} & $\pm$ & {fsr04e} & {csr04} & $\pm$ & {csr04e} & {rsr04} & $\pm$ & {rsr04e} & {tsr04} & $\pm$ & {tsr04e} & {sr04_o} \\\\ \\hline
5  & {fsr05} & $\pm$ & {fsr05e} & {csr05} & $\pm$ & {csr05e} & {rsr05} & $\pm$ & {rsr05e} & {tsr05} & $\pm$ & {tsr05e} & {sr05_o} \\\\ \\hline
6  & {fsr06} & $\pm$ & {fsr06e} & {csr06} & $\pm$ & {csr06e} & {rsr06} & $\pm$ & {rsr06e} & {tsr06} & $\pm$ & {tsr06e} & {sr06_o} \\\\ \\hline
7  & {fsr07} & $\pm$ & {fsr07e} & {csr07} & $\pm$ & {csr07e} & {rsr07} & $\pm$ & {rsr07e} & {tsr07} & $\pm$ & {tsr07e} & {sr07_o} \\\\ \\hline
8  & {fsr08} & $\pm$ & {fsr08e} & {csr08} & $\pm$ & {csr08e} & {rsr08} & $\pm$ & {rsr08e} & {tsr08} & $\pm$ & {tsr08e} & {sr08_o} \\\\ \\hline
                                                                                         
11 & {fsr11} & $\pm$ & {fsr11e} & {csr11} & $\pm$ & {csr11e} & {rsr11} & $\pm$ & {rsr11e} & {tsr11} & $\pm$ & {tsr11e} & {sr11_o} \\\\ \\hline
12 & {fsr12} & $\pm$ & {fsr12e} & {csr12} & $\pm$ & {csr12e} & {rsr12} & $\pm$ & {rsr12e} & {tsr12} & $\pm$ & {tsr12e} & {sr12_o} \\\\ \\hline
13 & {fsr13} & $\pm$ & {fsr13e} & {csr13} & $\pm$ & {csr13e} & {rsr13} & $\pm$ & {rsr13e} & {tsr13} & $\pm$ & {tsr13e} & {sr13_o} \\\\ \\hline
14 & {fsr14} & $\pm$ & {fsr14e} & {csr14} & $\pm$ & {csr14e} & {rsr14} & $\pm$ & {rsr14e} & {tsr14} & $\pm$ & {tsr14e} & {sr14_o} \\\\ \\hline
15 & {fsr15} & $\pm$ & {fsr15e} & {csr15} & $\pm$ & {csr15e} & {rsr15} & $\pm$ & {rsr15e} & {tsr15} & $\pm$ & {tsr15e} & {sr15_o} \\\\ \\hline
16 & {fsr16} & $\pm$ & {fsr16e} & {csr16} & $\pm$ & {csr16e} & {rsr16} & $\pm$ & {rsr16e} & {tsr16} & $\pm$ & {tsr16e} & {sr16_o} \\\\ \\hline
17 & {fsr17} & $\pm$ & {fsr17e} & {csr17} & $\pm$ & {csr17e} & {rsr17} & $\pm$ & {rsr17e} & {tsr17} & $\pm$ & {tsr17e} & {sr17_o} \\\\ \\hline
18 & {fsr18} & $\pm$ & {fsr18e} & {csr18} & $\pm$ & {csr18e} & {rsr18} & $\pm$ & {rsr18e} & {tsr18} & $\pm$ & {tsr18e} & {sr18_o} \\\\ \\hline
                                                                                         
21 & {fsr21} & $\pm$ & {fsr21e} & {csr21} & $\pm$ & {csr21e} & {rsr21} & $\pm$ & {rsr21e} & {tsr21} & $\pm$ & {tsr21e} & {sr21_o} \\\\ \\hline
22 & {fsr22} & $\pm$ & {fsr22e} & {csr22} & $\pm$ & {csr22e} & {rsr22} & $\pm$ & {rsr22e} & {tsr22} & $\pm$ & {tsr22e} & {sr22_o} \\\\ \\hline
23 & {fsr23} & $\pm$ & {fsr23e} & {csr23} & $\pm$ & {csr23e} & {rsr23} & $\pm$ & {rsr23e} & {tsr23} & $\pm$ & {tsr23e} & {sr23_o} \\\\ \\hline
24 & {fsr24} & $\pm$ & {fsr24e} & {csr24} & $\pm$ & {csr24e} & {rsr24} & $\pm$ & {rsr24e} & {tsr24} & $\pm$ & {tsr24e} & {sr24_o} \\\\ \\hline
25 & {fsr25} & $\pm$ & {fsr25e} & {csr25} & $\pm$ & {csr25e} & {rsr25} & $\pm$ & {rsr25e} & {tsr25} & $\pm$ & {tsr25e} & {sr25_o} \\\\ \\hline
26 & {fsr26} & $\pm$ & {fsr26e} & {csr26} & $\pm$ & {csr26e} & {rsr26} & $\pm$ & {rsr26e} & {tsr26} & $\pm$ & {tsr26e} & {sr26_o} \\\\ \\hline
27 & {fsr27} & $\pm$ & {fsr27e} & {csr27} & $\pm$ & {csr27e} & {rsr27} & $\pm$ & {rsr27e} & {tsr27} & $\pm$ & {tsr27e} & {sr27_o} \\\\ \\hline
28 & {fsr28} & $\pm$ & {fsr28e} & {csr28} & $\pm$ & {csr28e} & {rsr28} & $\pm$ & {rsr28e} & {tsr28} & $\pm$ & {tsr28e} & {sr28_o} \\\\ \\hline

\\end{{tabular}}
\\end{{center}}
\\end{{table}}

'''.format( cap=caption, lab=label,
    sr01_o=o['SR01'],sr02_o=o['SR02'],sr03_o=o['SR03'],sr04_o=o['SR04'],sr05_o=o['SR05'],sr06_o=o['SR06'],sr07_o=o['SR07'],sr08_o=o['SR08'],  
    sr11_o=o['SR11'],sr12_o=o['SR12'],sr13_o=o['SR13'],sr14_o=o['SR14'],sr15_o=o['SR15'],sr16_o=o['SR16'],sr17_o=o['SR17'],sr18_o=o['SR18'],
    sr21_o=o['SR21'],sr22_o=o['SR22'],sr23_o=o['SR23'],sr24_o=o['SR24'],sr25_o=o['SR25'],sr26_o=o['SR26'],sr27_o=o['SR27'],sr28_o=o['SR28'],
## ficitons...
    fsr01=a['SR01']['fn'],fsr02=a['SR02']['fn'],fsr03=a['SR03']['fn'],fsr04=a['SR04']['fn'],fsr05=a['SR05']['fn'],fsr06=a['SR06']['fn'],fsr07=a['SR07']['fn'],fsr08=a['SR08']['fn'],  
    fsr11=a['SR11']['fn'],fsr12=a['SR12']['fn'],fsr13=a['SR13']['fn'],fsr14=a['SR14']['fn'],fsr15=a['SR15']['fn'],fsr16=a['SR16']['fn'],fsr17=a['SR17']['fn'],fsr18=a['SR18']['fn'],
    fsr21=a['SR21']['fn'],fsr22=a['SR22']['fn'],fsr23=a['SR23']['fn'],fsr24=a['SR24']['fn'],fsr25=a['SR25']['fn'],fsr26=a['SR26']['fn'],fsr27=a['SR27']['fn'],fsr28=a['SR28']['fn'],
## werrors
    fsr01e=a['SR01']['fe'],fsr02e=a['SR02']['fe'],fsr03e=a['SR03']['fe'],fsr04e=a['SR04']['fe'],fsr05e=a['SR05']['fe'],fsr06e=a['SR06']['fe'],fsr07e=a['SR07']['fe'],fsr08e=a['SR08']['fe'],  
    fsr11e=a['SR11']['fe'],fsr12e=a['SR12']['fe'],fsr13e=a['SR13']['fe'],fsr14e=a['SR14']['fe'],fsr15e=a['SR15']['fe'],fsr16e=a['SR16']['fe'],fsr17e=a['SR17']['fe'],fsr18e=a['SR18']['fe'],
    fsr21e=a['SR21']['fe'],fsr22e=a['SR22']['fe'],fsr23e=a['SR23']['fe'],fsr24e=a['SR24']['fe'],fsr25e=a['SR25']['fe'],fsr26e=a['SR26']['fe'],fsr27e=a['SR27']['fe'],fsr28e=a['SR28']['fe'],
## fictions
    csr01=a['SR01']['cn'],csr02=a['SR02']['cn'],csr03=a['SR03']['cn'],csr04=a['SR04']['cn'],csr05=a['SR05']['cn'],csr06=a['SR06']['cn'],csr07=a['SR07']['cn'],csr08=a['SR08']['cn'],  
    csr11=a['SR11']['cn'],csr12=a['SR12']['cn'],csr13=a['SR13']['cn'],csr14=a['SR14']['cn'],csr15=a['SR15']['cn'],csr16=a['SR16']['cn'],csr17=a['SR17']['cn'],csr18=a['SR18']['cn'],
    csr21=a['SR21']['cn'],csr22=a['SR22']['cn'],csr23=a['SR23']['cn'],csr24=a['SR24']['cn'],csr25=a['SR25']['cn'],csr26=a['SR26']['cn'],csr27=a['SR27']['cn'],csr28=a['SR28']['cn'],
## werrors
    csr01e=a['SR01']['ce'],csr02e=a['SR02']['ce'],csr03e=a['SR03']['ce'],csr04e=a['SR04']['ce'],csr05e=a['SR05']['ce'],csr06e=a['SR06']['ce'],csr07e=a['SR07']['ce'],csr08e=a['SR08']['ce'],  
    csr11e=a['SR11']['ce'],csr12e=a['SR12']['ce'],csr13e=a['SR13']['ce'],csr14e=a['SR14']['ce'],csr15e=a['SR15']['ce'],csr16e=a['SR16']['ce'],csr17e=a['SR17']['ce'],csr18e=a['SR18']['ce'],
    csr21e=a['SR21']['ce'],csr22e=a['SR22']['ce'],csr23e=a['SR23']['ce'],csr24e=a['SR24']['ce'],csr25e=a['SR25']['ce'],csr26e=a['SR26']['ce'],csr27e=a['SR27']['ce'],csr28e=a['SR28']['ce'],
## ricitons...
    rsr01=a['SR01']['rn'],rsr02=a['SR02']['rn'],rsr03=a['SR03']['rn'],rsr04=a['SR04']['rn'],rsr05=a['SR05']['rn'],rsr06=a['SR06']['rn'],rsr07=a['SR07']['rn'],rsr08=a['SR08']['rn'],  
    rsr11=a['SR11']['rn'],rsr12=a['SR12']['rn'],rsr13=a['SR13']['rn'],rsr14=a['SR14']['rn'],rsr15=a['SR15']['rn'],rsr16=a['SR16']['rn'],rsr17=a['SR17']['rn'],rsr18=a['SR18']['rn'],
    rsr21=a['SR21']['rn'],rsr22=a['SR22']['rn'],rsr23=a['SR23']['rn'],rsr24=a['SR24']['rn'],rsr25=a['SR25']['rn'],rsr26=a['SR26']['rn'],rsr27=a['SR27']['rn'],rsr28=a['SR28']['rn'],
## werrors
    rsr01e=a['SR01']['re'],rsr02e=a['SR02']['re'],rsr03e=a['SR03']['re'],rsr04e=a['SR04']['re'],rsr05e=a['SR05']['re'],rsr06e=a['SR06']['re'],rsr07e=a['SR07']['re'],rsr08e=a['SR08']['re'],  
    rsr11e=a['SR11']['re'],rsr12e=a['SR12']['re'],rsr13e=a['SR13']['re'],rsr14e=a['SR14']['re'],rsr15e=a['SR15']['re'],rsr16e=a['SR16']['re'],rsr17e=a['SR17']['re'],rsr18e=a['SR18']['re'],
    rsr21e=a['SR21']['re'],rsr22e=a['SR22']['re'],rsr23e=a['SR23']['re'],rsr24e=a['SR24']['re'],rsr25e=a['SR25']['re'],rsr26e=a['SR26']['re'],rsr27e=a['SR27']['re'],rsr28e=a['SR28']['re'],
## tdicitons...
    tsr01=a['SR01']['t'],tsr02=a['SR02']['t'],tsr03=a['SR03']['t'],tsr04=a['SR04']['t'],tsr05=a['SR05']['t'],tsr06=a['SR06']['t'],tsr07=a['SR07']['t'],tsr08=a['SR08']['t'],  
    tsr11=a['SR11']['t'],tsr12=a['SR12']['t'],tsr13=a['SR13']['t'],tsr14=a['SR14']['t'],tsr15=a['SR15']['t'],tsr16=a['SR16']['t'],tsr17=a['SR17']['t'],tsr18=a['SR18']['t'],
    tsr21=a['SR21']['t'],tsr22=a['SR22']['t'],tsr23=a['SR23']['t'],tsr24=a['SR24']['t'],tsr25=a['SR25']['t'],tsr26=a['SR26']['t'],tsr27=a['SR27']['t'],tsr28=a['SR28']['t'],
## werrors
    tsr01e=a['SR01']['te'],tsr02e=a['SR02']['te'],tsr03e=a['SR03']['te'],tsr04e=a['SR04']['te'],tsr05e=a['SR05']['te'],tsr06e=a['SR06']['te'],tsr07e=a['SR07']['te'],tsr08e=a['SR08']['te'],  
    tsr11e=a['SR11']['te'],tsr12e=a['SR12']['te'],tsr13e=a['SR13']['te'],tsr14e=a['SR14']['te'],tsr15e=a['SR15']['te'],tsr16e=a['SR16']['te'],tsr17e=a['SR17']['te'],tsr18e=a['SR18']['te'],
    tsr21e=a['SR21']['te'],tsr22e=a['SR22']['te'],tsr23e=a['SR23']['te'],tsr24e=a['SR24']['te'],tsr25e=a['SR25']['te'],tsr26e=a['SR26']['te'],tsr27e=a['SR27']['te'],tsr28e=a['SR28']['te']))

	h.close()

def makeSpecialTables(list):
	if do3rdVeto:
		tabdir = 'tables_3rdVeto'
	else:
		tabdir = 'tables'
	o = {}
	for d in list:
		if not d['name'] == 'combined': continue
		srs = d.keys()
		for sr in srs:
			if sr is 'name': continue
			o[sr] = int(d[sr]['o'])

	x = list[0] # make sure this is UC
	y = list[1] # make sure this is UF
	z = list[2] # make sure this is EO
	a = list[3] # make sure this is the combined
			
	## make a table that puts the has all three groups
	filename = tabdir+'/ComboTable_special.tex'
	caption = '\caption{Predicted and observed yields for the SS-top and RPV regions. Note that UFL cannot provide fake predictions for SRs 30, 31, 34 and 35.}'
	label   = '\label{tab:combotable_special}'
	g = open(filename ,'w')
	g. write('''
\\begin{{table}}
\\begin{{center}}
{cap}
{lab}
\\begin{{tabular}}{{|c|rcl|rcl|rcl|c|}}
\\hline
SR        & \\multicolumn{{3}}{{|c|}}{{UC/FNAL}} & \\multicolumn{{3}}{{|c|}}{{UFL}}  & \\multicolumn{{3}}{{|c|}}{{ETH/Oviedo}}  & Observed \\\\ \\hline
30 (SS-1) & {ucsr30} & $\pm$ & {ucsr30e}         & \\multicolumn{{3}}{{|c|}}{{---}}  & {eosr30} & $\pm$ & {eosr30e}             & {sr30_o} \\\\ \\hline
31 (SS-2) & {ucsr31} & $\pm$ & {ucsr31e}         & \\multicolumn{{3}}{{|c|}}{{---}}  & {eosr31} & $\pm$ & {eosr31e}             & {sr31_o} \\\\ \\hline
34 (SS-3) & {ucsr34} & $\pm$ & {ucsr34e}         & \\multicolumn{{3}}{{|c|}}{{---}}  & {eosr34} & $\pm$ & {eosr34e}             & {sr34_o} \\\\ \\hline
35 (SS-4) & {ucsr35} & $\pm$ & {ucsr35e}         & \\multicolumn{{3}}{{|c|}}{{---}}  & {eosr35} & $\pm$ & {eosr35e}             & {sr35_o} \\\\ \\hline
32 (RPV1) & {ucsr32} & $\pm$ & {ucsr32e}         & {ufsr32} & $\pm$ & {ufsr32e}      & {eosr32} & $\pm$ & {eosr32e}             & {sr32_o} \\\\ \\hline
33 (RPV2) & {ucsr33} & $\pm$ & {ucsr33e}         & {ufsr33} & $\pm$ & {ufsr33e}      & {eosr33} & $\pm$ & {eosr33e}             & {sr33_o} \\\\ \\hline
\\end{{tabular}}
\\end{{center}}
\\end{{table}}

'''.format( cap=caption, lab=label,
    sr30_o=o['SR30'],sr31_o=o['SR31'],sr34_o=o['SR34'],sr35_o=o['SR35'],sr32_o=o['SR32'],sr33_o=o['SR33'],
## UCFNAL predicitons...
    ucsr30=x['SR30']['t'],ucsr31=x['SR31']['t'],ucsr34=x['SR34']['t'],ucsr35=x['SR35']['t'],ucsr32=x['SR32']['t'],ucsr33=x['SR33']['t'],
## with errors
    ucsr30e=x['SR30']['te'],ucsr31e=x['SR31']['te'],ucsr34e=x['SR34']['te'],ucsr35e=x['SR35']['te'],ucsr32e=x['SR32']['te'],ucsr33e=x['SR33']['te'],
## UFL predictions
    ufsr30=y['SR30']['t'],ufsr31=y['SR31']['t'],ufsr34=y['SR34']['t'],ufsr35=y['SR35']['t'],ufsr32=y['SR32']['t'],ufsr33=y['SR33']['t'],ufsr05=y['SR05']['t'],
## with errors
    ufsr30e=y['SR30']['te'],ufsr31e=y['SR31']['te'],ufsr34e=y['SR34']['te'],ufsr35e=y['SR35']['te'],ufsr32e=y['SR32']['te'],ufsr33e=y['SR33']['te'],
## ETH/Oviedo predicitons...
    eosr30=z['SR30']['t'],eosr31=z['SR31']['t'],eosr34=z['SR34']['t'],eosr35=z['SR35']['t'],eosr32=z['SR32']['t'],eosr33=z['SR33']['t'],
## with errors
    eosr30e=z['SR30']['te'],eosr31e=z['SR31']['te'],eosr34e=z['SR34']['te'],eosr35e=z['SR35']['te'],eosr32e=z['SR32']['te'],eosr33e=z['SR33']['te']))

	g.close()
	## make a table that has the has all three backgrounds
	filename = tabdir+'/splitTable_special.tex'
	caption = '\caption{Predicted and observed yields for the SS-top and RPV regions. Fake predictions for SRs 31 and 35 exclude predictions from UFL.}'
	label   = '\label{tab:splittable_special}'
	h = open(filename ,'w')
	h. write('''
\\begin{{table}}
\\begin{{center}}
{cap}
{lab}
\\begin{{tabular}}{{|c|rcl|rcl|rcl|rcl|c|}}
\\hline
SR & \\multicolumn{{3}}{{|c|}}{{Fakes}}   & \\multicolumn{{3}}{{|c|}}{{Flips}} & \\multicolumn{{3}}{{|c|}}{{Rares}}  & \\multicolumn{{3}}{{|c|}}{{Total}}  & Observed \\\\ \\hline
30 (SS-1) & {fsr30} & $\pm$ & {fsr30e} & {csr30} & $\pm$ & {csr30e} & {rsr30} & $\pm$ & {rsr30e} & {tsr30} & $\pm$ & {tsr30e} & {sr30_o} \\\\ \\hline
31 (SS-1) & {fsr31} & $\pm$ & {fsr31e} & {csr31} & $\pm$ & {csr31e} & {rsr31} & $\pm$ & {rsr31e} & {tsr31} & $\pm$ & {tsr31e} & {sr31_o} \\\\ \\hline
34 (SS-1) & {fsr34} & $\pm$ & {fsr34e} & {csr34} & $\pm$ & {csr34e} & {rsr34} & $\pm$ & {rsr34e} & {tsr34} & $\pm$ & {tsr34e} & {sr34_o} \\\\ \\hline
35 (SS-2) & {fsr35} & $\pm$ & {fsr35e} & {csr35} & $\pm$ & {csr35e} & {rsr35} & $\pm$ & {rsr35e} & {tsr35} & $\pm$ & {tsr35e} & {sr35_o} \\\\ \\hline
32 (RPV1) & {fsr32} & $\pm$ & {fsr32e} & {csr32} & $\pm$ & {csr32e} & {rsr32} & $\pm$ & {rsr32e} & {tsr32} & $\pm$ & {tsr32e} & {sr32_o} \\\\ \\hline
33 (RPV2) & {fsr33} & $\pm$ & {fsr33e} & {csr33} & $\pm$ & {csr33e} & {rsr33} & $\pm$ & {rsr33e} & {tsr33} & $\pm$ & {tsr33e} & {sr33_o} \\\\ \\hline

\\end{{tabular}}
\\end{{center}}
\\end{{table}}

'''.format( cap=caption, lab=label,
            sr30_o   = o['SR30'], sr31_o   = o['SR31'], sr34_o   = o['SR34'], sr35_o       = o['SR35'],sr32_o       = o['SR32'],sr33_o       = o['SR33'],
## fake predicitons...
            fsr30    = a['SR30']['fn'], fsr31    = a['SR31']['fn'], fsr34    = a['SR34']['fn'],fsr35  = a['SR35']['fn'],fsr32  = a['SR32']['fn'],fsr33  = a['SR33']['fn'],
## with the errors
            fsr30e   = a['SR30']['fe'], fsr31e   = a['SR31']['fe'], fsr34e   = a['SR34']['fe'],fsr35e = a['SR35']['fe'],fsr32e = a['SR32']['fe'],fsr33e = a['SR33']['fe'],
## flip predictions
            csr30    = a['SR30']['cn'], csr31    = a['SR31']['cn'], csr34    = a['SR34']['cn'],csr35  = a['SR35']['cn'],csr32  = a['SR32']['cn'],csr33  = a['SR33']['cn'],
## with the errors
            csr30e   = a['SR30']['ce'], csr31e   = a['SR31']['ce'], csr34e   = a['SR34']['ce'],csr35e = a['SR35']['ce'],csr32e = a['SR32']['ce'],csr33e = a['SR33']['ce'],
## rare predicitons...
            rsr30    = a['SR30']['rn'], rsr31    = a['SR31']['rn'], rsr34    = a['SR34']['rn'],rsr35  = a['SR35']['rn'],rsr32  = a['SR32']['rn'],rsr33  = a['SR33']['rn'],
## with the errors
            rsr30e   = a['SR30']['re'], rsr31e   = a['SR31']['re'], rsr34e   = a['SR34']['re'],rsr35e = a['SR35']['re'],rsr32e = a['SR32']['re'],rsr33e = a['SR33']['re'],
## total predicitons...
            tsr30    = a['SR30']['t'], tsr31    = a['SR31']['t'], tsr34    = a['SR34']['t'],tsr35   = a['SR35']['t'],tsr32   = a['SR32']['t'],tsr33   = a['SR33']['t'],
## with the errors
            tsr30e   = a['SR30']['te'], tsr31e   = a['SR31']['te'], tsr34e   = a['SR34']['te'],tsr35e = a['SR35']['te'],tsr32e = a['SR32']['te'],tsr33e = a['SR33']['te']))

	h.close()


