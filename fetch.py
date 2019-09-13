from bs4 import BeautifulSoup
import requests
import time

def getDefinition(vocab):
	# Grab word from user and fetch site source
	headers = {'User-Agent': 'Mozilla/5.0 | github.com/rekkuso'}
	source = requests.get('https://www.weblio.jp/content/' + vocab.strip(), headers=headers)
	time.sleep(1.5)

	# Check response
	print("Return code: " + str(source.status_code))
	if(source.status_code != 200 or source.text == ""):
		print("Error fetching HTML.")
		return -1

	# ~soup~
	soup = BeautifulSoup(source.text, 'lxml')

	# Find definitions block in website source
	results = soup.find_all('div', attrs={'class':'kiji'})

	# Create final result list and start with word itself;
	# The final list will have the word in front and its definitions afterwards
	final = list()
	final.append(vocab)
	final[0] = final[0].rstrip()
	if len(results) < 1:
		print("Error finding definition for " + vocab)
		return -2
	# Separate multiple definitions; WIP
	# Char 9312 = circled number; if one is present, its a multi-def.
	if results[0].text.strip().count(chr(9312)) > 0:
		cBuffer = ""
		for c in results[0].text.strip():
			if c >= chr(9312) and c <= chr(9331):
				final.append(cBuffer.strip())
				cBuffer = ""
				cBuffer += c
				continue
			cBuffer += c

	# Only one definition: Add the result that was found
	else:
		final.append(results[0].text.strip())

	return final


