import re
import os
import shutil

# https://www.w3schools.com/python/python_regex.asp
# Learned regex, from we3school


class RepoPath:
    def __init__(self, path):
        self.path = path

    def folder_or_url(self, default_val=False):
        urlCheck = re.search(r"github\.com(.*)", self.path, re.IGNORECASE)

        if urlCheck:
            if urlCheck.group(1).count("/") == 2:
                if default_val:
                    val = default_val
                else:
                    val = input(
                        "GitHub repo link found, would you like to download? [Y/N]: "
                    ).strip()
                if val == "y" or val == "Y" or val == "" or default_val:
                    FolderName = urlCheck.group(1)
                    self.download_To_local(FolderName, default_val)

        destination = os.path.expanduser(self.path)
        if os.path.exists(destination):
            print(f"Found path {destination}")
            return destination

    def download_To_local(self, FolderName, default_val=False):
        destination = os.path.expanduser(f"~/downloads{FolderName}")
        if os.path.exists(destination):
            if default_val:
                valRemove = default_val
            else:
                valRemove = input(
                    "Folder already exist, would you like to remove it and download the repo? [Y/n]: "
                ).strip()
            if valRemove == "y" or valRemove == "Y" or valRemove == "" or default_val:
                shutil.rmtree(destination)
                print("Removing existing directory...")

            else:
                print("Can't download to already occupied path")
                return "Error"

        os.system(f"git clone {self.path} {destination}")
        print(f"Repository cloned to {destination}")
