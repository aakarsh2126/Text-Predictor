import numpy as np
import tkinter as tk
import keras
from keras.preprocessing.sequence import pad_sequences
from pickle import load
from keras.models import load_model
from tkinter import *
from tkinter import ttk
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

#load the model
model=load_model('model.h5')
#load the tokenizer
tokenizer = load(open('tokenizer.pkl', 'rb'))
# load cleaned text sequences
in_filename = 'republic_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1

def cat1():
    new=e1.get()+' '+e2.get()
#    print(new)
    e1.delete(0,END)
    e1.insert(0,new)

def cat2():
    new=e1.get()+' '+e3.get()
#    print(new)
    e1.delete(0,END)
    e1.insert(0,new)

def cat3():
    new=e1.get()+' '+e4.get()
#    print(new)
    e1.delete(0,END)
    e1.insert(0,new)

    
def clear_text():
#    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    
def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
	result = list()
	in_text = seed_text
	# generate a fixed number of words
	for _ in range(n_words):
		# encode the text as integer
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# predict probabilities for each word
		yhat = model.predict_classes(encoded, verbose=0)
		# map predicted word index to word
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		# append to input
		in_text += ' ' + out_word
		result.append(out_word)
	return ' '.join(result)

def predict():
    fileD=open("input.txt", "a")
    fileD.write("%s\n" % e1.get())
    # select a seed text
    #seed_text = lines[randint(0,len(lines))]
    fileD=open("input.txt", "r+")
    seed_text=fileD.readline()
    #print(seed_text + '\n')
    fileD.truncate(0)
    seed_text=seed_text+' '
    # generate new text
    #print(seed_text)
    generated=generate_seq(model,tokenizer,seq_length,seed_text,3)
#    print(generated)
    generated=generated+' '
    s1=''
    s2=''
    s3=''
    i=0
    while generated[i]!=' ':
        s1=s1+generated[i]
        i=i+1
#    print(s1)
    i=i+1
    s1=s1+' '
    while generated[i]!=' ':
        s2=s2+generated[i]
        i=i+1
#    print(s2)
    s2=s1+s2    
    i=i+1
    while generated[i]!=' ':
        s3=s3+generated[i]
        i=i+1
#    print(s3)
    s2=s2+' '    
    s3=s2+s3
    f1=open("output1.txt","w")
    f1.write("%s\n" % s1)
    f2=open("output2.txt","w")
    f2.write("%s\n" % s2)
    f3=open("output3.txt","w")
    f3.write("%s\n" % s3)
    
    #inserting into 1st,2nd and 3rd perdiction entry
    f1=open("output1.txt", "r+")
    seed_text=f1.readline()
#    print(seed_text[:-1])
    e2.delete(0,END)
    e2.insert(0,seed_text[:-1])
    
    f2=open("output2.txt", "r+")
    seed_text=f2.readline()
#    print(seed_text[:-1])
    e3.delete(0,END)
    e3.insert(0,seed_text[:-1])
    
    f3=open("output3.txt", "r+")
    seed_text=f3.readline()
#    print(seed_text[:-1])
    e4.delete(0,END)
    e4.insert(0,seed_text[:-1])
    
    f1.truncate(0)
    f2.truncate(0)
    f3.truncate(0)
    
 # Structure and Layout
window=Tk()
window.title("Text Predictor")
window.geometry("1000x500")
window.config(background='silver')
Label(window,text='Type Here',font=("Helvetica", 18)).grid(row=1)  
e1=Entry(window,width=75,font=("Helvetica",12)) 
e1.grid(row=1,column=2,padx=10,pady=20)
#e1.insert(0,'A default') 

#l=Label(window,text='Predicted Text').grid(row=3,padx=10,pady=10)
l2=Label(window,text='1st Prediction',font=("Helvetica", 16)).grid(row=4)
l3=Label(window,text='2nd Prediction',font=("Helvetica", 16)).grid(row=5)
l4=Label(window,text='3rd Prediction',font=("Helvetica", 16)).grid(row=6)

e2 = Entry(window,width=75) 
e2.grid(row=4,column=2,padx=10,pady=5)
e3 = Entry(window,width=75) 
e3.grid(row=5,column=2,padx=10,pady=5) 
e4 = Entry(window,width=75) 
e4.grid(row=6,column=2,padx=10,pady=5)

b1=Button(window,text='Select',width=4,bg='black',fg='white',font=("Times New Roman",12,"bold"),command=cat1)
b1.grid(row=4,column=4,padx=10,pady=10)
b2=Button(window,text='Select',width=4,bg='black',fg='white',font=("Times New Roman",12,"bold"),command=cat2)
b2.grid(row=5,column=4,padx=10,pady=10)
b3=Button(window,text='Select',width=4,bg='black',fg='white',font=("Times New Roman",12,"bold"),command=cat3)
b3.grid(row=6,column=4,padx=10,pady=10)

button=Button(window,text='Predict',width=7,bg='black',fg='white',font=("Times New Roman",12,"bold"),command=predict)
button.grid(row=3,column=2,padx=10,pady=10)
 
clear=Button(window,text='Clear',width=7,bg='black',fg='white',font=("Times New Roman",12,"bold"),command=clear_text)
clear.grid(row=8,column=2,padx=10,pady=10)
window.mainloop()