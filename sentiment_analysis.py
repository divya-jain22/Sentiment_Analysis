# Importing all the necessary Libraries 
import string
from collections import Counter

import matplotlib.pyplot as plt

# Opening the input text file
data = open("input.txt", encoding="utf-8").read()

# converting to lowercase to disqualify any descrimination among the upper case and lower case alphabets 
lower_case = data.lower()

# Removing all the present punctuations from the data
# This process will clean all the data which is being converted to lower case.

cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
# Here the process of Tokenization is being performed without using NLTK library
tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# Here starts the analysing of the cleaned data to derive all the emotions involved in the given input data.
# To do so we have used a file named emotions.txt which  has the key value pair for the words as key and emotion they denote as value.

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)
