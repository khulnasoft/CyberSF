import os
import argparse
from cybersf.core.menu import set_readline
from cybersf.core.repo import GitHubRepo

def create_tool_class(name, org, repo, description, install="requirements.txt", command="python3"):
    class DynamicRepo(GitHubRepo):
        def __init__(self):
            super().__init__(
                path=f"{org}/{repo}",
                install={"pip": install},
                description=description,
            )

        def run(self):
            os.chdir(self.full_path)
            set_readline([])
            user_domain = input(f"\nEnter a domain to enumerate for {name}: ").strip()
            return os.system(f"{command} {name.lower()}.py -v -d {user_domain}")

    DynamicRepo.__name__ = f"{name}Repo"
    return DynamicRepo

def main():
    parser = argparse.ArgumentParser(description="Add a dynamic tool.")
    parser.add_argument("--item", required=True, help="The category of the tool (e.g., networking, information_gathering).")
    parser.add_argument("--name", required=True, help="The name of the tool.")
    parser.add_argument("--source", required=True, help="The source repository in the format 'org/repo'.")
    parser.add_argument("--description", required=True, help="The description of the tool.")
    parser.add_argument("--install", default="requirements.txt", help="The installation requirements file.")
    parser.add_argument("--command", default="python3", help="The command to run the tool.")

    args = parser.parse_args()

    org, repo = args.source.split('/')
    tool_class = create_tool_class(args.name, org, repo, args.description, args.install, args.command)

    category_dir = os.path.join("cybersf", args.item)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)

    tool_file_path = os.path.join(category_dir, f"{args.name.lower()}.py")
    with open(tool_file_path, "w") as tool_file:
        tool_file.write(f"import os\n\n")
        tool_file.write(f"from cybersf.core.menu import set_readline\n")
        tool_file.write(f"from cybersf.core.repo import GitHubRepo\n\n")
        tool_class_name = tool_class.__name__
        tool_file.write(f"class {tool_class_name}(GitHubRepo):\n")
        tool_file.write(f"    def __init__(self):\n")
        tool_file.write(f"        super().__init__(\n")
        tool_file.write(f"            path='{org}/{repo}',\n")
        tool_file.write(f"            install={{'pip': '{args.install}'}},\n")
        tool_file.write(f"            description='{args.description}',\n")
        tool_file.write(f"        )\n\n")
        tool_file.write(f"    def run(self):\n")
        tool_file.write(f"        os.chdir(self.full_path)\n")
        tool_file.write(f"        set_readline([])\n")
        tool_file.write(f"        user_domain = input('\\nEnter a domain to enumerate for {args.name}: ').strip()\n")
        tool_file.write(f"        return os.system('{args.command} {args.name.lower()}.py -v -d ' + user_domain)\n\n")
        tool_file.write(f"{args.name.lower()} = {tool_class_name}()\n")

    print(f"Tool {args.name} added to {args.item} category.")

if __name__ == "__main__":
    main()