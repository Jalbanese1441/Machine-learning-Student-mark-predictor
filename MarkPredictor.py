# Here we are importing all of library's that we will need
import os
import os.path
import time
cls = lambda: os.system("cls")
import pickle
import setup # this the custom module that I made, unpin being imported it will check to
# see if the program needs to be set up
# if it does it will run the program setup
def trainModel(n): # This will train train the AI model
    #n="176"
    file=open("n.runs","w")
    file.write(n)
    file.close()
    # This sets the number of time the model trainer is supposed to run

    os.startfile("startTrainer.vbs")  # This starts a vbs file that will (with the help of another file) start to train the model
    # I did not put any coments in non-python files
    # vbs files alows the user to "take over" commands and functions other program usualy controll
    # I used that to
    counter = 0
    cls()
    while os.path.exists("t.temp")==False:
        time.sleep(.5)
        cls()
        if counter==3: counter = 0
        print("Model training: "+"."*counter)
        counter += 1
        # this will play a "..." animation while waiting for the model to finish training
    time.sleep(2)
    cls()
    os.remove("t.temp") # we need to delete this so the user has the option of retraining the model later
    time.sleep(1)
    os.startfile("closeCodaTerminal.vbs")
    print("Model Successfully Trained!\nPress enter to continue")


def inputChecker(testText,type):
    if type=="string":
        if testText.isalpha() == True:
            return True
        else : return False
    else:
        if testText.isdigit() == True : return True
        else : return False
# this check to see if the text if valid or not. It just saves me from retyping this code several time

def edit_students(Students):
    with open("Students.pickle", "wb") as fp: # we need to be able to override the cruet file encase the user decides to delete a student
        pickle.dump(Students, fp)
        # this saves the nestled lists to a .pickle file like the Ai model uses

def get_students():
    open_pickle = open("Students.pickle", "rb")
    Students= pickle.load(open_pickle)
    return Students
# this loads in out pickle file of nestled lists

def student_finder(Students, target): # This will take in a target sn search the list of students for matches and print them out
    for i in range(len(Students)):
        if target in Students[i]:
            print(Students[i])



#setup.Setup_Program.test()
Students = [] # this will be the list that holds all of the students
#print(type(Students))
Students = get_students() # We need to load in our student file
#print(type(Students))
#print(Students)
#for s in Students: print(s)


print("Welcome to the mark predictor\nThis program uses a type of artificial intelligence known as machine learning")
print("The program uses a linear regression algorithm to look at all aspects of the data")
print("plots the data in multiple dimensions, then draws a line of best fit (look at the comments in the code for a better explanation)")
print("The model can then try to predict the results using the line of best fit")
print("\nThis AI takes in a data set of students information regarding their performance, and tries to predict their final mark")
print("press enter to continue")
input()
while True:
    cls()
    print("----------------------- Mark Predictor -----------------------")
    print("Type the number before the bracket and press enter to activate the corresponding action")
    print("Student options:")
    print("1) See a list of all students and their data\n2) Search for all students in a certain class")
    print("3) Search for a student by first name\n4) Search for a student by last name")
    print("5) Add or remove a student from the list\n6) Delete all students from the list")
    print("AI Model options:")
    print("7) see model info\n8) predict student’s marks")
    print("9) see model accuracy test results\n10) delete and retrain model\nOr type \"help\" and press enter for help / tutorial")
    print("Type \"exit\" and press enter to exit")
    x = input()

    # The following set of if statements does what it says above, so there will be very few comments in them

    if x == "exit": exit(0)
    if x == "1":
        cls()
        print("Number of Students:",len(Students))
        print("Please note: all student grades are out of 20")
        print("The data is arraigned first name, last name, grade, class name, final grade (if you know it), Ai predicted grade (if you ran that part of the program yet), first grade, second, grade, studytime, failures, then absences")
        #name, lastName, grade, subject, finalGrade, "NA", ai_stuff
        #G1, G2, Stime, failures, finalGrade, "NA", absences
        print("With commas separating the data")
        for s in Students:
            print(s)
        print("Press enter to continue")
        input()
    if x=="2":
        cls()
        print("Type in the class name you want to search for")
        target = input()
        print("Students who have the class of",target,"are:")
        student_finder(Students, target) # this calls on a search method I made
        print("Press enter to be taken back to the start")
        input()

    if x == "3":
        cls()
        print("Type in the students name you want to search for")
        target = input()
        print("Students named",str(target)+":")
        student_finder(Students, target)
        print("Press enter to be taken back to the start")
        input()
    if x == "4":
        cls()
        print("Type in the students last name you want to search for")
        target = input()
        print("Students with a last name of",target,"are:")
        student_finder(Students, target)
        print("Press enter to be taken back to the start")
        input()

