# Task 1: Read a File and Handle Errors 
'''Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.'''

try:
    # Open the file in read mode
    with open("sample.txt", "r") as f:
        print("Reading file content:")
        lines = 1
        # Loop through each line
        for i in f:
            print(f"Line {lines}: {i.strip()}")
            lines += 1  # Increase line number

# handle the error
except Exception as error:
    print("Error: the file 'sample.txt' was not found")


