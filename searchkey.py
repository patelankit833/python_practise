#Search total occurances of keyword in file
import sys

print 'Beginning of script'
count=0

#handle error if file name is incorrect
try:
	filename=sys.argv[1]
	fhandle=open(filename)
	try:
		searchkey=sys.argv[2]
	except:
		searchkey=raw_input('Enter keyword to search:')
except:
	print 'Cannot find file, please enter correct file name'
	exit()

for lines in fhandle:
	newline=lines.rstrip()
	wordlist=newline.split()
	for elements in wordlist:
		if elements==searchkey:
			count = count + 1

print 'There are total', count, 'occurances of keyword', '"',searchkey,'"'