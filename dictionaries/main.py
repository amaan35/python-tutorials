nameData = {
    "Amaan": "a",
    "Ali": "b",
    "Muhammad": "c"
}
print(nameData["Amaan"])
# printing all the keys in the dictionary
print(nameData.keys())
# iterating over a dictionary
for key in nameData.keys():
    print(key + " - " + nameData[key])
# printing all the values in the dictionary
print(nameData.values())
# printing each key-value pair in a tuple from the dictionary
print(nameData.items())
# updating dictionary
nameData.update({"Sufiyan": "d"})
print(nameData)
# removing a key-value pair from the dictionary
del nameData["Amaan"]
print(nameData)
# copying the dictionary
nameData2 = nameData.copy()
print(nameData2)
# clearing entire dictionary
nameData.clear()
print(nameData)

