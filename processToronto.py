import urllib
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/List_of_neighbourhoods_in_Toronto'
opener = urllib.FancyURLopener({})
f = opener.open(url);
html = f.read()
#print(html);
soup = BeautifulSoup(html,features="html.parser")
links = soup.find_all('a', title=True)
# proceed as normal from here
for tag in links:
    #print(tag);
    t = tag.get("title", None);
    if t is not None:
        print(t);
