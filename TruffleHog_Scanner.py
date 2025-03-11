import subprocess
import re


class TruffleHog:
    def __init__(self, path):
        self.path = path

    def run_scan_hog(self, allowFail=False):
        output = subprocess.run(
            ["trufflehog", "filesystem", self.path, "--results=verified,unknown"],
            capture_output=True,
            text=True,
        )
        with open(f"Report.txt", "a") as file:
            if not output.stdout.strip():
                text = f"🟢 Credentials not found\n"
                file.write(text)
                print(text.rstrip())
                return "0"
            else:
                text = f"🔴 Credentials found!\n"
                file.write(text)
                print(text.rstrip())
                if not allowFail:
                    return "1"
                else:
                    return "0"

# Runs TruffleHog to scan for credentials in the repository and logs the results.
