"""Main.py file for the Corpus Comb program."""

from development import develop_search_lists, develop_corpus
from printing import print_top_articles
from search import search_corpus

# Potential implementation of sentiment analysis
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer


print("Corpus Comb")
# location of corpus directory
directory = "data\corpus"
print("What would you like to search for?")
search = input()

# develop data structures
search_lists = develop_search_lists(search)
corpus = develop_corpus(directory)

# if a search was entered
if search != "":
    # search through the corpus for search_lists
    found_articles = search_corpus(corpus, search_lists)
    print("Number of article found:", len(found_articles))
    percentage = str(int(len(found_articles) / len(corpus) * 100)) + "%"
    print("Percentage of total corpus:", percentage)
    # st.write('Positivity percentage:', pos_percentage)
    # st.write('Negativity percentage:', neg_percentage)

    print("Top Articles Found", divider="gray")
    print_top_articles(found_articles)
