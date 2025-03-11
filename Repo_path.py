import re
import os
import shutil
import subprocess
import json

# https://www.w3schools.com/python/python_regex.asp
# Learned regex, from we3school


with open("config.json", "r") as file:
    config = json.load(file)

repo_folder = os.path.expanduser(config["repo_folder"])


class RepoPath:
    def __init__(self, path):
        self.path = path

    def folder_or_url(self):
        urlCheck = re.search(r"github\.com(.*)", self.path, re.IGNORECASE)
        if urlCheck:
            if urlCheck.group(1).count("/") == 2:
                FolderName = urlCheck.group(1)
                destination = self.download_To_local(FolderName)
                return destination

        destination = os.path.expanduser(self.path)
        if os.path.exists(destination):
            return destination
        print("The URL is not a GitHub repository or the local folder does not exist.")
        return "Error"

    # Determines if the given path is a GitHub URL or a local folder and returns the appropriate destination.

    def download_To_local(self, FolderName):
        destination = os.path.join(repo_folder, FolderName.strip("/"))
        makeLegitUrl = f"https://github.com{FolderName}"
        if os.path.exists(destination):
            shutil.rmtree(destination)
        #     print("Removing existing directory... ")

        #        os.system(f"git clone {self.path} {destination}")
        gitResult = subprocess.run(
            ["git", "clone", makeLegitUrl, destination],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        if gitResult.returncode != 0:
            print("Git clone failed")
            return "Error"

        # print(f"Removing existing directory - Repository cloned to {destination}")
        return destination


# Clones a GitHub repository to a local directory, replacing any existing folder with the same name.
