from bs4 import BeautifulSoup
import requests
import time

def fetchSource(vocab):
	# Grab word from user and fetch site source
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
	source = requests.get('https://www.weblio.jp/content/' + vocab, headers=headers)
	time.sleep(2)
	# Check response
	print("Return code: " + str(source.status_code))
	if(source.status_code != 200 or source.text == ""):
		print("Error fetching HTML.")
		return ConnectionAbortedError

	soup = BeautifulSoup(source.text, 'lxml')

	# Find definitions part of website source
	results = soup.find_all('a', attrs={'class':'crosslink'})

	# Final string
	resString = ""
	# Grab each definition and concatenate
	rtemp = ""
	for r in results:
		if rtemp == r.parent.text:
			continue
		resString += r.parent.text
		rtemp = r.parent.text


	# Strip ends of whitespace
	resString = resString.strip()

	print("/*------------------")
	print(resString)
	print("-------------------*/")

	if(len(resString) < 1):
		print("No definition found.")
		return ConnectionError

	# Buffer for definition separation
	buf = ""
	# List of final results
	definitions = list()

	for i in range(0, len(resString)):
		# 9312 = circled numbers; If one is present, there are multiple definitions
		if resString.count(chr(9312)) > 0:
			# Check for subsequent number symbols and add a string to the list for each definition
			if ord(resString[i]) >= 9312 and ord(resString[i]) <= 9331:
				if(buf != ""):
					definitions.append(buf)
					buf = ""
			buf += resString[i]
			continue
		# Only one definition
		buf += resString[i]
	# Return all definitions
	definitions.append(buf)
	return definitions


