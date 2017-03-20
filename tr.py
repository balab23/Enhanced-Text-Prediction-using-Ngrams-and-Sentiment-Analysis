from Tkinter import *
import msvcrt
from get_ngrams2 import predict_next_word
import collections
import operator
import subprocess
from decimal import Decimal
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle 



#	text.set()
sentilist=[]
se=0
coun=0

def senti_eval(st):
	tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,stop_words='english')
	file = open('C:\Users\\balaji\Desktop\\trial\\affectivetext_trial.txt', 'r')
	dataset=file.readlines()[1:-1]
	#print dataset
	for idx , headline in enumerate(dataset):
		dataset[idx]=headline.strip("\n")
		#if len(headline)<=1:
		#	print idx
		#print headline
	tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,stop_words='english')
	tt=tfidf_vectorizer.fit_transform(dataset)
#	print tt.shape
	tfidf_vectorizer.fit(dataset)
	clf=joblib.load('categorical.pkl')
	return clf.predict(tfidf_vectorizer.transform([st]))

print senti_eval("scared") 