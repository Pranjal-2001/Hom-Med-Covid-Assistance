class bedsavail: #to show the number of beds available
    def oxygen(self):
        print("For Oxygen beds: ")
        print("1. Ashoka Hospital \n Beds Available = 10 \n Contact : 1234567890 ")
        print("2. Apollo Hospital \n Beds Available = 20 \n Contact : 2345678901 ")
        print("3. Wokard Hospital \n Beds Available = 15 \n Contact : 4578901234 ")
        print("4. Lotus Hospital  \n Beds Available = 12 \n  Contact : 7890123456 ")
        print("5. Six Sigma hospital \n Beds Available = 25 \n Contact : 5678901234 ")
    def nonoxy(self):
        print("For Non-Oxygen beds: ")
        print("1. Ashoka Hospital \n Beds Available = 50 \n Contact : 1234567890 ")
        print("2. Apollo Hospital \n Beds Available = 40 \n Contact : 2345678901 ")
        print("3. Wokard Hospital \n Beds Available = 35 \n Contact : 4578901234 ")
        print("4. Lotus Hospital  \n Beds Available = 42 \n  Contact : 7890123456 ")
        print("5. Six Sigma hospital \n Beds Available = 50 \n Contact : 5678901234 ")

class query(): 
    list1=["0"]        #To put query , display query and answer query
    def enterquery(self):
        list1=["0"]
        query=input("Enter your query : ")
        list1.append(query)
        print(list1)
    def answerquery(self):
        list2=["0"]
        number=int(input("Which query you want to answer ? (enter index number)"))
        solution=input("Enter your solution. ")
        list2.append(solution)
        print(list2)
class vaccination:
    def vacc(self):
        print("Do you want to take 1. covishield or 2. covaxin [enter 1 or 2]")
        num_1=int(input())
        if num_1==1:
            print("Avialable slots for Covishield are: ")
            rows, cols = (7, 8)
            arr = [[0 for i in range(cols)] for j in range(rows)]
            arr[0][0]="day 1"
            arr[1][0]="day 2"
            arr[2][0]="day 3"
            arr[3][0]="day 4"
            arr[4][0]="day 5"
            arr[5][0]="day 6"
            arr[6][0]="day 7"
            for rows in arr:
                print(rows)
            
            day=int(input("Enter the day on which you wish to get vaccinated (1 to 7): \n"))
            slot=int(input("Enter the slot number (1-7) \n"))
            arr[day][slot]="B"
            for rows in arr:
                print(rows)
        elif num_1==2:
            print("Available slots for Covaxin are: ")
            rowss, colss = (7, 8)
            arrr = [[0 for k in range(colss)] for l in range(rowss)]
            arrr[0][0]="day 1"
            arrr[1][0]="day 2"
            arrr[2][0]="day 3"
            arrr[3][0]="day 4"
            arrr[4][0]="day 5"
            arrr[5][0]="day 6"
            arrr[6][0]="day 7"
            for rowss in arrr:
                print(rowss)
            
            day1=int(input("Enter the day on which you wish to get vaccinated (1 to 7): \n"))
            slot1=int(input("Enter the slot number (1-7) \n"))
            arrr[day1][slot1]="B"
            for rowss in arrr:
                print(rowss)
        else:
            print("Choose correct option. \n")
obj=vaccination()        
o1=bedsavail()
o2=query()
print("Welcome ! ")
print(" Enter the index number of the option you'd like to continue with: \n 1.To see availability of beds(oxygen)  \n 2.To see availability of beds( nonoxygen) \n 3. To book slot for vaccnation\n 4. To ask query  \n 5.To answer query ")
n=int(input())
dict={
    1 : o1.oxygen(),
    2 : o1.nonoxy(),
    3 : obj.vacc(),
    4 : o2.enterquery(),
    5 : o2.answerquery()
       
}
print("Thankyou ,  Be safe!")