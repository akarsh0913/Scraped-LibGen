import requests
from bs4 import BeautifulSoup

entry = input("Enter book name: ")
tags = entry.split()
formatted_tags = '+'.join(tags)
base_url = "https://libgen.li/index.php?req="
query_url = f'{base_url}{formatted_tags}'
page = requests.get(query_url)
soup = BeautifulSoup(page.content, 'html.parser')
 
links = soup.select("table tbody tr td a")
first1000 = links[:1000]
for anchor in first1000:
    href = anchor.get('href')
    if href and 'libgen.rocks' in href:
        print(f'href: {href}')
        print('-'*40)