# For 1-4 you can actually use any search target

    if x == "5":
        while True:
            cls()
            print("Type a to add a student or r to remove (press enter after)")
            x=input()
            if x=="r":
                cls()
                print("Please note: all student grades are out of 20")
                print("The index number will be displayed in front of the student's data, type in that number and press enter to delete the data")
                for i in range(len(Students)): print("Index number:",i+1,"Student's data:",Students[i]) # this prints out all of the students data to the user
                x = input()
                testText = x
                type ="number"
                if inputChecker(testText,type) == True:
                    x = int(x)
                    if x >1:
                        if x <= len(Students):
                            del Students[x-1]  # if all of the
                            # parameters are correct then the students dat wil be removed
                            edit_students(Students)
                            print("Student data removed")
                        else:
                            cls()
                            print("That was not a valid response, press enter to be taken back to the main screen")
                            input()
                            break
                    else:
                        cls()
                        print("There is only the example student that you can't delete, you need to add students first")
                        print("Press enter to be taken back to the main menu")
                        input()
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break

            elif x == "a":
                cls()
                print("Please note: all student grades are out of 20, please report the value out of 20 (with no decimals)")
                print("Please type the students first name")
                testText= input()
                type = "string"
                if inputChecker(testText,type) == True : name= testText
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break
                cls()
                print("Please type the students last name")
                testText= input()
                type = "string"
                if inputChecker(testText,type) == True : lastName= testText
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break
                cls()
                print("Please type the students grade")
                testText= input()
                type = "number"
                if inputChecker(testText,type) == True : grade= testText
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break
                cls()
                print("Please type the class name or class code the student is in")
                subject= input()
                cls()
                print("Please type the students first mark (out of 20, also no decimal places aloud)")
                testText = input()
                type = "number"
                if inputChecker(testText, type) == True:
                    G1 = testText
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break
                cls()
                print("Please type the students second mark (out of 20, also no decimal places aloud)")
                testText = input()
                type = "number"
                if inputChecker(testText, type) == True:
                    G2 = testText
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break
                cls()
                print("Please type the students study time (also you may need to round and no decimal places aloud)")
                print("ex: if they studies for two hours and 45 minuets type 2 and press enter")
                testText = input()
                type = "number"
                if inputChecker(testText, type) == True:
                    Stime = testText
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break
                cls()
                print("Please type the number of times the student has failed")
                testText = input()
                type = "number"
                if inputChecker(testText, type) == True:
                    failures = testText
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break
                cls()
                print("Please type the number of times the student has missed class")
                testText = input()
                type = "number"
                if inputChecker(testText, type) == True:
                    absences = testText
                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()
                    break
                cls()
                print("If you know it enter the grade the student got on their final test, if you don't know it just type Na")
                print("(Out of 20, also no decimal places aloud)")
                finalGrade = input()
                ai_stuff = [G1,G2,Stime,failures, absences]
                # the Na is where the ai predicted score goes
                temp = [name,lastName,grade,subject,finalGrade,"NA",ai_stuff]
                Students.append(temp)
                edit_students(Students) # calls on a method to add the new students to the save file
                # this bit adds the new student data to the Students list for storage
                # I used a nestled list so the data for the model was kept separate from the rest
                # did not need to check to see if the user entered a valid response for some of the questions above because the model
                # does not use them
                print(temp,"was successfully added to the list of students, press enter to be taken back to the main menu")
            else:
                cls()
                print("That was not a valid response, press enter to be taken back to the main screen")
            input()
            break

    if x == "6":
        cls()
        print("Are you sure that you want to delete all students from the list?")
        print("(y or n)")
        x = input()
        if x == "y":
            cls()
            Students = [] # This reinitialized the list, it wiped it
            Students.append(['Example', 'Student', '11', 'Math',"NA","Na", ['19', '18', '3', '0', '4']])
            # name,lastName,grade,subject,finalGrade,"NA",ai_stuff
            # I add in the example for two reasons, one it gives the user a template to go off of
            # and two certain functions won't work with an empty list
            edit_students(Students) # this saves the new empty model in a pickle file so it can be loaded upon program start up
        else:
            cls()
            print("Close call, press enter to be taken back to the main menu")
            input()

    if x == "7":
        cls()
        print("The model info is")
        file = open("model.log","r")
        info = file.readlines()
        print("completed on:",info[0])
        print("Time the modle trained:",info[1])
        print("The models accuracy is:",round(float(info[2])))
        print("It took:",(round(float(info[3]))),"seconds")
        input()
        # this does some conversions and displays information about the current Ai model

    if x == "8" :
            cls()
            targets = ""
            if len(Students) <= 1:
                cls()
                print("There is only the example student, and you can not predict the examples grade")
                print("press enter to be taken back to the main menu")
                input()
            print("The index number will be displayed in front of the student's data, type in that number and press enter  for the model to predict that students  grade")
            index_numbers = []
            for i in range(len(Students)):
                index_numbers.append(str(i))
                if i != 0: print("Index number:", i , "Student's data:",Students[i])  # this prints out all of the students data to the user
                # The i != 0 makes sure that the user won't try to select 0 as a possible answer
            x = input()
            if x != 0:
                if x in index_numbers:
                    #print("found it",x)
                    print("Student added")
                    targets = targets + str(x) + ","  # this adds "x" to a string that will later become a list of targets
                    file = open("d.temp", "w")  # it is important that we create a file as it server two purposes
                    # one, it tells the model what data to try and make a prediction from
                    # two, the program will check to see if it is deleted, and when it is this program will know when it's done
                    # Edit: I realised that there is no way it would take longer then 5 seconds so I decided against it
                    # I still wanted to leave the original comments in tho so you could see my thinking process
                    print("Press enter to have the model try and predict the students grade")
                    print("Note: Please don't touch your pc until it is all done (it should be around 7 seconds)")
                   # targets = targets + str(x) + ","
                    file.write(targets)
                    file.close()
                    os.startfile("startPredictor.vbs")  # This starts a .vbs file that will start the predictor program
                    time.sleep(5)# I probably should have some something  to check when the program is done, but there is no way it will
                    # take longer than 5 seconds so it should be fine
                    os.startfile("closeCodaTerminal.vbs")  # This closes the cConda terminal
                    Students = get_students()  # we have to pull in the new data from the other program
                    cls()
                    print("Success, you can now view the models prediction by pressing 1 on the main menu")
                    print("Highlights of data:\nActual mark:",Students[int(x)][4])
                    print("Predicted mark:",Students[int(x)][5])
                    print("press enter to continue")
                    input()

                else:
                    cls()
                    print("That was not a valid response, press enter to be taken back to the main screen")
                    input()

            else:
                cls()
                print("That was not a valid response, press enter to be taken back to the main screen")
                input()

    if x == "9":
        cls()
        print("The file will show you the final test of the test data against the AI (machine learning model)")
        print("The program will open a txt file in notepad, it will be up to you to close it once you are done reading it")
        print("Press enter to open the file")
        input()
        os.startfile("predictionsTest.txt")
        print("Press enter to be taken back to the main menu")

    if x == "10":
        cls()
        print("Are you sure that you want to delete the model and retrain it?\n( y or n )")
        x = input()
        if x == "y":
            cls()
            print("Select the amount of time you want the model to train and press enter")
            print("1) 10 times (not recommended)\n2) 100 times")
            print("3) 1000 times (recommended)\n4) 10000 times")
            x = input()
            n =1
            if x=="1": n="10"
            if x == "2": n = "100"
            if x == "3": n = "1000"
            if x == "4": n = "10000"
            #if x == "5": n = "100000"
            if n != 1:
                cls()
                print("The model may take a while to train or may be done in a few seconds, either way it will create")
                print("popup windows on your computer, please DO NOT TOUCH THEM")
                print("Press enter to start")
                input()
                trainModel(n) # this is actually wha call on the method tha retrains the model
                input()
            else:
                cls()
                print("You did not enter a valid response, press enter to be taken back to the main menu")
                input()
        else:
            cls()
            print("Close call, press enter to be taken back to the main menu")
            input()

    if x == "help":
        cls()
        print("Program Overview:")
        print("The Mark predictor was created by Jacob Albanese and uses a type of artificial intelligence known as machine learning")
        print("The program uses a linear regression algorithm to look at all aspects of the data")
        print("Then plots the data in multiple dimensions, then draws a line of best fit (look at the comments in the code for a better explanation")
        print("The model can then try to predict the results using the line of best fit")
        print("This AI takes in a data set of students information regarding their performance, and tries to predict their final mark\n")
        print("How to use it:")
        print("To start I would recommend that you watch the video that come with the program and also take a look at the code")
        print("The main menu displays 12 options 10 of which are operations this program can perform")
        print("The text before the number tells you what the operation does")
        print("Type in the number before the bracket and press enter to activate it, then follow the on-screen instructions")
        print("Please read the test on screen carefully because some instructions are very specific")
        print("You can predict a students grade from a list of students that the program wil save")
        print("If you select 5 and then \"a\" you will be able to add a student to the list")
        print("It is important to note that units are not required at all in this program ")
        print("There is also an example student that you can use as a reference when filling in data\n")
        print("Getting Started:")
        print("Now that the program has fished setting it\'s self you may need to enter some student data")
        print("Once you have done that you can then select 8 from the main menu to try and predict students marks")
        print("Please note: all student grades are out of 20")
        print("\nPress enter to continue")
        input()

# data order first name, last name, grade, subject, [G1", "G2", "studytime", "failures", "absences"]
# new data order: first name, last name, grade, class name, final grade (if you know it), Ai predicted grade (if you ran that part of the program yet), first grade, second, grade, studytime, failures, then absences"


# files that this program depends upon
#  studentData.csv
#  startTrainer.vbs"
#  start_conda_environment.bat
# python modelTrainer.py
# closeCodaTerminal.vbs
# Students.pickle
# gradeModelPredictor.py
# startPredictor.vbs
# setup.py
# start.vbs
# startup.txt
# requirements.txt
# createCondaEnvironment.bat
# finishSetUp.bat
#  MarkPredictor.py
