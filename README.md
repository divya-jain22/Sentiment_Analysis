# Sentiment_Analysis

**Introduction**

Sentiment analysis is widely used in various domains, including social media monitoring, customer feedback analysis, and market research. This project aims to build a sentiment analysis model using machine learning algorithms to classify text data based on its sentiment.


This project implements sentiment analysis without using natural language processing (NLP) techniques.
Sentiment analysis is the process of determining the sentiment or emotion expressed in a piece of text. In this project, we analyze the sentiment of textual data to derive the all involved emotions in a given text.

**Usage** 

1.Fetch your input text data.

2.Prepare another file as Emotions in which key value pairs are made where key denotes the words and values denotes the emotion.

3.Clean the input data first before going to the analysis section.

4.Then after cleanilng the data and Tokenize the data.

5.After this is done we can now implement the algorithm to derive the emotions from the text.

**Algorithm Works as**
  1) Check if the word in the final word list is also present in emotion.txt
   - open the emotion file
   - Loop through each line and clear it
   - Extract the word and emotion using split

  2) If word is present -> Add the emotion to emotion_list
  3) Finally count each emotion in the emotion list


6.Run the sentiment_analysis.py script to preprocess the data.

7.To visualize the output run the visualize.py.


