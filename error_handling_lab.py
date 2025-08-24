# error_handling_lab.py

def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as f:
            data = f.read()
            print("File content:")
            print(data)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please check the filename.")
    except PermissionError:
        print(f"Error: Permission denied to read {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
if __name__ == "__main__":
    read_file_with_error_handling()
