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
  - a, add - Adds the project in projects.json but doesn't give you the dev files, etc. It ONLY adds project data to projects.json.
  - R, remove - Removes the project in projects.json, however development files will still roam to be manually deleted.
  - d, dev, develop - Runs the development file in your project, which puts you into your projects development environment.
  - b, build - Runs the build file in your project, which builds your project in the build directory, or where ever the user set it to.
  - r, run - Runs the run/test file in your project, which runs the current build of your project, or whatever the user decides to for.

      > Note for using build and run commands. It may cause problems due to not being in the projects directory. You can run the dev files manually instead and use the command 'jdev' to be in the projects directory.`

## no
There is no official distribution of this software. Just run jbuild and jrun also don't use the argument in-home-dir that is for JAY ONLY unless you are really using this to manage your projects which I do not recommend. This is an addition to my digital portfolio not a addition to your computer where you actually use this software.
