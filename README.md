# Sentiment-Analysis-Amazon-Customer-Reviews-using-Web-Scrapping #
Sentiment Analysis of Amazon Customer mobile reviews using Web scrapping

Scapy is used for web scrapping customer reviews of 10 different mobile products. 
It scraps:
1. Name of customer
2. Title of review
3. Rating of Review
4. Text of review

The code for scrapping is present in /Scrape_AmazonReviews/spiders/amazon_reviews.py
If you want to scrape different products then goto above file and change the links in url_list. Also update the range of i to control the page number.

I used this as a guide for scrapping: https://www.usessionbuddy.com/post/How-To-Scrape-Amazon-Reviews-Using-Python/

## Sentiment Analysis ##
After Web scrapping we get reviews.csv file.

### Tools and Languages used: ###
* Python
* sci-kit learn
* Natural Language Toolkit (nltk)
* Pandas
* Numpy
* matplotlib
* Regular Exp (re)

### Steps: ###
1. Loading the data
i. Load the raw data into python lists

2. Data Visualisation
i. Count sentences in various ratings

3. Text preprocessing
i. Convert to lower case
ii. Remove punctuation  and special characters
iii. Remove numbers and emojis
iv. Remove whitespaces and newline characters
v. Removing stopwrods

4. Create Training set and Test set
i. Train-Test split ratio is 80:20 

5. Create Text Encoding
i. Using bigram TF-IDF encoding 

6. Fitting Classifier
i. Using SGD classifier to fit on vectorised data

Train dataset: 5781

Test dataset: 1446

### Model Evaluation ### 
The above implementation has **88% accuracy** for test data.

F1 score for positive sentiment: 0.91

F1 score for negative sentiment: 0.79

### Summary ###
1. To further improve F1 score for negative sentiment use balanced dataset.
2. To improve accuracy implement Word2Vec encoding rather than TF-IDF encoding.

