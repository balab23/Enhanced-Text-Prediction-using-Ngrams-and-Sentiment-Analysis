import subprocess
from decimal import Decimal
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle 
import operator
import sys
import unicodedata

#reload(sys)

#sys.setdefaultencoding('utf8')
bi=pickle.load(open('bi2.txt','rb'))
tri=pickle.load(open('tri2.txt','rb'))
quad=pickle.load(open('quad2.txt','rb'))

def ngram_prob(ngram):
	sd={}
	
	if len(ngram.split(" "))==2:
		sd=bi
	elif len(ngram.split(" "))==3:
		sd=tri
	elif len(ngram.split(" "))==4:
		sd=quad
	
	#print "sdnn "+str(sd["nn"])
	#print sd
	if ngram in sd:
		return sd[ngram]
	else:
		return 0
	'''
	st=subprocess.check_output("python getngrams.py "+ngram+" --startYear=2000 --endYear=2001 -nosave -caseInsensitive")
	print st
	return float(st.split("\n")[2].split(',')[1])
'''
def rank(ngram):
	sd={}
	print "rank ng is:- "+ngram
	if len(ngram.split(" "))==1:
		sd=bi
	if len(ngram.split(" "))==2:
		sd=tri
	elif len(ngram.split(" "))==3:
		sd=quad
	#elif len(ngram.split(" "))==4:
	#	sd=quad
	

	#print bi
	#gr="at the"
	print "ngram split is "
	print ngram.split(" ")
	#ngram=" ".join(ngram.split(" ")[1:]).strip(" ")
	print "rank test ng:- "+ngram
	re={}
	for i in bi:
		i=unicode(i, errors='ignore')
		if i.startswith(ngram+" "):
			if i in bi:
				re[i]=bi[i]
	print "re is "
	print re
	re=sorted(re.items(),key=operator.itemgetter(1),reverse=True)
	return re
#rank("")


#print ngram_prob("why are you looking at")
def predict_next_word(se,st):
	input_list=st.split(" ")
	li=[]
	le=0
	
	if len(input_list)==1:
		#li=zip(*[input_list[i:] for i in range(1)])
		print "1"
		le=1

	if len(input_list)==2:
		#li=zip(*[input_list[i:] for i in range(1)])
		print "2"
		le=2
	
	if len(input_list)>=3:
		#li=zip(*[input_list[i:] for i in range(2)])
		print "3"
		le=3
	'''
	elif len(input_list)>=4:
		li=zip(*[input_list[i:] for i in range(3)])
		print "4"
		le=3
	'''
	if len(input_list)==0:
		print "More text required"

	else:
		new=""
		

		#	print new.rstrip()
	#		print new
		new=" ".join(input_list[-le:])
		result=rank(new)

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
		if se==-1:
			ii=clf.predict(tfidf_vectorizer.transform([st]))
		else: 
			ii=se
			print "se not zero!!"
	#	print "initial is "+str(ii)
	#	print "..............................."
		ranks=[]
		for l in result:
			
			
			tfidf=tfidf_vectorizer.transform([l[0]])
			#print tfidf.shape
			pred=clf.predict(tfidf)
			if pred==ii:
				ranks.append(l)
				#print l
				#print pred 
		#return ranks
		if ranks:
			print "ranks aint none"
			print "ranks is"
			print ranks
			return ranks

		elif not ranks and le>2:
			print "yes sadly it is true.......:("
			lt=2
			print "trigrams check."
			new=""
			new=" ".join(input_list[-lt:])
			result=rank(new)
			#print li
			#print su
			print result
			ranks=[]
			for l in result:
				tfidf=tfidf_vectorizer.transform([l[0]])
				#print tfidf.shape
				pred=clf.predict(tfidf)
				if pred==ii:
					ranks.append(l)
					#print l
					#print pred 
			if ranks:
				print "yes"
				print ranks
				return ranks
			
			elif not ranks and le>1:
				print "yes sadly it is true.......:("
				lt=1
				print "bigram check."
				new=""
				new=" ".join(input_list[-lt:])
				result=rank(new)
				#print li
				#print su
				print result
				
				ranks=[]
				for l in result:
					tfidf=tfidf_vectorizer.transform([l[0]])
					#print tfidf.shape
					pred=clf.predict(tfidf)
					if pred==ii:
						ranks.append(l)
						#print l
						#print pred 
				if ranks:
					print "yes ranks"
					print ranks
					return ranks
				else:
					print "no ranks"
					print result
					result.append("::")
					return result

#st="it was a dark "
#predict_next_word("about your health")