"""Practicing with Dictionaries"""

# Making a new dictionary
flavors: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary. ")
print(flavors)

# Adding a = key, value pair to a dictionary
flavors["mint"] = 3
print("after adding mint! ")
print(flavors)

# removing a key from a dictionary
flavors.pop("mint")
print("after removing mint. ")
print(flavors)

# accessing a value
print(f"There are {flavors['chocolate']} orders of chocolate")

# adjust a value
flavors["vanilla"] = 10
print("after i change value of vanilla")
print(flavors)

#length of dictionary
print(len(flavors))

# check if key in dictionary
print("is chocolate in flavors? ")
print("chocolate" in flavors)

if "mint" in flavors:
    print(f"Number of orders: {flavors['mint']}")
else:
    print("No orders of mint")
