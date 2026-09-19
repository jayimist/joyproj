import sys, json, shutil, subprocess
from pathlib import Path

VERSION = "0.2.3-wip"
PROJECT_DIR_PATH = Path(__file__).parent
PROJECTS_FILE_PATH = PROJECT_DIR_PATH / "projects.json"
DEVFILES_DIR_PATH = PROJECT_DIR_PATH / "dev-files"
CWD = Path.cwd()



# Functions
def print_title() -> None:
    print(f'''joyproj v{VERSION} • By jayimist@github.com
A Jay-Exclusive Joyful Project Manager.''')

def print_if_no_args() -> None:
    print_title()
    print('''\nGet the full help page by using commands 'h' or 'help'! ''')

def print_help() -> None:
    print_title()
    print('''\nUsage: joyproj <command> [project]

Description:
  A Jay-Exclusive Joyful Project Manager. Create projects with development files to easily run, build, or test the project directly from the CLI!

Commands:
  • h, help - Shows the help page
  • v, version - Shows the version along side additional information.
  • l, ls, list - Lists the projects for the CLI to interact with.
  • n, new - Creates a new project in projects.json to be used in print_help CLI, along side development files to run, build, or test your project.
  • a, add - Adds the project in projects.json but doesn't give you the dev files, etc. It ONLY adds project data to projects.json.
  • R, remove - Removes the project in projects.json, however development files will still roam to be manually deleted.
  • d, dev, develop - Runs the development file in your project, which puts you into your projects development environment.
  • b, build - Runs the build file in your project, which builds your project in the build directory, or where ever the user set it to.
  • r, run - Runs the run/test file in your project, which runs the current build of your project, or whatever the user decides to for.
      -> Note for using build and run commands. It may cause problems due to not being in the projects directory. You can run the dev files manually instead and use the command 'jdev' to be in the projects directory.`
''')

def projs_read() -> dict[str, str]:
    with PROJECTS_FILE_PATH.open("r") as f:
        return json.load(f)

def projs_write(new_projs: dict[str, str]) -> None:
    with PROJECTS_FILE_PATH.open("w") as f:
        json.dump(new_projs, f, indent=4)

def proj_run_file(proj_name: str, file_name: str, extra_args: list[str]) -> None:
    projects = projs_read()
    project_path = projects[proj_name]

    subprocess.run([Path(project_path) / file_name] + extra_args)

def proj_list() -> None:
    projs = projs_read()

    print("joyproj projects:")

    for name, path in projs.items():
        print(f"  • {name} - {path}")

def proj_add(proj_name: str) -> None:
    projs = projs_read()

    projs[proj_name] = str(CWD)

    projs_write(projs)

    print(f"Added project '{proj_name}' into projects.json!")

def proj_new(proj_name: str) -> None:
    # Add project into projects.json
    proj_add(proj_name)

    # Copy all files from dev-files to current working directory.
    for file in DEVFILES_DIR_PATH.iterdir():
        shutil.copy2(file, CWD / file.name)

    # End with user configurating dev files.
    subprocess.run(["nvim", "jdev", "jbuild", "jrun"])

    print("Your Joyful project is ready! Feel free to configure more in the dev files.")

def proj_remove(proj_name: str) -> None:
    projs = projs_read()

    try:
        del projs[proj_name]
    except KeyError:
        print(f"Project '{proj_name}' does not exist.")
        return

    projs_write(projs)

    print(f"Project '{proj_name}' was removed.")


# Interfaces
def cli(args: list[str]) -> None:
    if len(args) < 2:
        print_if_no_args()
        return

    if args[1] in ("h", "help"):
        print_help()

    elif args[1] in ("v", "version"):
        print_title()

    elif args[1] in ("l", "ls", "list"):
        proj_list()

    elif args[1] in ("n", "new"):
        if len(args) < 3:
            print("No project argument for 'joyproj new'")
            return

        proj_new(args[2])

    elif args[1] in ("a", "add"):
        if len(args) < 3:
            print("No project argument for 'joyproj add'")
            return

        proj_add(args[2])

    elif args[1] in ("R", "remove"):
        if len(args) < 3:
            print("No project argument for 'joyproj remove'")
            return

        proj_remove(args[2])

    elif args[1] in ("d", "dev", "develop"):
        if len(args) < 3:
            print("No project argument for 'joyproj dev'")
            return

        proj_run_file(args[2], "jdev", args[4:])

    elif args[1] in ("b", "build"):
        if len(args) < 3:
            print("No project argument for 'joyproj build'")
            return

        proj_run_file(args[2], "jbuild", args[4:])

    elif args[1] in ("r", "run"):
        if len(args) < 3:
            print("No project argument for 'joyproj run'")
            return

        proj_run_file(args[2], "jrun", args[4:])

    else:
        print(f"The command '{args[1]}' does not exist for 'joyproj'")



# Main
cli(sys.argv)
