#________ creating dictionary______________
# user = {'name':'Harshit','age':24}
# print(type(user))
# print(user)
     
     #or

user1 = dict(name='Harshit',age=24,movie=['coco','kimi no na wa'],tune=['awakening','fairy tale'])
# print(type(user1))
# print(user1)
# print("Name: ",user1['name'])
# print("Age: ",user1['age'])
# print("Movie: ",user1['movie'])
# print("Movie 1: ",user1['movie'][0])
# print("Movie 2: ",user1['movie'][1])

#___________ Adding data to a dict ______________________
a = "teacher"
b="Bike"
c="Yes"
d = "No"
user2 = {}  #empty dict
user2['name']='mohit'
user2['age']='23'
user2[a]=""
user2[b]=d
print(user2)

#____________________ printing all values of the dict _____________

# print(user1.values())
# print(type(user1.values))
# print(user1.keys())
# print(type(user1.keys))


#_____________ if in dict _________________

# if 'name' in user1:  #checking key
#     print("Present")

# if 'Harshit' in user1.values():  #checking values
#     print("Present")

# if 24 in user1.values():  #checking values
#     print("Present")

# if ['coco','awakening'] in user2.values():  #checking values
#     print("Present")


#_____________ for loop in dict _________________

# for i in user1:  #printing key
#     print(i)

# for i in user1.values():  #printing values
#     print(i)

# for i in user1:  #printing values
#     print(user1[i])

#__________________ item methods ___________________

# user_item = user1.items()
# print(user_item)
# print(type(user_item))

# for key,value in user1.items():
#     print(f"Key: {key} and Value is {value}")


# for i in user1.items():
#      print(i)

#________________ Add data to dict __________________
# user1['fav_songs'] = ['song1','song2']
# print(user1)

#________________ POP() ____________________________
# poped = user1.pop('fav_songs')
# print(poped)
# print(user1)


# more_info = {'State': "WB" , "Hobbies" : ["coding","reading","Guitar"]}

#__________________ update()_________________________
# user1.update(more_info)
# print(user1)

#___________________ from keys() ____________________

# d = dict.fromkeys(['name','age','height'],'unknown') #when some keys have same values
# print(d)

#___________________ get() ___________________

# d.get(('name'))