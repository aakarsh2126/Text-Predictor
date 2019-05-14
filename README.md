# Text-Predictor
A GUI based Recurrent Neural Network Model which gives top 3 next predictions of words for user's input.
## Libraries Used
Tkinter
Numpy
Matplotlib
Keras
Pandas
Pickle
## Recurrent Neural Network
### Introduction
The Recurrent Neural Network(RNN) is a special type of neural network which has memory(LSTM).In Classical feed forward neural network,the output of any any node depends on the current input.In RNN the output of current state not only depends on current input,but also the output from previous state.
### ht=f(xt*w+h(t-1)*wrec)
ht=output of current state
xt=input at current state
w=weight matrix for node in current state
h(t-1)=output of previous state
wrec=weight matrix for node in previous state
### Long Short Term Memory(LSTM)
The LSTM cells functions the working of neuron in RNN model.The long means they can store memory for long period of time and short means they have limited memory.
## Working 
The working of model is done by first training the model with dataset of 3 novels.The current output at timestamp t depends on previous 5 outputs with timestamps t-1,t-2,t-3,t-4 and t-5.A GUI based application asks user to input a senetence of any given size.At any step we can generate top 3 predicted words based on current input ans select any of the 3 or can ignore it. 
