import re
import os
import shutil
import subprocess


# https://www.w3schools.com/python/python_regex.asp
# Learned regex, from we3school


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
            print(f"Found path {destination}")
            return destination
        print("The URL is not a GitHub repository or the local folder does not exist.")
        return "Error"

    def download_To_local(self, FolderName):
        destination = os.path.expanduser(f"~/Downloads{FolderName}")
        if os.path.exists(destination):
            shutil.rmtree(destination)
        #     print("Removing existing directory... ")

        #        os.system(f"git clone {self.path} {destination}")
        subprocess.run(
            ["git", "clone", self.path, destination],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )

        print(f"Removing existing directory - Repository cloned to {destination}")
        return destination
