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
    print("Exampel, https://github.com/JulianLundh/Linter")
    print("Absolute/Full path to folder, ~/Downloads/JulianLundh/Linter")
    AllowFailTruffle = locals().get("AllowFailTruffle", "0")
    AllowFailRepo = locals().get("AllowFailRepo", "0")
    while x == 1:
        Ran = False
        hogRun = False
        val = input("Enter URL or path,Exit to stop: ").strip()
        if val == "exit":
            if any(y == "1" for y in [AllowFailTruffle, AllowFailRepo]):
                print("Exit code: 1")
                return "1"
            else:
                print("Exit code: 0")
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
