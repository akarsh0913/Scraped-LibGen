import sys
import re
import requests
from bs4 import BeautifulSoup
import urllib.parse
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtCore import Qt 

class ScrapedLibGen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scraped LibGen")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.name_entry = QLineEdit(placeholderText='Enter Book Name')
        layout.addWidget(self.name_entry, alignment=Qt.AlignmentFlag.AlignTop)

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_books)
        layout.addWidget(self.search_button, alignment=Qt.AlignmentFlag.AlignTop)

        self.results = QTextEdit()
        layout.addWidget(self.results)

        central_widget.setLayout(layout)

    def get_url(self):
        entry = self.name_entry.text()
        encoded_entry = urllib.parse.quote(entry)
        base_url = "https://libgen.is/index.php?req="
        query_url = f'{base_url}{encoded_entry}'
        page = requests.get(query_url)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def links(self, tr_tag):
        a_tags = tr_tag.select('td a')
        for tag in a_tags:
            href_links = tag.get('href')
            match_string = 'library.lol'
            if match_string in href_links:
                return href_links
        return ""

    def book_name(self, tr_tag):
        book_name_element = tr_tag.select_one('td[width="500"] a')
        if book_name_element:
            book_name_parts = book_name_element.get_text().split('</br>')[0]
            book_name = re.sub(r"\d", "", book_name_parts)
            return f"Book Name: {book_name}"
        return ""

    def author_name(self, tr_tag):
        html_content = str(tr_tag)
        pattern = r'<td><a href="search\.php\?req=.*?">([^<]+)</a></td>'
        author_matches = re.search(pattern, html_content)
        if author_matches:
            author_name = author_matches.group(1)
            return f"Author Name: {author_name}"
        return ""

    def search_books(self):
        try:
            self.results.clear()
            self.get_url()
            tr_tags = self.soup.select('table tr')
            for tr_tag in tr_tags:
                book_name_result = self.book_name(tr_tag)
                author_name_result = self.author_name(tr_tag)
                links_result = self.links(tr_tag)
                result_text = f"{book_name_result}\n{author_name_result}\n{links_result}\n\n"
                self.results.insertPlainText(result_text)
        except:
            print("An error occurred:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrapedLibGen()
    window.setGeometry(100, 100, 600, 500)
    window.show()
