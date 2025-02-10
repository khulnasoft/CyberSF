import os

from cybersf.core.menu import set_readline
from cybersf.core.repo import GitHubRepo

class rang3rRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path='floriankunushevci/rang3r',
            install={'pip': 'requirements.txt'},
            description='rang3r is a python script which scans in multi thread',
        )

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        from shlex import quote
        user_domain = input('\nEnter a domain to enumerate for rang3r: ').strip()
        return os.system('python3 rang3r.py -v -d ' + quote(user_domain))

rang3r = rang3rRepo()
