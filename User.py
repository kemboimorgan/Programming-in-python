#

# Step 1: Ask user to input names separated by commas
names = input("Enter names separated by commas: ")

# Step 2: Convert input string into a list
name_list = names.split(",")

# Step 3: Remove any leading/trailing spaces
name_list = [name.strip() for name in name_list]

# Step 4: Count total names entered
total_count = len(name_list)

# Step 5: Remove duplicates using set, then sort alphabetically
unique_sorted_names = sorted(set(name_list))

# Step 6: Print results
print("\nFinal sorted list of names (duplicates removed):")
for name in unique_sorted_names:
    print(name)

print(f"\nTotal number of names entered: {total_count}")
