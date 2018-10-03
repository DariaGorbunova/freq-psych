#!/usr/bin/python
# # -*- coding: utf8 -*-

import re

# reading and decoding input files
textFile  = "/home/darya/work/lingvo_data/sample.txt"
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

def readInfWords():
	print "readInfWords()"

	textOpen = open(textFile,"rt")
	text =  textOpen.read().decode("UTF-8").lower()

	# text normalization 
	#   - lowercase
	#   - remove all markup signs (time,paralinguistic signs with *)
	clearData = re.sub(u"/", "", text)
	clearData = re.sub(u"ord[0-9a-zA-Zа-яА-Я-]*([^0-9a-zA-Zа-яА-Я-])[ 0-9]*", "", clearData)
	clearData = re.sub(u"#", "", clearData)
	clearData = re.sub(u"\*[а-яА-Я]+", "", clearData)
	clearData = re.sub(u"/", "", clearData)
	clearData = re.sub(u'[0-9]*:[0-9]+:[0-9]+\.[0-9]+', "", clearData)
	clearData = re.sub(u"@", "", clearData)
	clearData = re.sub(u"\?", "", clearData)
	clearData = re.sub(u"\(", "", clearData)
	clearData = re.sub(u"\)", "", clearData)
	clearData = re.sub(u"\:", "", clearData)
	clearData = re.sub(u"\.\.\.", "", clearData)
	clearData = re.sub(u"\*.", "", clearData)
	clearData = re.sub(u"[ \t]+"," ", clearData)
	clearData = re.sub(u"\n ","\n", clearData)
	clearData = re.sub(u" \n","\n", clearData)
	clearData = re.sub(u"\n+","\n", clearData)
	#print clearData
	#   - define informant|communicant
	infMatcher= ""
	comMatcher = ""
	info = ""
	comm = ""
	lastPerson = ""
	infMatch = re.compile(u'([sS][0-9]+).*')
	comMatch = re.compile(u'([mMwW][0-9]+).*')
	for line in clearData.split("\n"):
		#print "L: <%s>" % (line)
		#matching for informants and communicants
		infMatcher = infMatch.search(line)
		comMatcher = comMatch.search(line)
		if infMatcher:
			lastPerson = "informant"
			info = infMatcher.group(1)
			if not info in numOfWordsInf:
				numOfWordsInf[info] = 0
		if comMatcher:
			lastPerson = "communicant"
			comm = comMatcher.group(1)
			if not comm in numOfWordsCom:
				numOfWordsCom[comm] = 0
				
		for word in line.split(" "):
			#print word 
			if word != info and word != comm:
				if lastPerson == "informant":
					numOfWordsInf[info] += 1
					print numOfWordsInf[info]
					#print "Number of words for %s = %s For word = {%s}" %(info, numOfWordsInf, word)
				elif lastPerson  == "communicant":
					numOfWordsCom[comm] += 1

					#print "Number of words for %s = %s For word = {%s}" %(comm, numOfWordsCom, word)

				
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
	# assign a psychotype
	# count number of words by psychotype in numOfWordsPsych

def printResult():
	print "printResult()"
	# print psychInf  
	# print infWords 
	# print comWords 
	# print markWords 
	# print numOfWordsInf 
	# print numOfWordsCom 
	# print numMarkWords 
	# print numOfWordsPsych 


readInfWords()
sumNumOfWordsPsych()
printResult()
