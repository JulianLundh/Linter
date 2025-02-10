import os


class FolderWalker:
    def __init__(self, path):
        self.path = path

    def walker(self):
        gitignore = "does not exist"
        license = False
        GitHub_Work = False
        for path, dirs, files in os.walk(self.path, topdown=False):
            for names in files:
                if os.path.basename(names) == ".gitignore":
                    gitignore = "exist"
                print(os.path.basename(names))

        print("The .gitignore ", gitignore)
