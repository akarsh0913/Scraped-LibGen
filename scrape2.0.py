import requests
from bs4 import BeautifulSoup
import re 
import urllib.parse

entry = input("Enter book name: ")

#encodes the input into html encoded entry
encoded_entry = urllib.parse.quote(entry)
base_url = "https://libgen.is/index.php?req="
query_url = f'{base_url}{encoded_entry}'

page = requests.get(query_url)
soup = BeautifulSoup(page.content, 'html.parser')

#selecting each tr(table row) from the parsed soup object
trtags=soup.select('table tr')


#function for link fetching
def link():
    atags = trtag.select('tr td a')
    for tag in atags:
        href_links = tag.get('href')
        if 'library.lol' in href_links:
            print(href_links)

#function for book name fetching
def bookname():
    book_name_element = trtag.select_one('td[width="500"] a')
    if book_name_element:
        book_name_parts = book_name_element.get_text().split('<br/>')[0]
        book_name = re.sub(r"\d", "", book_name_parts)
        print("Book Name: ", book_name)


# Define a regex pattern to extract the author name
pattern = r'<td><a href="search\.php\?req=.*?">([^<]+)</a></td>'

#function for author name fetching
def authorname():
    html_content= str(trtag)
    authmatches = re.search(pattern,html_content)
    if authmatches:
        auth_name = authmatches.group(1)
        print('Author Name : ', auth_name)


#main loop
for trtag in trtags:
    bookname()
    authorname()
    link()
    print('-'*80)
