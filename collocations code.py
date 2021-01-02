import nltk, re, pprint, os
from nltk import word_tokenize, WordNetLemmatizer
os.chdir(r"C:\Users\loren\Dropbox\Estudios\Universidad\Uni Tübingen\ISCL\Asignaturas\1. Semester\Data Collection on the Web\Project\Data")
with open("total.txt", 'r', encoding="utf8") as f:
	text = f.read()

alpha = [t for t in word_tokenize(text.lower()) if t.isalpha()]
lemmatizer = WordNetLemmatizer()
preprocessed = [lemmatizer.lemmatize(t) for t in alpha]
newtext = nltk.Text(preprocessed)
newtext.collocations()

