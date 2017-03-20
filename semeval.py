import sklearn
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
#from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas
import numpy
from sklearn.externals import joblib
from sklearn import svm
import collections
import operator

dataset = fetch_20newsgroups(shuffle=True, random_state=1,remove=('headers', 'footers', 'quotes'))
data_samples = dataset.data

#tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,stop_words='english')
#tfidf = tfidf_vectorizer.fit_transform(data_samples)
#print tfidif.shape

def categorical(corpus,target):
	print"..................Categorical........................"
	file = open(corpus, 'r')
	dataset=file.readlines()[1:-1]
	#print dataset
	for idx , headline in enumerate(dataset):
		dataset[idx]=headline.strip("\n")
		#if len(headline)<=1:
		#	print idx
		#print headline
	tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,stop_words='english')
	tfidf = tfidf_vectorizer.fit_transform(dataset)
	print tfidf.shape

	file2 = open(target, 'r')
	targets=file2.readlines()

	for idx, targ in enumerate(targets):
		targets[idx]=targ.strip('\n').strip(',').lower()
		targets[idx]=targets[idx].split(" ")
		targets[idx]=targets[idx][1:]
		targets[idx]=targets[idx].index(max(targets[idx]))
	print targets

	clf = svm.LinearSVC()
	clf.fit(tfidf, targets)
	predicted = clf.predict(tfidf)
	joblib.dump(clf, 'categorical.pkl') 

	print predicted
	counter=collections.Counter(list(predicted))
	print max(counter.iteritems(), key=operator.itemgetter(1))[0]

	print accuracy_score(targets, predicted)
	print sklearn.metrics.confusion_matrix(targets, predicted, labels=None) 
	print len(targets)
def cluster(vc,corpus,target):
	print "................................Dimension................................."
	dimensions=pandas.DataFrame.from_csv(vc, sep=',', index_col=False)
	#print dimensions
	dim_matrix=dimensions.as_matrix()

	file = open(corpus, 'r')
	dataset=file.readlines()[1:-1]
	for idx, headline in enumerate(dataset):
		dataset[idx]=headline.strip('\n').strip(',').lower()
	print dataset

	dim=list(dim_matrix[:,0])
	
	#print dim

	f_vector=[]


	for idx, headline in enumerate(dataset):
		vector=numpy.tile(0.0,3)
		count=0
		print "headline is: "+headline
		for word in headline.split(" "):
			count+=1
			if word in dim:
				print "matrix values :"
				print [dim_matrix[dim.index(word)][2],dim_matrix[dim.index(word)][4],dim_matrix[dim.index(word)][6]]
				vector+=[dim_matrix[dim.index(word)][2],dim_matrix[dim.index(word)][4],dim_matrix[dim.index(word)][6]]
				print "word vector is :-"
				print vector
		print "vector of sentence :"
		print vector
		vector=vector/float(count)
		f_vector.append(vector)
	
	print f_vector

	ac=[2.55,6.60,5.05]
	fc=[3.20,5.92,3.60]
	jc=[7.40,5.73,6.20] 
	sc=[3.15,4.56,4.00]

	scores_matrix=[]
	predicted=[]
	for idx, headline in enumerate(dataset):
		scores=[cosine_similarity(f_vector[idx],ac),cosine_similarity(f_vector[idx],fc),cosine_similarity(f_vector[idx],jc),cosine_similarity(f_vector[idx],sc)]
		sem_label=scores.index(max(scores))
		print "label of "+ headline +" is "+ str(sem_label)	
		scores_matrix.append(scores)
		predicted.append(sem_label)
		print "predicted is:"
		print predicted

	file2 = open(target, 'r')
	targets=file2.readlines()

	for idx, targ in enumerate(targets):
		targets[idx]=targ.strip('\n').strip(',').lower()
		targets[idx]=targets[idx].split(" ")
		del targets[idx][2]
		targets[idx]=targets[idx][1:5]
		targets[idx]=targets[idx].index(max(targets[idx]))
	print "targets are:"
	print targets


	print accuracy_score(targets, predicted)
	print sklearn.metrics.confusion_matrix(targets, predicted, labels=None) 


#	sem_label=scores.index(max(scores))
	
#categorical("C:\Users\\balaji\Desktop\\trial\\affectivetext_trial.txt","C:\Users\\balaji\Desktop\\trial\\affectivetext_trial.emotions.gold")	
cluster("C:\HCI Project\\all.csv","C:\Users\\balaji\Desktop\\trial\\affectivetext_trial.txt","C:\Users\\balaji\Desktop\\trial\\affectivetext_trial.emotions.gold")