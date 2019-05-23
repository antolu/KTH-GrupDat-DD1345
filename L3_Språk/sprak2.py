vokaler = "aeiouåäöAEIOUÅÄÖ"
konsonant = "zxcvbnmsdfghjklqwrtpZXCVBNMSDFGHJKLQWRTP"

def stjarnsprak(inrad):
	utrad = "" 					#Definiera utrad
	for tkn in inrad: 			#För varje bokstav i inrad
		utrad += tkn 			#Lägg till bokstaven i utrad
		utrad += ' '			#Lägg till
	return utrad

def visk(inrad):
	utrad = "" 					#Definiera utrad
	for tkn in inrad:
		if tkn in vokaler:		#Hoppa över tecknet om tecknet är en vokal
			pass
		else:					#Och hoppa inte över annars
			utrad += tkn
	return utrad

def rovar(inrad):
	utrad = "" 					#Definiera utrad
	for tkn in inrad:
		if tkn in konsonant:	#Om tecknet är en konsonant, lägg till tecknet, ett o och ytterligare ett tecken
			utrad += tkn 		
			utrad += "o"
			utrad += tkn
		else:
			utrad += tkn 		#Om inte konsonant, lägg till tecknet.
	return utrad

def fylle(inrad):
	utrad = "" #Definiera utrad
	for tkn in inrad:
		if tkn in vokaler:		#Om tecknet är en vokal, lägg två tecken med ett f i mellan
			utrad += tkn
			utrad += "f"
			utrad += tkn
		else:
			utrad += tkn 		#Annars lägg till värdet
	return utrad

def bebis(inrad):
	utrad = "" #Definiera utrad
	n = 0
	ord = inrad.split()			#Splitta textsträngen till element i en lista
	while n < len(ord):			#Så att processen itereras en gång för varje ord
		for tkn in ord[n]:		#Repetera för varje bokstav i n-ordet
			if tkn in vokaler:	#Om tecknet visar sg vara en vokal, lägg till den och avbryt
				utrad += tkn
				break
			else:
				utrad += tkn 	#Annars kör på
		ord[n] = 3*utrad		#Det nya ordet multipliceras med 3 och läggs tillbaka i listan
		utrad = ""
		n += 1					#Iterera för nästa ord
	
	return " ".join(ord)		#Sätt ihop meningen och returna

def alla(inrad):
	fram = "" #Definiera utrad
	n = 0
	ord = inrad.split()			#Splitta inraden
	while n < len(ord):			#Iterera för varje ord
		for tkn in ord[n]:
			if tkn in vokaler:	#Bryt innan vokal
				break
			else:
				fram += tkn
		ord[n] = ord[n].lstrip(fram) + fram + 'all'		#Nya ordet blir det gamla strippat av 'fram', som läggs till efter, och 'all' läggs till
		fram = ""	
		n += 1					#Iterera igen
	
	return " ".join(ord)

def fikon(inrad):
	fram = "" #Definiera utrad
	n = 0
	ord = inrad.split()
	while n < len(ord):			#Iterera för varje ord
		for tkn in ord[n]:
			if tkn in vokaler:
				fram += tkn 	#Skapa orddelen som ska flyttas
				break
			else:
				fram += tkn
		ord[n] = 'fi' + ord[n].lstrip(fram) + fram + 'kon'
		fram = ""
		n += 1
	
	return " ".join(ord)
