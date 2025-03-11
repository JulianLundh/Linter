import os
import subprocess
import textwrap
import re


class gitCommit:
    def __init__(self, path):
        self.path = path


    def rankCommits(self):
        try:
            result = subprocess.run(
                ["git", "-C", self.path, "shortlog", "-s", "-n"],
                capture_output=True,
                text=True,
                check=True, 
                timeout=5
            )

            total_commits = sum(
                map(int, re.findall(r"^\s*(\d+)", result.stdout, re.MULTILINE))
            )
            commit_output = result.stdout if result.stdout.strip() else "\nNo commits found."

        except subprocess.TimeoutExpired:
            total_commits = 0
            commit_output = "\nNo commits found."

        text = f"""
╔══════════════════════════════════════════════════════════════════╗
║            Total Git Commits:  {total_commits}
╚══════════════════════════════════════════════════════════════════╝
{commit_output}
        """

        with open("Report.txt", "a") as file:
            file.write(textwrap.dedent(text + "\n"))
            print(textwrap.dedent(text + "\n"))

# Retrieves and ranks Git commit counts per author, logging the results and handling timeouts if not found commits.
