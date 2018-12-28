

import bs4 

def remove_sp_new(ll):
	ll2 = []

	for i in ll:
		if ((i != '') and (i != '\n')):
			ll2.append(i)

	return ll2 

def remove_special(ll):

	ll2 = []
	for i in ll:
		if i!='\n\n':
			ll2.append(i[:-1])

	return ll2

url = 'https://github.com/keras-team'

from urllib.request import urlopen
html = urlopen(url)
markup = (html.read())

soup = bs4.BeautifulSoup(markup, 'html.parser')

repo_tags = soup.find_all('li', attrs={'class': 'col-12 d-block width-full py-4 border-bottom public source'})

for tag in repo_tags:

	try:
		repo_name = tag.find('a',attrs={'itemprop':'name codeRepository'})
		print((repo_name.text).split(' ')[-1][:-1])

		repo_des = tag.find('p',attrs={'class':'col-9 d-inline-block text-gray mb-2 pr-4'})
		print (((' ').join(remove_sp_new(repo_des.text.split(' '))))[:-1])

		repo_tags = tag.find('div',attrs={'class':'topics-row-container col-9 d-inline-flex flex-wrap flex-items-center f6 my-1'})
		print (' '.join(remove_special(remove_sp_new(repo_tags.text.split(' ')))))

		print ()

	except:
		print ()








