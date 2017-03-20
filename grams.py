import pandas
import re
import pickle

df=pandas.read_csv('reduced_chat_data.csv')
#print df['message']
bi={}
bi["nn"]=2
tri={}
tri["nn"]=3
quad={}
quad["nn"]=4
penta={}
penta["nn"]=5

def create_grams(st):
	for j in range(200):
		print j
	#	print df["message"][j]
		input_list=df["message"][j].split(" ")
		li=zip(*[input_list[i:] for i in range(st["nn"])])
		#print li
		for l in li:
			l=" ".join(l)
			l=l.strip(" ")
			#print l
			#print type(l)
			st[l]=df.message.str.contains(r""+re.escape(l)).sum()
	return st
dic=create_grams(bi)
print dic
pickle.dump(dic,open('bi2.txt','wb'))