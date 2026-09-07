import os
from abc import ABCMeta
from base64 import b64decode
from socket import gethostbyname
from webbrowser import open_new_tab

from requests import get

from cybersf.console import console

from .config import GITHUB_PATH, INSTALL_DIR
from .hosts import add_host, get_hosts
from .menu import set_readline, tools_cli


class Utility(metaclass=ABCMeta):
    def __init__(self, description: str = None) -> None:
        self.description = description

    def __str__(self) -> str:
        return self.__class__.__name__

    def run(self) -> None:
        pass


class Host2IP(Utility):
    def __init__(self) -> None:
        super().__init__(description="Gets IP from host")

    def run(self) -> None:
        hosts = get_hosts()
        set_readline(hosts)
        user_host = input("\nEnter a host: ").strip()
        if user_host not in hosts:
            add_host(user_host)
        ip = gethostbyname(user_host)
        console.print(f"\n{user_host} has the IP of {ip}")


class Base64Decode(Utility):
    def __init__(self) -> None:
        super().__init__(description="Decodes base64")

    def run(self) -> None:
        user_base64 = input("\nEnter base64: ").strip()
        try:
            text = b64decode(user_base64)
            console.print(f"\nDecoded that is: {text}")
        except Exception as e:
            console.print(f"Error decoding base64: {e}")


class SpawnShell(Utility):
    def __init__(self) -> None:
        super().__init__(description="Spawns a local shell")

    def run(self) -> None:
        console.print("Enter `exit` to return to cybersf")
        shell = os.getenv("SHELL", "/bin/bash")
        os.chdir(INSTALL_DIR)
        os.system(shell)


class SuggestTool(Utility):
    def __init__(self) -> None:
        super().__init__(description="Suggest a tool or utility")

    def run(self) -> None:
        open_new_tab(
            f"https://github.com/{GITHUB_PATH}/issues/new?assignees=&labels=tool&template=---tool-request.md&title="
        )


class PrintContributors(Utility):
    def __init__(self) -> None:
        super().__init__(description="Prints the usernames of our devs")

    def run(self) -> None:
        console.print(
            """
    8888b.  888888 Yb    dP .dP"Y8
    8I  Yb 88__    Yb  dP  `Ybo."
    8I  dY 88""     YbdP   o.`Y8b
    8888Y"  888888    YP    8bodP'
    """,
            style="bold yellow",
            highlight=False,
        )
        response = get(
            f"https://api.github.com/repos/{GITHUB_PATH}/contributors", timeout=30
        )
        contributors = response.json()
        for contributor in sorted(
            contributors, key=lambda c: c["contributions"], reverse=True
        ):
            username = contributor.get("login")
            console.print(f" {username} ".center(30, "-"))


__tools__ = [
    tool()
    for tool in [Host2IP, Base64Decode, SpawnShell, SuggestTool, PrintContributors]
]


def cli() -> None:
    tools_cli(__name__, __tools__, links=False)
