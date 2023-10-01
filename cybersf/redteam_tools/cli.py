# Core
from cybersf.core.menu import tools_cli

from .nuclei import nuclei

__tools__ = [nuclei]

def cli():
    tools_cli(__name__, __tools__)