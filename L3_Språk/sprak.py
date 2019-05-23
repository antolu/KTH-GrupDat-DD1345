vokaler = "aeiouåäöAEIOUÅÄÖ"
konsonant = "zxcvbnmsdfghjklqwrtpZXCVBNMSDFGHJKLQWRTP"

def stjarnsprak(inrad):
	utrad = ""
	for tkn in inrad:
		utrad += tkn
		utrad += ' '
	return utrad

def visk(inrad):
	utrad = ""
	for tkn in inrad:
		if tkn in vokaler:
			pass
		else:
			utrad += tkn
	return utrad

def rovar(inrad):
	utrad = ""
	for tkn in inrad:
		if tkn in konsonant:
			utrad += tkn
			utrad += "o"
			utrad += tkn
		else:
			utrad += tkn
	return utrad

def fylle(inrad):
	utrad = ""
	for tkn in inrad:
		if tkn in vokaler:
			utrad += tkn
			utrad += "f"
			utrad += tkn
		else:
			utrad += tkn
	return utrad

def bebis(inrad):
	utrad = ""
	n = 0
	ord = inrad.split()
	while n < len(ord):
		for tkn in ord[n]:
			if tkn in vokaler:
				utrad += tkn
				break
			else:
				utrad += tkn
		ord[n] = 3*utrad
		utrad = ""
		n += 1
	
	return " ".join(ord)

def all(inrad):
	fram = ""
	n = 0
	r = 0
	ord = inrad.split()
	while n < len(ord):
		for tkn in ord[n]:
			if tkn in vokaler:
				break
			else:
				fram += tkn
				r += 1
		ord[n] = ord[n].lstrip(fram) + fram + 'all'
		fram = ""
		n += 1
	
	return " ".join(ord)

def fikon(inrad):
	fram = ""
	n = 0
	ord = inrad.split()
	while n < len(ord):
		for tkn in ord[n]:
			if tkn in vokaler:
				fram += tkn
				break
			else:
				fram += tkn
		ord[n] = 'fi' + ord[n].lstrip(fram) + fram + 'kon'
		fram = ""
		n += 1
	
	return " ".join(ord)
