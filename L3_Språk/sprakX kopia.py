vokaler = "aeiouåäöAEIOUÅÄÖ"
konsonant = "zxcvbnmsdfghjklqwrtpZXCVBNMSDFGHJKLQWRTP"

import time

val = 0

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
	utrad = "" 					#Definiera utrad
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

språk = [visk,rovar,fylle,bebis,alla,fikon]

while val != 8:
	print()
	print("Vilket språk önskas?")
	print()
	print("1 [Visk] 2 [Rövar] 3 [Fylle] 4 [Bebis]")
	print("5 [All] 6 [Fikon] 7 [Demonstration] 8 [Avsluta]")
	print()
	val = int(input())
	mening = str(input("Din mening"))
	print()
	print(språk[val-1](mening))

	if val == 7:
			print('"Får jag viska ditt namn?" i viskspråket')
			print(visk("Får jag viska ditt namn?"))
			print()
			print('"Att vara eller inte vara" i rövarspråket')
			print(rovar("Att vara eller inte vara"))
			print()
			print('"Blankett för ifyllan" i fyllespråket')
			print(fylle("Blankett för ifyllan"))
			print()
			print('"näringsrik mat är god" i bebisspråket')
			print(bebis("näringsrik mat är god"))
			print()
			print('"frostig vinter" i allspråket')
			print(alla("frostig vinter"))
			print()
			print('"anna och cissi springer en mil" i fikonspråket')
			print(fikon("anna och cissi springer en mil"))
	time.sleep(5)
print("Synd att du är så trist, vi ses nästa gång.")
print()



