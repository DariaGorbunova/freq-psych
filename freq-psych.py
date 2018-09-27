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
	#clearData = re.sub(u"\s+"," ", clearData)
	print clearData
	#   - define informant|communicant
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
