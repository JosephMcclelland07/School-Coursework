import random
import csv
import datetime

def helpmenu():
    print("This is My Help Menu, Where i have Q/A's for lots of commonly asked quesitons")#Print message

    print("Option 1- How Do i find out my Member ID")#All options
    print("Option 2- How do Ski Groups work?")#All options
    print("Option 3- How to view reports ")#All options
    print("Option 4- How are ski times calcutated?")#All options
    print("Option 5- How to answer the Ski quiz")#All options
    print("Option 6-exit")

#keeping choice as a string,not an int so it wont produce a syntax error when entered
    choice=input("Please choose an option: ")

    if choice=="1":
        print("You Have Selcted choice 1. \nYou can find out your member ID in the pupildeatilscsv file")#Lets user know what is selected
        helpmenu()
    
    elif choice=="2":
        print("You Have Selcted choice 2. \nGroups are banded bases of your ski times Being Advanced <60, Intermideite 60-89 and Beginner=>90 ")#Lets user know what is selected
        helpmenu()
    
    elif choice=="3":
        print("You Have Selcted choice 3. \n To type Reports you must enter the name of the report you wish to see e.g. Medical Report inside of option 5, Reports")#Lets user know what is selected
        helpmenu()

    elif choice=="4":
        print("You Have Selcted choice 4. \n Ski times are calcuted by entering your 5 ski scores then /5 which gives you an average.  ")#Lets user know what is selected
        helpmenu()

    elif choice=="5":
        print("You Have Selcted choice 5.  \n You answer the ski quiz by picking any of A,B,C,D anything else will be invalid, You can access this by selecting ski quiz in the menu")#Lets user know what is selected
        helpmenu()

    elif choice=="6":
        close=input("You have choosen to leave the help menu. Is this what you want to do? Y/N")#Lets user know what is selected, This one closes the Programm.
        close=close.upper()

        if close=="Y":
            menu()
        else:
            helpmenu()

    else:
        print("You have entered invalid detalis")# Invalid deteles detected by error.
        helpmenu()



