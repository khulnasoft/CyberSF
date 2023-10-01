import os
from shutil import which

from cybersf.core.repo import GitHubRepo


class NucleiRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="projectdiscovery/nuclei",
            install={
                "linux": "sudo apt install golang git build-essential libpcap-dev libusb-1.0-0-dev libnetfilter-queue-dev; go get -u github.com/projectdiscovery/nuclei/v2/cmd/nuclei",
                "arch": "sudo pacman -Sy nuclei",
                "brew": "install nuclei",
            },
            description="Fast and customizable vulnerability scanner based on simple YAML based DSL.",
        )

    def installed(self):
        return which("nuclei")

    def install(self):
        super().install(clone=False)

    def run(self):
        print("Please note that nuclei must be run with sudo")
        return os.system("sudo nuclei")


nuclei = NucleiRepo()