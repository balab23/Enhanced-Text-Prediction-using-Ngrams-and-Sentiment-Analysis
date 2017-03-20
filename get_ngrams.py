import subprocess
from decimal import Decimal
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle 

bi=pickle.load(open('bi.txt','rb'))
tri=pickle.load(open('tri.txt','rb'))
quad=pickle.load(open('quad.txt','rb'))

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
	if len(ngram.split(" "))==2:
		sd=bi
	elif len(ngram.split(" "))==3:
		sd=tri
	elif len(ngram.split(" "))==4:
		sd=quad
	

	#print bi
	#gr="at the"
	print "ngram split is "
	print ngram.split(" ")
	ngram=" ".join(ngram.split(" ")[1:]).strip(" ")
	print "rank test ng:- "+ngram
	re={}
	for i in bi:
		if i.startswith(ngram):
			re[i]=bi[i]
	return re
#rank("")


#print ngram_prob("why are you looking at")
def predict_next_word(st):
	input_list=st.split(" ")
	li=[]
	le=0
	'''
	if len(input_list)==2:
		li=zip(*[input_list[i:] for i in range(1)])
		print "2"
		le=1
	'''
	if len(input_list)==3:
		li=zip(*[input_list[i:] for i in range(2)])
		print "3"
		le=2
	elif len(input_list)>=4:
		li=zip(*[input_list[i:] for i in range(3)])
		print "4"
		le=3
	if len(input_list)<=2:
		print "More text required"

	else:
		new=""
		su=Decimal(0.0)

		for l, word in enumerate(li):
			new=""
			for i in range(le):
				new+=li[l][i]+" "
			li[l]=new.rstrip()
			new=new.strip(" ")
		#	print new.rstrip()
	#		print new
			resu=ngram_prob(new)
			if resu!=0:
				su+=Decimal(resu).ln()
			#print "score is "+str(Decimal(resu))
	#		print "log prob now is "+str(su)
		#print new
		result=rank(new)
		#print li
		#print su
	#	print result
#................................................................


#		pred=li[-1].split(' ',1)[1]
#		pred2=pred
#		pred+=" ?"
		#print pred
#		stf=subprocess.check_output("python getngrams.py "+pred+" --startYear=2000 --endYear=2001 -nosave -caseInsensitive")
#		print stf.split("\n")[0].split(',')[1:][0]
#		print st.replace(pred2,stf.split("\n")[0].split(',')[1:][0])
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
		ii=clf.predict(tfidf_vectorizer.transform([st]))
	
	#	print "initial is "+str(ii)
	#	print "..............................."
		ranks=[]
		for l in result.keys():
			
			
			tfidf=tfidf_vectorizer.transform([l])
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
		
		elif not ranks:
			print "yes sadly it is true.......:("
			li=zip(*[input_list[i:] for i in range(2)])
			print "2nd try list "+str(li)
			le=2
			new=""
			su=Decimal(0.0)

			for l, word in enumerate(li):
				new=""
				for i in range(le):
					new+=li[l][i]+" "
				li[l]=new.rstrip()
				new=new.strip(" ")
			#	print new.rstrip()
				print new
				resu=ngram_prob(new)
				if resu!=0:
					su+=Decimal(resu).ln()
				#print "score is "+str(Decimal(resu))
				print "log prob now is "+str(su)
			#print new
			result=rank(new)
			#print li
			#print su
			print result
	#................................................................


	#		pred=li[-1].split(' ',1)[1]
	#		pred2=pred
	#		pred+=" ?"
			#print pred
	#		stf=subprocess.check_output("python getngrams.py "+pred+" --startYear=2000 --endYear=2001 -nosave -caseInsensitive")
	#		print stf.split("\n")[0].split(',')[1:][0]
	#		print st.replace(pred2,stf.split("\n")[0].split(',')[1:][0])
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
			print tt.shape
			tfidf_vectorizer.fit(dataset)
			clf=joblib.load('categorical.pkl')
			ii=clf.predict(tfidf_vectorizer.transform([st]))
			print "initial is "+str(ii)
			print "..............................."
			ranks=[]
			for l in result.keys():
				
				
				tfidf=tfidf_vectorizer.transform([l])
				#print tfidf.shape
				pred=clf.predict(tfidf)
				if pred==ii:
					ranks.append(l)
					#print l
					#print pred 
			return ranks

#st="it was a dark "
#predict_next_word("about your health")