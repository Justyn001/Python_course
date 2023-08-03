food = ["pizza","kebab","spaghetti","maciek"]

# for foods in food:
#     print(foods)
print(food[0])

food[0] = "sushi"

print(food[0])

food.append("ice cream")
food.remove("ice cream")
food.pop()                  #Usuwa ostatni element
food.insert(0,"hot dog")
food.sort()
food.clear()                #usuwa wszystko z listy

foods = ["kebab","pizza","fizyka"]
drinks = ["woda","soplica wiśnia w czekoladzie 27.5%","cola"]
desserts = ["pudding","ice cream"]

list2d = [foods,drinks,desserts]

print(list2d[0][0])