import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import pickle
import os

open_pickle = open("StudentsT.pickle", "rb")  # this opens up the pickle file so it can be loaded into the linear model
linear = pickle.load(open_pickle)  # This loads the opened pickle file into linear

open_pickle = open("Students.pickle", "rb")
Students = pickle.load(open_pickle)

# This bit open up the list of students so this program can work with them

# for i in range(len(Students)):
#    print(i, Students[i])
# x = int(input())
# print(Students[x][5])


file = open("d.temp", "r")
targets = file.read()
#print(targets)
x = targets.split(",")
del x[len(x) - 1]  # because of loop in the main program that write data to the "targets" file
# there will always be an extra "" so this removes it
#print(type(x), x, len(x))
for i in range(len(Students)):
    #print(i)
    if str(i) in targets :  # this block of code searchers all of the “targeted” indexes of the students to see if are target for predictions
        print(Students[i])
        #  print(Students[i][6])
        temp = list(map(int, Students[i][6]))  # the map function converts all of the strings inside this list into numbers so the model can work with it
        # we know the location fo the relevant data because it is the 6th element in every list  and "i" is the current list
        test = np.array(temp).reshape(-1, 5)  # we have to reshape the array so the model can use the data
        prediction = linear.predict(test)  # This uses the model we loaded in from our pickle file to make a prediction
        # about what the final mark might be
        #print(prediction)
        #print(Students[i])
        Students[i][5] = round(float(prediction))  # Now that we know the models prediction we can update the data in the list
        #print(Students[i])
        #  This is why I used nested lists, the data the AI is all grouped together for easy access

# new data order: first name, last name, grade, class name, final grade (if you know it), Ai predicted grade (if you ran that part of the program yet), first grade, second, grade, studytime, failures, then absences

# Now that all of the work is done with the model we can update our saved version of the Students list
# so teh main program can work with it
with open("Students.pickle", "wb") as fp:  # we save our complete version of the students list
    pickle.dump(Students, fp)


