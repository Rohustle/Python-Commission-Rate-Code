#Author: Rohan Stephenson
#Date Created: 1/5/2022
#Course: ITT103
#Purpose: The purpose is to calculate the commission received by each sales person in three different classes. The program will also print the commission rate for each class. 

sales = int(input("please enter the sales amount: "))
Class = int(input("please enter salesperson class: "))

if Class == 1:
    if sales <= 1000:
        rate = 0.06
        commission_rate = rate*sales
        print('commission rate is:', commission_rate)
    elif sales > 1000 < 2000:
        rate = 0.07
        commission_rate = rate*sales
        print('commission rate is:', commission_rate)
    elif sales >= 2000:
        rate = 0.10
        commission_rate = rate*sales
        print('commission rate is:', commission_rate)

if Class == 2:
    if sales < 1000:
        rate = 0.04
        commission_rate = rate*sales
        print('commission rate is:', commission_rate)
    elif sales >= 1000:
        rate = 0.06
        commission_rate = rate*sales
        print('commission rate is:', commission_rate)
        
if Class == 3:
    rate = 4.5
    commission_rate = rate*sales
    print('commission rate is:', commission_rate)
        
else:
    if Class > 3:
        print("sorry, input error, please try again")
