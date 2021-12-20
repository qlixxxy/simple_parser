from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup
from parent_class import IterableUrl


class PythonScriptsParser(IterableUrl):

    def parse(self):
        self.parsed_text = self.get_request_text()
        self.found_text = self.parsed_text.find_all('h2')
        self.parsed_data = [e.text for e in self.found_text]
        


