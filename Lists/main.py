names = ["syed", "amaan", "ali"]
print(names)
print(len(names))
del names[1]
names.append("harry")
names.insert(2, "potter")
print(len(names))
names.sort()
names.reverse()
for i in range(4):
    print(names[i])
names2 = names[1:4]
print(names2)
print(names[1:3])
print("amaan" in names)
print("ali" in names)
print("syed" not in names2)
