# joyproj
A Jay-Exclusive Joyful Project Manager.

## What is this?
Jay's Project Manager to create projects with development files to easily run, build, or test the project directly from the CLI! Don't worry, this is practically a joke repo so don't expect too much from this!

## CLI
### Usage
`joyproj <command> [project]`

### Commands
  - h, help - Shows the help page
  - v, version - Shows the version along side additional information.
  - l, ls, list - Lists the projects for the CLI to interact with.
  - n, new - Creates a new project in projects.json to be used in print_help CLI, along side development files to run, build, or test your project.
  - d, dev, develop - Runs the development file in your project, which puts you into your projects development environment.
  - b, build - Runs the build file in your project, which builds your project in the build directory, or where ever the user set it to. (NOT RECOMMENDED)
  - r, run - Runs the run/test file in your project, which runs the current build of your project, or whatever the user decides to for. (NOT RECOMMENDED)
  - R, remove - Removes the project in projects.json, however development files will still roam to be manually deleted. (NOT IMPLEMENTED)

## bleh
Use the python interpreter to run the current build. I just want to tell you is that I use this. I use /home/jay/Projects/joyproj/build/joyproj/joyproj.py man. It's hard I keep rebuilding and my projects.json keeps resetting. That's a hard life.
