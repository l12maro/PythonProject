Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk, re, pprint, os
>>> from nltk import word_tokenize, WordNetLemmatizer
>>> os.chdir(r"C:\Users\loren\Dropbox\Estudios\Universidad\Uni Tübingen\ISCL\Asignaturas\1. Semester\Data Collection on the Web\Project\Data")
>>> with open("total.txt", 'r', encoding="utf8") as f:
	text = f.read()

	
>>> alpha = [t for t in word_tokenize(text.lower()) if t.isalpha()]
>>> lemmatizer = WordNetLemmatizer()
>>> preprocessed = [lemmatizer.lemmatize(t) for t in alpha]
>>> newtext = nltk.Text(preprocessed)
>>> newtext.collocations()
feel like; night night; make sense; animal crossing; look like; sound
like; last night; holy shit; good idea; sleep well; pretty sure; every
day; okay cutie; feel bad; good job; senior design; poor baby; make
sure; last year; seems like
>>> 
