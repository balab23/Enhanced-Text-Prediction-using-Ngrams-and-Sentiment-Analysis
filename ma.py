import pickle
import re

def rank(sd):
	bi=pickle.load(open('bi.txt','rb'))
	print bi
	gr="at the"
	gr="".join(gr.split(" ")[1]).strip(" ")
	re={}
	for i in bi:
		if i.startswith(gr):
			re[i]=bi[i]
	return re
rank("")