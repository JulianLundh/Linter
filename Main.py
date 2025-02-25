#!/usr/bin/env python3
# pip install pygithub
# pip required


import re
from Repo_path import RepoPath
from Folder_Walker import FolderWalker
from Reporter import Report


def main():
    x = 1
    print("Enter folder or URL")
    print("Exampel, https://github.com/Tyrrrz/YoutubeDownloader")
    print("For folder, ~/Downloads/Tyrrrz/YoutubeDownloader")
    print(
        "or full path, replace parallels with username, /home/parallels/Downloads/Tyrrrz/YoutubeDownloader"
    )
    while x == 1:
        print("Write Exit to stop")
        val = input("Enter Github repo URL or GitHub folder URL: ").strip()

        repo = RepoPath(val)  # Create instance of class RepoPath with the provided URL
        checkUrl = repo.folder_or_url()  # call  verify_url
        print(checkUrl)

        if checkUrl is not None and checkUrl != "Error":
            walk = FolderWalker(checkUrl)
            walk.walker()

        if val == "exit":
            break


#        "https://github.com/Tyrrrz/YoutubeDownloader",
#        "https://github.com/Tyrrrz",
#        "https://www.google.com",
#        "/Users/julian/Downloads/Tyrrrz/YoutubeDownloader",
#        "/finnsEj/",
#        "~/Downloads/Tyrrrz/YoutubeDownloader",
#        "https://github.com/JulianLundh/Linter"


if __name__ == "__main__":
    main()
