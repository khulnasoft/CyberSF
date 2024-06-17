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
        os.chdir(self.full_path)
        set_readline([])
        user_email = input("\nEnter a email: ").strip()
        return os.system(f"python3 setup.py install {user_email}")


stegocracker = StegnoCrackerRepo()