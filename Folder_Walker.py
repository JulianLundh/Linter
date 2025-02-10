import os


class FolderWalker:
    def __init__(self, path):
        self.path = path

    def walker(self):
        for path, dirs, files in os.walk(".", topdown=False):
            for names in files:
                print(os.path.join(path, names))
