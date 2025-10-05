def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':")
            for line in file:
                print(line.strip())  # Removes any trailing newline or extra spaces
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Call the function
read_file('sample.txt')
