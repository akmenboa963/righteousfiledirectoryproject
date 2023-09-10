# Step 1: Import the OS module to interact with the operating system.
import os

# Step 2: Create an empty list to store file details.
file_details = []

# Step 3: Get the current working directory and list files in it.
directory = os.getcwd()  # Get the current working directory.
file_list = os.listdir(directory)  # List files in the current directory.

# Step 4: Initialize variables to store file details.
for file in file_list:
    file_size = os.path.getsize(file)  # Get the size of the file in bytes.
    mod_time = os.path.getmtime(file)  # Get the last modification time.
    creation_time = os.path.getctime(file)  # Get the creation time.
    file_path = os.path.realpath(file)  # Get the absolute path of the file.

    # Create a dictionary for each file and append it to the file_details list.
    file_details.append({'name': file, 'size': file_size, 'mod time': mod_time, 'creation time': creation_time, 'path': file_path})

# Step 5: Print file details for better readability.
for details in file_details:
    print("File Details:")
    for key, value in details.items():
        print(f"{key}: {value}")
    print("\n")

# Step 6: Wrap the code in a function for reusability.
def file_details_fn():
    directory = os.getcwd()
    file_details = []

    for file in os.listdir(directory):
        file_size = os.path.getsize(file)
        mod_time = os.path.getmtime(file)
        creation_time = os.path.getctime(file)
        file_path = os.path.realpath(file)
        file_details.append({'name': file, 'size': file_size, 'mod time': mod_time, 'creation time': creation_time, 'path': file_path})

    for details in file_details:
        print("File Details:")
        for key, value in details.items():
            print(f"{key}: {value}")
        print("\n")

# Step 7: Call the function to execute the code.
file_details_fn()
