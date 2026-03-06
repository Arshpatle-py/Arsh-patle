student = {"roll_no": 5,"name": "Shravan kularkar","marks": 100}
print("Dictionary:", student)
print("Name:", student["name"])
print("Marks:", student.get("marks"))
print()

print("Update Dictionary")
student["marks"] = 90
student["grade"] = "A"
print("Updated Dictionary:", student)
print()

print("Removing Elements")
removed_value = student.pop("grade")
print("Removed Value:", removed_value)
print("After Removing 'grade':", student) 

student.popitem()
print("After popitem():", student)
print()

print("Merging Dictionaries")
dict1 = {"name": "shravan", "rollno": 5}
dict2 = {"grade": "A", "marks": 90}

merged_dict = dict1 | dict2
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)