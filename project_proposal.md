# Junior Seminar (CMPSC 580) Project Proposal

## Semester: Spring 2024

## GitHub Handle: hayleepierce

## Name: Haylee Pierce

## Major: Computer Science

## Project Title: Corpus Comb

---

## Introduction

The project I am proposing is called **Corpus Comb** (name subject to change). The goal of this project is to provide users with an automated way of detecting bias within their sources. My method for bias detection is through sentiment analysis. I hypothesize that the higher the neutral score the less biased the source. The project will use the HTML representation of the users' sources, which will be obtained using the process of web scraping. The user will provide a URL or DOI for their source and it will be used to gather the HTML code for the source. The HTML code will then be parsed using the Beautiful Soup library from Python, extracting the content of the source as a string. The content will then be cleaned and prepared for sentiment analysis, which will be performed on the string using a pre-trained model. The results of this analysis will be displayed to the user. The project will take the form of a web application, built with Flask.

The current literature primarily covers sentiment analysis in the context of social media, finance, and public opinion; therefore, this project will help to expand the scope of sentiment analysis. This project will also improve the process of finding quality sources. Finding quality sources is time-consuming and the researcher's bias can make it difficult for them to detect bias within their sources. This project will help to reduce the time it takes to find quality sources and the effect of the researcher's bias.

## Literature Review

### Sentiment Analysis

Sentiment analysis is the process of identifying the emotion/tone behind a piece of text. There are numerous models that are pre-trained to perform sentiment analysis, including VADER (Valence Aware Dictionary and sEntiment Reasoner), TextBlob, and BERT (Bidirectional Encoder Representations from Transformers).

The majority of existing literature uses VADER and/or TextBlob to analyze text from social media posts [1, 2, 3]. The VADER model provides a positive, negative, and neutral score that adds to a total of 100. A downside to this model is that it was trained using data from social media; consequently, the analysis of any other type of text is not guaranteed to be accurate. The TextBlob model produces a polarity score between -1 and 1 and a subjectivity score between 0 and 1. Unfortunately, the documentation about what data was used to train the model is minimal.

Some of the literature uses BERT to perform sentiment analysis; for example, Singh et. al. [2021] classifies the emotion of tweets relating to COVID-19 using a version of the BERT model [4]. Alaparthi and Mishra [2021] look at four different methods of performing sentiment analysis, two of them being the BERT and SentiWordNet models [5].

### Data: Gathering and Preparation

Web scraping is the process of extracting data from the web. Vincent Smith [2019] discusses web scraping in-depth and walks the reader through the process of developing a web scraping tool using the programming language Go [6]. This walk-through can be used to not only build a web scraper but also implement web scraping into other types of projects.

The Beautiful Soup Python library allows for the parsing of HTML files [7]. This library can be used to find specific information from the HTML files obtained by scraping the web, such as the URL and the title. It can also be used to prepare a string of text for analysis. Yongquan Li [2022] used several Python libraries, including the Beautiful Soup library to discuss methods of data collecting and HTML parsing [8].

Text mining is the process of deducing meaningful information from the patterns and trends found within text. One book written on this process covers several algorithms that are used to mine text, discussing the theory behind them and how to apply them in practice [9]. Another book on text mining focuses on the process of mining through text that is unstructured and how it differs from the process of mining through structured text [10].

### User Interface

Flask is a web framework that was written using Python. It can be used in conjunction with other libraries to build a web application and provide users with a friendly interface to interact with. Matt Copperwaite and Charles Leifer [2015] wrote a book that provides helpful explanations of Flask, walking the reader through how to build a web application using Flask [10].

## Prototype

The data used for this prototype is in the form of HTML files. The collection of this data was done manually by right-clicking on a web page and saving the page's HTML code. These files are saved within the `src/data/corpus` folder.

The processing of this data is done using the Beautiful Soup Python library [7]. A function called `develop_corpus_html()` was created that iterates through all the files within the `src/data/corpus` folder. The `get_text()` function from the Beautiful Soup library is used to extract the title and content from the files as strings. This information is added to a dictionary with corresponding keys and the dictionary is then added to a list called `corpus`. The function returns the list, which contains a dictionary for each of the files within the `src/data/corpus` folder. No cleaning of the text is done at this time.

Sentiment analysis is then performed on each of the context strings that were extracted from the files. Three pre-trained sentiment analysis models are used: VADER, TextBlob, and finBERT. To use VADER, the `vader_lexicon` from NTLK (Natural Language ToolKit) must first be downloaded. Next, the `polarity_scores()` function is called using the content string as the input. This function returns a positive, negative, and neutral score. TexBlob does not have any requirements; therefore, all that needs to be run is `TextBlob()` with the content string as the input. TextBlob produces a polarity and subjectivity score, which are accessed using `.sentiment.polarity` and `.sentiment.subjectivity` respectively. To use finBERT, the model first needs to be retrieved from the web by running the following function: `HappyTextClassification("BERT", "ProsusAI/finbert", num_labels=3)`. This model has a limit on the length of the input; therefore, the content needed to be split into multiple strings of at most 1,000 characters. The average of all the results was then found to determine the positive, negative, and neutral scores of the whole content string. All of these scores are first rounded to the second decimal place and then displayed to the user along with the title of their corresponding file.

## Preliminary Results and Outcomes

The prototype of this project acted as an analysis of the three different pre-trained sentiment analysis models that are used: VADER, TextBlob, and finBERT. Using the results of the sentiment analysis, I reached the conclusion that none of the models are the best to use for this project, as they did not provide what I would consider to be accurate results.

