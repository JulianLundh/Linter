import os


class FolderWalker:
    def __init__(self, path):
        self.path = path

    def walker(self):
        gitignore = "does not exist"
        license = "does not exist"
        GitHub_Work = "does not exist"
        for path, dirs, files in os.walk(self.path, topdown=False):
            for names in files:
                filenames = os.path.basename(names)

                if filenames == ".gitignore":
                    gitignore = "exist"

                if filenames.lower() == "license" or filenames.lower().startswith(
                    "license."
                ):
                    license = "exist"

            if ".github/workflows" in path:
                GitHub_Work = "exist"

        print("Gitignore file:", gitignore)
        print("license file:", license)
        print("GitHub Workflow file:", GitHub_Work)
