import json
from pathlib import Path
import shutil
import repo

# Define the path to your JSON file
json_file_path = 'settings.json'

folder_name = "bookmarkBackup"

def create_folder():
    # Define the folder name
    

    # Create the folder using pathlib
    folder_path = Path(folder_name)    

    if not folder_path.exists():
        # Create the folder
        folder_path.mkdir()
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")


def read_json():
    global repo_url_value
    global chrome_profile_value    
    try:
        # Open the JSON file for reading
        with open(json_file_path, 'r') as json_file:
            # Load the JSON data
            data = json.load(json_file)

            # Check if "chromeProfile" key is present
            if 'chromeProfileUrl' in data:
                chrome_profile_value = data['chromeProfileUrl']
                print(f'chromeProfile: {chrome_profile_value}')

            # Check if "repoUrl" key is present
            if 'repoUrl' in data:
                repo_url_value = data['repoUrl']
                print(f'repoUrl: {repo_url_value}')

    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {json_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_bookmarks():
    # Define the source file path
    source_file = Path(chrome_profile_value) / "Bookmarks"

    # Define the destination file path
    destination_file = Path(".") / folder_name / "Bookmarks.json"

    try:
        # Copy the source file to the destination
        shutil.copy(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Source file '{source_file}' not found.")
    except FileExistsError:
        print(f"Destination file '{destination_file}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")    

create_folder()
read_json()        
copy_bookmarks()
repo.run()

input("Press enter to exit...")
