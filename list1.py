numbers = [10, 5, 8, 2, 15]

# Access list elements
print("Original List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Add elements
numbers.append(20)
numbers.insert(2, 12)
print("List after adding elements:",numbers)

# Remove elements
numbers.remove(8)
numbers.pop()
print("List after removing elements:",numbers)

# Sort list elements
numbers.sort()
print("Sorted List:", numbers)

# Reverse list elements
numbers.reverse()
print("Reversed List:", numbers)