#Creating a Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)

#Accessing Tuple Elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-2])
print("Elements from index 1 to 3:", my_tuple[1:4])

#Nested Tuple
nested_tuple = (1, 2, (3, 4, 5), 6)
print("Nested Tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[2])
print("Accessing element inside nested tuple:", nested_tuple[2][1])

#Repetition of Tuple
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)

#Concatenation of Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)