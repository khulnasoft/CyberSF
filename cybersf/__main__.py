#!/usr/bin/env python3
import argparse
import platform
import sys
from random import choice

from rich.columns import Columns
from rich.text import Text

import cybersf.core.utilities
import cybersf.information_gathering
import cybersf.networking
import cybersf.obfuscation
import cybersf.passwords
import cybersf.redteam_tools
import cybersf.web_apps
from cybersf.console import console
from cybersf.core.config import CONFIG_FILE, get_config, write_config
from cybersf.core.menu import (
    clear_screen,
    format_tools,
    module_name,
    prompt,
    set_readline,
)

# Config
config = get_config()

# Menu
TERMS = """
I shall not use cybersf to:
(i) upload or otherwise transmit, display or distribute any
content that infringes any trademark, trade secret, copyright
or other proprietary or intellectual property rights of any
person; (ii) upload or otherwise transmit any material that contains
software viruses or any other computer code, files or programs
designed to interrupt, destroy or limit the functionality of any
computer software or hardware or telecommunications equipment;
"""
BANNER1 = r"""
   ______      __              _____ ______
  / ____/_  __/ /_  ___  _____/ ___// ____/
 / /   / / / / __ \/ _ \/ ___/\__ \/ /_
/ /___/ /_/ / /_/ /  __/ /   ___/ / __/
\____/\__, /_.___/\___/_/   /____/_/
     /____/

"""
BANNER2 = r"""
  _____      _               _____ ______
 / ____|    | |             / ____|  ____|
| |    _   _| |__   ___ _ _| (___ | |__
| |   | | | | '_ \ / _ \ '__\___ \|  __|
| |___| |_| | |_) |  __/ |  ____) | |
 \_____\__, |_.__/ \___|_| |_____/|_|
        __/ |
       |___/

"""
BANNER3 = r"""
 __    .         __..___
/  `  .|_  _ ._.(__ [__
\__.\_|[_)(/,[  .__)|
    ._|

"""
BANNER4 = r"""
    .::            .::                         .:: ::  .::::::::
 .::   .::         .::                       .::    .::.::
.::       .::   .::.::         .::    .: .::: .::      .::
.::        .:: .:: .:: .::   .:   .::  .::      .::    .::::::
.::          .:::  .::   .::.::::: .:: .::         .:: .::
 .::   .::    .::  .::   .::.:         .::   .::    .::.::
   .::::     .::   .:: .::    .::::   .:::     .:: ::  .::
           .::

"""
BANNERS = [BANNER1, BANNER2, BANNER3, BANNER4]
MENU_ITEMS = [
    cybersf.information_gathering,
    cybersf.networking,
    cybersf.web_apps,
    cybersf.passwords,
    cybersf.obfuscation,
    cybersf.core.utilities,
    cybersf.redteam_tools,
]
BUILTIN_FUNCTIONS = {
    "exit": lambda: exec("raise KeyboardInterrupt"),
}
items = {}


def print_menu_items():
    cols = []
    for value in MENU_ITEMS:
        name = module_name(value)
        tools = format_tools(value.__tools__)
        tools_str = Text()
        tools_str.append("\n")
        tools_str.append(name, style="command")
        tools_str.append(tools)
        cols.append(tools_str)

    console.print(Columns(cols, equal=True, expand=True))

    for key in BUILTIN_FUNCTIONS:
        print()
        console.print(key, style="command")


def agreement():
    while not config.getboolean("cybersf", "agreement"):
        clear_screen()
        console.print(TERMS, style="bold yellow")
        agree = input("You must agree to our terms and conditions first (Y/n) ")
        if agree.lower()[0] == "y":
            config.set("cybersf", "agreement", "true")


for item in MENU_ITEMS:
    items[module_name(item)] = item

commands = list(items.keys()) + list(BUILTIN_FUNCTIONS.keys())


def mainloop() -> None:
    """
    Main loop for the CLI application. Displays the menu, processes user input,
    and executes the corresponding command.
    """
    agreement()
    console.print(choice(BANNERS), style="red", highlight=False)
    print_menu_items()
    selected_command = input(prompt()).strip()

    if not selected_command or selected_command not in commands:
        console.print("Invalid Command", style="bold yellow")
        return

    if selected_command in BUILTIN_FUNCTIONS:
        func = BUILTIN_FUNCTIONS.get(selected_command)
        if func:
            func()
        return

    try:
        func = items[selected_command].cli
        func()
    except KeyError:
        console.print(f"Command '{selected_command}' not found.", style="bold yellow")
    except Exception as error:
        console.print(f"An error occurred: {str(error)}", style="bold red")
        console.print_exception()


def info():
    data = {}
    # Config File
    with open(CONFIG_FILE, encoding="utf-8") as file:
        data["Config File"] = file.read().strip()
    data["Python Version"] = platform.python_version()
    data["Platform"] = platform.platform()
    os = config.get("cybersf", "os")
    if os == "macos":
        data["macOS"] = platform.mac_ver()[0]
    elif os == "windows":
        data["Windows"] = platform.win32_ver()[0]

    for key, value in data.items():
        console.print(f"# {key}")
        console.print(value, end="\n\n")


def interactive():
    try:
        while True:
            set_readline(commands)
            mainloop()
    except KeyboardInterrupt:
        console.print("\nExitting...")
        write_config(config)
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="A Penetration Testing Framework")
    parser.add_argument("-i", "--info", action="store_true", help="gets cybersf info")
    parser.add_argument("-s", "--suggest", action="store_true", help="suggest a tool")

    args = parser.parse_args()

    if args.info:
        info()
    elif args.suggest:
        cybersf.core.utilities.suggest_tool()
    else:
        interactive()


if __name__ == "__main__":
    main()
