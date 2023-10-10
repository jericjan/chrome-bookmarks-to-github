from git import Repo
from pathlib import Path

import datetime

def run():
    def get_datetime():
        # Get the current date and time
        current_datetime = datetime.datetime.now()

        # Convert the datetime object to a string
        current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        return current_datetime_str

    bookmarkFolder = Path('.') / "bookmarkBackup"

    repo = Repo.init(str(bookmarkFolder))


    git = repo.git

    branch_exists = 'main' in repo.branches
    print(f"main branch exists: {branch_exists}")

    remote_exists = 'origin' in repo.remotes

    print(f"remotes: {remote_exists}")

    if not branch_exists:
        print("no branch. creating")
        git.branch("-M", "main")

    if not remote_exists:
        print("no remote. adding")
        repo.create_remote("origin", "https://github.com/jericjan/chrome-bookmarks.git")

    repo.index.add(['Bookmarks.json'])
    is_dirty = repo.is_dirty()
    print("is dirty: ", is_dirty)

    if is_dirty:
        print("dirty. commiting changes and pushing...")    
        repo.index.commit(f"backup {get_datetime()}")
        git.push("-u", "origin", "main")
    else:
        print("is clean. no need to commit or push")    



