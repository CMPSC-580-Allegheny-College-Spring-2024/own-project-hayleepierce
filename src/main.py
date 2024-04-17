"""Main file."""

import os
from b4 import BeautifulSoup

def develop_corpus_html(directory: str) -> dict:
    """Devlop a corpus list from given html files."""
    corpus = []
    # iterate through all html files in the given directory
    for filename in os.listdir(directory):
        # create empty dictionary for current file
        page = {}
        # create the full path for the current file
        path = os.path.join(directory, filename)
        # open and read file
        file = open(path, "r", encoding="utf-8")
        html_str = file.read()
        # create BeautifulSoup object
        soup = BeautifulSoup(html_str, 'html.parser')
        # add title to dictionary
        page["Title"] = soup.title.get_text()
        # add content to dictionary
        page["Content"] = soup.get_text()
        # add dictionary to corpus list
        corpus.append(page)