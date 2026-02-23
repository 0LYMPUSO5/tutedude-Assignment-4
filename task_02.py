# Task 2: Write and Append Data to a File
'''Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.'''

# Take input and write to file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as f:
    f.write(text + "\n")
print("Data successfully written to output.txt.")
# Append additional data
new_text = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(new_text + "\n")
print("Data successfully appended.")
# Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as f:
    print(f.read())