def report():
    


    #chooses the report that the user wants to Produce
    reportLevel=input("Please enter the level you want to produce a report for: ")
    reportLevel=reportLevel.upper()

    if reportLevel=="":
        print("You need to enter a valid report title")
        report()

    elif reportLevel=="BEGINNER":#Report level
        beginnerfile=open("beginnerreport.txt","w")#assigns the file to a variable for use throghout the programm, write function use as function use as time the report is created we want to overwrite the original
        beginnerfile.write("Clarendon High School Ski Trip 2022\n")
        beginnerfile.write("\n")#New line
        beginnerfile.write("Report Title: Beginner Group\n")
        todays_date=datetime.date.today()# Adds todays date
        beginnerfile.write("Report Created: " +str(todays_date)+"\n")#Shows Date/time on report

        with open ("SkiTimes.csv","r") as csvfile:#must open the Ski times file as that has the Level Variable
            csvreader= csv.reader(csvfile)
            for row in csvreader:
                if row [8]== "Beginner":
                   name=row[0]#Finds from Csv
                   surname=row[1]#Finds from Csv
                   average=row[6]#Finds from Csv
                   print("\nName: " + name +"\nSurname: " + surname +"\nAverage: " + average +"\n")
                   beginnerfile.write("Name: " + name +"\n")#writes from Csv
                   beginnerfile.write("Surname: " + surname +"\n")#writes from Csv
                   beginnerfile.write("Average: " + average +"\n")#writes from Csv

        csvfile.close()
        beginnerfile.close()



    elif reportLevel=="INTERMIDEITE":#Report level
        intermideitefile=open("Intermideitereport.txt","w")#assigns the file to a variable for use throghout the programm, write function use as function use as time the report is created we want to overwrite the original
        intermideitefile.write("Clarendon High School Ski Trip 2022\n")
        intermideitefile.write("\n")#New line
        intermideitefile.write("Report Title: Intermideite Group\n")
        todays_date=datetime.date.today()# Adds todays date
        intermideitefile.write("Report Created: " +str(todays_date)+"\n")#Shows Date/time on report

        with open ("SkiTimes.csv","r") as csvfile:#must open the Ski times file as that has the Level Variable
            csvreader= csv.reader(csvfile)
            for row in csvreader:
                if row [8]== "Intermideite":
                   name=row[0]#Finds from Csv
                   surname=row[1]#Finds from Csv
                   average=row[6]#Finds from Csv
                   print("\nName: " + name +"\nSurname: " + surname +"\nAverage: " + average +"\n")
                   intermideitefile.write("Name: " + name +"\n")#writes from Csv
                   intermideitefile.write("Surname: " + surname +"\n")#writes from Csv
                   intermideitefile.write("Average: " + average +"\n")#writes from Csv
               
        csvfile.close()
        intermideitefile.close()




    elif reportLevel=="ADVANCED":#Report level
        Advancedfile=open("Advancereport.txt","w")#assigns the file to a variable for use throghout the programm, write function use as function use as time the report is created we want to overwrite the original
        Advancedfile.write("Clarendon High School Ski Trip 2022\n")
        Advancedfile.write("\n")#New line
        Advancedfile.write("Report Title: Advanced Group\n")
        todays_date=datetime.date.today()# Adds todays date
        Advancedfile.write("Report Created: " +str(todays_date)+"\n")#Shows Date/time on report

        with open ("SkiTimes.csv","r") as csvfile:#must open the Ski times file as that has the Level Variable
            csvreader= csv.reader(csvfile)
            for row in csvreader:
                if row [8]== "Advanced":
                   name=row[0]#Finds from Csv
                   surname=row[1]#Finds from Csv
                   average=row[6]#Finds from Csv
                   print("\nName: " + name +"\nSurname: " + surname +"\nAverage: " + average +"\n")
                   Advancedfile.write("Name: " + name +"\n")#writes from Csv
                   Advancedfile.write("Surname: " + surname +"\n")#writes from Csv
                   Advancedfile.write("Average: " + average +"\n")#writes from Csv
        csvfile.close()
        Advancedfile.close()



    elif reportLevel=="MEDICALHISTORY":#Report level
        Medicalfile=open("Medical History.txt","w")#assigns the file to a variable for use throghout the programm, write function use as function use as time the report is created we want to overwrite the original
        Medicalfile.write("Clarendon High School Ski Trip 2022\n")
        Medicalfile.write("\n")#New line
        Medicalfile.write("Report Title: Medical History\n")
        todays_date=datetime.date.today()# Adds todays date
        Medicalfile.write("Report Created: " +str(todays_date)+"\n")#Shows Date/time on report

        with open ("pupildetails.csv","r") as csvfile:#must open the Ski times file as that has the Level Variable
            csvreader= csv.reader(csvfile)
            for row in csvreader:
                if row [8]!="None":
                   name=row[1]
                   surname=row[2]#Finds from Csv
                   medicalcondition=row[8]
                   print("\nName: " + name + "\nSurname: " + surname + "\nMedicalcondition" + medicalcondition +"\n")
                   Medicalfile.write("Name: " + name +"\n")#writes from Csv
                   Medicalfile.write("Surname: " + surname +"\n")#writes from Csv
                   Medicalfile.write("Medicalcondition: " + medicalcondition +"\n")

        csvfile.close()
        Medicalfile.close()



    elif reportLevel=="LOWER SCORES":#Report level
        Scorelowerfile=open("Ski Lower Scores.txt","w")#assigns the file to a variable for use throghout the programm, write function use as function use as time the report is created we want to overwrite the original
        Scorelowerfile.write("Clarendon High School Ski Trip 2022\n")
        Scorelowerfile.write("\n")#New line
        Scorelowerfile.write("Report Title: Ski Scores\n")
        todays_date=datetime.date.today()# Adds todays date
        Scorelowerfile.write("Report Created: " +str(todays_date)+"\n")#Shows Date/time on report

        with open ("SkiQuiz.csv","r") as csvfile:#must open the Ski times file as that has the Level Variable
            csvreader= csv.reader(csvfile)
            for row in csvreader:
                if row [2] =="0"  or row[2]=="1"  or row[2]=="2"  or row[2]=="3"  or row[2]=="4":
                   name=row[0] 
                   score=row[2]#Finds from Csv
                   print("\nName: " + name + "\nScore: " + score + "\n")
                   Scorelowerfile.write("Name: " + name +"\n")#writes from Csv
                   Scorelowerfile.write("Score: " + score +"\n")#writes from Csv
                   

        csvfile.close()
        Scorelowerfile.close()


    elif reportLevel=="HIGHER SCORES":#Report level
        Scorehigherfile=open("Ski Higher Scores.txt","w")#assigns the file to a variable for use throghout the programm, write function use as function use as time the report is created we want to overwrite the original
        Scorehigherfile.write("Clarendon High School Ski Trip 2022\n")
        Scorehigherfile.write("\n")#New line
        Scorehigherfile.write("Report Title: Ski Scores\n")
        todays_date=datetime.date.today()# Adds todays date
        Scorehigherfile.write("Report Created: " +str(todays_date)+"\n")#Shows Date/time on report

        with open ("SkiQuiz.csv","r") as csvfile:#must open the Ski times file as that has the Level Variable
            csvreader= csv.reader(csvfile)
            for row in csvreader:
                if row [2] =="5"  or row[2]=="6"  or row[2]=="7"  or row[2]=="8":
                   name=row[0] 
                   score=row[2]#Finds from Csv
                   print("\nName: " + name + "\nScore: " + score + "\n")
                   Scorehigherfile.write("Name: " + name +"\n")#writes from Csv
                   Scorehigherfile.write("Score: " + score +"\n")#writes from Csv
                   

        csvfile.close()
        Scorehigherfile.close()
                   
                   
    else:
        print("You need to enter a valid report title")
        report()
               



