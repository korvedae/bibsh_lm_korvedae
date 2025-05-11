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
 - Workspace
 	- Offset: int - This is the workspace offset that indicates where bsh_wm should start creating workspaces. You should set this so it doesn't interfere with any other workspaces you might have. This should be at least 1000 or greater, as the ones, tenths, and hundreds places are used for determining the workspace numbers for monitors and spanned workspaces.