VADER is pre-trained using social media posts, meaning the results are most accurate when analyzing social media content. The results of this model were extremely similar for each of the files analyzed, as shown in Figure 1. The text being analyzed is vastly different in content; therefore, the result indicates that the model is unable to detect these differences.

![Results of VADER sentiment analysis.](img/vader.png)

*Fig. 1. Results of VADER sentiment analysis.*

TextBlob provided the best results of the three, as shown in Figure 2; specifically, the results appear to be affected by the content that is being analyzed. However, the documentation about what data was used to train the model is limited, which makes this model less reliable. The results of this model are also in a different form than the other two, as it provides a polarity and subjectivity score instead of positive, neutral, and negative scores. This difference makes it difficult to compare these results to the results of the other two models.

![Results of TextBlob sentiment analysis.](img/textblob.png)

*Fig. 2. Results of TextBlob sentiment analysis.*

The last model finBERT is a model of BERT that is pre-trained using financial data. Similar to VADER, the results are most accurate when analyzing the data that was used to train it (financial data). Figure 3 displays this disparity, with file 6 (an article about stocks) having drastically different results. The length limit put on the input also makes the result less reliable, as the average of the results is less accurate than a result from an analysis of the whole string.

![Results of finBERT sentiment analysis.](img/finbert.png)

*Fig. 3. Results of finBERT sentiment analysis.*

## Conclusions and Future Work

Due to the results of this prototype, as explained above, my next steps include investigating other sentiment analysis models. I plan to look for other pre-trained BERT models that are not trained on one specific type of textual data but are trained on a vast array of types. Specifically, I plan to look at SentiWordNet, as the study done by Alaparthi and Mishra [2021] yielded promising results [5]. If I find that SentiWordNet and any other models I find do not produce adequate results, I will most likely use TextBlob, as it was the best of the three tested by this prototype. TextBlob also brings subjectivity and objectvity into play, which could make the detection of bias in sources more accurate.

After I decide on a model for sentiment analysis, I then need to automate the process of data gathering and process. Currently the process is done manually and the data is not being cleaned before sentiment analysis. Automating the process of data gathering will make this application easier to use and cleaning the data before performing sentiment analysis will increase the accuracy of the results. This process will use methods of web scraping and text mining and utilize the Beautiful Soup Python library.

Finally, a user interface will need to be developed, to provide the user with a way to easily interact with and use the application. This interface will be developed using Flask and supported libraries. The interface will allow the user to add new sources, remove old sources, and view the results of sentiment analysis for all the added sources.

## References

[1] Sai Dheeraj Kanaparthi, Anjali Patle, and K. Jairam Naik. 2023. Prediction and detection of emotional tone in online social media mental disorder groups using regression and recurrent neural networks. _Multimedia Tools and Applications_ 82 (April 2023) 43819–43839. <https://doi.org/10.1007/s11042-023-15316-x>

[2] Ilias Chalkias, Katerina Tzafilkou, Dimitrios Karapiperis, and Christos Tjortjis. 2023. Learning Analytics on YouTube Educational Videos: Exploring Sentiment Analysis Methods and Topic Clustering. _Electronics_ 12, 18 (Sep. 2023) 1-13. <https://doi.org/10.3390/electronics12183949>

[3] Wajdi Aljedaani, Furqan Rustam, Mohamed Wiem Mkaouer, Abdullatif Ghallab, Vaibhav Rupapara, Patrick Bernard Washington, Ernesto Lee, and Imran Ashraf. 2022. Sentiment analysis on Twitter data integrating TextBlob and deep learning models: The case of US airline industry. _Knowledge-Based _Systems_ 255 (Nov. 2022) 1-15. <https://doi.org/10.1016/j.knosys.2022.109780>

[4] Mrityunjay Singh, Amit Kumar Jakhar, and Shivam Pandey. 2021. Sentiment analysis on the impact of coronavirus in social life using
the BERT model. _Social Network Analysis and Mining_ 11, 1 (March 2021) 1-11. <https://doi.org/10.1007/s13278-021-00737-z>

[5] Shivaji Alaparthi and Manit Mishra. 2021. BERT: a sentiment analysis odyssey. _Journal of Marketing Analytics_ 9 (Feb. 2021) 118–126. <https://doi.org/10.1057/s41270-021-00109-8>

[6] Vincent Smith. 2019. _Go Web Scraping Quick Start Guide: Implement the Power of Go to Scrape and Crawl Data from the Web_. Packt Publishing, Birmingham, UK.

[7] Leonard Richardson. 2019. Beautiful Soup Documentation. (Dec. 2019) Retrieved from <https://beautiful-soup-4.readthedocs.io/en/latest/>

[8] Yongquan Li. 2022. Python Data Analysis and Attribute Information Extraction Method Based on Intelligent Decision System. _Mobile Information Systems_ 2022, (April 2022), 1–10. <https://doi.org/10.1155/2022/2495166>

[9] Michael W. Berry and Jacob Kogan (Eds.). 2010. _Text Mining: Applications and Theory_. John Wiley & Sons, Chichester, UK.

[10] Sholom M. Weiss, Tong Zhang, Nitin Indurkhya, and Fred J. Damerau. 2010. _Text Mining: Predictive Methods for Analyzing Unstructured Information_. Springer Science & Business Media, New York, NY.

[11] Matt Copperwaite and Charles Leifer. 2015. _Learning Flask Framework: Build Dynamic, Data-driven Websites and Modern Web Applications with Flask_. Packt Publishing, Birmingham, UK.
