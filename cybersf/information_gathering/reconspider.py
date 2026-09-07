import os

from cybersf.core.menu import set_readline
from cybersf.core.repo import GitHubRepo

class ReconSpiderRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path='bhavsec/reconspider',
            install={
                "linux": "sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install"
            },
            description='ReconSpider is most Advanced Open Source Intelligence (OSINT)',
        )

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_domain = input('\nEnter a domain to enumerate for ReconSpider: ').strip()
        return os.system('python3 reconspider.py -v -d ' + user_domain)

reconspider = ReconSpiderRepo()
