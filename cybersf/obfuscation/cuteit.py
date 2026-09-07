import os

from cybersf.core.repo import GitHubRepo


class CuteitRepo(GitHubRepo):
    def __init__(self) -> None:
        super().__init__(
            path="D4Vinci/Cuteit",
            install=None,
            description="IP obfuscator made to make a malicious ip a bit cuter",
        )

    def run(self) -> int:
        os.chdir(self.full_path)
        user_ip = input("\nEnter an IP: ").strip()
        if not user_ip:
            print("Invalid IP")
            return 1
        return os.system(f"python3 Cuteit.py {user_ip}")


cuteit = CuteitRepo()
