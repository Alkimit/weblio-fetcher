from bs4 import BeautifulSoup
import requests

# Grab word from user and fetch site source
vocab = input('Vocab Word: ')
source = requests.get('https://www.weblio.jp/content/' + vocab).text
soup = BeautifulSoup(source, 'html.parser')

# Find definitions part of website source
results1 = soup.find_all('div', attrs={'class':'NetDicBody'})

# Final string
resString = ""

# Grab each definition and concatenate
for i in range(0, len(results1)):
  resString += results1[i].text

# Strip of whitespace
resString = resString.strip()

# Buffer for definition separation
buf = ""

for i in range(0, len(resString)):
	# 9312: ①; If one is present, there are multiple definitions
	# TODO: Clean up checks
	if resString.count(chr(9312)) > 0:
		if resString[i] == chr(9312) or resString[i] == chr(9313) or resString[i] == chr(9314) or resString[i] == chr(9315) or resString[i] == chr(9316):
			print(buf)
			buf = ""
		buf += resString[i]
		continue
	buf += resString[i]
print(buf)

