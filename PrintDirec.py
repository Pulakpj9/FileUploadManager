import os

def list_directories(path):
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        return directories
    except OSError as e:
        print(f"Error: {e}")
        return []

def list_files(path):
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files
    except OSError as e:
        print(f"Error: {e}")
        return []

def list_data():
    # Replace 'path_to_directory' with the path you want to list the directories for.
    path_to_directory = 'C:\\Users\\Rishabh\\Desktop\\projects\\file\\uploads'
    directories_list = list_directories(path_to_directory)

    data={}

    if directories_list:
        print("List of directories:")
        for directory in directories_list:
            print(directory)
            data[directory]=[]
            files_list = list_files(path_to_directory+"\\"+directory)
            if files_list:
                print("List of files:")
                for file in files_list:
                    print(file)
                    data[directory].append(file)
            else:
                print("No files found in the specified path.")
                data[directory] = "No files found in the specified path."
    else:
        print("No directories found in the specified path.")

    print(data)

    return data