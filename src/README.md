# Project Prototype

## Key Features

The key feature of this prototype is performing sentiment analysis on the HTML files within the `data/corpus` folder. This prototype presents the user with the results of pre-trained models VADER, TextBlob, and finBERT.

## Requirements

The required software needed for the prototype are as follows:

* Beautiful Soup v4.9.3
* NLTK v3.8.1
* TextBlob v0.18.0
* Happy Transformer v3.0.0
  * Needed for finBERT (curretly commented out)

## Using the Prototype

To run the prototype do the following:

1. Clone the repository
2. Navigate to the repository's directory
3. Install the required dependencies by using the following command:
    * `python -m pip install -r requirements.txt`
4. Run the program using the following command:
    * `python src/main.py`
