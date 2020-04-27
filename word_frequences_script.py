import re
import sys
import collections

# Setting up the global --------------------------------------------------------
STOP_WORDS = ['a', 'about', 'above', 'across', 'after', 'afterwards']
STOP_WORDS += ['again', 'against', 'all', 'almost', 'alone', 'along']
STOP_WORDS += ['already', 'also', 'although', 'always', 'am', 'among']
STOP_WORDS += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
STOP_WORDS += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
STOP_WORDS += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
STOP_WORDS += ['because', 'become', 'becomes', 'becoming', 'been']
STOP_WORDS += ['before', 'beforehand', 'behind', 'being', 'below']
STOP_WORDS += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
STOP_WORDS += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
STOP_WORDS += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
STOP_WORDS += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
STOP_WORDS += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
STOP_WORDS += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
STOP_WORDS += ['every', 'everyone', 'everything', 'everywhere', 'except']
STOP_WORDS += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
STOP_WORDS += ['five', 'for', 'former', 'formerly', 'forty', 'found']
STOP_WORDS += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
STOP_WORDS += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
STOP_WORDS += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
STOP_WORDS += ['herself', 'him', 'himself', 'his', 'how', 'however']
STOP_WORDS += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
STOP_WORDS += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
STOP_WORDS += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
STOP_WORDS += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
STOP_WORDS += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
STOP_WORDS += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
STOP_WORDS += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
STOP_WORDS += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
STOP_WORDS += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
STOP_WORDS += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
STOP_WORDS += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
STOP_WORDS += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
STOP_WORDS += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
STOP_WORDS += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
STOP_WORDS += ['some', 'somehow', 'someone', 'something', 'sometime']
STOP_WORDS += ['sometimes', 'somewhere', 'st', 'still', 'such', 'system', 'take']
STOP_WORDS += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
STOP_WORDS += ['then', 'thence', 'there', 'thereafter', 'thereby']
STOP_WORDS += ['therefore', 'therein', 'thereupon', 'these', 'they']
STOP_WORDS += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
STOP_WORDS += ['three', 'through', 'th', 'throughout', 'thru', 'thus', 'to']
STOP_WORDS += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
STOP_WORDS += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
STOP_WORDS += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
STOP_WORDS += ['whatever', 'when', 'whence', 'whenever', 'where']
STOP_WORDS += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
STOP_WORDS += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
STOP_WORDS += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
STOP_WORDS += ['within', 'without', 'would', 'yet', 'you', 'your']
STOP_WORDS += ['yours', 'yourself', 'yourselves']
STOP_WORDS += ['\'\'', '\"', '"', "", '']
STOP_WORDS += ['france', 'new', 'end', 'date', 'time', 'use']


INPUT_FILE = "filetoread.txt" # File to read and extract word list from
OUTPUT_FILE = "frequencies_output.txt" # File to read and extract word list from

# ------------------------------------------------------------------------------
# Setting up mylogger package --------------------------------------------------
# ------------------------------------------------------------------------------

import sys
import os
import logging.config # to configure mylogger

# Setting up the global variables by importing the config.py module then -------
# importing the logger module --------------------------------------------------

from config import LOGGER # Initial settup of python login to configure mylogger
LOGGER_PATH_FOLDER = LOGGER.PATH_FOLDER # setting the logger package path as a global variable
LOGGER_CONF_FILE = LOGGER.CONF_FILE # setting the logger configuration file as a global variable
LOGGER_LOGGING_LEVEL = LOGGER.LOGGING_LEVEL # setting the default logging lever as a global variable

sys.path.append(LOGGER_PATH_FOLDER)
from loggerpkg import myloggerscript # import module myloggerscript (pythin script) from loggerpkg package (folder)

# Setting up mylogger functions ------------------------------------------------
import inspect

def DisplayLoggerSetupMsg():
    print("Importing the configuration file config.py from " + os.getcwd())
    print("Setting up the logger configuration file path as " + LOGGER_CONF_FILE)
    print("Setting up the default logging level as " + LOGGER_LOGGING_LEVEL)

# ------------------------------------------------------------------------------
# End of setting up mylogger package -------------------------------------------
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Setting up global functions --------------------------------------------------
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Setting up specific functions ------------------------------------------------
# ------------------------------------------------------------------------------

# Given a list of words, remove any that are in a list of stop words.
def removeStopwords(wordlist, stopwords):
	mylogger.info('Removing unecessary words called stopwords')
	return [word for word in wordlist if word not in stopwords]

# Given a text string, remove all non-alphanumeric
# 
# characters (using Unicode definition of alphanumeric)
def stripNonAlphaNum(text):
	pattern = '[^0-9 \t\\\/\-\.\"\n]\w+'
	mylogger.info('Filtering text with this pattern: ' + pattern)
	return_list = re.findall(pattern, text, flags=re.UNICODE | re.IGNORECASE)
	return return_list

def calculateWordFrequence(wordlist):
	mylogger.info('Calculating frequencies of words')
	word_freq = []
	[word_freq.append(wordlist.count(word)) for word in wordlist]
	return word_freq

def createUniqueListWords(wordlist, word_freq_list):
	mylogger.info('Creating a unique list of words')
	return list(set(zip(wordlist, word_freq_list)))

def dumpFiletoText(filename):
	mylogger.info('Dumping the file in a raw list')
	with open(INPUT_FILE) as f:
		return f.read()

def sortTuples(my_tuples, index=0, descending=False):
	mylogger.info('Sorting tuples index ' + str(index) + ' by descending=' + str(descending))
	my_tuples.sort(key=lambda tup: tup[index], reverse=descending)
	return my_tuples

# `from pprint import pprint as pp` is also useful
def printTuplesByLine(tuples):
	mylogger.info('Printing tupples line by line')
	print( '\n'.join(' '.join(map(str,t)) for t in tuples) )

# ------------------------------------------------------------------------------
# Main -------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main():
	mylogger.info('Start of the script')
	
	rawlist = dumpFiletoText(INPUT_FILE)
	raw_wordlist = stripNonAlphaNum(rawlist)
	lower_wordlist = [word.lower() for word in raw_wordlist]
	clean_wordlist = removeStopwords(lower_wordlist, STOP_WORDS)
	word_freq = calculateWordFrequence(clean_wordlist)
	unique_wordlist = createUniqueListWords(clean_wordlist, word_freq)
	unique_wordlist = sortTuples(unique_wordlist,1, True)
	printTuplesByLine(unique_wordlist)
	
	mylogger.info('End of the script')

# Initialize the logger---------------------------------------------------------	
if __name__ == '__main__':
    DisplayLoggerSetupMsg()
    myloggerscript.setup_logging(LOGGER_PATH_FOLDER, LOGGER_CONF_FILE,
        LOGGER_LOGGING_LEVEL)
    mylogger = logging.getLogger(__name__)
    main()
	
