import sys,requests,bs4,webbrowser

res=requests.get('https:/google.com/serch?q='+''.join(sys.argv[1:]))
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text, "html.parser")

linkElemants= soup.select('.r a')

linkToOpen= min(5,len(linkElemants))

for i in range(linkToOpen):
    webbrowser.open('http:/google.com'+linkElemants[i].get('href'))
