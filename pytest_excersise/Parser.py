import requests
from bs4 import BeautifulSoup as bs
import re
from .Language import Language

class Parser:
    def __init__(self, link):
        self.link = link

    def remove_links(self, text: str) -> str:
        return re.sub(r'\[.*?\]', '', text)
    
    def parse_popularity_to_int(self, text: str) -> int:
        return int(text.split()[0].replace(',', '').replace('.', ''))

    def parse_table(self, caption) -> list[Language]:
        wiki_page = requests.get(self.link).text
        soup = bs(wiki_page, 'html.parser')
        tables = soup.find_all('table')
        needed_table = None
        for table in tables:
            if table.find("caption").text.strip() == caption:
                needed_table = table
                break
        if not needed_table:
            raise AttributeError(f"No table with caption \"{caption}\" found.")
        
        rows = needed_table.find_all('tr')
        result = []
        for row in rows[1:]:
            cells = row.find_all('td')
            cell_data = [self.remove_links(cell.get_text().strip()) for cell in cells]
            lang = Language(cell_data[0], self.parse_popularity_to_int(cell_data[1]), cell_data[2], cell_data[3], cell_data[4])
            result.append(lang)
        return result