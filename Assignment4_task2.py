# Step 1: Get user input to write
write_text = input("Enter text to write to the file: ")

# Step 2: Write to output.txt (this will overwrite existing content)
with open("output.txt", "w") as file:
    file.write(write_text + "\n")

# Step 3: Get user input to append
append_text = input("Enter additional text to append: ")

# Step 4: Append to output.txt
with open("output.txt", "a") as file:
    file.write(append_text + "\n")

# Step 5: Read and display the final file content
print("\nFinal contents of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
