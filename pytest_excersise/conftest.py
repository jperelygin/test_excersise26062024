import pytest
from .Parser import Parser


LINK = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
CAPTION = "Programming languages used in most popular websites*"

@pytest.fixture(scope="session", autouse=True)
def parse_languages():
    p = Parser(LINK)
    return p.parse_table(CAPTION)
