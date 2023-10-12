import datetime
from pathlib import Path

from git import Repo


def run(folder_name, repo_url):
    def get_datetime():
        current_datetime = datetime.datetime.now()

        current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        return current_datetime_str

    bookmarkFolder = Path(".") / folder_name

    repo = Repo.init(str(bookmarkFolder))

    git = repo.git

    branch_exists = "main" in repo.branches
    print(f"main branch exists: {branch_exists}")

    remote_exists = "origin" in repo.remotes

    print(f"remotes: {remote_exists}")

    if not branch_exists:
        print("no branch. creating")
        git.branch("-M", "main")

    if not remote_exists:
        print("no remote. adding")
        repo.create_remote("origin", repo_url)

    repo.index.add(["Bookmarks.json"])
    is_dirty = repo.is_dirty()
    print("is dirty: ", is_dirty)

    if is_dirty:
        print("dirty. commiting changes and pushing...")
        repo.index.commit(f"backup {get_datetime()}")
        git.push("-u", "origin", "main")
    else:
        print("is clean. no need to commit or push")
