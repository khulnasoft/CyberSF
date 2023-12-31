#!/usr/bin/env python

import os
import sys

from setuptools import Command, find_packages, setup

# Package meta-data.
NAME = "cybersf"
DESCRIPTION = "A Modular Penetration Testing Framework"
URL = "https://khulnasoft.com/"
GIT_URL = "https://github.com/khulnasoft/cybersf"
PROJECT_URLS = {
    "Packages": GIT_URL + "/blob/main/PACKAGES.md",
    "Changelog": GIT_URL + "/blob/main/CHANGELOG.md",
    "Funding": "https://github.com/sponsors/thehappydinoa",
    "Tracker": GIT_URL + "/issues",
    "Source": GIT_URL,
}
EMAIL = "contact@khulnasoft.com"
AUTHOR = "khulnasoft"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = None

here = os.path.abspath(os.path.dirname(__file__))

pkg_vars = {}  # type: ignore
with open(os.path.join(here, NAME, "__version__.py"), encoding="utf-8") as f:
    exec(f.read(), pkg_vars)

try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


def get_requirements(path: str) -> list:
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()


class TagCommand(Command):
    """Support setup.py push_tag."""

    description = "Push latest version as tag."
    user_options = []  # type: ignore

    @staticmethod
    def status(s):
        print(f"\033[1m{s}\033[0m")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status("Pushing git tags…")
        os.system(f'git tag v{pkg_vars["__version__"]}')
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version=pkg_vars["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    project_urls=PROJECT_URLS,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points={
        "console_scripts": ["cybersf=cybersf.__main__:main"],
    },
    install_requires=get_requirements("requirements.txt"),
    extras_require={"dev": get_requirements("requirements-dev.txt")},
    include_package_data=True,
    license="MIT",
    keywords=NAME,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Topic :: Internet",
        "Topic :: Security",
        "Framework :: Flake8",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # python setup.py upload
    cmdclass={"push_tag": TagCommand},
)
