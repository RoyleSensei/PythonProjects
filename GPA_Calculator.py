#########GPA Calculator

def GPACalc():

#****Thought flow & Algorithm******
    '''
    - Thought flow:
        step 1: User inputs:
            - get student name, total number of subjects taken, and the total credit hours 
        step 2: Set up the calculations:
            Set up the for loop [for x in range(semClass)]
            - Need the nam of the subject {input()}
            - Need the number of credit hours of each subject {input()}
            - Need to get the numeric grade for the subject {input()}
        step 3: Conversions
            - If statement -> convert numeric grade to letter grade
            - If statemnet -> convert letter grade to letter grade points
        step 4: Finalize the calculation
            - Sum up the total credits of the semester [based on how many subjects taken (semClass)] --> semCreds
            - Sum up the total points of the semester gained --> semPoints
            GPA = sum(letter grade points * credit hours)/sum(credit_hour) = semPoints/semCreds
        step 5: Create the summary report & format everything 

    - A complete algorithm
        Problem: Desgn an algorithm to calculate the GPA of a student in a semester
        step 1 - START
        step 2 - Get values of student_name, semClass, & semCreds
        step 3 - Input values to subject_name, SubCreds, and Numeric_Grade
        step 4 - Begin loop & set semClass as the range
        step 5 - Convert Numeric_Grade to Letter Grade based on GPS Scale
        step 5 - Convert Letter Grade to Letter Points based on the GPA Scale
        step 6 - End loop
        step 7 - Sum up the letter points and divided by the semCreds to get GPA
        step 8 - Create summary display
        step 9 - STOP
    '''

#********* USER INPUTS ************ 
    student_name = input("Please enter student name: ") #get input for student name 
    semClass = int(input("How many subjects are you taking this semester? ")) #get the number of subjects taken in this semester
    semCreds = float(input("Total credit hours is: ")) #get the total credits of those subjects 
    print('\n') #start a new line before going to the processing part

#********* PROCESSING *************
    semPoints = 0 #start the initial point of semPoints

    for x in range(semClass):
        a = x+1 #set up the calculation for the subject number 
        subject_name = str(input("Name of the subject"+ str(a) + " " + "is: ")) #get the name of the subject 
        b = SubCreds = float(input("Number of credit hours for " + str(subject_name) + " " + "is: ")) #get the credit hours of a subject
        c = Numeric_Grade = int(input("Please enter numeric grade for " + str(subject_name) + ": ")) #get numeric grade of a subject
        
        #convert numeric grade to letter grade - use if statement [based on the GPA scale]
        if c >= 95:
            d = "A"
        elif c >= 90:
            d = "A-"
        elif c >= 87:
            d = "B+"
        elif c >= 83:
            d = "B"
        elif c >= 80:
            d = "B-"
        elif c >=77:
            d = "C+"
        elif c >= 73:
            d = "C"
        elif c >= 70:
            d = "C-"
        else:
            d = "F"

        print(str("The Letter grade is ")+ d) #show the letter grade of this subject

        #convert letter grade to letter grade point - use if statement [based on the GPA scale]
        if d == "A":
            e = 4.0
        elif d == "A-":
            e = 3.7
        elif d == "B+":
            e = 3.3
        elif d == "B":
            e = 3.0
        elif d == "B-":
            e = 2.7
        elif d == "C+":
            e = 2.3
        elif d == "C":
            e = 2.0
        elif d == "C-":
            e = 1.7
        else:
            e = 0.0

        print(str("The Letter Grade Point is ")+str(e)) #print out the letter grade points
        subPoints = b * e #points of each subject
        semPoints += subPoints #cumulative points
        print('\n') #add one line before the final result

    print("The Cumulative Letter Grade Points is: " + str(semPoints.__round__(3))) #print out the cumulative letter grade points


#calculate GPA
    GPA = semPoints / semCreds #the formula of GPA
    print("The GPA is: " + str(GPA.__round__(3))) #show the GPA
    print('\n') #start a new line before the final display

#display everything 
    name = student_name #the name of the student
    print("Summary Display: ") #display title
    print("{:40} {:2} {:}".format(name,"GPA:",GPA.__round__(3))) #format the first line of the report as name & GPA
    print("---------------------------------------------------") #add a division between the the header part and the content part
    print("{:15} {:20} {:}".format("Subject", "Numeric Grade", "Letter Grade")) #create and format the column name
    print("{:15} {:20} {:}".format("English", "95", "A")) #format the first subject
    print("{:15} {:20} {:}".format("Math", "90", "A-")) #format the second subject
    print("{:15} {:20} {:}".format("Science", "98", "A")) #format the third subject

GPACalc()