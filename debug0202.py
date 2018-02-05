 #1. Create an script that uses a two-dimensional
#  tuple to hold the following data: (this is
#   the same data as the last lab)

tHeader = ("Id","Name","Email")
tRow1 = (1,"Bob Smith","BSmith@Hotmail.com")
tRow2 = (2,"Sue Jones","SueJ@Yahoo.com")
tRow3 = (3,"Joe James","JoeJames@Gmail.com")

tTable = (tRow1, tRow2, tRow3)

# 2. Add code that searches for customers by name
#    and returns a customer Id. You code should
#    look similar to this:


boolVal = False
boolNew=True

while (boolNew):

    srchCusName = str(input("Enter the Customer name you are searching for: ").title())

    for row in tTable:
        if(srchCusName in row):
            print(srchCusName + " is Customer ID: " + str(row[0]))
            boolVal = True
            if(boolVal == True):
                boolNew = False
                break



    if boolVal == False:
        print("Customer does not exist!")

    if(boolNew == False ):break
    else:
        continueSrch = str(input("Do you want to continue? (Y/N): ").upper())

        if(continueSrch == 'Y'):
            continue
        else:
            break
