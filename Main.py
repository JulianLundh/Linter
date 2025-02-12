# pip install pygithub, Folder
# pip install gitpython, Repo
# pip required


import re
from Repo_path import RepoPath
from Folder_Walker import FolderWalker


def main():
    print("Enter folder or URL")
    print("Exampel, https://github.com/Tyrrrz/YoutubeDownloader")
    print(
        "For folder, ~/Downloads/Tyrrrz/YoutubeDownloade, or /Users/julian/Downloads/Tyrrrz/YoutubeDownloader"
    )
    val = input("Enter Github repo URL or GitHub folder URL: ").strip()

    repo = RepoPath(val)  # Create instance of class RepoPath with the provided URL
    checkUrl = repo.folder_or_url()  # call  verify_url
    # print(checkUrl)

    if checkUrl is not None and checkUrl != "Error":
        walk = FolderWalker(checkUrl)
        walk.walker()


#        "https://github.com/Tyrrrz/YoutubeDownloader",
#        "https://github.com/Tyrrrz",
#        "https://www.google.com",
#        "/Users/julian/Downloads/Tyrrrz/YoutubeDownloader",
#        "/finnsEj/",
#        "~/Downloads/Tyrrrz/YoutubeDownloader",
#        "https://github.com/JulianLundh/Linter"


if __name__ == "__main__":
    main()
