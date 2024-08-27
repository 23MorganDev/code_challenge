#creating an empty list

my_list = []

#append elemets to my_list
my_list.append(40)
my_list.append(30)
my_list.append(20)
my_list.append(10)

#appending elemts using concatenation
#my_list += [10,20,30,40]

#adding 15 to the second position in the list

my_list.insert(1, 15)

#extend list

another_list = [50,60,70]

my_list.extend(another_list)

#remove the last element of my-list using remove function
my_list.remove(70)

#remove the last element of my-list using del keyword
#del my_list[-1]

#sorting the list in ascending order use the sorted() method

#new sorted list while the original list remains the same

new_sorted_list = sorted(my_list)

print(my_list)
print(new_sorted_list)

#finding the index of 30 in my_list

index_of_thirty = my_list.index(30)
print('Index of Thirty: ', index_of_thirty)


