Bibsh Workspace
This is a component of my other project, birbshell, but it can be used independently.

Features:
	- Manage workspaces in a KDE-like way ()


Configuration
There are two main configuaration files and they both should be placed in the .config/hypr directory.

The first one should be an normal '.conf' file, which just adheres to hyprland syntax. Use this for setting the usual hyprland keybinds, executables, env files.

The second one should be exactly named spconfig.json. This file is necessary for the script to function properly.
Here are a list of it's configuration options:
 - Monitors: Array - List your monitors, making sure the first index is your primary monitor.
