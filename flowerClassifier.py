# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:29:10 2022

@author: Purushotam Sangroula
This project is used to classify flowers based upon dimensions length and breadth.
data variable is used as training data set in which 0->length, 1 -> breadth and 2 -> color or flower
where 0 indicates blue flower 
and 1 indicates red flower

mystery_flower: a variable to query whether a flower with given dimension is red or a blue one.
Windows text to speech converter has been used to produce voice in windows machine regarding flower's classification.

The concept of this project is taken from the following sources:
https://www.youtube.com/watch?v=LSr96IZQknc&t=112s
https://www.youtube.com/c/giantneuralnetwork
"""

from matplotlib import pyplot as plt 
import numpy as np

data = [[3,   1.5, 1],
        [2,   1,   0],
        [4,   1.5, 1],
        [3,   1,   0],
        [3.5, .5,  1],
        [2,   .5,  0],
        [5.5,  1,  1],
        [1,    1,  0]]

mystery_flower = [2,2]

#network
#  ips: width, length
#  


def sigmoid(x):
    return 1/(1+np.exp(-x))
def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))

# T = np.linspace(-20,20,100)
# Y = sigmoid(T)
# Y_p = sigmoid_p(T)
# # plt.plot(T,Y)
# # plt.plot(T,Y_p)

# #scatter data
# # plt.axis([0,6,0,6])
# # plt.grid()
# for i in range(len(data)):
#     point = data[i]
#     color='r'
#     if point[2] == 0:
#         color = 'b'
#     # plt.scatter(point[0], point[1], c =color)


def train():
    w1 = np.random.randn()
    w2 = np.random.randn()
    b = np.random.randn()
    costs = []
    learning_rate = 0.01
    for i in range(10000):
        ri = np.random.randint(len(data))
        point = data[ri]
        # print(point)
        
        z= point[0] *w1 + point[1]*w2 + b
        pred = sigmoid(z)
        
        target = point[2]
        cost = np.square(pred-target)
        if i%100 ==0:
            c = 0
            for j in range(len(data)):
                p = data[j]
                p_pred = sigmoid(w1 * p[0] + w2 * p[1] + b)
                c += np.square(p_pred - p[2])
            costs.append(c)
        
        dcost_pred = 2*(pred-target)
        dpred_z = sigmoid_p(z)
        
        dz_w1 = point[0]
        dz_w2 = point[1]
        dz_b = 1
        
        dcost_z = dcost_pred * dpred_z
        dcost_w1 = dcost_z * dz_w1
        dcost_w2 = dcost_z * dz_w2
        dcost_b = dcost_z * dz_b
        
        w1 = w1 - learning_rate*dcost_w1
        w2 = w2 - learning_rate*dcost_w2
        b = b - learning_rate*dcost_b
    # plt.plot(costs)
    return w1,w2,b, costs 
def predict_flower(mystery_flower,w1,w2,b):
    z = w1 * mystery_flower[0] + w2 * mystery_flower[1] + b
    pred = sigmoid(z)
    print(pred)
    from win32com.client import Dispatch
    
    speak = Dispatch("SAPI.SpVoice").Speak
    if pred>0.5:
        speak("The flower is red")
    else:
        speak("The flower is blue")
w1,w2,b,costs = train()
# plt.axis([0,1], kwargs)
fig = plt.plot(costs)
predict_flower(mystery_flower, w1, w2, b)




