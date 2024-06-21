import os
from shutil import which

from cybersf.core.repo import GitHubRepo

class StegnoCrackerRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="W1LDN16H7/StegoCracker",
            install=None,
            description="SteganoCracker is a tool that uncover hidden data inside "
            "files\n using brute-force utility",
        )
    
    def run(self):
        try:
            os.chdir(self.full_path)
            result = os.system(f"python3 setup.py install {user_email}")
            if result != 0:
                raise Exception("Command execution failed")
                return result
        except Exception as e:
            console.log(f"Error: {str(e)}")
            return -1


stegocracker = StegnoCrackerRepo()