def skitimes():

    name = input("Please Enter your Forename")# Personalised ID so Mr Walsh can see all the names on the csv file
    surname = input("Please Enter your Surname")
    if name == "":
        print("Please Enter a valid name")# Just name verification
        skitimes()
    print(" Please enter all your times in Seconds, Like this Example")
    print("=====================================")
    print("                88                   ")# Gives the user an example of how to enter 
    print("=====================================")


    while True:
        try:
            t1 = int(input("Please enter your First slope time?")) #Entering Slope times
            break
        except:
            print("you must enter a whole number")

    while True:
        try:
            t2 = int(input("Please enter your Second slope time?"))
            break
        except:
            print("you must enter a whole number")

    while True:
        try:        
            t3 = int(input("Please enter your Third slope time?"))
            break
        except:
            print("you must enter a whole number")

    while True:
        try:
            t4 = int(input("Please enter your Fourth slope time?"))
            break
        except:
            print("you must enter a whole number")

    while True:
        try:
            t5 = int(input("Please enter your Fifth slope time?"))
            break
        except:
            print("you must enter a whole number")


            
    av = (t1 + t2 + t3 + t4 + t5)/5
    round (av, 2)
    if av <= 60:
        group = "Advanced" #If statements for group banding 

    elif av <= 90:
        group = "Intermideite"

    elif av >= 91:
        group = "Beginner"


    print(name , "Your Average ski slope is", av, "You are in the following ski Group=", group) #Shows user Their time and Group that they have been put into



    def memberid():
        memberId=input("Enter the users Member Id: ")
        if memberId=="":
            print("***Error***\nYou Have Entered a invalid member ID, Please input correctly: ")
            memberId=input("Enter the users Member Id: ")
        else:
            found=0
            with open ("pupildetails.csv", "r") as csvfile:
                csvreader= csv.reader(csvfile)
                for row in csvreader:
                    if row[11]== memberId:
                        found=1
                        name=row[2]
                        surname=row[3]
                if found==0:
                    print("Member ID is not valid")
                    memberid()
                else:
                    print("You are adding information",name,surname)

            csvfile.close() 
                
        memberid()

    with open("SkiTimes.csv","a") as csvfile:
       writer=csv.writer(csvfile, lineterminator="\n")  #Line Terminator stops the csv file from making spaces and gaps in the csv file
       writer.writerow([name,surname,t1,t2,t3,t4,t5,av,group]) #Prints all details onto the cvs file, e.g. It will display the fullname, all 5 times, Average time, Skiing Group
       csvfile.close()
    print("Thank you for entering your details.")




