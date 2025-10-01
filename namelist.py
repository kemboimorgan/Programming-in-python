names = input("Enter names separated by commas: ").split(",")

names = [n.strip() for n in names]     
names = sorted(set(names))            

print("Final names:", names)
print("Total  names:", len(names))

