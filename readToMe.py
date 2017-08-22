import urllib
import urllib.request
from bs4 import BeautifulSoup
from gtts import gTTS

url = input("Enter the url: ")
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
paragraphs = soup.findAll('p')
paragraph = ""

for product in paragraphs:
	paragraph += product.text.strip() + " "

print(paragraph)
tts = gTTS(text = paragraph, lang='en-uk')
fileName = input("Give your mp3 file a name: ")
fileName += ".mp3"
print("Saving " + fileName + "...")
tts.save(fileName)
print("Done, enjoy!")
