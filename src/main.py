"""Main file."""

import os
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from happytransformer import HappyTextClassification

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
    return corpus

corpus = develop_corpus_html('src/data/corpus')

try:

    sia = SentimentIntensityAnalyzer()

    print("VADER Sentiment Analysis")
    for page in corpus:
        sia_scores = sia.polarity_scores(page["Content"])
        page["Negative"] = round(sia_scores["neg"] * 100, 2)
        page["Neutral"] = round(sia_scores["neu"] * 100, 2)
        page["Positive"] = round(sia_scores["pos"] * 100, 2)
        print(page["Title"])
        print(str(page["Negative"]) + "% Negative")
        print(str(page["Neutral"]) + "% Neutral")
        print(str(page["Positive"]) + "% Positive")

except:
    nltk.download('vader_lexicon')

    sia = SentimentIntensityAnalyzer()

    print("VADER Sentiment Analysis")
    for page in corpus:
        sia_scores = sia.polarity_scores(page["Content"])
        page["Negative"] = round(sia_scores["neg"] * 100, 2)
        page["Neutral"] = round(sia_scores["neu"] * 100, 2)
        page["Positive"] = round(sia_scores["pos"] * 100, 2)
        print(page["Title"])
        print(str(page["Negative"]) + "% Negative")
        print(str(page["Neutral"]) + "% Neutral")
        print(str(page["Positive"]) + "% Positive")

print()

print("TextBlob Sentiment Analysis")
for page in corpus:
    tb = TextBlob(page["Content"])
    polarity = round(tb.sentiment.polarity, 2)
    subjectivity = round(tb.sentiment.subjectivity, 2)
    page["Polarity"] = polarity
    page["Subjectivity"] = subjectivity
    print(page["Title"])
    print("Polarity " + str(page["Polarity"]))
    print("Subjectivity " + str(page["Subjectivity"]))

# Worked for me, failed for tester

# print()

# happy_tc = HappyTextClassification("BERT", "ProsusAI/finbert", num_labels=3)

# print("Happy Transformer: BERT Sentiment Analysis")
# for page in corpus:
#     page["Negative"] = []
#     page["Positive"] = []
#     page["Neutral"] = []
#     strings = [page["Content"][i:i+1000] for i in range(0, len(page["Content"]), 1000)]
#     for string in strings:
#         result = happy_tc.classify_text(string)
#         if result.label == "positive":
#             page["Positive"].append(result.score)
#             page["Neutral"].append(0)
#             page["Negative"].append(0)
#         elif result.label == "neutral":
#             page["Positive"].append(0)
#             page["Neutral"].append(result.score)
#             page["Negative"].append(0)
#         elif result.label == "negative":
#             page["Positive"].append(0)
#             page["Neutral"].append(0)
#             page["Negative"].append(result.score)
#     print(page["Title"])
#     print("Negative Score: " + str(round(sum(page["Negative"])/len(page["Negative"]), 2)))
#     print("Neutral Score: " + str(round(sum(page["Neutral"])/len(page["Neutral"]), 2)))
#     print("Positive Score: " + str(round(sum(page["Positive"])/len(page["Positive"]), 2)))
