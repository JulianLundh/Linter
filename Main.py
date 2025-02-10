# pip install pygithub, Folder
# pip install gitpython, Repo
# pip required


import re
from Repo_path import RepoPath


def main():        
    val = input("Enter Github repo URL or GitHub folder URL: ").strip()

    repo = RepoPath(val)  # Create instance of class RepoPath with the provided URL
    checkUrl = repo.folder_or_url()  # call calls verify_url
    print (checkUrl)

# Remove space from folder path
# Why do we need this feature
# Välj egen coding standard. för ens Repo också för lintern. 
# 20% buffer
# Kolla om det finns

def testRepoPath():
    TestUrlFolders = ["https://github.com/Tyrrrz/YoutubeDownloader","https://github.com/Tyrrrz","https://www.google.com","/Users/julian/Downloads/Tyrrrz/YoutubeDownloader","/finnsEj/","~Downloads/Tyrrrz/YoutubeDownloader"]
    AmountOrErrors = 0
    for i in TestUrlFolders:
        repo = RepoPath(i)
        checkUrl = repo.folder_or_url(True)
        if checkUrl == "Error":
            AmountOrErrors += 1
    
    print(AmountOrErrors)
    

if __name__ == "__main__":
    main()
    #testRepoPath()