team_player  = ["superman","batman","flash","wonder woman"]     
# print(team_player)                                                  THIS IS A LIST IN PYTHON
 
 
# print(team_player[-3])          indexing the element

# print(team_player[:2])          slicing the elements


# team_player[3]="ironman"                overwritting the value of index of third of team_player
# print(team_player)

# team_player[2:3] = "quick silver"    when we use slicing to add some string in at perticular place it will give a output
# print(team_player)                   like 'q','u','i','c','k',' ','s','i','l','v','e','r'at index 2 

# team_player[1:2] = ["quick silver"]            just wrap things into a array syntex to make whole thing a array and we
# print(team_player)                             are pushing a array not individual element of an array

# team_player[2:4] = ["thor", "loki"]       we can add a many element in our list as much we want 
# print(team_player)

# team_player[1:1] = ["test", "test"]         this will automatically shift the indexing of an list  
# print(team_player) 
 
# team_player[1:3] = []               passing empty array for index 1,2 means delete those index value
# print(team_player)

# for hero in team_player:             basic loop on our list and loop default have end="\n" so print all element in new row
#     print(hero, end=" | ") 

# if "flash" in team_player:                        a oormal if condition on a list if we don't have a flash as element this is going to print nothing
#     print("i have flash as our team-member")

# team_player.append("hulk")      appends add element at the end  of the list
# print(team_player) 

# team_player.pop()            pop will remove the element from the last and we know list is a mutable data type so 
# print(team_player)           last element will remove out and we get a new list

# team_player.remove("flash")    this returns the new modified list
# print(team_player)
  
# team_player.insert(3,"captain america")      we can add things using insert method on list
# print(team_player)

# team_player_copy = team_player.copy()
# print(team_player_copy)
# print(team_player)

# # team_player_copy.remove("wonder woman")
# # print(team_player_copy)
# # print(team_player)

# team_player.remove("wonder woman")
# print(team_player_copy)
# print(team_player)



# square_number = [x**2 for x in  range(15)]    we get the list of square of all numbers from o to 14                      
# print(square_number)                        this is called list comprehension in list we can make lists by applying some transformation or filtering to each element
 
# value_of_i = [i for i in range(10) if i%2==0]
# print(value_of_i)