def healthandSafteyquiz():
    score=0 #All users will start with a Score of 0, If they score correct they will get a +1 which will be presented to them at the end of the test
    def memberid():
        memberId=input("Enter the users Member Id: ")
        if memberId=="":
            print("***Error***\nYou Have Entered a invalid member ID, Please input correctly: ")
            memberId=input("Enter the users Member Id: ")
        else:
            found=0
            with open ("SkiQuiz.csv", "r") as csvfile:
                csvreader= csv.reader(csvfile)
                for row in csvreader:
                    if row[1]== memberId:
                        found=1
                        name=row[0]
                if found==0:
                    print("Member ID is not valid")
                    memberid()
                else:
                    print("You are adding information",name)

            csvfile.close() 
                
        memberid()
    print("Welcome to My skiing health and saftey quiz, there will be 8 Questions")
    q1=input("What is the correct footwear to use whilst skiing?\nA. Trainers\nB. Running Shoes\nC. Special Boots\nD. Hiking Boots\n") #E.g. \nD. this starts a new line very single time 
    q1=q1.upper()#Allows Lower and Upper Case Letters to be used e.g. c and C
    if q1=="C":
        score= score +1
        print("This is correct, good job!")

    elif q1=="D":
        print("This is a Valid answer But unfortunatley incorrect") #Lets the user know if they have scored Incorrect

    elif q1=="A":
        print("This is a Valid answer But unfortunatley incorrect")

    elif q1=="B":
        print("This is a Valid answer But unfortunatley incorrect")

    else:
         print("You Have entered a invalid answer. Automatic 0") # My code does not allow a repeat of the question regardless if you type a invalid answer, Error Trapping
        

    q2=input("What do you do whilst skiing?\nA. Slow down massively\nB. Weave side to side\nC. Wear lighter clothes\nD. Stop at the side of the slope and visible \n")#E.g. \nD. this starts a new line very single time 
    q2=q2.upper()#Allows Lower and Upper Case Letters to be used e.g. c and C
    if q2=="D":
        score= score +1
        print("This is correct, good job!")

    elif q2=="C":
        print("This is a Valid answer But unfortunatley incorrect")#Lets the user know if they have scored Incorrect

    elif q2=="A":
        print("This is a Valid answer But unfortunatley incorrect")

    elif q2=="B":
        print("This is a Valid answer But unfortunatley incorrect")

    else:
         print("You Have entered a invalid answer. Automatic 0") # My code does not allow a repeat of the question regardless if you type a invalid answer, Error Trapping
        

    q3=input("What shouldnt you wear whilst skiing?\nA. Shorts\nB. Hoddie\nC. Goggles\nD. Hat \n")#E.g. \nD. this starts a new line very single time 
    q3=q3.upper()#Allows Lower and Upper Case Letters to be used e.g. c and C
    if q3=="A":
        score= score +1
        print("This is correct, good job!")

    elif q3=="D":
        print("This is a Valid answer But unfortunatley incorrect")#Lets the user know if they have scored Incorrect

    elif q3=="C":
        print("This is a Valid answer But unfortunatley incorrect")

    elif q3=="B":
        print("This is a Valid answer But unfortunatley incorrect")

    else:
        print("You Have entered a invalid answer. Automatic 0") # My code does not allow a repeat of the question regardless if you type a invalid answer, Error Trapping
        

    q4=input("Which 3 things are most important when skiing?\nA. Attire, Look, Skills\nB.Adapability to new slopes, Balance, Control of the Skies\nC. What slope you are doing, Your time, You Ability\n")#E.g. \nD. this starts a new line very single time 
    q4=q4.upper()#Allows Lower and Upper Case Letters to be used e.g. c and C
    if q4=="B":
        score= score +1
        print("This is correct, good job!")

    elif q4=="D":
        print("This is a Valid answer But unfortunatley incorrect")#Lets the user know if they have scored Incorrect

    elif q4=="A":
        print("This is a Valid answer But unfortunatley incorrect")

    elif q4=="C":
        print("This is a Valid answer But unfortunatley incorrect")

    else:
        print("You Have entered a invalid answer. Automatic 0") # My code does not allow a repeat of the question regardless if you type a invalid answer, Error Trapping
        

    q5=input("What do you use to get to the top os a hill?\nA. Lift \nB. Walk\nC. Car\nD. Mobility Scooter\n")#E.g. \nD. this starts a new line very single time 
    q5=q5.upper()#Allows Lower and Upper Case Letters to be used e.g. c and C
    if q5=="A":
        score= score +1
        print("This is correct, good job!")

    elif q5=="C":
        print("This is a Valid answer But unfortunatley incorrect")#Lets the user know if they have scored Incorrect

    elif q5=="A":
        print("This is a Valid answer But unfortunatley incorrect")

    elif q5=="B":
        print("This is a Valid answer But unfortunatley incorrect")

    else:
        print("You Have entered a invalid answer. Automatic 0")# My code does not allow a repeat of the question regardless if you type a invalid answer, Error Trapping
        

    q6=input("What is the safest thing to do at the bottom of the hill\nA. stay where you stop \nB.Move to the side\nC. climb back up\nD. Stay on the slope\n")#E.g. \nD. this starts a new line very single time 
    q6=q6.upper()#Allows Lower and Upper Case Letters to be used e.g. c and C
    if q6=="B":
        score= score +1
        print("This is correct, good job!")

    elif q6=="D":
        print("This is a Valid answer But unfortunatley incorrect")#Lets the user know if they have scored Incorrect

    elif q6=="A":
        print("This is a Valid answer But unfortunatley incorrect")

    elif q6=="C":
        print("This is a Valid answer But unfortunatley incorrect")

    else:
        print("You Have entered a invalid answer. Automatic 0")# My code does not allow a repeat of the question regardless if you type a invalid answer, Error Trapping
        

    q7=input("Biggest Ski Resort In the world?\nA. Belfast \nB. Alps, Italy\nC. Car\n")#E.g. \nD. this starts a new line very single time 
    q7=q7.upper()#Allows Lower and Upper Case Letters to be used e.g. c and C
    if q7=="B":
        score= score +1
        print("This is correct, good job!")

    elif q7=="D":
        print("This is a Valid answer But unfortunatley incorrect")#Lets the user know if they have scored Incorrect

    elif q7=="A":
        print("This is a Valid answer But unfortunatley incorrect")

    elif q7=="C":
        print("This is a Valid answer But unfortunatley incorrect")

    else:
        print("You Have entered a invalid answer. Automatic 0")# My code does not allow a repeat of the question regardless if you type a invalid answer, Error Trapping
        

    q8=input("What would you do if you saw an accidnet on a Slope?\nA. Laugh \nB. Walk away\nC. Film it and post on Social Media\nD. Assist\n")#E.g. \nD. this starts a new line very single time 
    q8=q8.upper()#Allows Lower and Upper Case Letters to be used e.g. c and C
    if q8=="D":
        score= score +1
        print("This is correct, good job!")

    elif q8=="C":
        print("This is a Valid answer But unfortunatley incorrect")#Lets the user know if they have scored Incorrect

    elif q8=="A":
        print("This is a Valid answer But unfortunatley incorrect")

    elif q8=="B":
        print("This is a Valid answer But unfortunatley incorrect")

    else:
        print("You Have entered a invalid answer. Automatic 0")# My code does not allow a repeat of the question regardless if you type a invalid answer, Error Trapping

    print("Score is",score)# Shows User score

    with open("SkiQuiz.csv","a") as csvfile:
       writer=csv.writer(csvfile, lineterminator="\n")
       writer.writerow([memberid,score])#Writes User ID and score to csv
       csvfile.close()
    
    postcode= input("Postcode: ")
    memberid= random.randint(0,1000000) #Gives them a random number for the ID between a fixed range
