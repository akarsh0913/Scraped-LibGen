import requests
from bs4 import BeautifulSoup

entry = input("Enter book name: ")
tags = entry.split()
formatted_tags = '+'.join(tags)
base_url = "https://libgen.li/index.php?req="
query_url = f'{base_url}{formatted_tags}'
page = requests.get(query_url) # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
 
links = soup.select("table tbody tr td a") # Selecting all of the anchors with titles
first1000 = links[:1000] # Keep only the first 10 anchors
for anchor in first1000:
    href = anchor.get('href')
    if href and 'libgen.rocks' in href:
        print(f'href: {href}')
        print('-'*40)