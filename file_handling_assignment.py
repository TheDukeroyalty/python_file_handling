def create_file():
    try:
        # Opening/creating a file named for writing
        with open("my_file.txt", "w") as tryfile:
            # Writing at least three lines of text to the file
            tryfile.write("This is line one / 1.\n")
            tryfile.write("1564848116367\n")
            tryfile.write(" adding this third line.\n")
    except PermissionError as e:
        # Handle permission error
        print("Permission Error:", e)
    except Exception as e:
        # Handle other errors
        print("An error occurred while creating the file:", e)
    else:
        # Print success message if no errors occurred
        print("Try file 'my_file.txt' created successfully.")

def read_file():
    try:
        # Open the file named "my_file.txt" for reading
        with open("my_file.txt", "r") as tryfile:
            # Read the contents of the file
            contents = tryfile.read()
            # Print the contents to the console
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        # Handle file not found error
        print("Try file 'my_file.txt' not found.")
    except Exception as e:
        # Handle other errors
        print("An error occurred while reading the try file:", e)

def append_file():
    try:
        # Opening the file named "my_file.txt" for appending
        with open("my_file.txt", "a") as tryfile:
            # Append three additional lines of text to the file
            tryfile.write("Appending by adding this line 1.\n")
            tryfile.write("5 454 69 732 \n")
            tryfile.write("Another line appended for a third time.\n")
    except PermissionError as e:
        # Handle permission error
        print("Permission Error:", e)
    except Exception as e:
        # Handle other errors
        print("An error occurred while appending to the file:", e)
    else:
        # Print success message if no errors occurred
        print("Content appended to my_file.txt.")

def main():
    # Call functions to create, read, and append to the file
    create_file()
    read_file()
    append_file()

if __name__ == "__main__":
    # Running the main function if the script is executed directly
    main()