#error trapping



def details():
    print("Please enter all of the details below")#All details asked to be inputted

    title= input("Title: ")
    fname= input ("First Name:" )
    surname= input("Suranme: ")
    gender= input("Gender: (M/F/O): ")
    address= input("Address: ")
    medicalhistory= input("Medical History/Information: ")
    skiingexperince= input("Sking Experince: ")
    town= input("Town: ")
    postcode= input("Postcode: ")
    memberid= random.randint(0,1000000) #Gives them a random number for the ID between a fixed range
#error trapping
    while True:
        try:
            age= int(input("Age: "))
            break
        except:
           print("You must enter a number")
    while True:
        phonenumber=input("Phone Number: ")
        #length checking the phonenumber
        if len(phonenumber) !=11:
            phonenumber=input("Please enter a valid phone number")
        else:
            break

#presence check using selection and boolean operators. Ensures all data is entered for later use.
    if title=="" or fname=="" or surname=="" or gender=="" or address=="" or medicalhistory=="" or skiingexperince=="" or town=="" or postcode=="" or phonenumber=="":
        print("You have not completed all of the details")
        details()
    else:
        print("Please Double Check your details:")
        print("Titles: ", title, "\nName: ", fname, "\nSurname:  ", "\nGender: ", address, "\nMecdicalhistory; ", medicalhistory, "n\skiingexperince: ", skiingexperince, "\nTown: ", town, "\nPostcode: ", postcode, "\nAge: ", age, "\nPhonenumber: ", phonenumber)
        correct=input("Are these details correct(Y/N)")
        correct=correct.lower()
    if correct=="y":
        with open("pupildetails.csv","a") as csvfile:
            writer=csv.writer(csvfile, lineterminator="\n")
            writer.writerow([title,fname,surname,gender, address, town, postcode, age, medicalhistory, skiingexperince, phonenumber, memberid])
            csvfile.close()
        print("Thank you for entering your details.  Your Member id is: \n" , memberid)
        menu()
    else:
        details()



