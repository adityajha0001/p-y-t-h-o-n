
Bigdata ={}


#how many tickets you want to buy
n = input("enter the number of ticket you want :")

for i in range(int(n)):
    user = {}
    name = input("Enter your name :")
    age  = input("Enter your age :")
    day  = input("Enter your day :")
    user["Day"] = day
    user["Age"] = int(age)
    Bigdata[name] = user
    
totalPay = int(0)
# print(Bigdata)
for key,value in Bigdata.items():
    life = Bigdata[key]["Age"]
    print(life)  
    MovieDay = Bigdata[key]["Day"]
    print(MovieDay)
    
    if(life< 18):
        ticketPrice = int(8)
        print(f"you have to pay ${ticketPrice} only")
        if(MovieDay == "wednesday"):
            discount = int(2)
            ticketPrice = ticketPrice - discount
            print(f"Because you are booking ticket for wednesday show now you have to pay ${ticketPrice} only")
            totalPay += ticketPrice
    elif(life>=18):
        ticketPrice = int(12)
        print("you have to pay ${} only".format(ticketPrice))
        if(MovieDay == "wednesday"):
            discount = int(2)
            ticketPrice = ticketPrice - discount
            print("Because you are booking ticket for wednesday show now you have to pay ${} only".format(ticketPrice))
            totalPay += ticketPrice

print(f"your net payment is ${totalPay}")