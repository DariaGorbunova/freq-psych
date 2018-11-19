#!/usr/bin/python
# # -*- coding: utf8 -*-

import re

# reading and decoding input files
#textFile  = ["/home/darya/work/lingvo_data/sample2.txt"] 
textFile  = ["/home/darya/work/lingvo_data/Rasshifrovki_125-147.txt", 
             "/home/darya/work/lingvo_data/Rasshifrovki_do_I99.txt",  
             "/home/darya/work/lingvo_data/Rasshifrovki_I100-124.txt"] 
psychFile = "/home/darya/work/lingvo_data/PsyType.txt"

# create dictionaries
psychInf = {}
infWords = {}
comWords = {}
markWords = {}
numOfWordsInf = {}
numOfWordsCom = {}
numMarkWords = {}
numOfWordsPsych = {}
infReplicas = {}
comReplicas = {}

def readInfWords(text):
	print "readInfWords()"
	# print "first", text[0:10]
	
	# text normalization 
	#   - lowercase
	#   - remove all markup signs (time,paralinguistic signs with *)
	#clearData = re.sub(u"\w", "", text)
	#clearData = re.sub(u'[^\x00-\x7f]', '', clearData)
	clearData = re.sub(u"\r", "\n", text)
	#print "CLEAR 1 DATA start <", clearData, "> CLEAR DATA end"
	clearData = re.sub(u"/", "", clearData)
	clearData = re.sub(u"ord[0-9a-zA-Zа-яА-Я-]*([^0-9a-zA-Zа-яА-Я-])[ 0-9]*", "", clearData)
	clearData = re.sub(u"\*[а-яА-Я]+", "", clearData)
	clearData = re.sub(u"/", "", clearData)
	clearData = re.sub(u'[0-9]*:[0-9]+:[0-9]+\.[0-9]+', "", clearData)
	clearData = re.sub(u"@", "", clearData)
	clearData = re.sub(u"\?", "", clearData)
	clearData = re.sub(u"\!", "", clearData)
	clearData = re.sub(u"\(", "", clearData)
	clearData = re.sub(u"\)", "", clearData)
	clearData = re.sub(u"\+", "", clearData)
	clearData = re.sub(u"\:", "", clearData)
	clearData = re.sub(u"\.", "", clearData)
	clearData = re.sub(u"#", " ", clearData)
	clearData = re.sub(u"\*.", "", clearData)
	clearData = re.sub(u"и(\d+)", "s\\1", clearData)
	clearData = re.sub(u"(s\d+)","\n\\1 ", clearData)
	clearData = re.sub(u"[ \t]+"," ", clearData)
	clearData = re.sub(u"\n ","\n", clearData)
	clearData = re.sub(u" \n","\n", clearData)
	clearData = re.sub(u"\n+","\n", clearData)
	clearData = re.sub(u"frase-","", clearData)
	clearData = re.sub(u"speaker","", clearData)
	clearData = re.sub(u"frase","", clearData)
	clearData = re.sub(u"begin time","", clearData)
	clearData = re.sub(u" - ","", clearData)
	clearData = re.sub(u"hhmmssms","", clearData)
	clearData = re.sub(u"<с>","", clearData)
	clearData = re.sub(u"<к>","", clearData)

	#print clearData

	#   - define informant|communicant
	infMatcher= ""
	comMatcher = ""
	info = ""
	comm = ""
	lastPerson = ""
	infMatch = re.compile(u'([sи][0-9]+).*')
	comMatch = re.compile(u'([mwмрж][0-9]+).*')
	for line in clearData.split("\n"):
		#print "L: <%s>" % (line)
		#matching for informants and communicants
		isPersonFoundInLine = False
		infMatcher = infMatch.search(line)
		comMatcher = comMatch.search(line)
		if infMatcher:
			lastPerson = "informant"
			info = infMatcher.group(1)
			#print "New informant was found:", info
			isPersonFoundInLine = True
			if not info in numOfWordsInf:
				numOfWordsInf[info] = 0
				infWords[info] = []
				infReplicas[info] = []
		if comMatcher:
			lastPerson = "communicant"
			comm = comMatcher.group(1)
			#print "New communicant was found:", comm
			isPersonFoundInLine = True
			if not comm in numOfWordsCom:
				numOfWordsCom[comm] = 0
				comWords[comm] = []
				comReplicas[comm] = []

		#if isPersonFoundInLine == False:
			#print "Person is not found in line:", line
