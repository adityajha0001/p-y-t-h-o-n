# let's learn pyhton  [day01]  

 STRING

 







LIST 

01. SYNTEX OF LIST  {  name = [] }
02. Indexing In List {   name[1] }
03. Slicing In List {   name[1:3:1] }
04. Overwrite In List {     name[3] = "superman"    }
05. Insert Element In List Using The Slice  {    name[2:4] = ["batman", "hulk"]    } 
06. Delete element in list using the slice method  {     name[2:3] = []     }
07. For loop on the list {    for i in name:  print(i,end=" ")         }
08. If statement on list {   if i in the name : print("having a good time ")   }
09. Add element using APPEND {  name.append("hulk")   }
10. Delete element using POP    {    name.pop()   }
11. Remove the element using REMOVE {   name.remove("hulk")    } 
12. Insert the new element {    name.insert(3,"captian america")}
13. Copy the reference of list into new list {       list2 = list.copy()     }
14. List comprehension {     i_in_range =  [ i from i in range(10) if i%0==0 ]    }


DICTIONARY

0.   dictionary is a dynamic data structure in python it is used to store the key value pair inside the data just like javascript objects. dictionary is different than list . list stores data in sequential order and we can access each element by using index value but in dictionary we get the element by using their key value .

1.   dictionary stores in a merory space which can expend or srink as per needs . In dictionary a new term introduced named as hash function .Python uses this hash function to convert the key value of a dictionary into a unique hash value then this hash value is used to determine the index where the key-value is going to store into a underlying array.this hash funtion is designed to distribute the keys evenly across the array minimizing the collision. In case two or more key hash to the same index in this case python uses the technique called "chaining" to handle this senerio . Chaining involves storing multiple key-value pair at the same index in a array . Each element at this index forms a linked-list with each nodes containg the key-value pair and reference to the next node in list.

2.   when we increase the size of dictionary after a certain limit python reallocates the dictionary into a new big memory array and rehashes the key to ensure the efficiency of dictionary and copy data from old array to new array .This resizing of dictionary also introduces the fragmantation in memory which introduces the memory related problems.

3.   when we make all key-value pair remove from dictionary  it introduces a