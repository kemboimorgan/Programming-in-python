#
name1 = input("Name of student 1: ")
height1 = int(input(f"Height of {name1} (in cm): "))

name2 = input("Name of student 2: ")
height2 = int(input(f"Height of {name2} (in cm): "))

name3 = input("Name of student 3: ")
height3 = int(input(f"Height of {name3} (in cm): "))
    
print(f"\nSample input: {name1} {height1}, {name2} {height2}, {name3} {height3}")
    
    # Find the tallest
tallest_height = max(height1, height2, height3)
    
if tallest_height == height1:
        tallest = name1
elif tallest_height == height2:
        tallest = name2
else:
        tallest = name3
    
print(f"The tallest is {tallest}.")





