# Core
from cybersf.core.menu import tools_cli

from .stegocracker import stegocracker

__tools__ = [stegocracker]


def cli():
    tools_cli(__name__, __tools__)
