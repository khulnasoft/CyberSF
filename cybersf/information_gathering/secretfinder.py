import os

from cybersf.core.menu import set_readline
from cybersf.core.repo import GitHubRepo

class SecretFinderRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path='m4ll0k/SecretFinder',
            install={'pip': 'requirements.txt'},
            description='SecretFinder - A python script for find sensitive data',
        )

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_domain = input('\nEnter a domain to enumerate for SecretFinder: ').strip()
        return os.system('python3 SecretFinder.py -v -d ' + user_domain)

secretfinder = SecretFinderRepo()
