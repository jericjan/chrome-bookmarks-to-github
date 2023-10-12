import json
from pathlib import Path
import shutil
import repo

# Define the path to your JSON file
json_file_path = 'settings.json'

folder_name = "bookmarkBackup"

def create_folder():
    folder_path = Path(folder_name)    

    if not folder_path.exists():
        folder_path.mkdir()
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")


def read_json():
    global repo_url_value
    global chrome_profile_value    
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

            if 'chromeProfileUrl' in data:
                chrome_profile_value = data['chromeProfileUrl']
                print(f'chromeProfile: {chrome_profile_value}')

            if 'repoUrl' in data:
                repo_url_value = data['repoUrl']
                print(f'repoUrl: {repo_url_value}')

    except FileNotFoundError:
        print(f"{json_file_path} not found. Generating file...")
        chrome_profile_value = input("Paste the full path of your Chrome profile (ex. C:/Users/USER/AppData/Local/Google/Chrome/User Data/Profile 1): ")
        repo_url_value = input("Paste your repo URL (ex. https://github.com/jericjan/chrome-bookmarks.git): ")

        with open(json_file_path, 'w') as json_file:
            dic = {}
            dic['chromeProfileUrl'] = chrome_profile_value
            dic['repoUrl'] = repo_url_value
            json.dump(dic, json_file)        

    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {json_file_path}")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

def copy_bookmarks():
    source_file = Path(chrome_profile_value) / "Bookmarks"
    destination_file = Path(".") / folder_name / "Bookmarks.json"

    try:
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
repo.run(folder_name, repo_url_value)

input("Press enter to exit...")