#1. add a new dict with a key = Inf, value = list of replics
#2. delete the loop with words, NumOfWords + number of words in line
			#print replica
			#FIXME
		words = line.split()
		if line != info:

		#if line == comm:
		# if len(words) > 0 :
		# 	print "First word is:   %s"% (words[0])
		# 	print "Line content is: %s"% (" ".join(words[1:]))
		# 	print words
		# 	print len(words) 

			if lastPerson == "informant":
				infReplicas[info].append(line)
						
			elif lastPerson  == "communicant":
				comReplicas[comm].append(line)
		

		
		# if word != info and word != comm:
		# 	if lastPerson == "informant":
		# 		numOfWordsInf[info] += 1
		# 		infWords[info].append(word)
		# 		#print "Number of words for %s = %s For word = {%s}" %(info, numOfWordsInf, word)
		# 	elif lastPerson  == "communicant":
		# 		numOfWordsCom[comm] += 1
		# 		comWords[comm].append(word)

		for word in line.split(" "):
			#print word 
			if word != info and word != comm:
				if lastPerson == "informant":
					numOfWordsInf[info] += 1
					infWords[info].append(word)
					#print "Number of words for %s = %s For word = {%s}" %(info, numOfWordsInf, word)
				elif lastPerson  == "communicant":
					numOfWordsCom[comm] += 1
					comWords[comm].append(word)
					#print "Number of words for %s = %s For word = {%s}" %(comm, numOfWordsCom, word)

	for key in numOfWordsInf:
		print "%-4s = %-3d words" % (key, numOfWordsInf[key])
		#sorted_dict = sorted(numOfWordsInf, key = numOfWordsInf.get, reverse = True)
		#print sorted_dict

	#sorted_dict = sorted(numOfWordsInf.items(), key = lambda x:x[1])
	#print  sorted_dict
	

	#for key in numOfWordsCom:
		#print "%-4s = %-3d words" % (key, numOfWordsCom[key])
	
					
				# else:
				# 	print "Error with", info 
				#print "Found matcher:", infMatcher.group(1)
	
	
				#print "Found matcher:", infMatcher.group(1)

	#   - compose full replica
	#   - tokenize replicas by spaces and punctuation
	#   - distribute words by dictionaries infWords and comWords 
	#   - count them in numOfWordsInf and numOfWordsCom

def sumNumOfWordsPsych():
	print "sumNumOfWordsPsych()"
	# read psychtype from file
	tFile = open(psychFile, "rt")
	text = tFile.read().decode("Windows 1251").lower()
	#print text
	data = re.split(u'\t|\n', text)
	
	len_data = len(data)
	for i in range(0,len_data,2):
		infNum = data[i]
		if infNum == "":
			continue
		pType = data[i+1]
		#print " Info:%s Psy:%s " % (infNum, pType)
	
		psychInf[infNum] = pType

	#get psychtype for every informant and add to numOfWordsPsych
	for infNum in numOfWordsInf:
		if infNum in psychInf: 
			pType = psychInf[infNum]
			numWords  = numOfWordsInf[infNum]
			if pType not in numOfWordsPsych:
				numOfWordsPsych[pType] = 0
			#print "add",numWords, "words for informant", infNum, "which is", pType
			numOfWordsPsych[pType] += numWords
	for key, value in numOfWordsPsych.iteritems():
		print value, " for ", key
		#print "                       %s %d words = " % (key.encode("UTF-8"),numOfWordsPsych[key])


		#numOfWordsPsych[pType] += numOfWordsInf
		#if infNum not in numOfWordsInf[infNum]:
			#numOfWordsPsych[pType] = 0
			

	#if info in data 
	# count number of words by psychotype in numOfWordsPsych

def printResult():
	print "printResult()"
	# print psychInf  
	# print infWords 
	#for key in infWords:
		# if key != "s125":
		# 	continue
		#print "================================", key, "\n", " ".join(infWords[key])
	#for key in comWords:
		# if key != "m1":
		# 	continue
		#print "================================", key, "\n", " ".join(comWords[key])
	
	for key in infReplicas:
		#print "================================", key, "\n\n", infReplicas[key]
		print "================================", key, "\n", "\n".join(infReplicas[key])
	# for key in comReplicas:
	# 	#print "================================", key, "\n\n", comReplicas[key]
	# 	print "================================", key, "\n", "\n".join(comReplicas[key])
	# print comWords 
	# print markWords 
	# print numOfWordsInf 
	# print numOfWordsCom 
	# print numMarkWords 
	# print numOfWordsPsych 
	# print infReplicas

for fileName in textFile:
	print "========================= Opening file ",fileName
	textOpen = open(fileName,"rt")
	text =  textOpen.read().decode("UTF-8").lower()
	#print "========================= first", text 
	#print "..."
	readInfWords(text)

sumNumOfWordsPsych()
printResult()
