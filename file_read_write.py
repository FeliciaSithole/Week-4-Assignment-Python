# file_read_write.py

def read_and_write_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            data = f.read()
        
        # Modify data (convert to uppercase)
        modified_data = data.upper()

        with open(output_file, 'w') as f:
            f.write(modified_data)

        print(f"Modified data written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


