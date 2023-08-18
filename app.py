import customtkinter as ctk
import re
import requests
from bs4 import BeautifulSoup 
import urllib.parse
from tkinter import *

ctk.set_appearance_mode("light")

class ScrapedLibGen:
	def __init__(self, root):
		self.root = root
		self.root.title("Scraped LibGen")

		self.name_entry = ctk.CTkEntry(root, placeholder_text='Enter Book Name', width=400, validate='key')
		self.name_entry.pack(pady=20)

		self.search_button = ctk.CTkButton(root, text='Search', command=self.search_books)
		self.search_button.pack()

		self.text_frame = ctk.CTkFrame(root, corner_radius=10)
		self.text_frame.pack(pady=20)

		self.results = Text(self.text_frame, height=400, width=200)
		self.results.pack(padx=10, pady=10)

	def get_url(self):
		self.entry = self.name_entry.get()
		self.encoded_entry = urllib.parse.quote(self.entry)
		self.base_url = "https://libgen.is/index.php?req="
		self.query_url = f'{self.base_url}{self.encoded_entry}'
		self.page = requests.get(self.query_url)
		self.soup = BeautifulSoup(self.page.content, 'html.parser')
		
	def links(self, tr_tag):
		a_tags = tr_tag.select('td a')
		for tag in a_tags:
			href_links = tag.get('href')
			match_string = 'library.lol'
			if match_string in href_links:
				return href_links


	def book_name(self, tr_tag):
		book_name_element = tr_tag.select_one('td[width="500"] a')
		if book_name_element:
			book_name_parts = book_name_element.get_text().split('</br>')[0]
			book_name = re.sub(r"\d", "", book_name_parts)
			return f"Book Name: {book_name}"

	
	def author_name(self, tr_tag): 
		html_content = str(tr_tag)
		pattern = r'<td><a href="search\.php\?req=.*?">([^<]+)</a></td>'
		author_matches = re.search(pattern, html_content)
		if author_matches:
			author_name = author_matches.group(1)
			return f"Author Name: {author_name}"

	def search_books(self):
		self.get_url()
		tr_tags = self.soup.select('table tr')
		for tr_tag in tr_tags:
			book_name_result = self.book_name(tr_tag)
			author_name_result = self.author_name(tr_tag)
			links_result = self.links(tr_tag)
			result_text = f"{book_name_result}\n{author_name_result}\n{links_result}\n\n"
			self.results.insert(END, result_text)

if __name__ == "__main__":
	root = ctk.CTk()
	app = ScrapedLibGen(root)
	window_width, window_height = 500, 350
	root.geometry(f"{window_width}x{window_height}")
	root.mainloop()