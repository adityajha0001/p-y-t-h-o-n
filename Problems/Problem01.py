
data = {
    "aditya" : 21,
    "kirti" : 20,
    "satendra" : 35,
    "rohit" : 21,
    "mohan" : 11,
    "sohan" : 78,
    "rahul" : 6,
    "shyam" : 14
}
ageBelow13 = {}
ageAbove13Below19 = {}
ageAbove19Below60 = {}
ageAbove60 = {}
# print(data["aditya"])

for keys,value in data.items():
    # print(data[keys])
    if (data[keys]<13):
        # i= 0
        # print(keys ,"below 13")
        ageBelow13[keys] = value
    if(data[keys]>13 and data[keys]<19):
        print()
        ageAbove13Below19[keys] = value
    if(data[keys]>19 and data[keys]<60):
        print()
        ageAbove19Below60[keys] = value
    if(data[keys]>60):
        print()
        ageAbove60[keys] = value       
        
print(ageBelow13)
print(ageAbove13Below19)
print(ageAbove19Below60)
print(ageAbove60)


