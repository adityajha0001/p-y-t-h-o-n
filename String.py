# print("hello python")

name = "aditya kumar"

# first_character = name[0]    HERE WE CAN PRINT ANY CHARACTER OF OUR STRING BY JUST USING THE INDEX VALUE TO GET THE CHARACRTER OF THAT INDEX
# print(first_character)

# slice_name = name[0:5]     STARTING INDEX : LAST INDEX {EXCLUDE} : STEPS {DEFINES THE GAP OF EACH STEP}
# print(slice_name)

# slice_name = name[::2]      IF WE OMIT THE FIRST INDEX  THEN PYTHON ASSUMES IT AS 0  , IF  YOU OMIT THE END INDEX THEN IT ASSUMES IT  TO THE END OF THE STRING
# print(slice_name)

# slice_name = name[-1]       NEGATIVE COUNTES THE CHARACTER FROM THE END OF THE STRING LIKE START FROM THE  { RAMUK AYTIDA }
# print(slice_name)

# print(name.strip())       STRIP METHODS HELPS MOSTLY WHEN WE GET THE DATA IN WHICH A LOT OF WHITE SPACE FOUNDS IT REMOVES ALL

# print(name.replace("aditya", "satyam"))    THIS REPLACES THE STRING WITH NEW ONE

# heros = "spiderman,batman,ironman,thor,superman,green lantan,hulk "

# print(heros.split(","))  BY USING THE SPLIT METHOD ON STRING WE GET THE LIST OF ELEMENTS SEPERATED BY A COMMAS

# print(heros.find("batman"))    THIS FINDS OUT THE WORDS WE ARE SEARCHING ONY INPO

# villans = ["jokar", "ultron","thanos" ]
# print(villans.join(villans))


# city = "agra"

# for letter in city:
#     print(letter)


city = "agra,\"i am the best\""
print(city)
print("agra" in city)