import msvcrt
from get_ngrams import predict_next_word
from Tkinter import *



sentence=""
while True:
	i=""
	word=""
	while True:
		
		i=msvcrt.getche()
		k=ord(i)
		if i==" ":
			#print "yes"
			sentence=sentence+word+" "
			#print sentence
			break
		elif i!=" " and k!=13:
			word=word+str(i)
		if k==13:
			sentence=sentence+word+" "
			break
	#print sentence
	print predict_next_word(sentence.strip(" "))
	if k==13:
		break
print sentence