#procedure= will only run when valid
def menu():
    print("Welcome to my program")

    print("Option 1- Pupil Details")
    print("Option 2- Ski Quiz")
    print("Option 3- Ski Times")
    print("Option 4- Help Menu/ Messages")
    print("Option 5- Report")
    print("Option 6-exit")

#keeping choice as a string,not an int so it wont produce a syntax error when entered
    choice=input("Please choose an option: ")

    if choice=="1":
        print("Pupil Details is now selected")#Lets user know what is selected
        details()
        menu()
    
    elif choice=="2":
        print("Ski Quiz is now selected")#Lets user know what is selected
        healthandSafteyquiz()
        menu()
    
    elif choice=="3":
        print("Ski Times is now selected")#Lets user know what is selected
        skitimes()
        menu()

    elif choice=="4":
        print("Help Menu/ Messages is now selected")#Lets user know what is selected
        helpmenu()
        menu()
       

    elif choice=="5":
        print("Report is now selected")#Lets user know what is selected
        report()
        menu()

    elif choice=="6":
        close=input("You have choosen to leave the program. Is this what you want to do? Y/N")#Lets user know what is selected, This one closes the Programm.
        close=close.upper()

        if close=="Y":
            exit()
        else:
            menu()

    else:
        print("You have entered invalid detalis")
        menu()

          
#loop counter
i=0
while i< 3:
    username=input("USERNAME: ")
    password=input("PASSOWRD: ") 
#selectio is a booleam operator 
    if username=="Jmcclelland"  and password== "summer2022":
        print("Login Successful!")
        i=4
        menu()

    elif username=="CBobbert"  and password== "spring2022":#You can have multiple Users on your System using elif
        print("Login Successful!")
        i=4
        menu()

    elif username=="BillyBob"  and password== "Billbob":
        print("Login Successful!")
        i=4 #i=4 sends a valid linfromation to the code to allow them  to move on to the menu eg >4 allows you in
        menu()

    elif username=="User1"  and password== "Pass1:
        print("Login Successful!")
        i=4 #i=4 sends a valid linfromation to the code to allow them  to move on to the menu eg >4 allows you in
        menu()
        


    else:
        print("Login Unsuccessful")
        i=i+1 #increment the value of i by one each time

if i==3:
    print("Too Many Failed Attempts, System will shut down")#bascilly locks you out of the code
    exit()#Stops the program from continuing


