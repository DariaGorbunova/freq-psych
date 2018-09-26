#!/usr/bin/python
print "abc"
# reading and decoding input files
textFile  = [""]
psychFile = [""]

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
	# text = open(","rt" ").read().lower()
	# text normalization 
	#   - lowercase
	#   - remove all markup signs (time,paralinguistic signs with *)
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
