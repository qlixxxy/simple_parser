from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup
from parent_class import IterableUrl


class PythonScriptsParser(IterableUrl):

    def parse(self):
        self.parsed_text = self.get_request_text()
        self.found_text = self.parsed_text.find_all('h2')
        self.parsed_data = [e.text for e in self.found_text]
        

if __name__ == '__main__':
    with PythonScriptsParser('https://python-scripts.com/beautifulsoup-html-parsing') as url:
        url.parse()
        for i in url:
            print(i)
        print(len(url.parsed_data))
        print(url[0])
        