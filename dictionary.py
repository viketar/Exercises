stuff = {"food": 15, "energy": 100, "enemies": 3}

# # Dictionary get() method, fetches the value of a key in a dictionary
# print(stuff.get("food"))
#
# # Dictionary items() method fetches the keys and values in a dictionary
# print(stuff.items())
#
# # Dictionary keys() method fetches the keys in a dictionary
# print(stuff.keys())
#
# # Dictionary popitem() method removes the last item in the dictionary
# print(stuff.popitem())
# print(stuff)
#
# # setdefault() method fetches a default value for a key, and can also add key/value into a dictionary
# print(stuff.setdefault("food"))
# print(stuff)
# print(stuff.setdefault("friends", 123))
# print(stuff)

# update() method can add a dictionary to a dictionary
new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

# update() method can also update existing items in a dictionary
new_items = {"rocks": 2, "arrows": 5}
stuff.update(new_items)
print(stuff)

# add and update a dictionary at the same time
up_new = {"food": 3, "webs": 2}
stuff.update(up_new)
print(stuff)

# update value of food in the dictionary and also adding a new key/value
stuff.update(food = 450, cookies = 6)
print(stuff)
