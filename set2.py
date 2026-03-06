set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Access set elements 
print("Set 1 elements:")
for elem in set1:
  print(elem, end=" ")
  print("\nSet 2 elements:")
for elem in set2:
  print(elem, end=" ")
  print()

# Union of sets
union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:",
intersection_set)

# Difference of sets (Set1 - Set2)
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)

# Difference of sets (Set2 - Set1)
difference_set2 = set2.difference(set1)
print("Difference (Set2 - Set1):", difference_set2)