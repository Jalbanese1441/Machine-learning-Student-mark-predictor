import os
import time
cls = lambda: os.system("cls")
class Setup_Program(object):
    pass
    @staticmethod # This method does not change nor does it work with objects of the class
    #def test():
       # print("it worked!")
    def setup_Program():
        print("The program will open a text file with installation instructions, make sure you follow them")
        os.startfile("startup.txt")
        print("Type exit to close this program")
        while True:
            x = input()
            if x=="done":break
            if x == "exit":exit(0)
            cls()
        print("Pop-up windows will be created, just ignore them \nPlease don't touch your computer")
        print("This may take several minutes")
        print("The program will tell you when it is done, please don't use your computer until then")
        time.sleep(8)
        os.startfile("start.vbs") # this will open the .vbs file that will open another file and begin setting the program up
        counter = 0
        while os.path.exists("done.setup")==False: # this keeps the program in a loop until everything is hopefully done installing
            print("Please wait the program is setting up")
            if counter == 0: print("Loading: [-]")
            elif counter == 1: print("Loading: [\]")
            elif counter == 2: print("Loading: [-]")
            else: print("Loading: [/]")
            #print(counter)
            time.sleep(1)
            counter += 1
            if counter == 4: counter = 0
            cls()
            # this plays a loading animation until the program has finished setting up
        n="10"
        file = open("n.runs", "w")
        file.write(n)
        file.close()
        os.startfile("startTrainer.vbs")
        time.sleep(15)
        os.startfile("closeCodaTerminal.vbs")
        # this bit will quick;ly train the model but the user has the option to retrain the model for a
        # better accuracy
        cls()
        print("Done!\nPress enter to continue")
        input()

if os.path.exists("done.setup")==False: Setup_Program.setup_Program()

# When the main program runs it will automatically run this code so it will check to see if the setup is complete every time

# Yes, I know this is not the most practical use of classes, but it is a demonstration of my knowledge 
