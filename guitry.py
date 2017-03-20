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
se=-1
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


def assign(event=None):
	global coun 
	global se
	global sentilist
	coun+=1
	inpu=text.get("1.0",END)
	print inpu
	if coun==3:
		sentilist=sentilist[-3:]
	se=senti_eval(inpu)
	sentilist.append(se[0])
	counter=collections.Counter(list(sentilist))
	se=max(counter.iteritems(), key=operator.itemgetter(1))[0]
	print "senti is "+str(se)
	print sentilist
	text.delete('1.0',END)
	#label=Label(window,textvariable=result)
	#nolabel=Label(window,text='None')




def refresh():
	label.destroy()
	nolabel.destroy()

def retrieve_input(event=None):
	#print "Suggestions:"
	#print predict_next_word(text.get("1.0",END).strip(" "))
	inpu=text.get("1.0",END)

	#print inpu 
	inpu=inpu.strip("\n").strip(' ')
	print inpu.split(" ")
	resu=predict_next_word(se,inpu)
	# url=""
	

	if resu is None: 
	    
		#label.pack_forget()
		nolabel.pack()
		#label.destroy()
			#label.grid(row=i)
			#label.bind("<Button-1>",)
		print "resu is none"


	if not resu is None: 
	    for i,url in enumerate(resu):
			#nolabel.pack_forget()
			#label.pack_forget()
			#label(frame,text=url).pack()
			#label.grid(row=i)
			#label.bind("<Button-1>",)
			#label=Label(frame,text=url)
		print "resu is"
		print resu
	#	nolabel.destroy()
		if len(resu)>10:
			resu=resu[0:10]
		result.set(str(resu))
		label.pack()
	if not resu is None:
		if "::" in resu:
			Label(window,text="no senti-match :(",bg="red").pack()
		else:
			Label(window,text="senti-match :)",bg="green").pack()


	


window = Tk()

frame=Frame(window)
frame.pack()

text = Text(frame, width=40, height=10)
text.insert('1.0', 'here')
text.pack()

result = StringVar()
label=Label(window,textvariable=result)
nolabel=Label(window,text='None')
#label.pack()

#button=Button(window,text="Count", command=retrieve_input)
#button.pack()

window.bind("<space>",retrieve_input)
window.bind("<Return>",assign)
window.mainloop()