heroes = {"flying" : "superman", "speedster" : "flash", "water" : "aquaman"}
# print(heroes)

# print(heroes["flying"])    accessing the element here dot method not works

# heroes["flying"] = "thor"   updating the value of key 
# print(heroes)

# for hero in heroes:      we get the key of all element and in list we get the value of index not number
#     print(hero)

# for hero in heroes:
#     print(hero, heroes[hero])

# for  key,value in heroes.items():          we get value with key here
#     print(key,value) 
 
# if "flying" in heroes:                 here we can only use key as a condition not value
#     print("we have superman")


# heroes["magic"] = "doctor strange"      we add new key-value pair like this
# print(heroes)

# heroes.pop("speedster")         this thing removes the value of key you used inside the pop() mathod
# print(heroes) 


# del heroes["water"]         this deletes the key with it's value
# print(heroes)

# heroes_copy = heroes.copy()    this make a copy of referenced array or data 
# print(heroes_copy)

keys = ["flying", "speedster", "water"]
default_value = "badpersons"
# new_dictionary = dict.fromkeys(keys, default_value)
# # print(new_dictionary)

new_dictionary02 = dict.fromkeys(keys,keys)
print(new_dictionary02)