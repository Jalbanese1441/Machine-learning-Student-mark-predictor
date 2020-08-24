# modelTrainer
import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import time
import pickle  # this allows for the saving of trained models
import os
from datetime import datetime
# Here we are importing all of library's that we will need
#print (os.path.abspath("test"))
#print(tensorflow.__version__,"v")
data = pd.read_csv("studentData.csv",sep=";")
# This allows us to access the data set, the sep=";" tells the program how the data is separated in the excel file

#print(data)
#print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
# the data set contains 33 pieces of information for each student, the model does not need all of that
# data and it would be extra work to constantly use it. So now "data" contains only the useful data
#print(data)
predict = "G3"  # This is the final grade, that the program will try to predict
x = np.array(data.drop([predict], 1))  # This will create an array but with out the values of the G3 column in it
y = np.array(data[predict]) # this will cerate an array with only the perdictign values
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
# This line of code takes all of our attributes and splits them up into 4 different array, then we have test data that we
# will use to test the models accuracy.
# $The 0.1 tells the computer to slit 10% into values that will be used for testing
best = 0
runs = 1
#runs=100000
#runTest=False # I had to initialize this so I could use it later
file=open("n.runs","r")
opened_file=file.read()
runs=int(opened_file)  # This gets the first line in the test file, sets it to "runs" and converts the string into a number
# Note: the model can only be tested against the data one more time after it has been created (in this program) otherwise it starts to memorie the  results
file.close()
# This grabs the number of times the trainer model is supposed to run, that was set in the other program
#print(runs)
#print(runTest)
#runs=30
start = time.time()
for i in range(runs): # this will retrain the model "runs" times in the hopes we can find a more accurate model

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1) # the reasion why it is still defined above and here
    # is so  that when we stop training the model it can
    # still can get the data divided
    linear = linear_model.LinearRegression() # This tells the computer that we are working with a linear regression model
    linear.fit(x_train, y_train) # it is going to find a line of best fit using the date from the training set
    # to find a line of best fit which it will then store in linear

    accuracy = linear.score(x_test, y_test)*100 # this will test the models accuracy against the testing data and store it in accuracy
    #  print(accuracy) # this shows the accuracy, it will fluctuate every time it runs
    #  print(linear.coef_) #
    #Shows the coefficient Note:
    # because there are 5 attributes the line is drawn across 5 dimensional  space and therefor has 5 coefficients
    #  print(linear.intercept_) # Shows the intercept(y)
    #print(best,i+1)

    if accuracy > best:
        # this will save the best model
        best = accuracy
       # print("accuracy updated")
        with open("StudentsT.pickle", "wb") as f:
            pickle.dump(linear, f)
        # this saves our trained model so it can be used later
        # Some models may take days to train so this way we don't need to retrain them each time the program runs
        # Saves it as a .pickel file
end = time.time()
timeTook= end - start # calculates the time it took for the model to train
#print("time operation took is",timeTook, "seconds for",runs)
current_time = datetime.now().time() # this lets me add time to the log files
file = open("model.log", "w") # the "w" writes over the current file
# only the last run is logged
file.writelines([str(current_time),"\n",str(runs),"\n",str(best),"\n",str(timeTook)])
file.close()
# stores this information in a log file for later use


# G3 is out of 20
#open_pickle = open("student_model.pickle", "rb")
# this opens up the pickle file so it can be loaded into the linear model
#linear = pickle.load(open_pickle)
# This loads the opened pickle file into linear
#print(linear.intercept_)
#print("the selected models accucary is",best)
#accuracy = linear.score(x_test, y_test)*100
#print("The model current accucary is",accuracy,"with this data set")
#accuracy = linear.score(x_test, y_test)*100
#print("The model current accucary is",accuracy,"with this data set")
#accuracy = linear.score(x_test, y_test)*100
#print("The model accucary is",accuracy)



open_pickle = open("StudentsT.pickle", "rb")  # this opens up the pickle file so it can be loaded into the linear model
linear = pickle.load(open_pickle)  # This loads the opened pickle file into linear
# x=np.array([90,90,20,0,0]).reshape(-1,5)
# x=np.array([5,6,2,0,6]).reshape(-1,5)
predictions = linear.predict(x_test) # This will make the model predict the finales grades in the testing data set
# and store them in predictions
file = open("predictionsTest.txt","w")

for i in range(len(predictions)):
    #  print(predictions[i], x_test[i], y_test[i])
    if predictions[i] < 0: predictions[i] = 0  # You can't get a negative test score, you just fail
    data = "Model prediction: " + str(round(float((predictions[i]/20)*100)))+"% Actual mark: " + str(round(float((y_test[i]/20)*100)))+"%\n"
    # This long line of code converts the predicted grade and real grade into percentages,
    # then rounds them, then converts
    # them ino strings so they can be written to a text file.
    # The "\n" just makes sure that the text will be on different lines
    # G3 is out of 20
    #  data=(predictions[i]/20)*100
    #  print(data,predictions[i])
    #  print(data)
    file.write(data,)
file.close()

file = open("t.temp", "w")
file.write("Delete Me")
file.close()
# This program is run from a conda virtual environment so the main program can't tell then this has
# finished running. My solution is to create a temporary file that the main program wil check to see if it is there
# if the temporary file is detected the main program will know that the model is now trained and can now use it

exit(0)  # This exit function is very important because this script will be run in a conda virtual environment
# it needs to be exited or else it would just stay on teh screen
#  print(best)





