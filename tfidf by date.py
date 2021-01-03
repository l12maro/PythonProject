Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import nltk, re, pprint, os, itertools
from nltk import word_tokenize, WordNetLemmatizer
from gensim.corpora.dictionary import Dictionary
from gensim.models.tfidfmodel import TfidfModel
from collections import defaultdict

with open("Chat.txt", 'r', encoding="utf8") as f:
	text = f.readlines()

	
def line_split(line):
        last_seen_month = 0
        last_seen_year = 0
	if ' - ' in line:
		date_time, full_message = line.split(' - ', 1)
		date, time = date_time.split(' ', 1)
		day, month, year = date.split('/', 2)
		author, message = full_message.split(': ', 1)
		last_seen_month = month
		last_seen_year = year
		return month, year, message
	else:
		message = line
		return last_seen_month, last_seen_year, message

	
# Create a list with the relevant information of each line, for each line
extracted_date_text = [line_split(l) for l in text]

# Add list to a dictionary
categorized = {}
for i in range(0, len(extracted_date_text),1):
	month = extracted_date_text[i][0]
	year = extracted_date_text[i][1]
	#preprocess text
	alpha_only = [t for t in word_tokenize(extracted_date_text[i][2].lower())if t.isalpha()] 
	wordnet_lemmatizer = WordNetLemmatizer()
	message = [wordnet_lemmatizer.lemmatize(t) for t in alpha_only]

	if (month, year) in categorized:
		categorized[(month, year)].append(message)
	else:
		categorized[(month, year)] = [message]

# Simplify dictionary
def flattenList(l):
    return [item for sublist in l for item in sublist]
corpus_docs = [ flattenList(e) for e in list(categorized.values())]

number_of_docs = len(corpus_docs)

# Apply tfidf model to our data
# Create a Dictionary 
dictionary = Dictionary(corpus_docs)
# Create a corpus from a bag of words
corpus = [dictionary.doc2bow(doc) for doc in corpus_docs]
# Create a defaultdict
total_word_count = defaultdict(int)
# populate the empty defaultdict with word count from the whole corpus
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count
# instantiate a tfidf model
tfidf = TfidfModel(corpus)
number_of_words_from_every_doc = 1 # you can change this to get more words out of every portion/doc
total_unique_words = {}
for i in range(len(corpus_docs)):
    # weigh a certain document against the corpus
    tfidf_weights = tfidf[corpus][i]
    # Sort the unique words
    sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)
    # Print the top unique word in every portion
    for term_id, weight in sorted_tfidf_weights[:number_of_words_from_every_doc]:
        total_unique_words[dictionary.get(term_id)] = weight
"""
final result
"""
unique_words_descending_wights = sorted(total_unique_words.items(), key=lambda w: w[1], reverse=True)
unique_words = [t[0] for t in unique_words_descending_wights]
print(','.join(unique_words[0:50])) #first 50 words

