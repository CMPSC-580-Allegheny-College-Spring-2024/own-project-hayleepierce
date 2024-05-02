# Project Prototype

TODO: The result of your work will be the delivery of some type of proof-of-concept prototype which will likely contain software programming solutions (i.e., Python code, HTML pages, or similar). All source code for the prototype must be stored in this directory. If your prototype uses data, please create `data/` subdirectory in `src/` and include your data file(s) in `src/data/` directory.

To allow the user to experience and execute your prototype, you must first explain how to set up the initial conditions to run or use the artifact. Be sure to offer explicit details and instructions regarding the installation of the necessary foundational libraries, drivers, external software projects, containers and similar types of tertiary software which are involved in executing your artifact. Once these initial software installations have been completed, then you are asked to offer the necessary instructions for actually executing the artifact. For this, please provide all command line parameters or associated bash commands for execution. Please remember that users are unwilling to "figure-out" how to use code in absence of the essential instructions concerning the execution of project artifacts.

## Key Features

TODO: Outline the  main technical features of your prototype.

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
