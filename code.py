import os

# Function to get file details in the current directory
def get_file_details():
    # Step 1: Get the current working directory
    current_directory = os.getcwd()

    # Step 2: List all files in the current directory
    file_list = os.listdir(current_directory)

    # Step 3: Create an empty list to store file details
    file_details = []

    # Step 4: Loop through each file in the directory
    for file_name in file_list:
        # Step 5: Get file information
        file_path = os.path.join(current_directory, file_name)  # Get the full file path
        file_size = os.path.getsize(file_path)  # Get the file size in bytes
        mod_time = os.path.getmtime(file_path)  # Get the last modification time
        creation_time = os.path.getctime(file_path)  # Get the creation time

        # Additional Step: Get file permissions, owner, and type
        file_stat = os.stat(file_path)
        permissions = oct(file_stat.st_mode & 0o777)  # Get permissions in octal format
        owner = file_stat.st_uid
        file_type = 'File' if os.path.isfile(file_path) else 'Directory'

        # Step 5.8: Create a dictionary for each file and append it to the file_details list
        file_info = {
            'name': file_name,
            'size': file_size,
            'permissions': permissions,
            'owner': owner,
            'mod time': mod_time,
            'creation time': creation_time,
            'type': file_type,
            'path': file_path,
        }
        file_details.append(file_info)

    # Step 7: Return the list of file details
    return file_details

# Step 8: Call the function and print file details
def main():
    file_details = get_file_details()
    for details in file_details:
        print("File Details:")
        for key, value in details.items():
            print(f"{key}: {value}")
        print("\n")

if __name__ == "__main__":
    main()

