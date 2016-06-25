from bs4 import BeautifulSoup
from urllib import urlopen
from sys import argv

place = raw_input("Please enter the business name: ")
filename = raw_input("Please enter a name for the output: ")
queries = 0
while queries <201:
	stringQ = str(queries)
	page = urlopen('http://www.yelp.com/biz/' + place + '?start=' + stringQ)

	soup = BeautifulSoup(page, 'lxml')
	reviews = soup.findAll('p', attrs={'itemprop':'description'})
	authors = soup.findAll('span', attrs={'itemprop':'author'})

	flag = True
	indexOf = 1

	for review in reviews:
		dirtyEntry = str(review)
		while dirtyEntry.index('<') != -1:
			indexOf = dirtyEntry.index('<')
			endOf = dirtyEntry.index('>')
			if flag:
				dirtyEntry = dirtyEntry[endOf+1:]
				flag = False
			else:
				if(endOf+1 == len(dirtyEntry)):
					cleanEntry = dirtyEntry[0:indexOf]
					break
				else:
					dirtyEntry = dirtyEntry[0:indexOf]+dirtyEntry[endOf+1:]
		f=open(filename, "a")
		f.write(cleanEntry)
		f.write("\n")
		f.close

	for author in authors:
		dirty = str(author)
		closing = dirty.index('>')
		dirty = dirty[closing+1:]
		opening = dirty.index('<')
		cleanEntry = dirty[0:opening]
		f=open("fuk.txt", "a")
		f.write(cleanEntry)
		f.write("\n")
		f.close

	queries = queries + 40
