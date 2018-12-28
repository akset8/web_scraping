import bs4 

url = 'https://www.rottentomatoes.com/m/aquaman_2018'

from urllib.request import urlopen
html = urlopen(url)

markup = (html.read())
soup = bs4.BeautifulSoup(markup, 'html.parser')

name_tag = soup.find('h1', attrs={'class': 'title hidden-xs'})
print (name_tag.text)

concensus_tag = soup.find('p', attrs={'class': 'critic_consensus superPageFontColor'})
print (concensus_tag.text)

tom_rating = soup.find('span', attrs={'class': 'meter-value superPageFontColor'})
print (tom_rating.text)

aud_rating = soup.find('div', attrs={'class': 'audience-score meter'})
print (aud_rating.text)

reviews = soup.find_all('div', attrs={'class': 'quote_bubble'})


for review in reviews:

	out_rat = review.find('span',attrs={'rel': 'tooltip'})
	out = review.find('div',attrs={'class': 'media-body'})
	out_rev = out.find('p')
	out_auth = review.find('a',attrs={'class':'unstyled articleLink'})
	out_org = review.find('a',attrs={'class':'small subtle articleLink'})

	print (out_rev.text)

	if (out_rat!=None):
		print (out_rat['title'])

	if (out_auth!=None):
		print (out_auth.text)

	if (out_org!=None):
		print (out_org.text)









