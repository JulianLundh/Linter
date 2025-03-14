import os
from pathlib import Path
import textwrap
import json
import gitignore_parser


with open("config.json", "r") as file:
    config = json.load(file)

Allow_GitIgnore_Fail = config.get("Allow_GitIgnore_Fail", False)
Allow_license_Fail = config.get("Allow_license_Fail", False)
Allow_README_Fail = config.get("Allow_README_Fail", False)
Allow_workflows_Fail = config.get("Allow_workflows_Fail", False)
Allow_test_Fail = config.get("Allow_test_Fail", False)


class FolderWalker:
    def __init__(self, path):
        self.path2 = Path(path).resolve()
        self.path = path
        gitignore_path = self.path2 / ".gitignore"
        self.is_ignored = (
            gitignore_parser.parse_gitignore(gitignore_path)
            if gitignore_path.exists()
            else lambda x: False
        )

    # Converts the given path to an absolute path and stores original path.
    # If ".gitignore" exists, create a function to check if files should be ignored; otherwise, return a function that always returns False.
    # Initializes the object with a given path and handles .gitignore if it exists.

    def startReport(self):
        with open(f"Report.txt", "a") as file:
            short_path = self.path.replace(os.path.expanduser("~"), "~")
            text = f"""
                ╔══════════════════════════════════════════════════════════════════╗
                ║            New repo search                                       ║
                ╠══════════════════════════════════════════════════════════════════╣
                ║ Path: {short_path}
                ╚══════════════════════════════════════════════════════════════════╝
                """
            file.write(textwrap.dedent(text))
            print(textwrap.dedent(text))

    # Appends a formatted report header to "Report.txt" and prints it to the console.

    def updateRecord(self, nowStatus, updateStatus):
        if nowStatus.startswith("⚪️"):
            return updateStatus
        elif nowStatus.startswith("🟢"):
            if updateStatus.startswith("🟡") or updateStatus.startswith("🔴"):
                return updateStatus
            else:
                return nowStatus
        elif nowStatus.startswith("🟡"):
            if updateStatus.startswith("🔴"):
                return updateStatus
            else:
                return nowStatus

    # Updates the status based on priority rules, ensuring transitions follow a defined order.

    def fileSearch(self, fileToSearch, folderSearch=False, allowFail=False):
        nowStatus = f"⚪️ {fileToSearch} \n"
        files_Found = []
        with open(f"Report.txt", "a") as file:
            amount_of_files = 0
            for path, dirs, files in os.walk(self.path, topdown=False):
                dirs[:] = [d for d in dirs if not self.is_ignored(Path(path) / d)]

                for names in files:
                    full_path = Path(path) / names
                    if self.is_ignored(full_path):
                        continue

                    filenames = os.path.basename(names)

                    if (
                        filenames.lower() == fileToSearch.lower()
                        or filenames.lower().startswith(f"{fileToSearch.lower()}.")
                    ):
                        amount_of_files += 1
                        pathToFile = os.path.join(path, filenames)

                        if os.path.getsize(pathToFile) == 0:
                            nowStatus = self.updateRecord(
                                nowStatus, f"🟡 {fileToSearch} one or more is empty\n"
                            )
                            files_Found.append(f"       - {pathToFile}\n")
                        else:
                            nowStatus = self.updateRecord(
                                nowStatus, f"🟢 {fileToSearch}\n"
                            )
                            files_Found.append(f"       - {pathToFile}\n")

            if amount_of_files == 0 and not folderSearch:
                nowStatus = self.updateRecord(
                    nowStatus, f"🔴 {fileToSearch} does not exist \n"
                )
                file.write(nowStatus)
                print(nowStatus.rstrip())
                if not allowFail:
                    return "1"
            elif amount_of_files == 0 and folderSearch:
                self.folderSearch(fileToSearch)
            else:
                file.write(nowStatus)
                file.writelines(files_Found)
                print(nowStatus.rstrip())
                print("".join(files_Found).rstrip())
                if amount_of_files > 1:
                    text = f"         There are: {amount_of_files} {fileToSearch} files in this repository\n"
                    file.write(text)
                    print("".join(text.rstrip()))

    # Searches for a specified file in the directory, logs the results, and updates the status based on file existence and size.

    def folderSearch(self, folderToSearch, allowFail=False):
        nowStatus = f"⚪️ {folderToSearch} \n"
        folder_Found = []
        with open(f"Report.txt", "a") as file:
            amount_of_files = 0
            for path, dirs, files in os.walk(self.path, topdown=False):
                dirs[:] = [d for d in dirs if not self.is_ignored(Path(path) / d)]
                if folderToSearch.lower() in (name.lower() for name in dirs):
                    search_folder = Path(os.path.join(path, folderToSearch))
                    if any(search_folder.iterdir()):
                        nowStatus = self.updateRecord(
                            nowStatus,
                            f"🟢 {folderToSearch} folder\n",
                        )

                        folder_Found.append(f"       - {search_folder}\n")
                    else:
                        nowStatus = self.updateRecord(
                            nowStatus, f"🟡 {folderToSearch} folder is empty\n"
                        )
                        folder_Found.append(f"       - {search_folder}\n")
                    amount_of_files += 1
            if amount_of_files == 0:
                nowStatus = self.updateRecord(
                    nowStatus, f"🔴 {folderToSearch} does not exist\n"
                )
                file.write(nowStatus)
                print(nowStatus.rstrip())
                if not allowFail:
                    return "1"
            else:
                file.write(nowStatus)
                file.writelines(folder_Found)
                print(nowStatus.rstrip())
                print("".join(folder_Found).rstrip())
                if amount_of_files > 1:
                    text = f"         There are: {amount_of_files} {folderToSearch} folders in this repository\n"
                    file.write(text)
                    print("".join(text).rstrip())

    # Searches for a specified folder in the directory, logs the results, and updates the status based on its existence and contents.

    def stringSearch(self, stringToSearch, allowFail=False):
        with open(f"Report.txt", "a") as file:
            amount_of_files = 0
            amount_of_folders = 0
            tests_Found = []
            for path, dirs, files in os.walk(self.path, topdown=False):
                dirs[:] = [d for d in dirs if not self.is_ignored(Path(path) / d)]

                for names in files:
                    full_path = Path(path) / names
                    if self.is_ignored(full_path):
                        continue

                    filenames = os.path.basename(names)

                    if stringToSearch.lower() in filenames.lower():
                        pathToFile = os.path.join(path, filenames)
                        amount_of_files += 1
                        tests_Found.append(f"       - {pathToFile}\n")

            for folder in dirs:
                foldername = Path(os.path.join(path, folder))
                if (stringToSearch.lower() in folder.lower()) and any(
                    foldername.iterdir()
                ):
                    pathToFolder = os.path.join(path, folder)
                    amount_of_folders += 1
                    tests_Found.append(f"       - {pathToFolder}\n")

            if amount_of_files == 0 and amount_of_folders == 0:
                text = f"🔴 {stringToSearch}: No files found or empty '{stringToSearch}' folder at {self.path}\n"

                file.write(text)
                print(text.rstrip())
                if not allowFail:
                    return "1"
            else:
                text = f"🟢 {stringToSearch}: Found {amount_of_files} files and {amount_of_folders} folders containing '{stringToSearch}'\n"
                file.write(text)
                file.writelines(tests_Found)
                print(text.rstrip())
                print("".join(tests_Found).rstrip())

    # Searches for a specified string in file and folder names, logs the results, and updates the status based on matches found.

    def folderPathSearchExtension(
        self,
        folderPathToSearch,
        extensions,
        shortFolderName,
        allowFail=False,
    ):
        nowStatus = f"⚪️ {shortFolderName} \n"
        amount_of_files = 0

        with open("Report.txt", "a") as file:
            search_folder = Path(os.path.join(self.path, folderPathToSearch))
            if search_folder.exists() and search_folder.is_dir():
                if any(search_folder.iterdir()):
                    for path, dirs, files in os.walk(str(search_folder), topdown=False):
                        for filename in files:
                            if any(
                                filename.lower().endswith(ext.lower())
                                for ext in extensions
                            ):
                                amount_of_files += 1
                                pathToFile = os.path.join(path, filename)

                                if os.path.getsize(pathToFile) == 0:
                                    nowStatus = self.updateRecord(
                                        nowStatus,
                                        f"🟡 {shortFolderName} one or more files are empty\n",
                                    )
                                else:
                                    nowStatus = self.updateRecord(
                                        nowStatus,
                                        f"🟢 {shortFolderName} contains valid files\n",
                                    )
                    if amount_of_files == 0:
                        nowStatus = self.updateRecord(
                            nowStatus, f"🟡 {shortFolderName} folder is empty\n"
                        )
            else:
                nowStatus = self.updateRecord(
                    nowStatus, f"🔴 {shortFolderName} folder does not exist\n"
                )

            file.write(nowStatus)
            print(nowStatus.rstrip())
            if not allowFail:
                return "1"

    # Searches for files with specific extensions in a given folder, logs the results, and updates the status based on file existence and validity.

    def walker(self):
        self.startReport()
        gitIgnoreFile = self.fileSearch(".gitignore", False, Allow_GitIgnore_Fail)
        licenseFile = self.fileSearch("license", True, Allow_license_Fail)
        READMEFile = self.fileSearch("README.md", False, Allow_README_Fail)
        workflowsFolder = self.folderPathSearchExtension(
            ".github/workflows", ["yml", "yaml"], "Workflows", Allow_workflows_Fail
        )
        stringSearch = self.stringSearch("test", Allow_test_Fail)

        if any(
            x == "1"
            for x in [
                gitIgnoreFile,
                licenseFile,
                READMEFile,
                workflowsFolder,
                stringSearch,
            ]
        ):
            return "1"

        else:
            return "0"


# Runs a series of predefined file and folder searches, logging results and returning "1" if any critical checks fail.
