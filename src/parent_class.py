import requests
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer

class IterableUrl():

    def __init__(self, url):
        self.url = url
        self.parsed_data = []

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Parsing ended')

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        try:
            self.tag = self.prettify(self.parsed_data[self.cursor])
            return self.tag
        except IndexError:
            self.cursor = 0
            raise StopIteration
        finally:
            self.cursor += 1 

    def __len__(self):
        return len(self.parsed_data)

    def __getitem__(self, index):
        return self.parsed_data[index]

    def get_request_text(self):
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        return self.soup

    def prettify(self, tag):
        self.format_template = 'Parsed tag: {}'
        return self.format_template.format(tag)
    
    


 