# 1: Create a new text file and write three lines
try:
    with open('my_file.txt', 'w') as file:
        file.write("This is the first line.\n")
        file.write("Here is a number: 42\n")
        file.write("Last line for this task.\n")
except Exception as e:
    print(f"An error occurred: {e}")


#2: Read and display the content of the file
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("File content after writing:")
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#3: Open the file in append mode and add three more lines
try:
    with open('my_file.txt', 'a') as file:
        file.write("Appending this new line.\n")
        file.write("Appending another line with a number: 100\n")
        file.write("Final line added in append mode.\n")

    # Read the file again to display the new content
    with open('my_file.txt', 'r') as file:
        updated_content = file.read()
        print("\nFile content after appending:")
        print(updated_content)
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("Permission error: Unable to write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")


# Final version with try, except, and finally block for enhanced error handling
try:
    with open('my_file.txt', 'a') as file:
        file.write("This line is added with error handling in place.\n")
    print("\nNew line successfully appended.")
    
    # Display updated content
    with open('my_file.txt', 'r') as file:
        print("\nFinal file content:")
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You don't have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile operation completed.")
