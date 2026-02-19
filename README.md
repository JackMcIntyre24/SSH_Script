##What this program does
This script provides an automated process for its user to verify that an ssh key is installed in the .ssh folder, and to install a new key if one isn’t already installed. The program uses the python module subprocess included in the standard python library to execute command line prompts on the users system. This program only works on systems that use Windows Powershell.
Installation and Usage Instructions
This program can be downloaded and executed using a python interpreter in any powershell terminal. Prompts from the script walk the user through the input prompts required for installation of an .ssh key. Ensure that the executable has access to the .ssh folder, which is where .ssh keys are typically stored on a system.
##Necessary dependencies
The two relevant necessary dependencies for this script are access to windows powershell and python with its standard library modules.
##Warnings and Limitations
This program uses command line scripts to search for file names and create .ssh keys. With any script that accesses the command line, it is important to understand which directories this program searches and what files it creates. Using this script irresponsibly could result in creating too many .ssh keys or overwriting existing ones.
It is important to note that this tool does not guarantee that a user does not have an .ssh key installed if it cannot find one. The tool uses a rudimentary approach for locating .ssh keys, and variations in either the names of these files or the location of them will prevent the tool from working correctly. Keys must be both in the .ssh folder and include a recognized name.
##Ethical Considerations and Misuse
This tool accesses the terminal in a user’s system, so it could be modified to execute malicious commands on the user's computer. The code should not be used in any other way other than what it is intended to do, and users should review the code before executing it to ensure that it hasn’t been modified to do something else.
Additionally, users should not rely on this tool to install .ssh keys. This script speeds up the process of installing .ssh keys for users, but it is not designed to be a failsafe for installing .ssh keys. If the accuracy of an .ssh key installation is critically important, do not use this tool.
