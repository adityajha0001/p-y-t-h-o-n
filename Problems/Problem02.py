
Bigdata ={}
user = {}

name = input("Enter your name :")
age  = input("Enter your age :")
day  = input("Enter your day :")


user["Day"] = day
user["Age"] = int(age)

# print(user)

Bigdata[name] = user
# print(Bigdata)

life = Bigdata[name]["Age"]
# print(age)

MovieDay = Bigdata[name]["Day"]

# user[value] = value
# print(user[key])

if(life< 18):
    ticketPrice = int(8)
    print(f"you have to pay ${ticketPrice} only")
    if(MovieDay == "wednesday"):
        discount = int(2)
        ticketPrice = ticketPrice - discount
        print(f"Because you are booking ticket for wednesday show now you have to pay ${ticketPrice} only")
elif(life>=18):
    ticketPrice = int(12)
    print("you have to pay ${} only".format(ticketPrice))
    if(MovieDay == "wednesday"):
        discount = int(2)
        ticketPrice = ticketPrice - discount
        print("Because you are booking ticket for wednesday show now you have to pay ${} only".format(ticketPrice))