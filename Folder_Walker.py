import os
from Reporter import Report
from pathlib import Path

# https://stackoverflow.com/questions/25675352/how-to-check-if-a-directory-contains-files-using-python-3
# Check if path is empty


class FolderWalker:
    def __init__(self, path):
        self.path = path

    def fileSearch(self, fileToSearch, folderSearch=False):
        with open(f"{self.path}/Report.txt", "a") as file:
            amount_of_files = 0
            for path, dirs, files in os.walk(self.path, topdown=False):
                for names in files:
                    filenames = os.path.basename(names)

                    if (
                        filenames.lower() == fileToSearch.lower()
                        or filenames.lower().startswith(f"{fileToSearch.lower()}.")
                    ):
                        amount_of_files += 1
                        pathToFile = os.path.join(path, filenames)

                        if os.path.getsize(pathToFile) == 0:
                            file.write(f"🟡 {fileToSearch} {pathToFile}\n")
                        else:
                            file.write(f"🟢 {fileToSearch} {pathToFile}\n")
            if amount_of_files == 0 and not folderSearch:
                file.write(f"🔴 {fileToSearch} \n")
            elif amount_of_files == 0 and folderSearch:
                self.folderSearch(fileToSearch)
            else:
                file.write(
                    f"      There are: {amount_of_files} {fileToSearch} files in this repository\n"
                )

    def folderSearch(self, folderToSearch):
        with open(f"{self.path}/Report.txt", "a") as file:
            amount_in_folder = 0
            written_to_log = 0
            for path, dirs, files in os.walk(self.path, topdown=False):
                if amount_in_folder == 0 and folderToSearch in (
                    name.lower() for name in dirs
                ):
                    search_folder = Path(os.path.join(path, folderToSearch))
                    if any(search_folder.iterdir()):
                        file.write(f"🟢 {folderToSearch} folder exist and is not empty {path}\n")
                        written_to_log += 1
                    else:
                        file.write(f"🔴/🟡 {folderToSearch} folder is empty {path}\n")
                        written_to_log += 1
                elif amount_in_folder > 0:
                    file.write(
                        f"      There are: {amount_in_folder} {folderToSearch} in this repository\n"
                    )
                    written_to_log += 1
            if written_to_log == 0:
                file.write(f"🔴 {folderToSearch} does not exist {path}\n")

    def walker(self):
        self.fileSearch(".gitignore")
        self.fileSearch("license", True)
        self.fileSearch("README.md")
        self.folderSearch("workflows")
        self.fileSearch("test",True)

