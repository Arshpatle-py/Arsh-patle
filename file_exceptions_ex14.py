def read_file():
    filename = input("Enter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content:\n")
            print(content)
        
    except FileNotFoundError:
        print("Error: The file does not exist.")

    except PermissionError:
        print("Error: You do not have permission to readthis file.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file()
