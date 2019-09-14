from bs4 import BeautifulSoup
import requests

def getSentence(vocab):
     #Temporary input for testing purposes. Rather than an input by hand it would sync up with the vocab file in weblio-fetcher,
     #Therefore the vocab in the list would be fetched from both tatoeba.org and weblio.jp

     headers = {'User-Agent': 'Mozilla/5.0 | github.com/rekkuso'}
     source = requests.get('https://tatoeba.org/eng/sentences/search?query=' + vocab + '&from=jpn&to=und')

     invalid_tags = ['div']
     soup = BeautifulSoup(source.text, 'lxml')

     results = soup.find('div', attrs={'class': "text", 'dir': "ltr", 'flex': ""})

     #Rather than printing, this would be synced up to main.py in order to be written into the output csv file.
     print("-------------------")
     if results == None or results.text == "":
          return vocab.strip
     else: 
          print(results.text.strip())
          return results.text.strip()
