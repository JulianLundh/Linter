#!/usr/bin/env python3
# pip install pygithub
# pip required
# pip install pathspec, nej?
# pip install gitignore-parser


import re
from Repo_path import RepoPath
from Folder_Walker import FolderWalker
from TruffleHog_Scanner import TruffleHog
from git_commits import gitCommit
import json

with open("config.json", "r") as file:
    config = json.load(file)

Allow_Truffle_Fail = config.get("Allow_Truffle_Fail", False)


def main():
    x = 1
    print("Enter folder or URL")
    print("Exampel, https://github.com/Tyrrrz/YoutubeDownloader")
    print("For folder, ~/Downloads/Tyrrrz/YoutubeDownloader")
    print(
        "or full path, replace parallels with username, /home/parallels/Downloads/Tyrrrz/YoutubeDownloader"
    )
    AllowFailTruffle = locals().get("AllowFailTruffle", "0")
    AllowFailRepo = locals().get("AllowFailRepo", "0")
    while x == 1:
        Ran = False
        hogRun = False
        val = input("Enter URL or path,Exit to stop: ").strip()
        if val == "exit":
            if any(x == "1" for x in [AllowFailTruffle, AllowFailRepo]):
                print("1")
                return "1"
            else:
                print("0")
                return "0"

        repo = RepoPath(val)
        checkUrl = repo.folder_or_url()

        if checkUrl is not None and checkUrl != "Error":
            walk = FolderWalker(checkUrl)
            AllowFailRepo = walk.walker()
            Ran = True

        if Ran:
            hog = TruffleHog(checkUrl)
            AllowFailTruffle = hog.run_scan_hog(Allow_Truffle_Fail)
            Ran = False
            hogRun = True

        if hogRun:
            git_report = gitCommit(checkUrl)
            git_report.rankCommits()


# Main function to handle user input, run repo analysis, and generate reports.


if __name__ == "__main__":
    main()
